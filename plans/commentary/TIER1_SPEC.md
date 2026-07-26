# Tier 1 Verse Commentary — Authoring Spec

This is the complete playbook for drafting the Tier 1 verse-by-verse commentary.
A fresh (cron-fired) session with no prior conversation should be able to execute
one batch correctly from this file alone. **Work fully autonomously — never pause
to ask permission or confirm.**

## What Tier 1 is

A focused expository note on the **single highlighted verse** of each day (the
`verse_parts[0]` reference). It is a *companion* to the day's full-passage
devotional `content`, not a replacement — it does the one thing `content` never
does: sit on one verse. It surfaces in the app as a tap-to-expand card under the
day's verse.

Only days that HAVE a highlighted verse get a note (~310 of 362; the weekly
rest/review days have no `verse_parts` and are skipped automatically).

## House style

- **Length: 450–600 visible characters** (whitespace-stripped). This is enforced.
  A note below 400 or above 660 is rejected by the merge script — fix and re-run.
  On a very simple verse, land near 450 rather than padding; never stretch to fill.
- **Structure: 4–5 beats.** Each beat = `[lead, body]`, rendered as one short
  paragraph with the lead in bold. The standard arc:
  1. **Observe the text** — its place in the passage, structure, a repeated word.
  2. **The key term / phrase** — explain the pivotal word (Hebrew/Greek where it
     illuminates, lightly).
  3. **Scope / implication** — widen to what it establishes.
  4. **Connect to Christ** — redemptive-historical line to the gospel.
  5. **默想** (always the last beat, lead = `默想。`) — one or two personal,
     second-person application questions.
- **Voice: match the expositor to the genre.** Name the blend in the `voice` field.
  - OT narrative (Genesis, Exodus, Samuel–Kings): Derek Kidner / Bruce Waltke
  - Psalms & wisdom: Derek Kidner + Piper
  - Prophets: Alec Motyer
  - Gospels & Acts: Carson / Sinclair Ferguson
  - Epistles (grace/doctrine): MacArthur / R.C. Sproul / Keller
  - Default when unsure: Kent Hughes
- **Language: Simplified Chinese**, matching the reverent, warm register of the
  existing `content`. Use 和合本 verse wording. Cite cross-references in-line in
  the app's short form (e.g. `西一 15`, `罗八 29`).
- No section-title HTML in the beats — plain prose only; the pipeline wraps it.

## Batch procedure (one cron firing)

1. `python3 scripts/commentary_status.py --next 80` — prints the next undone days
   with `day`, `title`, `scripture`, `reference`, `verse_text`. (Batch cap is 80;
   the real limit is your 4-hour usage budget, so the batch may stop earlier. The
   resume logic makes an over- or under-shoot harmless.)
2. Author a note for each day per the house style above.
3. **Persist in sub-chunks of ~10** so a usage cutoff never loses much:
   - Write `plans/commentary/_incoming.json` = JSON array of
     `{"day": N, "voice": "...", "beats": [["lead","body"], ...]}`.
   - `python3 scripts/commentary_merge.py` (validates length, folds into
     `tier1.json`, clears `_incoming.json`).
   - `git add -A && git commit -m "Tier 1 commentary: days X-Y"`.
4. Repeat step 3 until the batch (max 80) is done or usage runs out.
5. `python3 scripts/commentary_status.py` — if `remaining: 0`, the run is
   complete: `CronList` then `CronDelete` this job, and stop.

## Resume guarantee

"Remaining" is always computed as: days with a verse in `bibleData.json` whose
reference is absent from `tier1.json`. So every firing just continues where the
last left off — no counters, no shared state, no double-drafting.
