# Chapter Commentary — Authoring Spec

This is the complete playbook for drafting the chapter-by-chapter commentary
pilot. A fresh (cron-fired) session with no prior conversation should be able
to execute one batch correctly from this file alone. **Work fully
autonomously — never pause to ask permission or confirm.** Nobody is
available to respond; if you stop and wait, the batch is wasted.

## What this is

A companion to [TIER1_SPEC.md](TIER1_SPEC.md) (verse-grain commentary, one
key verse per *reading day*), but keyed to the Bible's own **chapter**
structure instead, decoupled from the reading plan's day boundaries.

**Each chapter is a handful of pericope-level *sections*, not one
whole-chapter note.** (Revised 2026-07-28 — the original pilot authored one
key verse + 4-5 beats per whole chapter; that under-covers any chapter with
more than one real movement, e.g. Luke 15's three parables collapsed into a
single reflection on one of them. `chapters.json` is now `{"书 章": [section,
...]}` — an array — so a chapter can carry as many sections as it actually
needs.) It surfaces in the app as a tappable mark on every verse in the Bible
reading panel: tapping a verse inside a section's own range shows that
section's note (an "exact" mark, same tier as a Tier 1 verse hit); tapping a
verse between sections falls back to the nearest section, shown as an
approximate "chapter" mark. See `index.html`'s `resolveVerseCommentary` and
the design doc at
`~/.gstack/projects/jteng-daily-walking/jingteng-commentary-design-20260727-204502.md`
for the full architecture.

**Current pilot book: 使徒行传 (Acts), all 28 chapters.** 路加福音 (Luke)
and 约翰福音 (John) are both fully drafted (24/24 and 21/21). Acts is
narrative history (Luke's sequel), so it takes the same Carson / Sinclair
Ferguson voice as the Gospels (see TIER1_SPEC.md's genre table). When Acts
is fully drafted, moving to the next book means editing three constants at
the top of `scripts/chapter_status.py` (`PILOT_BOOK_NAME` /
`PILOT_BOOK_NUMBER` / `PILOT_CHAPTERS`) — see that file's inline comments
for exact locations.

## Key difference from Tier 1: you choose the sections

Tier 1 authors a note for an already-chosen verse (the day's `verse_parts`).
Chapter commentary has no verse pre-selected — `chapter_status.py --next N`
gives you the **full text of the chapter**, and breaking it into sections is
your first job before writing anything.

- Read the whole chapter and identify its natural pericopes — the places a
  study Bible or preaching outline would put a paragraph break: a scene
  change, a new parable, a shift from narrative to teaching, etc.
- **Typically 3-5 sections per chapter.** A short or single-scene chapter
  (e.g. a brief narrative aside) may need only 2; don't force more sections
  than the chapter's actual structure supports. A long chapter with several
  distinct units (e.g. Luke 15's three parables, Luke 18's several short
  pericopes) may need up to 5-6.
- Each section gets its own key verse or short range — the same convention
  as Tier 1 (prefer a single verse or a tight 2-4 verse range that carries
  that *section's* central movement, not the whole chapter's). Write it as
  `"C:V"` or `"C:V-V"` in `key_verse` — the merge script resolves the verse
  text from the chapter automatically.
- Sections should roughly span the chapter (few large gaps), but don't force
  contiguous coverage — a short connecting verse between two pericopes
  doesn't need its own section; it'll fall back to whichever neighboring
  section is closer when a reader taps it.

## House style

Identical to Tier 1's (see TIER1_SPEC.md for the full rationale) — the two
corpora should read as one voice across the app. Applies **per section**:

- **Length: 350-450 visible characters** (whitespace-stripped), hard bounds
  300-550, enforced by `chapter_merge.py`. Each section is narrower in scope
  than a whole-chapter note used to be — don't pad to reach the old
  450-600 range.
- **Structure: 3-4 beats**, each `[lead, body]`. Standard arc, compressed
  from Tier 1's 4-5 since a section is a smaller unit of text:
  1. **Observe the text** — what happens in this section, its place in the
     chapter's flow, a repeated word or turn.
  2. **The key term / phrase** — the pivotal word in the chosen verse(s).
  3. *(if the section carries it)* **Connect to Christ** — redemptive-
     historical line to the gospel. Fold into beat 2 on a shorter section
     rather than forcing a fourth beat where there isn't room.
  4. **默想** (always last, lead = `默想。`) — one or two second-person
     application questions. Every section ends with its own — each section
     is independently tappable while reading, so each must be a complete,
     self-contained reflection, not half a thought that depends on a reader
     having also opened a different section of the same chapter.
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
   below makes an over- or under-shoot harmless.
3. For each chapter: read the full text, break it into 3-5 sections per
   "Key difference" above, write each section's beats per the house style.
4. **Persist in sub-chunks of ~2 chapters' worth of sections** (a chapter now
   produces 3-5x the content of the old single-note pilot, so a smaller
   chunk keeps loss-protection granularity similar to before):
   - Write `plans/commentary/_incoming_chapters.json` = JSON array of
     `{"chapter": N, "sections": [{"key_verse": "C:V" or "C:V-V", "voice": "...", "beats": [["lead","body"], ...]}, ...]}`.
   - `python3 scripts/chapter_merge.py` (validates length/beat-count per
     section via `commentary_common.py`, upserts into `chapters.json` by
     section reference — safe to re-run/extend a chapter across multiple
     chunks — and clears the inbox).
   - `git add -A && git commit -m "Chapter commentary: Luke N-M"`.
5. Repeat step 4 until remaining chapters are exhausted or usage runs out.
6. `python3 scripts/chapter_status.py` — if `remaining: 0` for the current
   pilot book, the run is complete: `CronList` then `CronDelete` this job,
   and stop. (If there's a next book queued, update the three constants
   per "Current pilot book" above instead of deleting the job.)

## Resume guarantee

"Remaining" is always computed as: chapters in `PILOT_CHAPTERS` whose key
(`"书名 章"`) is absent from `chapters.json`. A chapter counts as drafted
once its key exists with at least one section — so within a chapter, adding
sections across multiple firings/chunks is safe (upsert-by-reference in
`chapter_merge.py`), but a chapter you've started should be finished (all its
sections written) in the same firing before moving to the next chapter,
since `chapter_status.py` has no notion of "partially sectioned." This is the
same no-shared-state guarantee TIER1_SPEC.md's pipeline already proved across
100→310 entries over multiple unattended cron batches without losing work.

## Sanity checks before ending a batch

- `python3 -m pytest tests/` should still pass (commentary_common.py's
  regression tests + the rest of the suite).
- `python3 scripts/chapter_status.py` output should show `drafted` increased
  by exactly the number of *chapters* (not sections) merged this batch.
