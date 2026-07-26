#!/usr/bin/env python3
"""Fold authored notes from _incoming.json into tier1.json.

The authoring step (Claude, in a batch) writes plans/commentary/_incoming.json:
a JSON array of records, each:
    {
      "day": 329,                      # day number from day_label (1-365)
      "voice": "MacArthur + Keller",   # expositor blend used
      "beats": [["lead", "body"], ...] # 4-5 beats; last is the 默想
    }

This script resolves the day -> verse reference/text from bibleData.json,
validates length, upserts into tier1.json (keyed by reference), sorts by day,
and clears _incoming.json. Idempotent: re-running with the same input is safe.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIBLE = os.path.join(ROOT, "bibleData.json")
COMM = os.path.join(ROOT, "plans", "commentary")
TIER1 = os.path.join(COMM, "tier1.json")
INCOMING = os.path.join(COMM, "_incoming.json")

LEN_MIN, LEN_MAX = 450, 600
LEN_HARD_MIN, LEN_HARD_MAX = 400, 660


def day_num(entry):
    m = re.search(r"第\s*(\d+)\s*/\s*365", entry.get("day_label", ""))
    return int(m.group(1)) if m else None


def build_index():
    with open(BIBLE, encoding="utf-8") as f:
        data = json.load(f)
    by_day = {}
    for e in data:
        vp = e.get("verse_parts") or []
        if not vp:
            continue
        by_day[day_num(e)] = {
            "reference": vp[0]["reference"],
            "verse_text": " ".join(p["text"] for p in vp),
        }
    return by_day


def note_len(beats):
    text = "".join((lead or "") + (body or "") for lead, body in beats)
    return len(re.sub(r"\s+", "", text))


def main():
    if not os.path.exists(INCOMING):
        print("no _incoming.json — nothing to merge")
        return 0
    with open(INCOMING, encoding="utf-8") as f:
        incoming = json.load(f)
    if not isinstance(incoming, list):
        print("ERROR: _incoming.json must be a JSON array", file=sys.stderr)
        return 1

    by_day = build_index()
    tier1 = {}
    if os.path.exists(TIER1):
        with open(TIER1, encoding="utf-8") as f:
            tier1 = json.load(f)

    merged, warnings, errors = 0, [], []
    for rec in incoming:
        day = rec.get("day")
        beats = rec.get("beats") or []
        if day not in by_day:
            errors.append(f"day {day}: not a commentable day (no verse) — skipped")
            continue
        if not (2 <= len(beats) <= 6):
            errors.append(f"day {day}: expected 4-5 beats, got {len(beats)} — skipped")
            continue
        n = note_len(beats)
        if n < LEN_HARD_MIN or n > LEN_HARD_MAX:
            errors.append(f"day {day}: {n} chars OUTSIDE hard bounds {LEN_HARD_MIN}-{LEN_HARD_MAX} — skipped")
            continue
        if n < LEN_MIN or n > LEN_MAX:
            warnings.append(f"day {day}: {n} chars (target {LEN_MIN}-{LEN_MAX})")
        info = by_day[day]
        tier1[info["reference"]] = {
            "reference": info["reference"],
            "verse_text": info["verse_text"],
            "sample_day": day,
            "voice": rec.get("voice", ""),
            "beats": beats,
        }
        merged += 1

    # sort by day for a stable, reviewable file
    ordered = dict(sorted(tier1.items(), key=lambda kv: kv[1].get("sample_day") or 0))
    with open(TIER1, "w", encoding="utf-8") as f:
        json.dump(ordered, f, ensure_ascii=False, indent=2)
        f.write("\n")
    # clear the inbox so a crashed/re-fired batch never double-processes
    os.remove(INCOMING)

    print(f"merged {merged} note(s); tier1.json now holds {len(ordered)} total")
    for w in warnings:
        print(f"  [warn] {w}")
    for e in errors:
        print(f"  [ERROR] {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
