#!/usr/bin/env python3
"""
Report migration progress of the overview-plan (self-authored survey content that
replaces 苏颖智's original, written in place into bibleData.json).

Since we overwrite the same file rather than filling an initially-empty overlay,
"migrated" = a day whose content/title differs from the pre-migration snapshot at
the overview-plan branch-point commit.

Usage:
  python scripts/devo_gap_base.py                 # summary + migrated/unmigrated ranges
  python scripts/devo_gap_base.py 1 20             # show status for a day range
  python scripts/devo_gap_base.py --base <sha>     # override the branch-point commit
"""
import json
import re
import subprocess
import sys
from devo_lib import BASE_PATH, REPO_ROOT

# overview-plan branch point (git checkout -b overview-plan off main), recorded once.
DEFAULT_BASE_COMMIT = '46c7fed'


def day_num(label):
    m = re.search(r'(\d+)\s*/\s*365', label or '')
    return int(m.group(1)) if m else None


def ranges(nums):
    nums = sorted(nums)
    if not nums:
        return []
    out = []
    start = prev = nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
        else:
            out.append((start, prev)); start = prev = n
    out.append((start, prev))
    return out


def load(base_commit):
    current = json.load(open(BASE_PATH, encoding='utf-8'))
    original_raw = subprocess.run(
        ['git', 'show', f'{base_commit}:bibleData.json'],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    ).stdout
    original = json.loads(original_raw)
    original_by_label = {e.get('day_label'): e for e in original}

    current_by_day = {day_num(e.get('day_label')): e for e in current}
    migrated, unmigrated = set(), set()
    for e in current:
        d = day_num(e.get('day_label'))
        if d is None:
            continue
        orig = original_by_label.get(e.get('day_label'))
        if orig is None:
            migrated.add(d)  # shouldn't happen; treat unmatched as migrated/new
            continue
        if orig.get('content') != e.get('content') or orig.get('title') != e.get('title'):
            migrated.add(d)
        else:
            unmigrated.add(d)
    return current_by_day, migrated, unmigrated


def main():
    args = sys.argv[1:]
    base_commit = DEFAULT_BASE_COMMIT
    if '--base' in args:
        i = args.index('--base')
        base_commit = args[i + 1]
        del args[i:i + 2]

    current_by_day, migrated, unmigrated = load(base_commit)
    all_days = sorted(d for d in current_by_day if d)

    if len(args) == 2 and args[0].isdigit():
        lo, hi = int(args[0]), int(args[1])
        for d in range(lo, hi + 1):
            e = current_by_day.get(d)
            if not e:
                print(f'{d}: <no entry>'); continue
            flag = '✓' if d in migrated else ' '
            print(f'[{flag}] Day {d}  W{e.get("week")}D{e.get("day")}  {e.get("scripture","")}  | {e.get("title","")}')
        return

    print(f'Base commit: {base_commit}')
    print(f'Total days: {len(all_days)}  Migrated: {len(migrated)}  Unmigrated: {len(unmigrated)}')
    print('MIGRATED   ranges:', ranges(migrated))
    print('UNMIGRATED ranges:', ranges(unmigrated))


if __name__ == '__main__':
    main()
