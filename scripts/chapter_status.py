#!/usr/bin/env python3
"""Chapter-grain commentary status / worklist — pilot book.

Adapted from commentary_status.py for the chapter-by-chapter commentary pilot
(see the commentary design doc, Next Step 2). Unlike Tier 1, there is no
pre-chosen key verse per chapter — the author picks one after reading the
whole chapter, so this reports full chapter text as authoring context instead
of a single verse.

Scope is intentionally narrow and hardcoded (PILOT_BOOK_NAME / PILOT_CHAPTERS
below) rather than generalized to "any book" — a full book/chapter browser is
explicitly deferred (Approach B); this pilot only needs to walk forward one
book, one chapter range at a time. Extend PILOT_CHAPTERS to widen scope later.

Usage:
    python3 scripts/chapter_status.py              # summary counts
    python3 scripts/chapter_status.py --next 5      # next N undone chapters + full text
"""
import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commentary_common import LEN_MAX, LEN_MIN, note_len  # noqa: F401 (kept for a future --validate)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(ROOT, "plans", "commentary", "chapters.json")
XML_PATH = os.path.join(ROOT, "ChineseSimplifiedBible.xml")

# Pilot scope — edit these to move on to the next book. 路加福音 (Luke),
# 约翰福音 (John), and 使徒行传 (Acts) are all fully drafted and stay in
# chapters.json.
PILOT_BOOK_NAME = "罗马书"
PILOT_BOOK_NUMBER = 45  # matches index.html's Reader.bookMap['罗'] and the XML's book@number
PILOT_CHAPTERS = range(1, 17)  # all 16 chapters of Romans


def load_done():
    if not os.path.exists(CHAPTERS):
        return {}
    with open(CHAPTERS, encoding="utf-8") as f:
        return json.load(f)


def load_chapter_text(chapter):
    """Return {verse_num: text} for the given chapter of the pilot book."""
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
    book = root.find(f".//book[@number='{PILOT_BOOK_NUMBER}']")
    if book is None:
        raise SystemExit(f"book number {PILOT_BOOK_NUMBER} not found in {XML_PATH}")
    chapter_elem = book.find(f".//chapter[@number='{chapter}']")
    if chapter_elem is None:
        raise SystemExit(f"{PILOT_BOOK_NAME} {chapter} not found in {XML_PATH}")
    verses = {}
    for v in chapter_elem.findall("verse"):
        num = v.get("number")
        verses[int(num)] = (v.text or "").strip()
    return verses


def verses_for_reference(chapter, ref):
    """Resolve a "C:V" or "C:V-V" reference (chapter redundant with `chapter`,
    kept for consistency with Tier 1's reference convention) to its joined
    verse text, e.g. verses_for_reference(1, "1:1-4") -> the text of John 1:1-4.
    """
    m = re.match(r"^(\d+):(\d+)(?:-(\d+))?$", ref)
    if not m:
        raise SystemExit(f"unrecognized reference format: {ref!r} (expected 'C:V' or 'C:V-V')")
    ref_chapter, start, end = int(m.group(1)), int(m.group(2)), m.group(3)
    end = int(end) if end else start
    if ref_chapter != chapter:
        raise SystemExit(f"reference {ref!r} chapter does not match chapter {chapter}")
    verses = load_chapter_text(chapter)
    missing = [v for v in range(start, end + 1) if v not in verses]
    if missing:
        raise SystemExit(f"verses {missing} not found in chapter {chapter}")
    return "".join(verses[v] for v in range(start, end + 1))


def load_worklist():
    """Ordered list of pilot-book chapters, with full chapter text for authoring context."""
    items = []
    for chapter in PILOT_CHAPTERS:
        verses = load_chapter_text(chapter)
        items.append({
            "key": f"{PILOT_BOOK_NAME} {chapter}",
            "book": PILOT_BOOK_NAME,
            "chapter": chapter,
            "verse_count": len(verses),
            "verses": verses,
        })
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", type=int, metavar="N", help="print next N undone chapters with full text")
    args = ap.parse_args()

    work = load_worklist()
    done = load_done()
    remaining = [w for w in work if w["key"] not in done]

    if args.next:
        print(f"# next {min(args.next, len(remaining))} of {len(remaining)} remaining")
        print(json.dumps(remaining[: args.next], ensure_ascii=False, indent=2))
        return

    total = len(work)
    drafted = total - len(remaining)  # scoped to PILOT_BOOK_NAME, not len(done) which spans every book in the file
    print(f"Chapter commentary status ({PILOT_BOOK_NAME}, chapters {PILOT_CHAPTERS.start}-{PILOT_CHAPTERS.stop - 1})")
    print(f"  target chapters: {total}")
    print(f"  drafted: {drafted}")
    print(f"  remaining: {len(remaining)}")
    if remaining:
        print("  next up: " + ", ".join(w["key"] for w in remaining))
    else:
        print("  ALL DONE for this pilot scope.")


if __name__ == "__main__":
    main()
