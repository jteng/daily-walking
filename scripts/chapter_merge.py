#!/usr/bin/env python3
"""Fold authored chapter notes from _incoming_chapters.json into chapters.json.

Chapter-keyed adaptation of commentary_merge.py (see the commentary design
doc, Next Step 3). Each chapter is now a handful of pericope-level *sections*
rather than one whole-chapter note (see CHAPTER_SPEC.md) — the authoring step
writes plans/commentary/_incoming_chapters.json: a JSON array of records,
each:
    {
      "chapter": 1,                    # chapter number within the pilot book
      "sections": [
        {
          "key_verse": "1:5-25",       # "C:V" or "C:V-V" within that chapter
          "voice": "Carson + Ferguson",
          "beats": [["lead", "body"], ...]   # 3-4 beats; last is the 默想
        },
        ...                             # typically 3-5 sections per chapter
      ]
    }

This script resolves each section's key_verse -> verse text from the XML
(via chapter_status.verses_for_reference), validates length/beat-count per
section, upserts into chapters.json (keyed "约翰福音 N" -> array of sections,
replacing a section with a matching reference or appending a new one, sorted
by starting verse), sorts chapters by chapter number, and clears the inbox.
Idempotent: re-running with the same input is safe.
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
from chapter_status import PILOT_BOOK_NAME, PILOT_CHAPTERS, verses_for_reference

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
        chapter = rec.get("chapter")
        sections_in = rec.get("sections") or []
        if chapter not in PILOT_CHAPTERS:
            errors.append(f"chapter {chapter}: outside pilot scope {PILOT_CHAPTERS} — skipped")
            continue
        if not sections_in:
            errors.append(f"chapter {chapter}: no sections — skipped")
            continue

        key = f"{PILOT_BOOK_NAME} {chapter}"
        existing = {s["reference"]: s for s in chapters.get(key, [])}

        for sec in sections_in:
            key_verse = sec.get("key_verse", "")
            beats = sec.get("beats") or []
            label = f"chapter {chapter} section {key_verse!r}"

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
                verse_text = verses_for_reference(chapter, key_verse)
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

    # sort by chapter number for a stable, reviewable file
    def chapter_num(key):
        return int(key.rsplit(" ", 1)[-1])

    ordered = dict(sorted(chapters.items(), key=lambda kv: chapter_num(kv[0])))
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
