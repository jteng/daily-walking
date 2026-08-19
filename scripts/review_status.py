#!/usr/bin/env python3
"""Theological/factual review pass — status / worklist.

Companion to REVIEW_SPEC.md. Unlike the drafting pipelines
(chapter_status.py / commentary_status.py), the content here already exists
in tier1.json and chapters.json — this script's job is only to track which
entries have been *reviewed*, not to author anything.

Review state lives in a sidecar file, plans/commentary/_review_state.json,
kept separate from tier1.json/chapters.json because both of those are
fetch()-ed directly by index.html at runtime — review metadata has no
reader-facing purpose and shouldn't bloat what ships to the client.

Usage:
    python3 scripts/review_status.py                        # summary counts
    python3 scripts/review_status.py --next 60 --corpus tier1
    python3 scripts/review_status.py --next 150 --corpus chapters
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMM = os.path.join(ROOT, "plans", "commentary")
TIER1 = os.path.join(COMM, "tier1.json")
CHAPTERS = os.path.join(COMM, "chapters.json")
REVIEW_STATE = os.path.join(COMM, "_review_state.json")


def _load(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_tier1():
    return _load(TIER1, {})


def load_chapters():
    return _load(CHAPTERS, {})


def load_review_state():
    state = _load(REVIEW_STATE, {})
    state.setdefault("tier1", {})
    state.setdefault("chapters", {})
    return state


def chapter_section_key(chapter_key, section_reference):
    """Composite review-state key for one chapter section, e.g.
    "罗马书 1|1:19-23". chapter_key is chapters.json's own key ("书名 章")."""
    return f"{chapter_key}|{section_reference}"


def tier1_worklist(tier1=None, state=None):
    """[{key, reference, verse_text, voice, beats}, ...] not yet reviewed."""
    tier1 = load_tier1() if tier1 is None else tier1
    state = load_review_state() if state is None else state
    reviewed = state["tier1"]
    items = []
    for ref, rec in tier1.items():
        if ref in reviewed:
            continue
        items.append({
            "key": ref,
            "reference": ref,
            "verse_text": rec.get("verse_text", ""),
            "voice": rec.get("voice", ""),
            "beats": rec.get("beats", []),
        })
    items.sort(key=lambda x: (x.get("key") or ""))
    return items


def chapters_worklist(chapters=None, state=None):
    """[{key, chapter_key, reference, verse_text, voice, beats}, ...] not yet reviewed."""
    chapters = load_chapters() if chapters is None else chapters
    state = load_review_state() if state is None else state
    reviewed = state["chapters"]
    items = []
    for chapter_key, sections in chapters.items():
        for sec in sections:
            key = chapter_section_key(chapter_key, sec["reference"])
            if key in reviewed:
                continue
            items.append({
                "key": key,
                "chapter_key": chapter_key,
                "reference": sec["reference"],
                "verse_text": sec.get("verse_text", ""),
                "voice": sec.get("voice", ""),
                "beats": sec.get("beats", []),
            })
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", type=int, metavar="N", help="print next N unreviewed entries with full context")
    ap.add_argument("--corpus", choices=["tier1", "chapters"], help="which corpus --next applies to (required with --next)")
    args = ap.parse_args()

    if args.next:
        if not args.corpus:
            raise SystemExit("--next requires --corpus tier1|chapters")
        work = tier1_worklist() if args.corpus == "tier1" else chapters_worklist()
        print(f"# next {min(args.next, len(work))} of {len(work)} unreviewed in {args.corpus}")
        print(json.dumps(work[: args.next], ensure_ascii=False, indent=2))
        return

    t1_remaining = len(tier1_worklist())
    ch_remaining = len(chapters_worklist())
    t1_total = len(load_tier1())
    ch_total = sum(len(v) for v in load_chapters().values())

    print("Review pass status")
    print(f"  tier1:    {t1_total - t1_remaining}/{t1_total} reviewed, {t1_remaining} remaining")
    print(f"  chapters: {ch_total - ch_remaining}/{ch_total} sections reviewed, {ch_remaining} remaining")
    if t1_remaining == 0 and ch_remaining == 0:
        print("  ALL DONE — both corpora fully reviewed.")
    elif t1_remaining:
        print("  next up: tier1 (finish before starting chapters)")
    else:
        print("  next up: chapters")


if __name__ == "__main__":
    main()
