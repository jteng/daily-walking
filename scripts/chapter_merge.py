#!/usr/bin/env python3
"""Fold authored chapter notes from _incoming_chapters.json into chapters.json.

Chapter-keyed adaptation of commentary_merge.py (see the commentary design
doc, Next Step 3). The authoring step writes plans/commentary/_incoming_chapters.json:
a JSON array of records, each:
    {
      "chapter": 1,                # chapter number within the pilot book
      "key_verse": "1:1-4",        # "C:V" or "C:V-V" within that chapter
      "voice": "Carson + Ferguson",
      "beats": [["lead", "body"], ...]  # 4-5 beats; last is the 默想
    }

This script resolves key_verse -> verse text from the XML (via
chapter_status.verses_for_reference), validates length/beat-count the same
way Tier 1 does, upserts into chapters.json (keyed "约翰福音 N"), sorts by
chapter, and clears the inbox. Idempotent: re-running with the same input is
safe.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commentary_common import LEN_HARD_MAX, LEN_HARD_MIN, LEN_MAX, LEN_MIN, note_len
from chapter_status import CHAPTERS, PILOT_BOOK_NAME, PILOT_CHAPTERS, verses_for_reference

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCOMING = os.path.join(ROOT, "plans", "commentary", "_incoming_chapters.json")


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
        beats = rec.get("beats") or []
        if chapter not in PILOT_CHAPTERS:
            errors.append(f"chapter {chapter}: outside pilot scope {PILOT_CHAPTERS} — skipped")
            continue
        if not (2 <= len(beats) <= 6):
            errors.append(f"chapter {chapter}: expected 4-5 beats, got {len(beats)} — skipped")
            continue
        n = note_len(beats)
        if n < LEN_HARD_MIN or n > LEN_HARD_MAX:
            errors.append(f"chapter {chapter}: {n} chars OUTSIDE hard bounds {LEN_HARD_MIN}-{LEN_HARD_MAX} — skipped")
            continue
        if n < LEN_MIN or n > LEN_MAX:
            warnings.append(f"chapter {chapter}: {n} chars (target {LEN_MIN}-{LEN_MAX})")
        key_verse = rec.get("key_verse", "")
        try:
            verse_text = verses_for_reference(chapter, key_verse)
        except SystemExit as e:
            errors.append(f"chapter {chapter}: {e} — skipped")
            continue
        key = f"{PILOT_BOOK_NAME} {chapter}"
        chapters[key] = {
            "reference": key_verse,
            "verse_text": verse_text,
            "voice": rec.get("voice", ""),
            "beats": beats,
        }
        merged += 1

    # sort by chapter number for a stable, reviewable file
    def chapter_num(key):
        return int(key.rsplit(" ", 1)[-1])

    ordered = dict(sorted(chapters.items(), key=lambda kv: chapter_num(kv[0])))
    with open(CHAPTERS, "w", encoding="utf-8") as f:
        json.dump(ordered, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.remove(INCOMING)

    print(f"merged {merged} note(s); chapters.json now holds {len(ordered)} total")
    for w in warnings:
        print(f"  [warn] {w}")
    for e in errors:
        print(f"  [ERROR] {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
