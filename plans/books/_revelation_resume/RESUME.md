# Revelation 06-22: resume notes (delete this folder before publishing)

User request (2026-11-26): "Start the workflow to finish the rest of Revelation." Chapters 00-05 are published on this branch (v2.26.0 prep, not yet merged to main).
When all of 06-22 pass all three reviews: book-publisher (quote check, build, tests, REVIEW_LOG rows, commit), add Revelation 06-22 lessons/themes to WORKFLOW.md, release (bump version: index.html #app-version + APP_SW_VERSION, sw.js CACHE_NAME), push, open PR to main and merge (book complete; WORKFLOW Release rule). Delete this folder first.

Brief for drafters: `revelation_brief.md` (this folder). Review reports are saved here as `revNN_<theology|application|chinese>.md`; log rows go in `review_log_rows.md`.

Pipeline per pair: draft (general-purpose, Opus) → theology-reviewer → apply (reviser agent) → application + chinese reviewers in parallel → apply → log rows.

## Status (2026-11-26 16:50 UTC, after second usage-limit pause)
| Files | Draft | Theology | Application | Chinese |
|---|---|---|---|---|
| 06-07 | done | passed, applied | running → rev0607_application.md | report done (rev0607_chinese.md), not applied |
| 08-09 | done | passed, applied | running → rev0809_application.md | running → rev0809_chinese.md |
| 10-11 | done | passed (rev1011_theology.md); reviser applying | — | — |
| 12-13 | done | passed after must-fix (rev1213_theology.md); not applied | — | — |
| 14-15 | done | passed, applied | — | — |
| 16-17 | done | passed (rev1617_theology.md); reviser applying | — | — |
| 18-19 | done | passed (rev1819_theology.md); reviser applying | — | — |
| 20 | done | passed, applied | report done; reviser applying app + Chinese | report done; reviser applying |
| 21-22 | done | passed (rev2122_theology.md); reviser applying | — | — |

If a report has no "## Applied (reviser)" section, its fixes are not applied yet.

## Cross-chapter fixes still to do
- Meditation names now: 06 老陈, 07 老刘, 08 李阿姨, 09 老郑, 12 秀兰 (rename: 21 keeps 秀兰), 13 小陈 (rename + new scenario), 14 郑妈妈 (clashes with 09 老郑: rename 14), 15 黄弟兄, 22 小周. No surname may repeat.
- 20.md: apply rev1415_theology.md S4 (use 「有条件不朽论（又称灭绝论）」 and point to ch. 14 and 2 Thess 1).
- 13 meditation must change scenario (11 has the false-inspection-report scene).
