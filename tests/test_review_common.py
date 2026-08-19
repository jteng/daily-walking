import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import review_apply
import review_status


def test_chapter_section_key_composes_chapter_and_reference():
    assert review_status.chapter_section_key("罗马书 1", "1:19-23") == "罗马书 1|1:19-23"


def test_tier1_worklist_excludes_reviewed_entries():
    tier1 = {
        "创世记 1:27": {"verse_text": "v1", "voice": "Kidner", "beats": []},
        "罗马书 1:20": {"verse_text": "v2", "voice": "MacArthur", "beats": []},
    }
    state = {"tier1": {"创世记 1:27": {"status": "ok"}}, "chapters": {}}
    work = review_status.tier1_worklist(tier1=tier1, state=state)
    assert [w["key"] for w in work] == ["罗马书 1:20"]


def test_tier1_worklist_empty_state_returns_everything():
    tier1 = {"创世记 1:27": {"verse_text": "v1", "voice": "Kidner", "beats": []}}
    state = {"tier1": {}, "chapters": {}}
    work = review_status.tier1_worklist(tier1=tier1, state=state)
    assert len(work) == 1
    assert work[0]["reference"] == "创世记 1:27"


def test_chapters_worklist_excludes_reviewed_sections():
    chapters = {
        "罗马书 1": [
            {"reference": "1:1-13", "verse_text": "a", "voice": "MacArthur + Sproul", "beats": []},
            {"reference": "1:19-23", "verse_text": "b", "voice": "MacArthur + Sproul", "beats": []},
        ]
    }
    state = {"tier1": {}, "chapters": {"罗马书 1|1:1-13": {"status": "ok"}}}
    work = review_status.chapters_worklist(chapters=chapters, state=state)
    assert [w["key"] for w in work] == ["罗马书 1|1:19-23"]


def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def _patch_paths(monkeypatch, tmp_path):
    tier1_path = tmp_path / "tier1.json"
    chapters_path = tmp_path / "chapters.json"
    state_path = tmp_path / "_review_state.json"
    incoming_path = tmp_path / "_incoming_review.json"
    flagged_path = tmp_path / "REVIEW_FLAGGED.md"
    monkeypatch.setattr(review_apply, "TIER1", str(tier1_path))
    monkeypatch.setattr(review_apply, "CHAPTERS", str(chapters_path))
    monkeypatch.setattr(review_apply, "REVIEW_STATE", str(state_path))
    monkeypatch.setattr(review_apply, "INCOMING", str(incoming_path))
    monkeypatch.setattr(review_apply, "FLAGGED_LOG", str(flagged_path))
    return tier1_path, chapters_path, state_path, incoming_path, flagged_path


def _sample_tier1_beats():
    return [
        ["lead one", "body one is long enough to pass validation " * 3],
        ["lead two", "body two is long enough to pass validation " * 3],
        ["lead three", "body three is long enough to pass validation " * 3],
        ["默想。", "personal application question here to close the note out nicely."],
    ]


def test_apply_ok_marks_reviewed_without_changing_content(monkeypatch, tmp_path):
    tier1_path, chapters_path, state_path, incoming_path, flagged_path = _patch_paths(monkeypatch, tmp_path)
    original_beats = [["lead", "body"]]
    _write_json(tier1_path, {"创世记 1:27": {"verse_text": "v", "voice": "Kidner", "beats": original_beats}})
    _write_json(chapters_path, {})
    _write_json(incoming_path, [{"corpus": "tier1", "key": "创世记 1:27", "status": "ok", "note": ""}])

    assert review_apply.main() == 0

    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["tier1"]["创世记 1:27"]["status"] == "ok"
    tier1_after = json.loads(tier1_path.read_text(encoding="utf-8"))
    assert tier1_after["创世记 1:27"]["beats"] == original_beats
    assert not incoming_path.exists()
    assert not flagged_path.exists()


def test_apply_fixed_patches_beats_and_marks_reviewed(monkeypatch, tmp_path):
    tier1_path, chapters_path, state_path, incoming_path, flagged_path = _patch_paths(monkeypatch, tmp_path)
    _write_json(tier1_path, {"罗马书 1:20": {"verse_text": "v", "voice": "MacArthur", "beats": [["old", "old body"]]}})
    _write_json(chapters_path, {})
    new_beats = _sample_tier1_beats()
    _write_json(incoming_path, [{
        "corpus": "tier1", "key": "罗马书 1:20", "status": "fixed",
        "note": "collapsed purpose/result", "beats": new_beats,
    }])

    assert review_apply.main() == 0

    tier1_after = json.loads(tier1_path.read_text(encoding="utf-8"))
    assert tier1_after["罗马书 1:20"]["beats"] == new_beats
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["tier1"]["罗马书 1:20"] == {
        "status": "fixed", "reviewed_at": state["tier1"]["罗马书 1:20"]["reviewed_at"],
        "note": "collapsed purpose/result",
    }


def test_apply_fixed_rejects_beats_outside_length_bounds(monkeypatch, tmp_path):
    tier1_path, chapters_path, state_path, incoming_path, flagged_path = _patch_paths(monkeypatch, tmp_path)
    original_beats = [["old", "old body"]]
    _write_json(tier1_path, {"罗马书 1:20": {"verse_text": "v", "voice": "MacArthur", "beats": original_beats}})
    _write_json(chapters_path, {})
    _write_json(incoming_path, [{
        "corpus": "tier1", "key": "罗马书 1:20", "status": "fixed",
        "note": "too short", "beats": [["lead", "way too short"]],
    }])

    assert review_apply.main() == 0

    tier1_after = json.loads(tier1_path.read_text(encoding="utf-8"))
    assert tier1_after["罗马书 1:20"]["beats"] == original_beats
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert "罗马书 1:20" not in state["tier1"]


def test_apply_flagged_writes_report_and_leaves_content_untouched(monkeypatch, tmp_path):
    tier1_path, chapters_path, state_path, incoming_path, flagged_path = _patch_paths(monkeypatch, tmp_path)
    _write_json(chapters_path, {
        "罗马书 1": [{"reference": "1:19-23", "verse_text": "v", "voice": "MacArthur + Sproul", "beats": [["a", "b"]]}]
    })
    _write_json(tier1_path, {})
    _write_json(incoming_path, [{
        "corpus": "chapters", "key": "罗马书 1|1:19-23", "status": "flagged",
        "note": "contested Calvinist/Arminian framing, not a clear error",
    }])

    assert review_apply.main() == 0

    assert flagged_path.exists()
    text = flagged_path.read_text(encoding="utf-8")
    assert "罗马书 1|1:19-23" in text
    assert "contested Calvinist/Arminian framing" in text
    chapters_after = json.loads(chapters_path.read_text(encoding="utf-8"))
    assert chapters_after["罗马书 1"][0]["beats"] == [["a", "b"]]
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["chapters"]["罗马书 1|1:19-23"]["status"] == "flagged"


def test_apply_unknown_key_is_skipped_as_error(monkeypatch, tmp_path):
    tier1_path, chapters_path, state_path, incoming_path, flagged_path = _patch_paths(monkeypatch, tmp_path)
    _write_json(tier1_path, {})
    _write_json(chapters_path, {})
    _write_json(incoming_path, [{"corpus": "tier1", "key": "不存在 9:9", "status": "ok", "note": ""}])

    assert review_apply.main() == 0

    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["tier1"] == {}


def test_apply_clears_incoming_inbox(monkeypatch, tmp_path):
    tier1_path, chapters_path, state_path, incoming_path, flagged_path = _patch_paths(monkeypatch, tmp_path)
    _write_json(tier1_path, {"创世记 1:27": {"verse_text": "v", "voice": "Kidner", "beats": [["a", "b"]]}})
    _write_json(chapters_path, {})
    _write_json(incoming_path, [{"corpus": "tier1", "key": "创世记 1:27", "status": "ok", "note": ""}])

    review_apply.main()

    assert not incoming_path.exists()
