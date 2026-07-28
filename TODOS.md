# TODOS

## Infrastructure

### Consolidate the book-abbreviation→number table in index.html

**What:** The 66-entry Chinese book-abbreviation→number table is duplicated verbatim in three places in `index.html`: `Reader.bookMap` (line 389), the local `bookMap` inside `getBookNumber()` (line 718), and the `bookNames` regex-source string (line 800).

**Why:** Any future book-numbering or abbreviation fix (e.g. adding an alternate spelling, or correcting a typo) has to be made correctly in all three places or it silently drifts — one could get fixed and the other two forgotten, producing a bug that only shows up for specific books.

**Context:** Found while reviewing the chapter-by-chapter commentary pilot plan (`commentary` branch, 2026-07-27). The pilot's design reuses `Reader.bookMap` and `getFullBookName()` but doesn't touch `getBookNumber()` or the regex source, so this is pre-existing debt unrelated to that plan's file surface — fixing it there would have broken the "minimal diff" scope for that PR. Fix: extract to one shared const (e.g. `Reader.bookMap` as the single source), have `getBookNumber()` and the regex-source builder both derive from it instead of hardcoding their own copy.

**Effort:** S
**Priority:** P3
**Depends on:** None
