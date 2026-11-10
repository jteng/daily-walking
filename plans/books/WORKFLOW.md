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

## Lessons learned (John, Acts, Romans, 1 Corinthians)

**Tools.**
- `python3 scripts/bible_lookup.py 46:7:1,2` prints CUV | ESV for verses; use it before quoting anything.
- `python3 scripts/check_cuv_quotes.py plans/books/<book>/NN.md` lists 「」 text that is not verbatim CUV. Fix real misquotes. Remove the quote marks from glosses unless they mark a slogan or prayer.
- The CUV uses 「－」 as its dash (「耶和华－你神」). Verses joined in one quote keep the CUV's own punctuation at the boundary.

**References and the build.**
- A bare reference written right after another book's reference inherits that book (「（徒18:8；1:14）」 becomes 徒1:14). Put same-book references first in a list.
- A full Chinese book name before a reference is shortened to its abbreviation at build time (「申命记2:14」 becomes 申2:14), because the tooltip only matches abbreviations. Writing full names in the sources is fine.
- A bare reference right after a character that is also a book abbreviation is read as that book: 「记得11:11」 becomes Ruth (得), 「多5:3」 Titus. Put a non-abbreviation word before bare references (「保罗在11:11说」).
- CUV and ESV versification can differ (e.g. Rom 16:23–24). Check the tooltip target.
- Spell names and places as the CUV does (克劳第, 非罗罗古, 基利司布). Keep 该撒利亚 to match the Acts chapters.

**Chinese reviewer's recurring flags.** Avoid:
- translationese: 两者, 两个字, 作为…, 以…的身份, 对…来说;
- stacked 的, and several colons in one sentence;
- English apposition and the serial comma (「A、B、和C」);
- 它 chains, and ESV wording or English words inside ::zh;
- quote marks on non-CUV words.

Write 「这个词」, not 「这个字」, for a Greek word. Use 马丁·路德 with U+00B7.

**Theology reviewer.**
- Present debated readings as options. Label every side symmetrically and name representative scholars or traditions (Reformed / Arminian, Calvin / Wesleyan, Catholic Catechism references).
- Mark Greek points as "many take…", not as settled fact.
- State substitution and the ground of justification plainly. Guard the Trinity wherever the Son is said to submit.
- Do not overstate history (temple prostitutes, "Caesar is Lord", Roman adoption). Check every ESV quotation against the XML.

**Application reviewer.**
- Every meditation ends on Christ and grace, not on a task.
- Give the gospel ground before the command.
- Speak to the reader who has failed, not only the one succeeding.
- Avoid stock themes already used. Before drafting, list the meditation themes of the book so far and of the previous book.

**Safeguarding wording.** Wherever forgiveness, submission, reconciliation, not suing, or "not avenging yourself" comes up, say:
- reporting abuse or crime to the police or courts is right (Rom 13:4);
- victims need not stay in danger or reconcile with someone unsafe;
- forgiveness does not restore an offender's office or give him access to victims or children;
- the church must not hide abuse to save face (「家丑不可外扬」).

**Release.** When a book is complete:
- add it to the Book Study description in `plans/manifest.json`;
- bump the version (`index.html` `#app-version` and `APP_SW_VERSION`, `sw.js` `CACHE_NAME`);
- run the tests and a headless check, then push;
- ask the user before opening and merging the PR to `main`.

**Meditation themes already used** (do not repeat):
- *Romans:*
  - ledger of sin; long-unbelieving family member; empty hands;
  - presenting tongue, eyes and phone; rejoicing in God himself;
  - hidden heart sins and confession; the fear list of 8:38–39; fear of not being elect;
  - monuments of zeal; renqing / owing God; vengeance;
  - honest taxes and putting on Christ; the weak/strong meal; prayer answered unexpectedly (Gethsemane);
  - thanking unseen servants.
- *1 Corinthians:*
  - partisanship around leaders; status and education; praying for illumination;
  - fruitless ministry; freedom from others' judgment; mourning over sin and the old leaven;
  - money disputes among believers; pressure to marry (催婚) and worth when single or divorced;
  - being "right" without love, and being known by God; a church reaching people unlike itself.
  - children's success as an idol (望子成龙); feeling too unworthy for the Lord's Supper, eating alone at church;
  - "only useful people matter" and feeling superfluous in the body.
- *Note:* chs. 7, 10, 11 and 12 all resolve on "I am not lacking / unworthy / superfluous"; vary the shape of later meditations.
