#!/usr/bin/env python3
"""
Batch verse-text lookup for drafting devotional quotes.

Usage:
  PYTHONPATH=scripts python3 scripts/devo_lookup.py "创世记一章廿六至廿七节" "罗马书八章卅二节" ...

Prints each ref and its canonical CUNP text, one call instead of N.
"""
import sys
from devo_lib import text_for_ref


def main():
    for ref in sys.argv[1:]:
        text, _ = text_for_ref(ref)
        print(f'--- {ref} ---')
        print(text if text is not None else '(unresolved)')


if __name__ == '__main__':
    main()
