#!/usr/bin/env python3
"""
Merge candidate devotional entries into plans/devotional.json, matching by day_label
(replace existing, insert new), and keep entries sorted by day number. Writes a
timestamped backup first.

Usage:
  python scripts/devo_merge.py path/to/candidate_entries.json
"""
import json
import re
import shutil
import sys
import time
from devo_lib import DEVO_PATH, fill_day_labels


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

    plan = json.load(open(DEVO_PATH, encoding='utf-8'))
    entries = plan['entries']
    by_label = {e.get('day_label'): i for i, e in enumerate(entries)}

    added, replaced = 0, 0
    for e in cand:
        lbl = e.get('day_label')
        if lbl in by_label:
            entries[by_label[lbl]] = e
            replaced += 1
        else:
            entries.append(e)
            by_label[lbl] = len(entries) - 1
            added += 1

    entries.sort(key=lambda e: day_num(e.get('day_label')))
    plan['entries'] = entries

    bak = str(DEVO_PATH) + f'.bak.{int(time.time())}'
    shutil.copy(DEVO_PATH, bak)
    json.dump(plan, open(DEVO_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'Merged: +{added} new, {replaced} replaced. Total now {len(entries)}. Backup: {bak}')


if __name__ == '__main__':
    main()
