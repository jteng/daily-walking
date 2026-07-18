#!/usr/bin/env python3
"""
Merge candidate overview-plan entries directly into bibleData.json (the base file,
a flat list), matching by day_label (full-entry replace). Keeps entries sorted by
day number. Writes a timestamped backup first.

Unlike devo_merge.py (which fills an initially-empty overlay), this overwrites the
base file's existing 苏颖智 content in place -- that's the whole point of the
overview-plan migration.

Usage:
  python scripts/devo_merge_base.py path/to/candidate_entries.json
"""
import json
import re
import shutil
import sys
import time
from devo_lib import BASE_PATH, fill_day_labels


def day_num(label):
    m = re.search(r'(\d+)\s*/\s*365', label or '')
    return int(m.group(1)) if m else 10 ** 9


def main():
    path = sys.argv[1]
    cand = json.load(open(path, encoding='utf-8'))
    cand = cand['entries'] if isinstance(cand, dict) and 'entries' in cand else cand
    missing = fill_day_labels(cand)
    if missing:
        print(f'ERROR: entries with unresolvable day_label: {missing}')
        sys.exit(1)

    entries = json.load(open(BASE_PATH, encoding='utf-8'))
    by_label = {e.get('day_label'): i for i, e in enumerate(entries)}

    replaced, unmatched = 0, []
    for e in cand:
        lbl = e.get('day_label')
        if lbl in by_label:
            entries[by_label[lbl]] = e
            replaced += 1
        else:
            unmatched.append(lbl)

    if unmatched:
        print(f'ERROR: candidate day_labels not found in base plan (base file only has 362 existing days, no new ones): {unmatched}')
        sys.exit(1)

    entries.sort(key=lambda e: day_num(e.get('day_label')))

    bak = str(BASE_PATH) + f'.bak.{int(time.time())}'
    shutil.copy(BASE_PATH, bak)
    json.dump(entries, open(BASE_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'Merged into base: {replaced} replaced. Total {len(entries)}. Backup: {bak}')


if __name__ == '__main__':
    main()
