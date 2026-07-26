#!/usr/bin/env python3
"""Tier 1 verse-commentary status / worklist.

Single source of truth for "what still needs a note". A fresh (cron-fired)
session runs this first to learn exactly which days to draft next, with all the
context needed to author, so no prior conversation memory is required.

Usage:
    python3 scripts/commentary_status.py              # summary counts
    python3 scripts/commentary_status.py --next 40    # next 40 undone days + context
    python3 scripts/commentary_status.py --validate   # length-check every stored note
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIBLE = os.path.join(ROOT, "bibleData.json")
TIER1 = os.path.join(ROOT, "plans", "commentary", "tier1.json")

# House-style length target (visible chars, whitespace stripped). See TIER1_SPEC.md.
LEN_MIN, LEN_MAX = 450, 600
LEN_HARD_MIN, LEN_HARD_MAX = 400, 660


def day_num(entry):
    m = re.search(r"第\s*(\d+)\s*/\s*365", entry.get("day_label", ""))
    return int(m.group(1)) if m else None


def load_worklist():
    """Ordered list of days that HAVE a highlighted verse, with author context."""
    with open(BIBLE, encoding="utf-8") as f:
        data = json.load(f)
    items = []
    for e in data:
        vp = e.get("verse_parts") or []
        if not vp:
            continue  # weekly rest/review day — no single verse to comment on
        items.append({
            "day": day_num(e),
            "title": e.get("title", ""),
            "scripture": e.get("scripture", ""),
            "reference": vp[0]["reference"],
            "verse_text": " ".join(p["text"] for p in vp),
        })
    items.sort(key=lambda x: (x["day"] is None, x["day"]))
    return items


def load_done():
    if not os.path.exists(TIER1):
        return {}
    with open(TIER1, encoding="utf-8") as f:
        return json.load(f)


def note_len(record):
    """Visible-char count of an assembled note record."""
    beats = record.get("beats") or []
    text = "".join((lead or "") + (body or "") for lead, body in beats)
    return len(re.sub(r"\s+", "", text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", type=int, metavar="N", help="print next N undone days with context")
    ap.add_argument("--validate", action="store_true", help="length-check all stored notes")
    args = ap.parse_args()

    work = load_worklist()
    done = load_done()
    remaining = [w for w in work if w["reference"] not in done]

    if args.validate:
        flagged = []
        for ref, rec in done.items():
            n = note_len(rec)
            if n < LEN_HARD_MIN or n > LEN_HARD_MAX:
                flagged.append((rec.get("sample_day"), ref, n, "OUT"))
            elif n < LEN_MIN or n > LEN_MAX:
                flagged.append((rec.get("sample_day"), ref, n, "warn"))
        print(f"validated {len(done)} notes; {len(flagged)} outside target {LEN_MIN}-{LEN_MAX}")
        for day, ref, n, sev in sorted(flagged, key=lambda x: (x[0] or 0)):
            print(f"  [{sev}] day {day} {ref}: {n} chars")
        return

    if args.next:
        print(f"# next {min(args.next, len(remaining))} of {len(remaining)} remaining")
        print(json.dumps(remaining[: args.next], ensure_ascii=False, indent=2))
        return

    total = len(work)
    print(f"Tier 1 commentary status")
    print(f"  target verses (days with a highlighted verse): {total}")
    print(f"  drafted: {len(done)}")
    print(f"  remaining: {len(remaining)}")
    if remaining:
        nxt = remaining[:5]
        print("  next up: " + ", ".join(f"day {w['day']} ({w['reference']})" for w in nxt))
    else:
        print("  ALL DONE — the run is complete; the cron job can be deleted.")


if __name__ == "__main__":
    main()
