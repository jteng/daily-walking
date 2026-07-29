import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from commentary_common import (
    LEN_HARD_MAX,
    LEN_HARD_MIN,
    LEN_MAX,
    LEN_MIN,
    SECTION_BEATS_MAX,
    SECTION_BEATS_MIN,
    SECTION_LEN_HARD_MAX,
    SECTION_LEN_HARD_MIN,
    SECTION_LEN_MAX,
    SECTION_LEN_MIN,
    day_num,
    note_len,
)


def test_day_num_parses_standard_label():
    assert day_num({"day_label": "第 156 / 365 天"}) == 156


def test_day_num_parses_without_spaces():
    assert day_num({"day_label": "第156/365天"}) == 156


def test_day_num_missing_label_returns_none():
    assert day_num({}) is None


def test_day_num_unrecognized_format_returns_none():
    assert day_num({"day_label": "Day 156"}) is None


def test_note_len_counts_visible_chars_across_beats():
    beats = [["lead one", "body one"], ["lead two", "body two"]]
    assert note_len(beats) == len("leadonebodyoneleadtwobodytwo")


def test_note_len_strips_all_whitespace_including_internal():
    beats = [["a b", "c\nd\te"]]
    assert note_len(beats) == len("abcde")


def test_note_len_handles_none_lead_or_body():
    beats = [[None, "body"], ["lead", None]]
    assert note_len(beats) == len("bodylead")


def test_note_len_empty_beats_is_zero():
    assert note_len([]) == 0


def test_length_constants_unchanged():
    # Regression guard: these are enforced by commentary_merge.py's validation
    # gate — silently changing them would change which notes get accepted.
    assert (LEN_MIN, LEN_MAX) == (450, 600)
    assert (LEN_HARD_MIN, LEN_HARD_MAX) == (400, 660)


def test_section_constants_unchanged():
    # Regression guard for the chapter-section bounds (CHAPTER_SPEC.md),
    # enforced by chapter_merge.py's per-section validation gate.
    assert (SECTION_LEN_MIN, SECTION_LEN_MAX) == (350, 500)
    assert (SECTION_LEN_HARD_MIN, SECTION_LEN_HARD_MAX) == (300, 550)
    assert (SECTION_BEATS_MIN, SECTION_BEATS_MAX) == (3, 4)
