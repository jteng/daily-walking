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

If an agent type isn't registered in the current session, start a
general-purpose agent and tell it to read and follow the matching file in
`.claude/agents/`.

## 3. Application and Chinese-language review (required)

After the theology review passes, run two more independent reviewers on the
chapter. They can run in parallel, and neither may be the agent that drafted
the chapter.

- **`application-reviewer`** (`.claude/agents/application-reviewer.md`):
  pastoral review in the tradition of Tim Keller and John Piper. It reads the
  overview, the 要点 / "The point" lines and the meditations, and checks that
  the application is grace-driven rather than moralistic, centered on Christ,
  aimed at God's glory, and reaches a real reader's heart and life.
- **`chinese-reviewer`** (`.claude/agents/chinese-reviewer.md`): reviews the
  `::zh` body for natural, fluent Chinese (no translationese), consistent
  terms, fit with Chinese church life, and clear calls to repentance and
  faith, with a Reformed evangelical lens in the tradition of Stephen Tong
  (唐崇荣).

Neither reviewer re-checks exegesis or quotations, and neither may change
text inside Scripture quotation marks. If a change alters the meaning of a
sentence, make the matching change in the other language.

## 4. Revise

Apply every `must-fix` and `should-fix` finding from all three reviewers to both languages. For a
`consider` finding, apply it or note why not. If the revisions were large,
run the reviewer again on the changed sections.

Record the outcome in `plans/books/REVIEW_LOG.md`: chapter, date, verdict,
and a one-line summary of what changed. Log each reviewer's pass as its own
row, naming the reviewer (theology, application, Chinese).

## 5. Build and publish

```bash
python scripts/build_book_plan.py   # regenerates plans/books.json
```

Then commit the `.md` sources, `plans/books.json` and the review log entry
together.

Same-book references can be written bare in the sources (「（3:3、5）」, "(3:3, 5)");
the build adds the book name (「约3:3」, "John 3:3") so the app's verse tooltip
recognizes them. A bare reference right after another book's reference in a
list (「（林前9:1；15:8）」) keeps that book. Section headings are left as written.

The reviewers are models applying these teachers' published emphases, not the
people themselves. Before the plan is shared widely, a human reviewer (a
pastor or seminary New Testament teacher) should still read it.
