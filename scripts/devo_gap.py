#!/usr/bin/env python3
"""
Report coverage of the devotional overlay vs. the base plan.

Usage:
  python scripts/devo_gap.py                 # summary + list of uncovered days
  python scripts/devo_gap.py 84 97           # show base passage/title for a day range
  python scripts/devo_gap.py --covered       # show which day ranges ARE covered
"""
import json
import re
import sys
from devo_lib import DEVO_PATH, BASE_PATH


def day_num(label):
    m = re.search(r'(\d+)\s*/\s*365', label or '')
    return int(m.group(1)) if m else None


def load():
    base = json.load(open(BASE_PATH, encoding='utf-8'))
    devo = json.load(open(DEVO_PATH, encoding='utf-8'))['entries']
    base_by_day = {day_num(e.get('day_label')): e for e in base}
    covered = {day_num(e.get('day_label')) for e in devo}
    covered.discard(None)
    return base_by_day, covered


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


def main():
    base_by_day, covered = load()
    all_days = sorted(d for d in base_by_day if d)
    uncovered = [d for d in all_days if d not in covered]

    args = [a for a in sys.argv[1:]]
    if args and args[0] == '--covered':
        print('COVERED ranges:', ranges(covered))
        return
    if len(args) == 2 and args[0].isdigit():
        lo, hi = int(args[0]), int(args[1])
        for d in range(lo, hi + 1):
            e = base_by_day.get(d)
            if not e:
                print(f'{d}: <no base entry>'); continue
            flag = '✓' if d in covered else ' '
            print(f'[{flag}] Day {d}  W{e.get("week")}D{e.get("day")}  {e.get("scripture","")}  | {e.get("title","")}')
        return

    print(f'Base days: {len(all_days)}  Covered: {len(covered)}  Uncovered: {len(uncovered)}')
    print('COVERED  ranges:', ranges(covered))
    print('UNCOVERED ranges:', ranges(uncovered))


if __name__ == '__main__':
    main()
