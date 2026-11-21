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

Hand this step to the `book-publisher` agent (`.claude/agents/book-publisher.md`).
It runs on Sonnet and does only mechanical work: the quote check, the build,
the tests, appending the review-log rows you give it, and the commit. It never
edits chapter content, and it stops on any flagged quote or failure.

**Model choice.** Drafting and all three reviewers stay on Opus. A blind A/B test
on 2026-11-11 compared the two models on pre-review drafts of John 10, Acts 5
and Acts 7, scoring each review against the fixes the original reviews made:

| Role | Opus | Sonnet |
|---|---|---|
| Theology | 19/21 | 13/21 |
| Application | 7/8 | 5/8 |
| Chinese | 12/14 | 9/14 |

Sonnet also reported three wrong ESV quotations as verified. That is why
Sonnet is limited to the mechanical steps.

What the publish step runs:

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

## Lessons learned (John, Acts, Romans, 1 Corinthians, 2 Corinthians, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians, 2 Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon, Hebrews, James, 1 Peter, 2 Peter)

**Tools.**
- `python3 scripts/bible_lookup.py 46:7:1,2` prints CUV | ESV for verses; use it before quoting anything.
- `python3 scripts/check_cuv_quotes.py plans/books/<book>/NN.md` lists 「」 text that is not verbatim CUV. Fix real misquotes. Remove the quote marks from glosses unless they mark a slogan or prayer.
- The CUV uses 「－」 as its dash (「耶和华－你神」). Verses joined in one quote keep the CUV's own punctuation at the boundary.

**References and the build.**
- A bare reference written right after another book's reference inherits that book (「（徒18:8；1:14）」 becomes 徒1:14). Put same-book references first in a list.
- A full Chinese book name before a reference is shortened to its abbreviation at build time (「申命记2:14」 becomes 申2:14), because the tooltip only matches abbreviations. Writing full names in the sources is fine.
- A bare reference right after a character that is also a book abbreviation is read as that book: 「记得11:11」 becomes Ruth (得), 「多5:3」 Titus. Put a non-abbreviation word before bare references (「保罗在11:11说」).
- The tooltip only knows the app's abbreviations: write 1 John as 约一, not 约壹. A bare reference right after another book's reference (「创1:1……1:18」) is read as that book; write 「本章18节」.
- CUV and ESV versification can differ (e.g. Rom 16:23–24). Check the tooltip target.
- Spell names and places as the CUV does (克劳第, 非罗罗古, 基利司布). Keep 该撒利亚 to match the Acts chapters.

**Lists.** A "- " list may follow its lead-in line directly (no blank line); the build splits the block into a paragraph and a list. Before 2026-11-12 such lists were rendered inline as " - " text.

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

**Batches.** The build reads every `.md` in the book folder. When publishing one batch while later drafts sit in the same folder, move the unreviewed drafts out (e.g. to a scratch folder) for the publish step and put them back afterwards; never move files while a reviewer is reading them. Better: build in a temporary `git worktree` of HEAD with the unreviewed drafts deleted there, copy its `plans/books.json` back, and commit only `books.json` and the review log (used for Hebrews 6-10).

**Release.** When a book is complete:
- add it to the Book Study description in `plans/manifest.json`;
- bump the version (`index.html` `#app-version` and `APP_SW_VERSION`, `sw.js` `CACHE_NAME`);
- run the tests and a headless check, then push;
- open the PR to `main` and merge it without asking, once every chapter has passed all three reviews, the build and tests pass, and the push succeeded (if a check fails or the merge is blocked, stop and report instead of forcing it).

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
  - loving the hardest person (read 13:4-7 with my name, then with Jesus'); words that once built me up, and "your sins are forgiven" as the source of speech.
  - grief and regret at a believer's death, from "if" (15:19) to "but in fact" (15:20); looking back over the whole letter, ending in a written prayer (Maranatha).
- Non-biblical chapter:verse references (e.g. 《十二使徒遗训》10:6) are linked by the build as same-book references. Write them as 第十章 / "chapter 10" or with a period (10.6).
- *Note:* chs. 7, 10, 11 and 12 all resolve on "I am not lacking / unworthy / superfluous"; vary the shape of later meditations.
- *2 Corinthians:*
  - the curated image and fear of losing face (cracked jar); despair beyond strength and not wanting to trouble others (with a crisis-help line);
  - welcoming back a repentant brother / the one who fell (elder brother, best robe); slow change, inspecting myself vs beholding Christ;
  - aging, fear of becoming a burden (拖累儿女), caring for parents and dementia (ends in a written prayer); labels from the past vs new creation;
  - a heart narrowed by church hurt (lament, safety, rumors); worldly vs godly grief, self-punishment, Peter by the fire;
  - fear of not having enough, giving in poverty; motives for giving (face, bargaining, guilt) ending on 9:15;
  - comparison and the Lord's commendation; divided devotion and "another Jesus" as a protector-deity;
  - living with a thorn that is not removed; self-examination toward assurance, ending on the benediction (13:14).
- *Galatians:*
  - "Christ plus..." as my ticket, ending on 5:1 freedom; regret over hidden or wasted years and a past opposing Christ (set apart before birth);
  - wearing different masks before different groups (Peter at Antioch), going back to the table; feeling cursed (bad fate, 八字, feng shui, "generational curses"), Christ became a curse;
  - relating to God as an employee with a performance review, a father who only checked grades vs Abba; the need to win in group-chat quarrels (5:26), apologizing;
  - weariness in long doing good, letting others carry part of the load, the cross as God's harvest.
- *Ephesians:*
  - a hard life and "every spiritual blessing" (Paul praising in chains, to the praise of his glory); praying for circumstances vs praying for eyes to know God, God's own inheritance;
  - dividing walls in the church (language congregations, generations, politics), praying together before the Father; knowing Christ's love as doctrine only, coming back at once after falling again;
  - speaking the truth in love vs keeping quiet to save face (以和为贵) or bluntness; what I fill my emptiness with at night (phone, drink), filled by Christ's Spirit;
  - the "evil day" as a returning temptation fought alone by willpower, standing in God's own armor (Isa 59), "It is written" (3:12), telling others and praying together.
- *Philippians:*
  - the "first day" of faith (or no datable day) and God completing the work, "Lord, that was you";
  - "for me to live is ____" and what makes death loss, Christ "far better";
  - feeling shortchanged (吃亏) and scorekeeping, Christ the one with the right to say "why me";
  - belonging nowhere (overseas, a lost job title), heavenly citizenship and the transformed body;
  - worries turned into written requests with thanksgiving, the garrison of peace.
- *Colossians:*
  - the ordinary person who brought the gospel (Epaphras) and kept praying, Christ who intercedes more surely (with a line for a messenger who later harmed me);
  - "how large is Jesus in my mind": the lab, office, kitchen and news as if they had nothing to do with him, all things "for him" (1:16-17), ending on reconciliation;
  - the restless search for "something more" (the next conference, method, breakthrough), "filled in him" (2:10) as rest;
  - a hidden, unseen life (caregiving, a back kitchen, hidden bitterness), "Christ who is your life" (3:3-4);
  - past conversations about faith with an unbeliever (silence, arguing, not listening), asking someone to pray, Christ's patience with me as an outsider, "Grace be with you" (4:18).
- *1 Thessalonians:*
  - dry Bible reading, reading without waiting for feelings, the word "at work" (2:13) because of the Word made flesh;
  - the idols I still turn back to for peace (they demand payment first), Jesus "who delivers us" while my back was turned (1:9-10);
  - giving people verses but not myself (too busy), one safe person to step toward, Christ "gave himself for me" (2:8);
  - faith shaken by suffering and hidden for shame, Jesus praying for Peter, the Lord who establishes the heart (3:3, 13);
  - comforting a grieving friend "with these words": words for Martha, tears with Mary, then "Lazarus, come out" (4:18; John 11);
  - fear of the day of the Lord and of being left behind, for the reader unsure they belong to Christ too, "he died for us" and "he will surely do it" (5:9-10, 24).
- *2 Thessalonians:*
  - being "in the know" about end-time claims and timetables, waiting for a person not a date (2:1, 2:16);
  - a list of abandoned good resolves, fulfilled "by his power" for his name's glory and according to grace (1:11-12);
  - loving the truth vs what I want to hear, the truth about myself I keep refusing to hear, "if the Son sets you free" (2:10; John 8:36);
  - writing off a fellow believer as an enemy, the risen Lord's "go and tell my brothers" (Matt 28:10; Heb 2:11), grace "with you all" (3:18).
- *1 Timothy:*
  - staying in a hard place when the trusted leader moves on (Timothy left at Ephesus), Christ who could have come down from the cross and stayed, with a word for one who already left;
  - the shape of my testimony: Christ's perfect patience, not my improvement (1:16), for the "too ordinary" and the "too dark" past, ending on the 1:17 doxology;
  - 找关系 / needing a go-between or a gift before God will hear, the one Mediator who is himself the gift, sent by "God our Savior" (2:3-6);
  - godliness as a checklist of habits vs the person in the 3:16 hymn, reading the six lines and choosing one;
  - being despised for youth / despising the young out of seniority, Christ despised in Nazareth (Mark 6:3; Isa 53:3), progress as his work;
  - the lonely widow whose prayer feels empty, Anna waiting and seeing Christ (Luke 2:36-38), Jesus making a home for his mother (John 19:26-27; Ps 68:6);
  - the number that keeps moving (salary, savings, flat), Christ who went out with nothing (John 19:23-24), God my portion (Ps 73:25-26; Heb 13:5).
- *2 Timothy:*
  - entrusting what I refuse to let go (children, health, wasted service, my own death) to the One who "is able to guard" (1:12), not because my faith is big;
  - Onesiphorus searching for the one in "chains" everyone stopped visiting, the lost sheep found (Luke 15:4-5; 19:10), with a safeguarding line for offenders;
  - despair over church decline and children leaving, "the word of God is not bound" because Christ is risen (2:8-9), with a line for the parent who feels they failed;
  - called unfilial at a funeral or ostracized at work, self-caused suffering separated out, ending on 1 Pet 4:14;
  - no one came at my hour of need, "but the Lord stood by me" (4:16-17), the forsaken Christ (Matt 27:46), "the Lord has not charged it against me", ending on the 4:18 doxology.
- *Titus:*
  - broken promises (a father's weekend, "I will always love you", a boss, a friend's loan) and my own, "God, who never lies" (1:2), forgiveness for my broken word, every promise Yes in Christ (2 Cor 1:20);
  - the sins my own culture treats as normal (inflated CVs, pressing drink, looking down on outsiders, polite untruths), "this testimony is true", Cretans at Pentecost (Acts 2:11), the Lamb's blood from every tribe (Rev 5:9);
  - what I wait for each day (weekend, payday, exams, the mortgage, retirement) vs the blessed hope, the great God who gave himself for us (2:13-14);
  - looking down on unbelievers, the Pharisee's prayer (Luke 18:11), "we ourselves were once" (3:3-5), mercy not withdrawn for tomorrow's pride, heirs together (3:7).
- *Philemon:*
  - a relationship I am afraid to go back to (a wronged family member, an unpaid loan, a church let down), "charge that to my account" (1:18-19), the Father who sent the Son to pay, with a line for the closed road back;
  - the person I find hard to "receive" (gossiping coworker, hurtful church member), being Onesimus before God first, received "in the Beloved" (Eph 1:6), with a safety line.
- *Hebrews:*
  - 00-05: see the Hebrews note under *Watch in later books* (Son who speaks, drifting, Gethsemane tears, rest, the dull hearer);
  - Abraham's long wait and a promise I'm tired of believing, God's oath "for the heirs" (6:17), ending on the anchor held in his hands (6);
  - spiritual carers who died, retired, moved or fell, Christ's permanent priesthood (7:23-25), with a safeguarding line, ending on the Ps 110:4 oath (7);
  - second-hand faith, alone in a strange city, God's repeated "I will" and the one Mediator (8);
  - serving harder at church as penance for an old wrong ("dead works"), restitution as the freedom of the forgiven (Matt 5:23-24), ending on 9:28 (9);
  - drifting from gathering after the pandemic livestream or out of shame, 10:26 answered for the one away for years, the bread and cup, one gentle step (10);
  - prayers not answered in my lifetime, God promised the city, the departed prayer partner (12:23), ending on 11:16 (11);
  - hardship read as 报应, a father who hit in anger named as wrong, LXX Isa 53:5 / Heb 12 "discipline", thanksgiving at Zion (12);
  - the unchanging Christ among changing leaders and my own faith, staying inside the camp for face, the raised great Shepherd, ending on the 13:20-21 doxology (13).
- *James:*
  - reading James as a medical report of failures, the brother who did not believe found by the risen Lord (1 Cor 15:7, no rebuke recorded), ending in adoration of "the Lord of glory" (2:1) (00);
  - blaming my sin on others, circumstances or "how God made me" (Adam, Gen 3:12), the two births (1:15, 18), the sinless Christ who took my sin, with a line for those truly sinned against, ending on the unchanging Father of lights (01);
  - partiality at the church door, wedding seating and small group, the man in filthy garments (Zech 3:3-4), the Lord who took the lowest place saying "Friend, move up higher" (Luke 14:10) (02);
  - sharp words at the family dinner table, "Father, forgive them" and 1 Pet 2:22-24, a line for one wounded by such words as a child, the renewed mouth that blesses God and his image-bearers, ending on Pentecost's "mighty works of God" (03);
  - putting off the good I know to do as if tomorrow were mine (4:13-17), Christ who never put off his Father's will (John 4:34; 10:18), new-morning mercies (Lam 3:22-23), ending "I do not know tomorrow, but I know you" (Ps 31:15) (04);
  - feeling my prayers do not count because I am not "righteous", Elijah under the broom tree (1 Kgs 19:4-5), praying in the Son's name, ending in adoration of 5:11 and waiting on the God of the early and late rain (05).
- *After James:* 4:6 "he gives more grace" and 「我的罪很多，他的恩典更多」 are used in James 00; 1 Cor 15:7 (James found by the risen Lord) is 00's scene; Luke 14:10 "Friend, move up higher" ends James 02; Pentecost's "tongues as of fire" against the tongue "set on fire by hell" is James 03's; Lam 3:22-23 ends James 04; Christ's intercession (1 John 2:1) was cut from James 05 to avoid Hebrews 05. Avoid exam/grade images (medical report used in James 00). In ::zh write 天特会议 / 第六会期, 《天特会议决议的解毒剂》 and Calvin's line 「叫人称义的只是信心，但叫人称义的信心不是孤单的」; write 交账 (not 交帐); 英王钦定本 (KJV), 英文标准版 (ESV). The CUV makes "the spirit" the subject of James 4:5 (a question): do not say it follows the ESV. James 5:20 in the CUV has no comma before 便是.
- *1 Peter:*
  - Peter's "Far be it from you" (Matt 16:22) against the cross that saved him, "What am I saying 'far be it' about?", ending on seeing the One we love unseen (1:8) (00);
  - inherited family ways (no apology, cold silence, 报喜不报忧) as "futile ways inherited from your forefathers", already ransomed, ending on the Lamb and 1:21 (01);
  - the pew-sitter who keeps faith inside the church, priesthood as mercy and an open door (2:10; 2:24-25), ending in adoration of the living stone (02);
  - delaying baptism under family pressure ("baptized means abandoning your ancestors"), the price he paid "to bring us to God" (3:18), safety and infant-baptism lines, a prayer that admits fear (03);
  - a grievance kept and retold, Ham vs Shem and Japheth (Gen 9:22-23), God clothing the first sinners (Gen 3:21), standing together clothed in Christ (Gal 3:27) (04);
  - giving up a ministry or a vow partway, Mark "my son" before "useful", God who "himself" mends torn nets (5:10; Mark 1:19), ending on the mender's hand (05).
- *After 1 Peter:* John 21's breakfast and three questions stay retired (2 Corinthians 7); Peter's denials are named in 1 Peter 00 and 05. Baptism as a meditation theme is 1 Peter 3's; Shem and Japheth (Gen 9:23) and Gen 3:21 are 1 Peter 4's; the torn net and Mark are 1 Peter 5's. Doxology endings remain retired (5:11 kept in the body). Col 3:23 is used in 1 Timothy 6 and 2 Thessalonians 3. In ::zh keep 交帐 inside CUV quotations of 1 Pet 4:5 (prose uses 交账); write 七十士译本 consistently; 凯伦·乔布斯 on first mention. Bare references after another book's reference in the same sentence can be misread: write 彼前5:1 / "1 Pet 5:1" when it follows a Gospel reference. Jobes on 3:19 could not be confirmed; Dalton and Schreiner are named instead.
- *2 Peter:*
  - ranking believers (apostles, preachers, "spiritual" members) and putting myself near the bottom or others behind me, "a faith of equal standing" (1:1) received by Christ's impartial righteousness, Simeon put first (still the Simon who needed grace), Luke 22:31-32, ending with the same Lord welcoming us at the door of the eternal kingdom (1:11) (00);
  - faith gone dull because forgiveness became "an old entry in a file" (1:9), Peter reminding them of the Father's "This is my beloved Son" (1:17), cleansing resting on the Son (Matt 26:28), John 6:37 for the doubter, ending "Rise, and have no fear… Jesus only" (Matt 17:7-8) (01);
  - Lot lingering in a compromise I grieve but don't leave (kickbacks, a wrong relationship, a habit), brought out by the LORD's mercy (Gen 19:16), a line for those trapped in someone else's harm, Zacchaeus's restitution after "I must stay at your house today" (Luke 19:5, 8), Christ judged outside the gate (Heb 13:12), ending on 2:9 "the Lord knows" and "will not leave me in Sodom" (02);
  - "how long?" over injustice and the one who hurt me (Rev 6:10-11), the fig tree "let it alone this year also" (Luke 13:7-9) as the patience that waited for me, Rom 3:25-26 for those who repent and trust, safeguarding with Rom 12:19 (宁可让步 left out) and 13:4, Luke 9:51, ending "the years of his patience included me" (03).
- *After 2 Peter:* Hands-of-Christ endings are now in 1 Peter 05, 2 Peter 00 and 01 (and were cut from 2 Peter 02): vary the ending image. Matt 17:7-8 "Jesus only", John 6:37 (2 Peter 01), Luke 13:6-9, Rev 6:10-11 and Luke 9:51 (2 Peter 03) are used. A faithful-pastor balance (1 Pet 5:2-3; 1 Thess 5:13) belongs wherever false teachers are the topic (2 Peter 2; watch Jude). In ::zh: 包衡 (Bauckham), 道格拉斯·穆尔 / 穆尔 (Moo), 施莱纳, 神化 (*theosis*) with 能 (*energeia*), 托名 for pseudonymity, 阿民念派和卫斯理宗, 亚目拉督派, 协同 (*concursus*, not 同工), CUV 「去世」 for *exodos* (not 出路), 爱席 (Jude 12), 耽延 (3:9). Do not write ESV words in ::zh, even in parentheses. Non-biblical references take a period (《以诺一书》20.2 / *1 Enoch* 20.2), and a bare reference after a Gospel reference in English needs the book name ("(Luke 19:5)"): both broke `test_en_own_book_references_exist`. Jude next: 2 Peter 00 and 02 already cover Jude/2 Peter dependence (Michael Green leans to 2 Peter priority), 2:4 / Jude 6 angels and 1 Enoch (quoting it does not make it Scripture), and Balaam.
- *Watch in later books:* Pastoral Letters: keep the 3:16 variant note (CUV 「神」 vs earliest "who") and complementarian/egalitarian labels as worded in 1 Timothy 2; "comparison" meditations are now in 2 Corinthians 10, so avoid reunion-comparison scenes. Jesus weeping at Lazarus's tomb (John 11:35) is now in Acts 8, 1 Corinthians 15 and 1 Thessalonians 4; 「这就够了」 / "that is enough" (1 Thessalonians 2) is close to the retired "filled" ending. "The Lord is faithful" endings are now in 1 Thessalonians 5 (5:24) and 2 Thessalonians (3:3); Romans 5:10 "while we were enemies" and "at least pray for them" are in Romans 12. Write 推罗 (CUV), not 泰尔, for Tyre, and 《威斯敏斯德信条》 with book-title marks. Use the CUV spelling 克劳第 for Claudius, and in Chinese 古德恩, 加芬, 终止论/延续论, 三分说/二分说. After 2 Timothy: the Gethsemane flight (Mark 14:50) is in 2 Thessalonians 3 and Acts 23 (and was cut from 2 Timothy 4); "the Lord stood by me" (Acts 23:11; 2 Tim 4:17) is now in Acts 23 and 2 Timothy 4; John 16:33 is John 16's anchor; "who brought me the gospel" is in Colossians 00 and Romans 16. Doxology endings are now in 1 Timothy 2 (1:17) and 2 Timothy 4 (4:18); 2 Timothy 00 and 02 both resolve on handing over what I try to hold up myself, so vary that shape. After Titus: temper and slow change with "he will not give up on me" is in 2 Corinthians 3 and was cut from Titus 2; "he will surely do it" endings are in 1 Thessalonians 5, 2 Thessalonians 3 and were cut from Titus 00; complementarian/egalitarian labels for the home are worded in Titus 2 (夫妻角色男女有别 / 不以性别区分). Write 东方闪电（自称全能神教会）, 英文钦定本, 七十士译本, and 为亡者祷告.
- *After Hebrews:* Chapters 6-13 use few tasks: 06, 07, 08, 09, 11, 12, 13 end in adoration, a promise or a doxology, and 10 alone ends on one step; later books can return to concrete steps. 「主耶稣，……」 closing prayers are in Hebrews 06, 07 and 09; 2:11 is now in 2 Thessalonians 3 and Hebrews 2 and 11; 7:25 "always lives to intercede" ends Hebrews 05; 13:7 is quoted in Hebrews 07, 08 and 13; the departed-carers scene is Hebrews 7's; moving to a strange city is Hebrews 8's. In ::zh write 前约 for the old covenant and 旧约圣经 for the Scriptures (旧约 alone reads as the Old Testament). Do not cite O'Brien's Hebrews commentary (withdrawn 2016). Write the incarnation as "became truly human" (2:14), not "took a body". A bare reference right after 但 is read as Daniel (「但10:26」 broke a test): write 不过10:26. Earlier Hebrews notes: Gethsemane's "loud cries and tears" (5:7) and "the high priest who once prayed with tears" are used in the Hebrews 2 meditation, so chapters 4-5 should not rebuild that scene; Heb 2:11 "not ashamed to call them brothers" is now in 2 Thessalonians 3 and Hebrews 2. Hebrews 00 and 02 both use 「如果我从来没有信靠他，今天就可以……」 and all of 00-02 end "today I can... then pray": vary the shape from chapter 3 on. Chapters 3-5 end "today / this week I can [task]," then Christ: for chapter 6 on, try one meditation ending in adoration of the high priest, or one with no task at all. "He will not give up on me / slow growth" (2 Corinthians 3) was cut from Hebrews 5; "work-group messages" in Hebrews 4 is close to the retired phone image, so do not build on it.
- *Retired frames:* the accusing inner voice ("you'll never change", quoted accusations) has been used in Romans 6, Romans 8, 2 Corinthians and Ephesians 3; the phone as an image in Romans 12 and Ephesians 5; 吃亏 in 1 Corinthians 6, Galatians 6 and Philippians 2; sleeplessness as the opening of a meditation in Romans 8 and Philippians 4; Jesus as a helper or protector-deity for my plans (2 Corinthians 11), with exam and interview examples (2 Corinthians 11, Ephesians 1); the inner circle / standing outside looking in (1 Corinthians 11–12, Philippians 3, Colossians 2); ending a meditation on "filled" (Colossians 00 and 02). Do not use them again.
