#!/usr/bin/env python3
"""Chapter-grain commentary status / worklist — full-Bible queue.

Adapted from commentary_status.py for the chapter-by-chapter commentary
pilot. Unlike Tier 1, there is no pre-chosen key verse per chapter — the
author picks one after reading the whole chapter, so this reports full
chapter text as authoring context instead of a single verse.

Originally scoped to one hardcoded PILOT_BOOK_* at a time (Luke, then John,
then Acts, then Romans), requiring a manual edit + commit to move to the
next book. As of 2026-07-31 the user asked to finish all remaining 62 books,
so scope is now the ordered queue in bible_books.py (QUEUE): this script
auto-advances through it — the "current" book is just the first one in
QUEUE with an undone chapter, no manual scope edit needed between books.

Usage:
    python3 scripts/chapter_status.py              # summary counts
    python3 scripts/chapter_status.py --next 48     # next N undone chapters + full text,
                                                     # possibly spanning multiple queued books
"""
import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commentary_common import LEN_MAX, LEN_MIN, note_len  # noqa: F401 (kept for a future --validate)
from bible_books import BOOKS, NAME_TO_NUMBER, QUEUE, voice_for_book  # noqa: F401 (voice_for_book used by callers)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(ROOT, "plans", "commentary", "chapters.json")
XML_PATH = os.path.join(ROOT, "ChineseSimplifiedBible.xml")

_XML_ROOT = None


def _xml_root():
    global _XML_ROOT
    if _XML_ROOT is None:
        _XML_ROOT = ET.parse(XML_PATH).getroot()
    return _XML_ROOT


def load_done():
    if not os.path.exists(CHAPTERS):
        return {}
    with open(CHAPTERS, encoding="utf-8") as f:
        return json.load(f)


def load_chapter_text(book_number, chapter):
    """Return {verse_num: text} for the given chapter of the given book."""
    book_name = BOOKS[book_number][0]
    book = _xml_root().find(f".//book[@number='{book_number}']")
    if book is None:
        raise SystemExit(f"book number {book_number} not found in {XML_PATH}")
    chapter_elem = book.find(f".//chapter[@number='{chapter}']")
    if chapter_elem is None:
        raise SystemExit(f"{book_name} {chapter} not found in {XML_PATH}")
    verses = {}
    for v in chapter_elem.findall("verse"):
        num = v.get("number")
        verses[int(num)] = (v.text or "").strip()
    return verses


def verses_for_reference(book_number, chapter, ref):
    """Resolve a "C:V" or "C:V-V" reference (chapter redundant with `chapter`,
    kept for consistency with Tier 1's reference convention) to its joined
    verse text, e.g. verses_for_reference(45, 1, "1:1-4") -> Romans 1:1-4's text.
    """
    m = re.match(r"^(\d+):(\d+)(?:-(\d+))?$", ref)
    if not m:
        raise SystemExit(f"unrecognized reference format: {ref!r} (expected 'C:V' or 'C:V-V')")
    ref_chapter, start, end = int(m.group(1)), int(m.group(2)), m.group(3)
    end = int(end) if end else start
    if ref_chapter != chapter:
        raise SystemExit(f"reference {ref!r} chapter does not match chapter {chapter}")
    verses = load_chapter_text(book_number, chapter)
    missing = [v for v in range(start, end + 1) if v not in verses]
    if missing:
        raise SystemExit(f"verses {missing} not found in chapter {chapter}")
    return "".join(verses[v] for v in range(start, end + 1))


def all_chapters_in_queue_order():
    """Every (book_number, chapter) pair across QUEUE, in queue order."""
    items = []
    for book_number in QUEUE:
        _, total_chapters = BOOKS[book_number]
        for chapter in range(1, total_chapters + 1):
            items.append((book_number, chapter))
    return items


def load_worklist(limit=None):
    """Next `limit` undone (book, chapter) pairs across the queue, with full
    chapter text for authoring context. None = every remaining chapter in
    the queue (expensive for the 1000+ chapter full queue; prefer a limit).
    """
    done = load_done()
    items = []
    for book_number, chapter in all_chapters_in_queue_order():
        book_name = BOOKS[book_number][0]
        key = f"{book_name} {chapter}"
        if key in done:
            continue
        if limit is not None and len(items) >= limit:
            break
        verses = load_chapter_text(book_number, chapter)
        items.append({
            "key": key,
            "book": book_name,
            "book_number": book_number,
            "chapter": chapter,
            "voice": voice_for_book(book_number),
            "verse_count": len(verses),
            "verses": verses,
        })
    return items


def current_book():
    """First book in QUEUE with at least one undone chapter, or None if the
    whole queue is drafted."""
    done = load_done()
    for book_number in QUEUE:
        book_name, total_chapters = BOOKS[book_number]
        for chapter in range(1, total_chapters + 1):
            if f"{book_name} {chapter}" not in done:
                return book_number
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", type=int, metavar="N", help="print next N undone chapters (across queued books) with full text")
    args = ap.parse_args()

    if args.next:
        done = load_done()
        total_remaining = sum(
            1 for b, c in all_chapters_in_queue_order() if f"{BOOKS[b][0]} {c}" not in done
        )
        work = load_worklist(limit=args.next)
        print(f"# next {len(work)} of {total_remaining} remaining in queue")
        print(json.dumps(work, ensure_ascii=False, indent=2))
        return

    done = load_done()
    all_pairs = all_chapters_in_queue_order()
    remaining_pairs = [(b, c) for b, c in all_pairs if f"{BOOKS[b][0]} {c}" not in done]
    total = len(all_pairs)
    remaining = len(remaining_pairs)
    drafted = total - remaining

    print(f"Chapter commentary status (full-queue, {len(QUEUE)} books, {total} chapters)")
    print(f"  drafted: {drafted}")
    print(f"  remaining: {remaining}")

    cb = current_book()
    if cb is None:
        print("  ALL DONE — every book in the queue is fully drafted.")
        return

    book_name, book_total = BOOKS[cb]
    book_done = sum(1 for c in range(1, book_total + 1) if f"{book_name} {c}" in done)
    print(f"  current book: {book_name} ({book_done}/{book_total} chapters, voice: {voice_for_book(cb)})")

    upcoming = []
    for book_number in QUEUE:
        if book_number == cb:
            continue
        name, total_c = BOOKS[book_number]
        if any(f"{name} {c}" not in done for c in range(1, total_c + 1)):
            upcoming.append(name)
    if upcoming:
        print("  next books: " + ", ".join(upcoming[:8]) + (" ..." if len(upcoming) > 8 else ""))


if __name__ == "__main__":
    main()
