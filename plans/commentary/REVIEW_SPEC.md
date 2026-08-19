# Theological Review Pass — Playbook

This is the complete playbook for reviewing the already-published Tier 1
verse commentary (`tier1.json`) and chapter commentary (`chapters.json`) for
theological/factual accuracy. A fresh (cron-fired) session with no prior
conversation should be able to execute one batch correctly from this file
alone. **Work fully autonomously — never pause to ask permission or
confirm.** Nobody is available to respond; if you stop and wait, the batch
is wasted.

## What this is

Neither `TIER1_SPEC.md` nor `CHAPTER_SPEC.md` (the specs that drove the
original autonomous drafting) include a review step — the `voice` field on
every entry (e.g. `"MacArthur + Sproul"`) is only a stylistic instruction
given *before* drafting, never checked *after*. This pass closes that gap:
read what was already published, and ask whether the tagged expositor(s)
would actually agree with what's on the page.

It was triggered by a real example. Romans 1:19-23's commentary claimed
general revelation's "功用是定罪性的" (function IS condemnatory). Checked
against MacArthur's own commentary and 唐崇荣's *普遍启示与特殊启示*, both
explicitly distinguish revelation's *purpose* (self-disclosure, meant to
elicit worship) from inexcusability as the *result* of humans suppressing
it — the published claim collapsed that distinction. That's the shape of
error this pass hunts for: not heresy, but an overstated or flattened
version of a claim the named voices would actually qualify.

**This is a review pass, not new authoring.** You are not writing fresh
commentary — you are reading what exists and either leaving it, correcting
a specific overstatement, or flagging it as a genuine judgment call.

## Checklist

For each entry, read the full `beats` array against its `verse_text` and
`voice` tag, watching for:

1. **Purpose/result collapse** — phrasing like "…的功用是…性的" or
   "…不是…而是…" that flattens a text's *stated purpose* into a *downstream
   result* (or the reverse). The Romans 1:20 case exactly. This is the
   single most common failure mode found so far — read every "不是A，而是B"
   construction with extra suspicion.
2. **Absolutist overreach** — "唯一"/"从来不是"/totalizing claims where
   mainstream evangelical exegesis holds a both/and, or where there's a real
   live debate the entry has flattened into a false certainty.
3. **Verse-text fidelity** — `verse_text` should read as a faithful,
   unmodified 和合本 quotation of the reference given. (Mechanical — you're
   spot-checking for corruption/truncation, not re-deriving the whole XML
   lookup by hand.)
4. **Cross-reference accuracy** — short-form refs in the prose (`西一 15`,
   `罗八 29`) should actually say what the beat claims they say. Check any
   cross-reference that's doing real argumentative work; skip ones that are
   just "see also" decoration.
5. **Voice plausibility** — would the tagged expositor pairing actually
   hold this claim? Reason from your own theological knowledge of these
   writers — MacArthur, Sproul, Carson, Ferguson, Kidner, Waltke, Piper,
   Motyer, Keller, plus 唐崇荣/Goldsworthy as secondary reference points from
   this project's other reviewed corpora (see `[[devotional-voice-preferences]]`
   in project memory for the full roster and their theological centers of
   gravity). **Do not web-search every claim** — at ~4,800 entries that's
   infeasible (verifying the single Romans 1:20 claim took ~8 searches).
   Reserve WebSearch/WebFetch for the rare case where you're genuinely
   unsure and a quick check would resolve it.
6. **Internal coherence** — beats within one entry/section shouldn't
   contradict each other (e.g. beat 2 asserts X, beat 3's 默想 presupposes
   not-X).

## Auto-fix vs. flag

This is the judgment call that matters most — get it wrong in either
direction and the pass isn't trustworthy.

- **Fix it** when multiple named voices in this project's own tradition
  would clearly reject the claim as stated — i.e. the same kind of
  convergent evidence that resolved Romans 1:20 (MacArthur's own words,
  Tong's own words, and mainstream commentary consensus all agreeing against
  the published claim). If you're confident a careful reader of MacArthur,
  Carson, Kidner, etc. would call this an overstatement, fix it.
- **Flag it, don't touch it** when the disagreement is a live, legitimate
  debate *within* evangelical scholarship the entry's voice pairing could
  reasonably land on either side of — Calvinist/Arminian tension on specific
  texts, continuationism/cessationism, differing eschatology camps, etc.
  Don't let your own theological leanings silently overwrite a defensible
  reading just because a different reasonable reading exists. When in doubt,
  flag rather than fix.
- **Leave it (`"ok"`)** for everything else — the large majority. Most
  entries will have no issue; don't manufacture a finding to justify the
  pass.

## Fix constraints

When fixing, only rewrite the specific beat(s) carrying the flagged claim —
don't rewrite an entry wholesale, and don't change its `voice` tag. Keep the
same `[lead, body]` shape. The replacement `beats` array must still satisfy
the corpus's existing house-style bounds (enforced by `review_apply.py`,
reusing `commentary_common.py` — the same gate `chapter_merge.py` /
`commentary_merge.py` already apply to fresh drafts):

- **tier1**: 2-6 beats, 400-660 visible chars total (target 450-600).
- **chapters**: 3-4 beats, 300-550 visible chars total (target 350-500).

If a fix would need to grow or shrink beyond the target range, tighten or
expand the surrounding prose in the same beat(s) to land back in bounds —
don't let the fix silently violate house style.

## Batch procedure (one cron firing)

1. `python3 scripts/review_status.py` — see how many entries remain in each
   corpus. **Finish tier1 (310 entries) before starting chapters (4,481
   sections)** — smaller corpus first.
2. `python3 scripts/review_status.py --next N --corpus tier1` (N ≈ 60) or
   `--corpus chapters` (N ≈ 150) once tier1 is done — prints the next N
   unreviewed entries as `{key, reference, verse_text, voice, beats}`
   (chapters entries also include `chapter_key`). The cap is a batch-size
   choice, not a usage estimate — the real limit is your usage budget, so a
   firing may stop partway through; the resume guarantee below makes an
   over- or under-shoot harmless.
3. For each entry, apply the checklist and decide `ok` / `fixed` / `flagged`
   per the rule above.
4. **Persist in sub-chunks of ~20 entries** (tighter than the drafting
   pipeline's chunks, since a review batch can include far more entries per
   firing than a drafting batch):
   - Write `plans/commentary/_incoming_review.json` = JSON array of
     `{"corpus": "tier1"|"chapters", "key": "...", "status": "ok"|"fixed"|"flagged", "note": "...", "beats": [[...]] }`
     (`beats` required for `"fixed"`, omit/null otherwise; `note` required
     for `"fixed"`/`"flagged"`, explaining what's wrong and why — this note
     is what shows up in `REVIEW_FLAGGED.md` for flagged items, so make it
     legible to the user later without this session's context).
   - `python3 scripts/review_apply.py` (validates, patches `tier1.json` /
     `chapters.json` for `"fixed"` entries, records every entry's outcome in
     `plans/commentary/_review_state.json`, appends flagged entries to
     `plans/commentary/REVIEW_FLAGGED.md`, clears the inbox).
   - `git add -A && git commit -m "Review pass: <corpus> batch <range/desc>"`.
   - `git push origin commentary:main` — **immediately, after every single
     commit, not batched up for later.** Same discipline as the drafting
     pipeline: a clean fast-forward that triggers `pages-deploy.yml`, so
     fixes go live per chunk, and nothing sits unpushed if a firing gets cut
     off.
5. Repeat step 4 until the worklist from step 2 is exhausted or usage runs
   out.
6. `python3 -m pytest tests/` (via `.venv/bin/python` if system Python lacks
   `pdfplumber`) — should still pass.
7. `python3 scripts/review_status.py` — if both corpora show
   `remaining: 0`, the pass is complete: leave `REVIEW_FLAGGED.md` in place
   for the user's own go/no-go read-through, `CronList` then `CronDelete`
   this job, and stop. Otherwise, this firing is done — leave the cron job
   running for the next firing to pick up wherever `review_status.py` says
   to.

## Resume guarantee

"Remaining" is always computed as: every tier1 reference absent from
`_review_state.json["tier1"]`, plus every chapter section key (`"书名
章|C:V"`) absent from `_review_state.json["chapters"]`. The sidecar state
file is the only source of truth for review progress — `tier1.json` and
`chapters.json` themselves are never used to infer what's been reviewed, so
a firing that stops mid-batch, mid-chunk, or exactly on a corpus boundary
all resume identically next time. This is the same no-shared-state guarantee
`TIER1_SPEC.md`/`CHAPTER_SPEC.md`'s pipelines already proved across their
own runs.

## Why review state isn't stored in tier1.json / chapters.json

Both files are `fetch()`-ed directly by `index.html` at runtime (see
`resolveVerseCommentary` and the `tier1.json`/`chapters.json` fetch calls).
Adding review metadata to every entry would ship dead weight to every reader
for no reader-facing benefit — so it lives in
`plans/commentary/_review_state.json` instead, a file the app never fetches.
