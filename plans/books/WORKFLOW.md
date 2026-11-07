# Book Study — Authoring Workflow

Every chapter of the Book Study plan goes through the same steps. Do not skip
the review step, and do not publish or merge a chapter that has open
`must-fix` findings.

## 1. Draft

Write `plans/books/<book>/NN.md` (front matter, then `::zh` and `::en`
bodies; format documented at the top of `scripts/build_book_plan.py`).

Each chapter has:

- **本章脉络 / The Shape of the Chapter**: how the chapter divides.
- **3–5 深读 / Going Deeper sections**, each on one verse or short range, with
  numbered points (bold lead-in, then explanation), optionally closing with a
  `> 要点：` / `> The point:` line.
- **默想 / Meditation**: one or two questions.

Quote Scripture from 和合本 (`ChineseSimplifiedBible.xml`) in Chinese and the
ESV (`EnglishESVBible.xml`) in English.

## 2. Independent theological review (required)

Run the `theology-reviewer` agent (`.claude/agents/theology-reviewer.md`) on
the new or changed chapter files. It must be a separate agent from the one
that drafted the chapter, so the review is independent. It reviews as a
Reformed-evangelical scholar in the tradition of D.A. Carson and J.I. Packer:
doctrine, exegesis, facts, background, application, and Chinese/English
parity. It never edits files.

If the agent type isn't registered in the current session, start a
general-purpose agent and tell it to read and follow
`.claude/agents/theology-reviewer.md`.

## 3. Revise

Apply every `must-fix` and `should-fix` finding to both languages. For a
`consider` finding, apply it or note why not. If the revisions were large,
run the reviewer again on the changed sections.

Record the outcome in `plans/books/REVIEW_LOG.md`: chapter, date, verdict,
and a one-line summary of what changed.

## 4. Build and publish

```bash
python scripts/build_book_plan.py   # regenerates plans/books.json
```

Then commit the `.md` sources, `plans/books.json` and the review log entry
together.

The reviewer is a model applying these scholars' published positions, not the
scholars themselves. Before the plan is shared widely, a human reviewer (a
pastor or seminary New Testament teacher) should still read it.
