# TODOS

## Infrastructure

### Consolidate the book-abbreviation→number table in index.html

**What:** The 66-entry Chinese book-abbreviation→number table is duplicated verbatim in three places in `index.html`: `Reader.bookMap` (line 389), the local `bookMap` inside `getBookNumber()` (line 718), and the `bookNames` regex-source string (line 800).

**Why:** Any future book-numbering or abbreviation fix (e.g. adding an alternate spelling, or correcting a typo) has to be made correctly in all three places or it silently drifts — one could get fixed and the other two forgotten, producing a bug that only shows up for specific books.

**Context:** Found while reviewing the chapter-by-chapter commentary pilot plan (`commentary` branch, 2026-07-27). The pilot's design reuses `Reader.bookMap` and `getFullBookName()` but doesn't touch `getBookNumber()` or the regex source, so this is pre-existing debt unrelated to that plan's file surface — fixing it there would have broken the "minimal diff" scope for that PR. Fix: extract to one shared const (e.g. `Reader.bookMap` as the single source), have `getBookNumber()` and the regex-source builder both derive from it instead of hardcoding their own copy.

**Effort:** S
**Priority:** P3
**Depends on:** None

### Add keyboard/ARIA support to the prose verse-ref hover tooltip

**What:** `.verse-ref` spans (index.html, inside `enhanceVerseReferences`) have no `tabindex`/`role`/keyboard handler — a keyboard or screen-reader user can't reach an inline scripture-reference tooltip at all.

**Why:** The Bible-panel commentary tap feature (same branch) fixes this exact gap for its own tooltip trigger; leaving this one unfixed means the app has two nearly-identical tooltip patterns with inconsistent accessibility.

**Pros:** Small, well-scoped; consistent a11y app-wide once done.
**Cons:** Not blocking; slightly wider diff if bundled into another PR.

**Context:** Noticed while refactoring `showVerseTooltipFromData` into a shared `showTooltipAt()` helper for the Bible-panel commentary tap feature (`commentary` branch, 2026-07-28) — cheapest to fix now while the helper is fresh, but deferred to keep that PR scoped to the Bible panel.

**Effort:** S
**Priority:** P3
**Depends on:** None

### Add next/prev commentary-verse navigation within a chapter

**What:** Small ▸/▷ controls (or similar) letting a reader jump directly between marked verses in the currently displayed chapter(s), instead of scanning for underlines.

**Why:** Serves someone who wants to deliberately read through the available commentary rather than discover it incidentally while reading Scripture.

**Pros:** Turns the tap feature into a real "study mode" for engaged readers.
**Cons:** Real new UI surface (controls, placement, keyboard behavior); low payoff today since only 14 chapters have any commentary.

**Context:** Surfaced as a cherry-pick during `/plan-ceo-review` of the Bible-panel commentary-tap plan (`commentary` branch, 2026-07-28); deferred because coverage is still too sparse to justify dedicated navigation UI. Revisit once chapter-commentary coverage grows substantially past the pilot.

**Effort:** S/M
**Priority:** P3
**Depends on:** The Bible-panel tap feature itself (verse→note lookup), already shipped on this branch.

### Add JS test coverage for index.html's reader logic

**What:** This repo has Python tests (`tests/test_commentary_common.py`) but zero JS test infrastructure — everything in `index.html` (parsing, rendering, the commentary lookup/tap logic) is untested except by manual browser verification.

**Why:** The verse→note lookup (range expansion, chapter fallback) added for the Bible-panel commentary tap feature is exactly the kind of small pure-function logic that's cheap to unit test and easy to silently break in a later edit. A real bug (the outside-click-closes-tooltip listener not recognizing the new trigger element) only surfaced during manual browser testing, not before — automated coverage would have caught it immediately.

**Pros:** Would catch regressions in `parseScripture`, the commentary index, and similar logic without a full browser session.
**Cons:** Requires standing up a JS test runner in a repo that currently has none — real infra decision (which runner, how it fits `make` targets), not a small addition.

**Context:** Out of scope for the Bible-panel commentary tap feature specifically (`commentary` branch, 2026-07-28) — that feature shipped on manual browser verification, consistent with how the rest of `index.html` is tested today.

**Effort:** M (infra) + S (initial tests)
**Priority:** P3
**Depends on:** None
