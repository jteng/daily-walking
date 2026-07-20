#!/usr/bin/env python3
"""
Dump full chapter text (canonical CUNP, verse by verse) for exegetical/accuracy
review, instead of writing ad hoc XML-parsing snippets each time.

Usage:
  PYTHONPATH=scripts python3 scripts/devo_chapter.py 尼希米记 4 5
  PYTHONPATH=scripts python3 scripts/devo_chapter.py NEH 4-6
  PYTHONPATH=scripts python3 scripts/devo_chapter.py 以斯帖记 1-10

Book can be given as a Chinese name/abbreviation (resolved via devo_lib's
CHINESE_BOOK_MAP, same aliases devo_lookup.py understands) or a 3-letter book
code (e.g. NEH, EST). Chapters can be single numbers, space-separated, and/or
"start-end" ranges, in any combination.
"""
import sys
from devo_lib import resolve_book_token, chapter_verses, CHINESE_BOOK_MAP


def _resolve_book(token):
    if token.upper() in set(CHINESE_BOOK_MAP.values()):
        return token.upper()
    return resolve_book_token(token)


def _expand_chapters(args):
    chapters = []
    for a in args:
        if '-' in a:
            start, end = a.split('-', 1)
            chapters.extend(range(int(start), int(end) + 1))
        else:
            chapters.append(int(a))
    return chapters


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    book_token = sys.argv[1]
    code = _resolve_book(book_token)
    if not code:
        print(f"Could not resolve book '{book_token}'")
        sys.exit(1)

    for chapter in _expand_chapters(sys.argv[2:]):
        verses = chapter_verses(code, chapter)
        print(f"=== {book_token} {chapter} ===")
        if not verses:
            print("(no verses found -- check book/chapter)")
            continue
        for vnum, text in verses:
            print(f"{vnum}\t{text}")


if __name__ == '__main__':
    main()
