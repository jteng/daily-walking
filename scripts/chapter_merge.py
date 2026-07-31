#!/usr/bin/env python3
"""Fold authored chapter notes from _incoming_chapters.json into chapters.json.

Chapter-keyed adaptation of commentary_merge.py (see the commentary design
doc, Next Step 3). Each chapter is now a handful of pericope-level *sections*
rather than one whole-chapter note (see CHAPTER_SPEC.md) — the authoring step
writes plans/commentary/_incoming_chapters.json: a JSON array of records,
each:
    {
      "book": "加拉太书",              # Chinese book name, must be in bible_books.BOOKS
      "chapter": 1,                    # chapter number within that book
      "sections": [
        {
          "key_verse": "1:5-25",       # "C:V" or "C:V-V" within that chapter
          "voice": "MacArthur + Sproul + Keller",
          "beats": [["lead", "body"], ...]   # 3-4 beats; last is the 默想
        },
        ...                             # typically 3-5 sections per chapter
      ]
    }

As of 2026-07-31 the pilot spans the full remaining-Bible queue (bible_books.
QUEUE) instead of one hardcoded book, so each record now names its own book —
a single batch's _incoming_chapters.json can (and, at a 48-chapter-per-batch
worklist, often will) span several queued books at once.

This script resolves each section's key_verse -> verse text from the XML
(via chapter_status.verses_for_reference), validates length/beat-count per
section, upserts into chapters.json (keyed "书名 N" -> array of sections,
replacing a section with a matching reference or appending a new one, sorted
by starting verse), sorts all chapters by (book's canonical number, chapter),
and clears the inbox. Idempotent: re-running with the same input is safe.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commentary_common import (
    SECTION_BEATS_MAX,
    SECTION_BEATS_MIN,
    SECTION_LEN_HARD_MAX,
    SECTION_LEN_HARD_MIN,
    SECTION_LEN_MAX,
    SECTION_LEN_MIN,
    note_len,
)
from bible_books import BOOKS, NAME_TO_NUMBER
from chapter_status import verses_for_reference

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCOMING = os.path.join(ROOT, "plans", "commentary", "_incoming_chapters.json")
CHAPTERS = os.path.join(ROOT, "plans", "commentary", "chapters.json")


def section_start_verse(reference):
    """Sort key: the starting verse number of a "C:V" / "C:V-V" reference."""
    m = re.match(r"^\d+:(\d+)", reference or "")
    return int(m.group(1)) if m else 0


def main():
    if not os.path.exists(INCOMING):
        print("no _incoming_chapters.json — nothing to merge")
        return 0
    with open(INCOMING, encoding="utf-8") as f:
        incoming = json.load(f)
    if not isinstance(incoming, list):
        print("ERROR: _incoming_chapters.json must be a JSON array", file=sys.stderr)
        return 1

    chapters = {}
    if os.path.exists(CHAPTERS):
        with open(CHAPTERS, encoding="utf-8") as f:
            chapters = json.load(f)

    merged, warnings, errors = 0, [], []
    for rec in incoming:
        book_name = rec.get("book")
        chapter = rec.get("chapter")
        sections_in = rec.get("sections") or []

        book_number = NAME_TO_NUMBER.get(book_name)
        if book_number is None:
            errors.append(f"record {rec.get('book')!r} chapter {chapter}: unknown book name — skipped")
            continue
        total_chapters = BOOKS[book_number][1]
        if not (isinstance(chapter, int) and 1 <= chapter <= total_chapters):
            errors.append(f"{book_name} {chapter}: chapter outside 1-{total_chapters} — skipped")
            continue
        if not sections_in:
            errors.append(f"{book_name} {chapter}: no sections — skipped")
            continue

        key = f"{book_name} {chapter}"
        existing = {s["reference"]: s for s in chapters.get(key, [])}

        for sec in sections_in:
            key_verse = sec.get("key_verse", "")
            beats = sec.get("beats") or []
            label = f"{book_name} {chapter} section {key_verse!r}"

            if not (SECTION_BEATS_MIN <= len(beats) <= SECTION_BEATS_MAX):
                errors.append(f"{label}: expected {SECTION_BEATS_MIN}-{SECTION_BEATS_MAX} beats, got {len(beats)} — skipped")
                continue
            n = note_len(beats)
            if n < SECTION_LEN_HARD_MIN or n > SECTION_LEN_HARD_MAX:
                errors.append(f"{label}: {n} chars OUTSIDE hard bounds {SECTION_LEN_HARD_MIN}-{SECTION_LEN_HARD_MAX} — skipped")
                continue
            if n < SECTION_LEN_MIN or n > SECTION_LEN_MAX:
                warnings.append(f"{label}: {n} chars (target {SECTION_LEN_MIN}-{SECTION_LEN_MAX})")
            try:
                verse_text = verses_for_reference(book_number, chapter, key_verse)
            except SystemExit as e:
                errors.append(f"{label}: {e} — skipped")
                continue

            existing[key_verse] = {
                "reference": key_verse,
                "verse_text": verse_text,
                "voice": sec.get("voice", ""),
                "beats": beats,
            }
            merged += 1

        chapters[key] = sorted(existing.values(), key=lambda s: section_start_verse(s["reference"]))

    # sort by (book's canonical number, chapter) for a stable, reviewable file
    def sort_key(key):
        name, chapter_str = key.rsplit(" ", 1)
        return (NAME_TO_NUMBER.get(name, 999), int(chapter_str))

    ordered = dict(sorted(chapters.items(), key=lambda kv: sort_key(kv[0])))
    with open(CHAPTERS, "w", encoding="utf-8") as f:
        json.dump(ordered, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.remove(INCOMING)

    print(f"merged {merged} section(s); chapters.json now holds {len(ordered)} chapter key(s)")
    for w in warnings:
        print(f"  [warn] {w}")
    for e in errors:
        print(f"  [ERROR] {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
