#!/usr/bin/env python3
"""Shared helpers for the commentary authoring pipeline (Tier 1 verse notes
and chapter-grain notes both use these): day-label parsing and house-style
length validation.
"""
import re

# House-style length target (visible chars, whitespace stripped). See TIER1_SPEC.md.
LEN_MIN, LEN_MAX = 450, 600
LEN_HARD_MIN, LEN_HARD_MAX = 400, 660

# Per-section bounds for chapter commentary (CHAPTER_SPEC.md): each chapter is
# now a handful of pericope-level sections rather than one whole-chapter note,
# so each section covers less ground than a Tier 1 / old whole-chapter entry
# and is validated against its own (narrower) length target.
SECTION_LEN_MIN, SECTION_LEN_MAX = 350, 500
SECTION_LEN_HARD_MIN, SECTION_LEN_HARD_MAX = 300, 550
SECTION_BEATS_MIN, SECTION_BEATS_MAX = 3, 4


def day_num(entry):
    m = re.search(r"第\s*(\d+)\s*/\s*365", entry.get("day_label", ""))
    return int(m.group(1)) if m else None


def note_len(beats):
    """Visible-char count of a beats list ([[lead, body], ...])."""
    text = "".join((lead or "") + (body or "") for lead, body in beats)
    return len(re.sub(r"\s+", "", text))
