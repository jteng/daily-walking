# Chapter Commentary — Authoring Spec

This is the complete playbook for drafting the chapter-by-chapter commentary
pilot. A fresh (cron-fired) session with no prior conversation should be able
to execute one batch correctly from this file alone. **Work fully
autonomously — never pause to ask permission or confirm.** Nobody is
available to respond; if you stop and wait, the batch is wasted.

## What this is

A companion to [TIER1_SPEC.md](TIER1_SPEC.md) (verse-grain commentary, one
key verse per *reading day*), but keyed to the Bible's own **chapter**
structure instead, decoupled from the reading plan's day boundaries. It
surfaces in the app as one collapsible "逐章释义" card per chapter, stacked
on any reading day whose highlighted verse falls in a pilot book — see
`index.html`'s `PILOT_BOOKS` constant and the design doc at
`~/.gstack/projects/jteng-daily-walking/jingteng-commentary-design-20260727-204502.md`
for the full architecture and gating rule.

**Current pilot book: 路加福音 (Luke), all 24 chapters.** 约翰福音 (John)
1-2 already shipped as the original proof of concept and needs no further
work. When Luke is fully drafted, moving to the next book means editing three
constants at the top of `scripts/chapter_status.py`
(`PILOT_BOOK_NAME` / `PILOT_BOOK_NUMBER` / `PILOT_CHAPTERS`) and adding the
new book's full Chinese name to `PILOT_BOOKS` in `index.html` — see that
file's inline comments for exact locations.

## Key difference from Tier 1: you choose the key verse

Tier 1 authors a note for an already-chosen verse (the day's `verse_parts`).
Chapter commentary has no such verse pre-selected — `chapter_status.py --next
N` gives you the **full text of the chapter**, and picking the key verse (or
short verse range) is your first job before writing anything. Choose the
verse or range that best carries the chapter's central movement — usually
where the narrative turns, the theological claim lands, or (in Luke)
where Jesus's own words or action crystallize the scene's point. Prefer a
single verse or a tight 2-4 verse range (matches Tier 1's own convention of
occasional short ranges like `"9:12-13"`). Write the choice as `"C:V"` or
`"C:V-V"` in the `key_verse` field — the merge script resolves the verse text
from the chapter automatically, so you don't need to copy it in yourself.

## House style

Identical to Tier 1's (see TIER1_SPEC.md for the full rationale) — the two
corpora should read as one voice across the app:

- **Length: 450–600 visible characters** (whitespace-stripped), hard bounds
  400-660, enforced by `chapter_merge.py`. On a simple chapter, land near 450
  rather than padding.
- **Structure: 4-5 beats**, each `[lead, body]`. Standard arc:
  1. **Observe the text** — its place in the chapter/book, structure, a
     repeated word or turn.
  2. **The key term / phrase** — the pivotal word in the chosen verse(s).
  3. **Scope / implication** — widen to what the chapter establishes.
  4. **Connect to Christ** — redemptive-historical line to the gospel.
  5. **默想** (always last, lead = `默想。`) — one or two second-person
     application questions.
- **Voice: match the expositor to genre.** For Luke (Gospel narrative):
  **Carson / Sinclair Ferguson** — the same blend already used for John.
  (Full genre table in TIER1_SPEC.md if the pilot ever moves to a different
  kind of book.)
- **Language: Simplified Chinese**, 和合本 wording, warm reverent register
  matching existing content. Cross-references in short form (`西一 15`,
  `罗八 29`). No section-title HTML — plain prose only.

## Batch procedure (one cron firing)

1. `python3 scripts/chapter_status.py` — see how many chapters remain.
2. `python3 scripts/chapter_status.py --next 40` — prints every undone
   chapter's full verse-by-verse text as `{key, book, chapter, verse_count,
   verses}`. The cap (40) is intentionally above the pilot book's total
   chapter count (24) — don't self-limit to a small slice; attempt the whole
   remaining book each firing. The real limit is your 4-hour usage budget, so
   a firing may stop partway through — that's fine, the resume guarantee
   below makes an over- or under-shoot harmless. Lower the 40 only if a
   future, larger pilot book makes one firing's context genuinely too much
   to hold at once.
3. For each chapter: read the full text, choose the key verse/range, write
   the beats per the house style above.
4. **Persist in sub-chunks of ~4** (smaller than Tier 1's 10 — a whole
   chapter is more source text to synthesize than a single pre-chosen verse,
   so a chunk takes longer). This is about loss-protection granularity
   *within* a firing (commit every ~4 chapters so a cutoff mid-firing loses
   little), not a cap on how much the firing as a whole should attempt:
   - Write `plans/commentary/_incoming_chapters.json` = JSON array of
     `{"chapter": N, "key_verse": "C:V" or "C:V-V", "voice": "...", "beats": [["lead","body"], ...]}`.
   - `python3 scripts/chapter_merge.py` (validates length/beat-count via
     `commentary_common.py`, folds into `chapters.json`, clears the inbox).
   - `git add -A && git commit -m "Chapter commentary: Luke N-M"`.
5. Repeat step 4 until remaining chapters are exhausted or usage runs out.
6. `python3 scripts/chapter_status.py` — if `remaining: 0` for the current
   pilot book, the run is complete: `CronList` then `CronDelete` this job,
   and stop. (If there's a next book queued, update the three constants
   per "Current pilot book" above instead of deleting the job.)

## Resume guarantee

"Remaining" is always computed as: chapters in `PILOT_CHAPTERS` whose key
(`"书名 章"`) is absent from `chapters.json`. Every firing continues where
the last left off — no counters, no shared state, no double-drafting. This
is the same guarantee TIER1_SPEC.md's pipeline already proved across 100→310
entries over multiple unattended cron batches without losing work.

## Sanity checks before ending a batch

- `python3 -m pytest tests/` should still pass (commentary_common.py's
  regression tests + the rest of the suite).
- `python3 scripts/chapter_status.py` output should show `drafted` increased
  by exactly the number of chapters merged this batch.
