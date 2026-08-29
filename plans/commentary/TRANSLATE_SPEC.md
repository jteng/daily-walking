# Chapter Commentary — English Translation Spec (beats_en)

This is the playbook for translating the already-drafted Chinese chapter
commentary (`plans/commentary/chapters.json`, complete at 1100/1100
chapters per CHAPTER_SPEC.md) into English. A fresh (cron-fired) session
with no prior conversation should be able to execute one batch correctly
from this file alone. **Work fully autonomously — never pause to ask
permission or confirm.** Nobody is available to respond; if you stop and
wait, the batch is wasted.

The user is on a metered subscription and explicitly asked this effort to
be *paced* — don't try to translate everything in one sitting. Each cron
firing does a bounded batch and stops; the cron schedule itself provides
the pacing across many firings.

## What this is

Every chapter section in `chapters.json` has Chinese `beats` (3-4 `[lead,
body]` pairs). This pass adds a parallel `beats_en` array of the same
length to each section — a faithful, natural-English rendering, not a
literal word-for-word translation. Nothing else about a section (its
`reference`, `verse_text`, `voice`, or Chinese `beats`) changes.

**Scope: all 66 books in canonical order** (`bible_books.BOOKS`, numbered
1-66, Genesis through Revelation) — this is *not* the drafting pilot's
NT-first `QUEUE`. Translation has been proceeding straight through in
canonical order and, as of 2026-08-29, has reached Song of Songs (books
1-21 fully translated; Song of Songs 3/8 done; Isaiah through Revelation
still untranslated — 515 chapters remaining of 1189 total chapter-entries).
`scripts/translate_status.py` walks this in canonical order automatically.

## House style

- **Faithful, idiomatic English** — translate meaning and register, not
  word order. The Chinese was already written in a warm, reverent
  expository voice (Keller/Piper/Carson/etc. per book); the English
  should read like it was drafted by that same voice natively, not like a
  translation.
- **Quoted Scripture: ESV-style English wording.** When a beat quotes the
  passage's own text (most leads do — they're a clause lifted from
  `verse_text`), render it in standard modern English Bible phrasing
  matching the existing translated entries (e.g. "In the beginning, God
  created the heavens and the earth..."), not a fresh ad-hoc translation
  of the Chinese back into English.
- **Cross-references: converted to English form.** `西一 15` becomes
  `Colossians 1:15`; `罗八 29` becomes `Romans 8:29`. Use standard English
  book names/abbreviations, not the Chinese short forms.
- **默想 (meditation) beats**: translate the second-person application
  questions naturally — "今天，你是否愿意..." becomes "Today, are you
  willing to...", not a stilted calque.
- **Length/structure**: beats_en does not need to hard-match the Chinese
  character-count bounds (those are Chinese-specific); just keep each
  beat's English roughly proportionate to its Chinese counterpart — don't
  pad or truncate.

## Batch procedure (one cron firing)

1. `python3 scripts/translate_status.py` — see how many chapters remain,
   current book, upcoming books.
2. `python3 scripts/translate_status.py --next 15` — prints the next 15
   untranslated chapters' full content (every section's reference,
   verse_text, voice, and Chinese beats to translate), possibly spanning
   a book boundary. 15 is a batch-size choice for pacing, not a hard
   limit — a firing may stop partway through if usage runs low; that's
   fine, the resume guarantee below makes an over- or under-shoot
   harmless. Do not increase this above ~20 per firing without the user's
   say-so — the batch size is deliberately conservative to pace token
   spend across firings.
3. For each chapter, for each section: translate `beats` -> `beats_en`
   per house style above, preserving the exact `reference`.
4. **Persist in sub-chunks of ~3 chapters** (matches the granularity of
   prior translation commits, keeps loss-protection tight):
   - Write `plans/commentary/_incoming_translations.json` = JSON array of
     `{"book": "书名", "chapter": N, "sections": [{"reference": "C:V" or "C:V-V", "beats_en": [["lead_en","body_en"], ...]}, ...]}`.
     Every section for a chapter must be present (translate_merge.py
     validates the beats_en count matches that section's existing beats
     count).
   - `python3 scripts/translate_merge.py` (validates, upserts beats_en by
     section reference into chapters.json, clears the inbox).
   - `git add -A && git commit -m "Translate chapters.json: <book> N-M to English (beats_en)"`
     (span-a-book-boundary chunks: name both books). Follow the existing
     commit body convention (see `git log --oneline | grep beats_en` for
     examples) — a short paragraph naming what each chapter covers, plus
     a closing progress line "`X/Y chapters.json sections done. Next: <book chapter>.`"
   - `git push origin commentary:main` — **immediately, after every
     single commit, not batched up for later.** This is a clean
     fast-forward that triggers `pages-deploy.yml`. Never let more than
     one commit sit unpushed.
5. Repeat step 4 until the batch worklist from step 2 is exhausted or
   usage runs low. Book boundaries need no special handling — just keep
   going into the next book already present in the worklist.
6. `python3 scripts/translate_status.py` — if `remaining: 0`, the whole
   translation project is complete: `CronList` then `CronDelete` this
   job, run `python3 -m pytest tests/` one last time, and stop. Otherwise
   this firing is done — leave the cron job running for the next firing.

## Resume guarantee

A chapter counts as translated once every section in its `chapters.json`
entry has a `beats_en` of the same length as its `beats`. Within a
chapter, don't leave it partially translated across firings — finish all
of a chapter's sections in the same firing before moving on (mirrors
CHAPTER_SPEC.md's rule). `translate_status.py` has no notion of "partially
translated" beyond that per-chapter check, so a firing that stops
mid-book, mid-batch, or exactly on a book boundary all resume identically
next time — no shared state beyond `chapters.json` itself.

## Sanity checks before ending a batch

- `.venv/bin/python -m pytest tests/` should still pass (plain `python3 -m
  pytest` may fail on `ModuleNotFoundError: pdfplumber` if the venv isn't
  active — that's an unrelated extraction-pipeline dependency, not a sign
  of a translation bug, but use the venv to avoid the false alarm).
- `python3 scripts/translate_status.py` output should show `translated`
  increased by exactly the number of *chapters* (not sections) merged
  this batch.
