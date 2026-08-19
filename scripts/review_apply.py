#!/usr/bin/env python3
"""Fold review results from _incoming_review.json into review state
(+ patch tier1.json/chapters.json for auto-fixed entries).

Companion to review_status.py / REVIEW_SPEC.md. The review step (Claude, in
a batch) writes plans/commentary/_incoming_review.json: a JSON array of
records, each:
    {
      "corpus": "tier1" | "chapters",
      "key": "...",                # review_status.py's own "key" field for
                                    # that entry (tier1: the reference string
                                    # itself; chapters: "书名 章|C:V")
      "status": "ok" | "fixed" | "flagged",
      "note": "...",                # required for "fixed"/"flagged"; why
      "beats": [["lead","body"], ...]  # required for "fixed", else omit/null
    }

"ok": no content change, just marks the entry reviewed.
"fixed": validates replacement beats against the corpus's existing
  length/beat-count house-style bounds (same gate chapter_merge.py /
  commentary_merge.py already enforce via commentary_common.py), patches the
  specific entry/section's beats in place, marks reviewed.
"flagged": no content change; appends a human-readable entry to
  plans/commentary/REVIEW_FLAGGED.md for the user's own go/no-go pass.

Idempotent: re-running with the same input is safe. Clears the inbox on
success so a crashed/re-fired batch never double-processes.
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commentary_common import (
    SECTION_BEATS_MAX,
    SECTION_BEATS_MIN,
    SECTION_LEN_HARD_MAX,
    SECTION_LEN_HARD_MIN,
    LEN_HARD_MAX,
    LEN_HARD_MIN,
    note_len,
)

# tier1's beat-count bound isn't a named constant in commentary_common.py —
# commentary_merge.py hardcodes it inline; mirrored here for the same gate.
TIER1_BEATS_MIN, TIER1_BEATS_MAX = 2, 6

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMM = os.path.join(ROOT, "plans", "commentary")
TIER1 = os.path.join(COMM, "tier1.json")
CHAPTERS = os.path.join(COMM, "chapters.json")
REVIEW_STATE = os.path.join(COMM, "_review_state.json")
INCOMING = os.path.join(COMM, "_incoming_review.json")
FLAGGED_LOG = os.path.join(COMM, "REVIEW_FLAGGED.md")


def _load(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def append_flagged(key, corpus, voice, beats, note):
    is_new = not os.path.exists(FLAGGED_LOG)
    with open(FLAGGED_LOG, "a", encoding="utf-8") as f:
        if is_new:
            f.write("# Flagged for go/no-go review\n\n"
                     "Entries the review pass was not confident enough to auto-fix — "
                     "genuine theological debate, or a claim the reviewer couldn't "
                     "resolve on its own. See REVIEW_SPEC.md.\n\n")
        f.write(f"## {corpus}: {key}\n\n")
        f.write(f"- **Voice:** {voice}\n")
        f.write(f"- **Note:** {note}\n\n")
        for lead, body in beats:
            f.write(f"- **{lead}** {body}\n")
        f.write("\n")


def main():
    if not os.path.exists(INCOMING):
        print("no _incoming_review.json — nothing to apply")
        return 0
    with open(INCOMING, encoding="utf-8") as f:
        incoming = json.load(f)
    if not isinstance(incoming, list):
        print("ERROR: _incoming_review.json must be a JSON array", file=sys.stderr)
        return 1

    tier1 = _load(TIER1, {})
    chapters = _load(CHAPTERS, {})
    state = _load(REVIEW_STATE, {})
    state.setdefault("tier1", {})
    state.setdefault("chapters", {})

    today = datetime.date.today().isoformat()
    applied, flagged_n, warnings, errors = 0, 0, [], []

    for rec in incoming:
        corpus = rec.get("corpus")
        key = rec.get("key")
        status = rec.get("status")
        note = rec.get("note", "")
        beats = rec.get("beats")
        label = f"{corpus}:{key}"

        if corpus not in ("tier1", "chapters"):
            errors.append(f"{label}: unknown corpus — skipped")
            continue
        if status not in ("ok", "fixed", "flagged"):
            errors.append(f"{label}: unknown status {status!r} — skipped")
            continue

        if corpus == "tier1":
            if key not in tier1:
                errors.append(f"{label}: not found in tier1.json — skipped")
                continue
            current = tier1[key]
        else:
            chapter_key, _, reference = key.rpartition("|")
            sections = chapters.get(chapter_key)
            current = None
            if sections:
                current = next((s for s in sections if s["reference"] == reference), None)
            if current is None:
                errors.append(f"{label}: not found in chapters.json — skipped")
                continue

        if status == "fixed":
            if not beats:
                errors.append(f"{label}: status=fixed but no beats given — skipped")
                continue
            if corpus == "tier1":
                if not (TIER1_BEATS_MIN <= len(beats) <= TIER1_BEATS_MAX):
                    errors.append(f"{label}: expected {TIER1_BEATS_MIN}-{TIER1_BEATS_MAX} beats, got {len(beats)} — skipped")
                    continue
                n = note_len(beats)
                if n < LEN_HARD_MIN or n > LEN_HARD_MAX:
                    errors.append(f"{label}: {n} chars OUTSIDE hard bounds {LEN_HARD_MIN}-{LEN_HARD_MAX} — skipped")
                    continue
            else:
                if not (SECTION_BEATS_MIN <= len(beats) <= SECTION_BEATS_MAX):
                    errors.append(f"{label}: expected {SECTION_BEATS_MIN}-{SECTION_BEATS_MAX} beats, got {len(beats)} — skipped")
                    continue
                n = note_len(beats)
                if n < SECTION_LEN_HARD_MIN or n > SECTION_LEN_HARD_MAX:
                    errors.append(f"{label}: {n} chars OUTSIDE hard bounds {SECTION_LEN_HARD_MIN}-{SECTION_LEN_HARD_MAX} — skipped")
                    continue
            current["beats"] = beats
            if not note:
                warnings.append(f"{label}: status=fixed with no note")

        if status == "flagged":
            append_flagged(key, corpus, current.get("voice", ""), current.get("beats", []), note)
            flagged_n += 1

        state[corpus][key] = {"status": status, "reviewed_at": today, "note": note}
        applied += 1

    _write_json(TIER1, tier1)
    _write_json(CHAPTERS, chapters)
    _write_json(REVIEW_STATE, state)
    os.remove(INCOMING)

    print(f"applied {applied} review result(s) ({flagged_n} flagged)")
    for w in warnings:
        print(f"  [warn] {w}")
    for e in errors:
        print(f"  [ERROR] {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
