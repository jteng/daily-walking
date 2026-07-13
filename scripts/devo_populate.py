#!/usr/bin/env python3
"""
Populate verse_text + verse_parts for candidate devotional entries from the XML,
using each entry's `verse` (Chinese reference) field. Canonicalizes the highlighted
verse so it always matches the CUNP text exactly.

Usage:
  python scripts/devo_populate.py path/to/candidate_entries.json   # in place
Reports any entry whose `verse` reference could not be resolved.
"""
import json
import sys
from devo_lib import text_for_ref, fill_day_labels


def main():
    path = sys.argv[1]
    entries = json.load(open(path, encoding='utf-8'))
    if isinstance(entries, dict) and 'entries' in entries:
        wrapper, entries = entries, entries['entries']
    else:
        wrapper = None
    missing = fill_day_labels(entries)
    for wd in missing:
        print(f'  ✗ no base day_label for week/day {wd}')
    failures = []
    for e in entries:
        ref = (e.get('verse') or '').strip()
        if not ref:
            # sabbath / summary entries may legitimately have no highlighted verse
            continue
        txt, parts = text_for_ref(ref)
        if not txt:
            failures.append((e.get('day_label'), ref))
            continue
        e['verse_text'] = txt
        e['verse_parts'] = parts
    out = wrapper if wrapper is not None else entries
    json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'Populated {len(entries)} entries; {len(failures)} verse-ref failures.')
    for lbl, ref in failures:
        print(f'  ✗ {lbl}: {ref!r}')
    if failures:
        sys.exit(1)


if __name__ == '__main__':
    main()
