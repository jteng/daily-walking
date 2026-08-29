#!/usr/bin/env python3
"""Fold translated beats_en from _incoming_translations.json into chapters.json.

Translation-pass counterpart to chapter_merge.py. The translating step
writes plans/commentary/_incoming_translations.json: a JSON array of
records, each:
    {
      "book": "创世记",              # Chinese book name, must be in bible_books.BOOKS
      "chapter": 1,
      "sections": [
        {"reference": "1:1-5", "beats_en": [["lead_en", "body_en"], ...]},
        ...                          # one per section already in chapters.json,
                                      # same order/count as that section's "beats"
      ]
    }

This script matches each section by its "reference" against the existing
chapters.json entry for that (book, chapter), validates the beats_en count
matches the existing beats count and every beat is a non-empty [lead, body]
pair, sets that section's "beats_en", and clears the inbox. Idempotent:
re-running with the same input is safe. Does not touch verse_text, voice,
beats, or reference — translation-only.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bible_books import BOOKS, NAME_TO_NUMBER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCOMING = os.path.join(ROOT, "plans", "commentary", "_incoming_translations.json")
CHAPTERS = os.path.join(ROOT, "plans", "commentary", "chapters.json")


def sort_key(key):
    name, chapter_str = key.rsplit(" ", 1)
    return (NAME_TO_NUMBER.get(name, 999), int(chapter_str))


def main():
    if not os.path.exists(INCOMING):
        print("no _incoming_translations.json — nothing to merge")
        return 0
    with open(INCOMING, encoding="utf-8") as f:
        incoming = json.load(f)
    if not isinstance(incoming, list):
        print("ERROR: _incoming_translations.json must be a JSON array", file=sys.stderr)
        return 1

    if not os.path.exists(CHAPTERS):
        print("ERROR: chapters.json not found", file=sys.stderr)
        return 1
    with open(CHAPTERS, encoding="utf-8") as f:
        chapters = json.load(f)

    merged, errors = 0, []
    for rec in incoming:
        book_name = rec.get("book")
        chapter = rec.get("chapter")
        sections_in = rec.get("sections") or []

        book_number = NAME_TO_NUMBER.get(book_name)
        if book_number is None:
            errors.append(f"record {book_name!r} chapter {chapter}: unknown book name — skipped")
            continue
        key = f"{book_name} {chapter}"
        existing = chapters.get(key)
        if not existing:
            errors.append(f"{key}: no existing chapter in chapters.json — skipped")
            continue
        by_ref = {s["reference"]: s for s in existing}

        for sec_in in sections_in:
            ref = sec_in.get("reference")
            beats_en = sec_in.get("beats_en") or []
            label = f"{key} section {ref!r}"

            target = by_ref.get(ref)
            if target is None:
                errors.append(f"{label}: no matching section reference in chapters.json — skipped")
                continue
            want_n = len(target.get("beats") or [])
            if len(beats_en) != want_n:
                errors.append(f"{label}: expected {want_n} beats_en (matching beats), got {len(beats_en)} — skipped")
                continue
            bad = [
                b for b in beats_en
                if not (isinstance(b, list) and len(b) == 2 and all(isinstance(x, str) and x.strip() for x in b))
            ]
            if bad:
                errors.append(f"{label}: malformed beat(s) in beats_en — skipped")
                continue

            target["beats_en"] = beats_en
            merged += 1

    ordered = dict(sorted(chapters.items(), key=lambda kv: sort_key(kv[0])))
    with open(CHAPTERS, "w", encoding="utf-8") as f:
        json.dump(ordered, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.remove(INCOMING)

    print(f"merged {merged} section(s) of beats_en")
    for e in errors:
        print(f"  [ERROR] {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
