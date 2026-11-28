# Luke — Resume Notes

## The request

The user asked to "work on Luke using the workflow": write the Book Study for the Gospel of Luke (00 introduction + chapters 1-24) following `plans/books/WORKFLOW.md`, in batches per section 6 (about four chapters, two Opus drafters per batch, review of one batch overlapping the drafting of the next, publish each batch when it clears all three reviews). When the whole book is complete, release and merge per the WORKFLOW **Release** rule: bump the version (`index.html` `#app-version` and `APP_SW_VERSION`, `sw.js` `CACHE_NAME`), run the tests and a headless check, push, open the PR to `main` and merge it without asking once every chapter has passed all three reviews, the build and tests pass and the push succeeded (if a check fails or the merge is blocked, stop and report). Delete this folder before the release commit, and add a "*Luke:*" meditation list and an "*After Luke:*" note to WORKFLOW's Lessons learned.

Plan: `plans/books/_luke_resume/luke_brief.md` (framework, debated points, meditation assignments, names list, batches).

## Status

Columns: draft / theology / application / Chinese / published. Mark each cell `—` (not started), `wip`, `ok`, or `fix` (findings not yet applied; report file named).

| File | Batch | Draft | Theology | Application | Chinese | Published |
|---|---|---|---|---|---|---|
| 00 | 1 | — | — | — | — | — |
| 01 | 1 | — | — | — | — | — |
| 02 | 1 | — | — | — | — | — |
| 03 | 1 | — | — | — | — | — |
| 04 | 2 | — | — | — | — | — |
| 05 | 2 | — | — | — | — | — |
| 06 | 2 | — | — | — | — | — |
| 07 | 2 | — | — | — | — | — |
| 08 | 3 | — | — | — | — | — |
| 09 | 3 | — | — | — | — | — |
| 10 | 3 | — | — | — | — | — |
| 11 | 3 | — | — | — | — | — |
| 12 | 4 | — | — | — | — | — |
| 13 | 4 | — | — | — | — | — |
| 14 | 4 | — | — | — | — | — |
| 15 | 4 | — | — | — | — | — |
| 16 | 5 | — | — | — | — | — |
| 17 | 5 | — | — | — | — | — |
| 18 | 5 | — | — | — | — | — |
| 19 | 5 | — | — | — | — | — |
| 20 | 6 | — | — | — | — | — |
| 21 | 6 | — | — | — | — | — |
| 22 | 6 | — | — | — | — | — |
| 23 | 6 | — | — | — | — | — |
| 24 | 6 | — | — | — | — | — |

Only `plans/books/luke/book.json` exists so far. The build already runs with it (it adds an empty Luke book to `books.json`; tests pass); restore `plans/books.json` with `git checkout` after any check build until batch 1 is published.

## Next steps

1. User reviews the 25 meditation assignments in the brief (section 4) and the names list (section 5).
2. Batch 1 (00-03): two Opus drafters (A: 00, 01; B: 02, 03), each told to read WORKFLOW, the brief and the files in its section 0.
3. On each draft: `theology-reviewer`, then `application-reviewer` and `chinese-reviewer` in parallel; reports to this folder; revise; log rows.
4. Start batch 2 drafting while batch 1 is in review; drafters read batch 1's finished meditations first.
5. Publish each batch through `book-publisher` (worktree build without unreviewed drafts), update this table, and commit work in progress often.
6. After batch 6: release per the rule above.
