#!/usr/bin/env python3
"""English-translation (beats_en) status / worklist for chapters.json.

Companion to chapter_status.py, but for the beats_en translation pass that
runs after a chapter's Chinese commentary is drafted. Unlike the drafting
pilot, there's no XML lookup needed — every chapter already fully exists in
chapters.json (reference, verse_text, voice, beats); the only job is adding
an English beats_en to every section that's missing one.

Scope: all 66 books in canonical order (bible_books.BOOKS, numbered 1-66,
Genesis -> Revelation) — NOT bible_books.QUEUE, which is the drafting
pilot's NT-first order and irrelevant here. A chapter counts as translated
once every section in its list has a beats_en of the same length as its
beats.

Usage:
    python3 scripts/translate_status.py              # summary counts
    python3 scripts/translate_status.py --next 15    # next N untranslated chapters, full content
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bible_books import BOOKS, NAME_TO_NUMBER, voice_for_book  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(ROOT, "plans", "commentary", "chapters.json")


def load_chapters():
    with open(CHAPTERS, encoding="utf-8") as f:
        return json.load(f)


def sort_key(key):
    name, chapter_str = key.rsplit(" ", 1)
    return (NAME_TO_NUMBER.get(name, 999), int(chapter_str))


def is_translated(entries):
    if not entries:
        return False
    for e in entries:
        beats_en = e.get("beats_en")
        if not beats_en or len(beats_en) != len(e.get("beats") or []):
            return False
    return True


def all_keys_in_order(chapters):
    return sorted(chapters.keys(), key=sort_key)


def current_book(chapters):
    for key in all_keys_in_order(chapters):
        if not is_translated(chapters[key]):
            name, _ = key.rsplit(" ", 1)
            return NAME_TO_NUMBER.get(name)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", type=int, metavar="N", help="print next N untranslated chapters with full content to translate")
    args = ap.parse_args()

    chapters = load_chapters()
    keys = all_keys_in_order(chapters)
    remaining_keys = [k for k in keys if not is_translated(chapters[k])]

    if args.next:
        work = []
        for key in remaining_keys[: args.next]:
            name, chapter_str = key.rsplit(" ", 1)
            work.append({
                "key": key,
                "book": name,
                "book_number": NAME_TO_NUMBER.get(name),
                "chapter": int(chapter_str),
                "sections": chapters[key],
            })
        print(f"# next {len(work)} of {len(remaining_keys)} remaining chapters")
        print(json.dumps(work, ensure_ascii=False, indent=2))
        return

    total = len(keys)
    remaining = len(remaining_keys)
    translated = total - remaining
    print(f"beats_en translation status ({total} chapters)")
    print(f"  translated: {translated}")
    print(f"  remaining: {remaining}")

    if remaining == 0:
        print("  ALL DONE — every chapter has beats_en.")
        return

    cb = current_book(chapters)
    book_name, book_total = BOOKS[cb]
    book_done = sum(
        1 for c in range(1, book_total + 1)
        if f"{book_name} {c}" in chapters and is_translated(chapters[f"{book_name} {c}"])
    )
    print(f"  current book: {book_name} ({book_done}/{book_total} chapters, voice: {voice_for_book(cb)})")

    upcoming = []
    for num in range(cb + 1, 67):
        name, total_c = BOOKS[num]
        if any(
            f"{name} {c}" not in chapters or not is_translated(chapters[f"{name} {c}"])
            for c in range(1, total_c + 1)
        ):
            upcoming.append(name)
    if upcoming:
        print("  next books: " + ", ".join(upcoming[:8]) + (" ..." if len(upcoming) > 8 else ""))


if __name__ == "__main__":
    main()
