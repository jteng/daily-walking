# Luke — Book Brief (planning only; delete this folder before the release commit)

Book: 路加福音 / Luke, book 42, abbr 路, 24 chapters + 00 introduction.
Files: `plans/books/luke/00.md` … `24.md`; `plans/books/luke/book.json` exists.

## 0. Read before drafting or revising

1. `plans/books/WORKFLOW.md` in full: section 6, Lessons learned, every "Meditation themes already used" list, every "After X" note, *Retired frames*.
2. Format and voice: `plans/books/acts/00.md` (same author; Luke-Acts framing below must agree with it), `plans/books/john/00.md` and one John chapter (e.g. `john/11.md`), `plans/books/revelation/00.md` and a late Revelation chapter (e.g. `revelation/14.md`) for current meditation length and texture.
3. `scripts/build_book_plan.py` header (front matter, `::zh` / `::en`, body syntax).
4. This brief, section 5 (names and scenes used), and the finished meditations of earlier Luke batches.

## 1. Tools and rules for every agent

- `python3 scripts/bible_lookup.py 42:1:1,3,4` prints CUV | ESV. Look up every verse before quoting it (other books: their number, e.g. 44 for Acts).
- `python3 scripts/check_cuv_quotes.py plans/books/luke/NN.md` lists 「」 text that is not verbatim CUV. Fix real misquotes; remove quote marks from glosses.
- Build and test to check, then restore: `python3 scripts/build_book_plan.py && python -m pytest tests/ -q`, then `git checkout plans/books.json`. Only the book-publisher commits `books.json`.
- **No commits by drafters or reviewers.** The coordinator commits work in progress; the `book-publisher` (Sonnet) does the publish commit per batch.
- Reviewers write full reports to `plans/books/_luke_resume/NN_<theology|application|chinese>.md` and reply with a verdict and counts only. Revisers append an "Applied (reviser)" section to each report.
- Versification: CUV has no separate 1:2 (1:1 carries 1:1-2; `bible_lookup` shows 1:2 as —). Write 1:1-4 as a range and check the tooltip target.
- Spellings (CUV): 提阿非罗, 居里扭 (Quirinius), 凯撒奥古斯都 (2:1), 撒马利亚 inside CUV quotes, 撒玛利亚 in prose (as in Acts and 1 John notes), 古利奈人西门, 亚利马太, 以马忤斯, 革尼撒勒, 拿因, 撒该. Keep 该撒利亚 as in Acts.
- References: same-book refs bare (「（9:51）」); put same-book refs first in a list; after another book's ref write 本章N节 or repeat 路. Do not put a bare ref right after a character that is a book abbreviation (得, 多, 但, 来, 加, 约…); none of the assigned surnames is one, but still write 「老钟在9:41……」 style with a word between. In ::en a bare ref after a Gospel ref of another book needs "Luke".
- Target ~35 KB per file (Revelation ran 36-41 KB).

## 2. Shared framework (00 sets it out; chapters point back)

**Author.** Anonymous in the text; early, unanimous tradition: Luke, "the beloved physician" (Col 4:14), Paul's fellow worker (Philem 24; 2 Tim 4:11). The "we" passages (Acts 16:10-17; 20:5-21:18; 27:1-28:16): the author travelled with Paul (word as Acts 00). External: Irenaeus 《驳异端》3.1.1 (Paul's follower put in a book the gospel Paul preached); the 《穆拉多利残篇》 (usually late 2nd c.) names Luke the physician. Most take him as a Gentile (Col 4:10-14); some (Earle Ellis) a Hellenistic Jew. Do not argue from "medical language" (Hobart 1882, answered by Cadbury).

**Date.** (a) Before c. 62: Acts ends with Paul two years in Rome, no trial outcome, no Nero (64) or temple fall (70), and Luke precedes Acts (Bock, Bruce on Acts, J. A. T. Robinson). (b) 70s-80s: Luke uses Mark (c. 65-70) and 21:20 is read as after 70 (Fitzmyer 80-85; Marshall open, c. 70). Both have evangelical support; 21:20 can be genuine prediction. Same two options as Acts 00.

**Theophilus and the prologue (1:1-4).** "Most excellent" (Acts 23:26; 26:25, of governors) suggests rank and likely patronage; most take Theophilus as a real person, not a code name. Luke's method: earlier accounts; tradition from "eyewitnesses and ministers of the word"; careful research; "an orderly account" (καθεξῆς, orderly, not necessarily strict chronology); goal: *asphaleia*, certainty (1:4). Form like Hellenistic historical prefaces (Loveday Alexander). Eyewitness claim: 包衡《耶稣与目击者》.

**Luke-Acts as one work.** Same author and addressee (Acts 1:1 "the first book"); the Gospel moves *to* Jerusalem (9:51; 13:33; 19:28), Acts *from* it to Rome (Acts 1:8; Luke 24:47); the ascension ends one volume and opens the other (24:50-53; Acts 1:9-11). Cadbury coined "Luke-Acts" (1927); unity of authorship is near-universal, unity of genre and reception debated (Andrew Gregory, C. Kavin Rowe): mention lightly.

**Synoptic problem** (00 only; chapters point back; same length for each view, no verdict pressed):
- *Markan priority / two-source:* Matthew and Luke each used Mark and a sayings source "Q" (material they share without Mark: e.g. 6:20-49; 11:2-4). Majority view; Fitzmyer, Marshall, Stein, Bock.
- *Farrer-Goulder (Farrer, Goulder, Mark Goodacre):* Markan priority without Q; Luke used Mark and Matthew.
- *Griesbach / two-Gospel (Griesbach, William Farmer):* Matthew first, then Luke, Mark combining both.
- Luke's own material ("L": 10:30-37; 15:11-32; 16:19-31; 19:1-10). Any theory fits inspiration: Luke says he used sources and research (1:1-3).

**Key themes** (00 lists them with one or two refs each; chapters pick up the relevant one):
salvation *today* (2:11; 4:21; 19:9; 23:43); the outcast and the lost (5:32; 7:34; 15; 19:10); prayer, Jesus praying at turning points (3:21; 6:12; 9:18, 28; 11:1; 22:41); the Holy Spirit (1:35; 3:22; 4:1, 14, 18; 11:13; 24:49); joy (1:14; 2:10; 10:21; 15:7; 24:52); wealth and poverty (1:53; 6:20, 24; 12; 16; 18:18-30); the journey to Jerusalem (9:51-19:27); women (1-2; 7:36-50; 8:1-3; 10:38-42; 23:49-24:11); all nations (2:32; 3:6, 38; 24:47); divine necessity, δεῖ (2:49; 4:43; 9:22; 24:7, 26, 44).

**::zh name forms.** Established (keep): 霍华德·马歇尔, 莱昂·莫里斯, 弗雷德里克·布鲁斯, 汤姆·赖特, 理查德·包衡 / 包衡, 道格拉斯·穆尔, 卡森, 雷蒙德·布朗, 克雷格·基纳, 马丁·路德 (U+00B7), 爱任纽《驳异端》, 优西比乌, 《穆拉多利残篇》, 约翰·卫斯理, 七十士译本, 英文钦定本, 英文标准版. New for Luke (full name at each chapter's first mention): 达雷尔·博克 (Bock; 博克 appears in Hebrews 08), 约瑟夫·费茨迈尔 (Fitzmyer), 乔尔·格林 (Joel Green; always with given name: 迈克尔·格林 and 吉恩·格林 are used), 罗伯特·斯坦 (Stein), 约翰·诺兰 (Nolland), 肯尼斯·贝利 (Bailey), 布鲁斯·麦慈格 (Metzger), 克雷格·布鲁姆伯格 (Blomberg), 马克·古德卡 (Goodacre), 格里斯巴赫, 亨利·卡德伯里 (Cadbury), 洛夫迪·亚历山大 (Loveday Alexander). The theology reviewer verifies every attribution; no invented quotations.

## 3. Debated points by chapter (options, named representatives, symmetric labels)

- **00:** authorship, date, Synoptic problem, Luke-Acts (above).
- **01:** 1:34-35 virginal conception: the creedal confession (Apostles' and Nicene Creeds; Machen, *The Virgin Birth of Christ*; Bock, Marshall) vs critical readings as theological legend (Bultmann's heirs); Raymond Brown held it historically likely but unprovable. Say plainly why it matters (1:35 "therefore… Son of God"). John/Jesus parallel structure.
- **02:** 2:1-2 Quirinius: (a) a census *before* Quirinius' AD 6 governorship (πρώτη as "before"), (b) an earlier command of Quirinius in Syria (Ramsay; cautious about inscriptions), (c) Luke erred or conflated (Fitzmyer, Raymond Brown). Say it is unresolved and (a)/(b) are serious options. Also 2:7 κατάλυμα "inn" or guest room (Bailey); 2:49 "Father's house" vs "business".
- **03:** 3:23-38 vs Matt 1: (a) Luke gives Mary's line (Annius of Viterbo onward; older harmonies), (b) both Joseph's, legal and biological via levirate marriage (Julius Africanus in Eusebius HE 1.7), (c) Matthew the royal-legal line, Luke Joseph's descent (Machen). The line runs up to "son of Adam, son of God", tying to 4:3, 9. 3:22 Western "today I have begotten you": mention only.
- **04:** 4:16-30: Luke's placing vs Mark 6:1-6 (same visit moved forward, Fitzmyer; or an earlier visit); Isa 61:1-2 stopping before "the day of vengeance"; Jubilee (Lev 25) political vs spiritual readings: hold poor and forgiveness together as Luke does. Temptation order differs from Matthew (Luke ends at the temple).
- **05:** 5:1-11 and John 21:1-11 (two events, most conservatives; one tradition, Raymond Brown).
- **06:** 6:20-49 Plain vs Mount (Matt 5-7): one sermon edited (most two-source scholars) or similar teaching given more than once (Carson, Blomberg, Bock); "poor" vs "poor in spirit": hold economic and spiritual together.
- **07:** 7:36-50 vs the Mark 14 / John 12 anointings (most: a different event); 7:47 "for she loved much": love as evidence of forgiveness (7:47b, 50; most exegetes now) vs love as ground: give the grammar.
- **08:** 8:10 (Isa 6:9-10): purpose vs result readings of hardening. Gerasenes/Gadarenes place-name variants (Metzger).
- **09:** 9:27 "some will not taste death" (transfiguration, resurrection-Pentecost, AD 70, Parousia). 9:51 ἀνάλημψις (ascension) and the journey section. 9:54-56: CUV prints the longer text (「你们的心如何……是要救人的性命」), ESV the shorter: a CUV/ESV parity point (Metzger).
- **10:** 10:25-37: neighbor-love first ("who proved a neighbor?"); allegory (Origen, Augustine: Samaritan = Christ, inn = church) vs no allegory (Calvin, Jülicher, most modern); a middle view (Bailey, Blomberg: Christ the true Neighbor as theological echo, not code). 10:1 seventy or seventy-two (Metzger).
- **11:** 11:2-4 shorter Lord's Prayer vs Matthew; 11:8 ἀναίδεια: the asker's shamelessness vs the sleeper's honor (Bailey); 11:13 "the Holy Spirit" vs Matthew's "good things".
- **12:** 12:10 blasphemy against the Spirit (persistent rejection of the Spirit's witness to Christ; pastoral line for the anxious). 12:49-53 fire, baptism, division.
- **13:** 13:1-5 (events not attested outside Luke: do not invent); 13:23-30 "few saved?": Jesus refuses speculation and says "strive"; the unevangelized briefly: inclusivism (Clark Pinnock; *Lumen Gentium* 16) vs exclusivism (Carson, Ronald Nash). 13:32 "third day".
- **14:** 14:26 "hate" as Semitic preference (Matt 10:37; not neglect of parents, 1 Tim 5:8). 14:23 "compel them": Augustine against the Donatists; reject coercion plainly.
- **15:** 15:3 "this parable": one parable in three parts; the father's running (Bailey, cautiously); the elder brother left open; "forgiveness without the cross?" answered (Keller, *The Prodigal God*: the true elder brother pays).
- **16:** 16:1-13 manager: (a) cut his own commission (Derrett, Fitzmyer), (b) removed hidden interest (Bailey), (c) plain fraud praised only for foresight (Marshall, Bock, Snodgrass); "the master" of 16:8a. 16:19-31: parable (most) vs actual account (Lazarus named; Tertullian; some dispensational writers); intermediate state: conscious existence before the resurrection (WCF 32.1; Calvin's *Psychopannychia*) vs soul-sleep (Seventh-day Adventists) and 「有条件不朽论（又称灭绝论）」 (as Revelation 14). Do not map hell from a parable's scenery.
- **17:** 17:21 ἐντὸς ὑμῶν: CUV 「在你们心里」 (inward: KJV, Origen) vs ESV "in the midst of you" (present in Jesus: most moderns, Marshall, Fitzmyer, Bock) vs "within your reach" (C. H. Roberts). Addressed to Pharisees, which weighs against "hearts". Do not call the CUV wrong. 17:34-36 "one taken": judgment (as in Noah's flood, 17:27) vs rapture readings (Walvoord); point to 1 Thess 4 and Revelation 00.
- **18:** 18:14 "justified": declared righteous (Reformation) vs infused/progressive (Trent, session 6), stated symmetrically; 18:25 no "needle gate" (medieval, unattested).
- **19:** 19:11-27 minas vs talents (same parable or not); the throne-claimant motif (Archelaus: Josephus *Ant.* 17.9.3); nobleman = Christ vs a protest reading (third servant as hero; Herzog on Matt 25): give it and why most reject it (19:11, 27).
- **20:** 20:25 Caesar and God: Lutheran two-kingdoms, Reformed transformationalist, Anabaptist; 20:34-36 no marriage in the resurrection, yet recognition and love not lost (Augustine, Calvin); "like angels" in deathlessness (20:36).
- **21:** Olivet: (a) mainly AD 70 (preterist: R. T. France on Mark 13, Wright, Gentry), (b) mainly the end (futurist: Walvoord), (c) near and far together (Carson on Matt 24, Stein, Marshall, Bock; most evangelicals). Luke separates 21:20-24 (city, "times of the Gentiles") from 21:25-28 (cosmic, Son of Man). 21:32 "this generation" options. Point to Revelation 00 for millennial schools.
- **22:** 22:19b-20: shorter text (Codex D, some Old Latin; Westcott-Hort) vs longer (P75 and the major uncials; NA28, ESV, CUV; Metzger): most accept the longer. 22:43-44: absent from several early witnesses (P75, B and others), present in others (ℵ*, D) and known to Justin and Irenaeus; ESV and CUV print it; later addition (Ehrman) vs authentic or undecided (Raymond Brown, Bock, Nolland). "Like great drops of blood" is a simile. Check sigla against Metzger before citing. 22:36-38 swords.
- **23:** 23:34a: absent from P75, B and others, present in ℵ*, A, C and most; ESV and CUV print it; many (Metzger) judge it authentic tradition even if textually uncertain; give both. 23:43 "today": comma after "today" (Jehovah's Witnesses, some conditionalists) vs before (nearly all; Luke's σήμερον; Phil 1:23); Paradise and the creed's descent clause (Calvin; Catechism 632-635; Formula of Concord IX) briefly.
- **24:** Jerusalem appearances vs Galilee (Matt 28; John 21): Luke's selection and compression (24:50 vs Acts 1:3 forty days: same author); order of appearances (1 Cor 15:5-8; John Wenham, *Easter Enigma*); 24:12, 40, 51b (Western omissions; longer text accepted); empty tomb and the women's testimony (Wright, *The Resurrection of the Son of God*; Licona); 24:44 "Moses, the Prophets and the Psalms".

## 4. Meditation assignments

Rules: open in the assigned scene; gospel ground before any step; speak to the reader who has failed; a safeguarding or care line where marked; end on Christ, never on a task. Avoid every retired frame in WORKFLOW (accusing voice, phone, 吃亏, sleeplessness openings, protector-deity, "outside looking in", "filled", exams, doxology, "came near", hands-of-Christ, door, morning star, keys, "the Lord is faithful" / "he will surely do it" / "that is enough" endings). Verses already used in other books' meditations (do not use as pivot or ending; a passing mention in the body is fine): Luke 1:10; 2:36-38; 3:23; 4:6-8, 18; 5:8; 7:13, 47; 9:51; 10:20; 12:19, 32; 13:4-9; 14:10; 15:2, 4-5, 20, 28; 18:11; 19:5, 8, 10, 41-42; 22:15, 20, 24, 31-32; 23:30, 34, 42-43; 24:27, 34, 39; parallels Mark 6:3, 14:36, 15:31; Matt 3:17, 17:5-8, 8:20, 27:46. Peter's denials, the prodigal's elder brother and best robe, the lost sheep, Zacchaeus, the thief's "today", "Father, forgive them", Gethsemane's cup and the John 21 breakfast are all taken.

| Ch | Shape | Name | Scene (Chinese church / family life) | Theme | Pivot | Ending (Christ) |
|---|---|---|---|---|---|---|
| 00 | adoration | 老顾 | Retired bridge engineer, baptized at 66, keeps a notebook of dates and "problems" (Quirinius, two genealogies); afraid his faith is only feeling | certainty that rests on what God accomplished, not on my reconstruction | 1:1-4 「所成就的事」「确实的」 | 2:28-30 Simeon "my eyes have seen your salvation": salvation is a person held in arms |
| 01 | story | 姜姊妹 | Married nine years, no child, at a cousin's 满月酒; mother-in-law's 「不孝有三，无后为大」 | lineage pressure and worth; no promise of a child (say so); line for miscarriage | 1:50 mercy 「直到世世代代」 not carried by my bloodline; 1:48 lowliness | 1:68-69 the horn of salvation raised in David's house |
| 02 | adoration | 小邓 | Food-delivery rider on the Christmas Eve night shift, outside the church's carol service with a stack of orders | good news that comes to the workplace at night (not "outside looking in") | 2:8-11 shepherds "keeping watch… by night", 「为你们」 | 2:12 the sign: the Savior in the manger, a poor family's bed |
| 03 | one step | 老曹 | Small building contractor delaying migrant workers' wages before 春节 (拖欠工资) | concrete repentance in my own trade | 3:12-14 「我们当做什么呢？」 | 3:21 Jesus baptized among all the people: the sinless one in line with sinners (not about the reader's baptism) |
| 04 | short prayer | 谭弟兄 | Laid off at 35 (35岁危机); tempted by a shortcut (fake credentials, a "can't-lose" scheme) | hunger and the temptation to use my standing to serve myself | 4:1-3 Spirit-led into the wilderness, hungry | 4:4 with 3:38 / 4:3: the faithful Son who did not turn stones to bread, for me |
| 05 | story | 小蔡 | New believer, a Macau casino croupier, holds a birthday dinner for colleagues and her small group; both sides awkward | bringing my old world to Jesus' table; the church's discomfort | 5:29-31 Levi's feast; "those who are sick" | 5:32 「我来本不是召义人悔改，乃是召罪人悔改」 |
| 06 | one step | 姚阿姨 | Mother-in-law measuring her daughter-in-law (housework, how she raises the grandchild) | the measure I use on family; safeguarding line (abusive in-law relationships) | 6:36-38 merciful as the Father; the measure | 6:35 he is kind to the ungrateful and the evil: shown in the Son who died for me |
| 07 | adoration | 陆弟兄 | Has left four churches in six years (too loud, too dry, too long, too short); line for those who left because of real abuse | the never-satisfied critic (7:31-32) | 7:31-34 flute and dirge | 7:34 the insult 「税吏和罪人的朋友」 is my gospel |
| 08 | one step | 小蒋 | Three years in drug rehab; now a believer in a city recovery fellowship; dreads going home to his village for 春节 | testifying at home where I was known at my worst; relapse line | 8:38-39a "return to your home" | 8:39b 「耶稣为他做了何等大的事」: what God did is what Jesus did |
| 09 | short prayer | 老钟 | One-child-policy father; his only son (29) has schizophrenia; the church's prayer team "could not" (9:40); medicine is good, healing may wait for the resurrection | Jesus did not stay on the mountain | 9:37-41 「求你看顾我的儿子……独生子」「将你的儿子带到这里来吧」 | 9:42-43 he healed the boy and gave him back to his father: God's majesty in the Son |
| 10 | one step | 小卢 | Sees an old man fall at a bus stop; 「扶不扶？」 fear of being blamed (彭宇案 memory); personal-safety line | justifying myself (10:29) by shrinking "neighbor" | 10:29-33 | 10:33 with caution (section 3): Christ, called a Samaritan (John 8:48), who counted no risk in coming to me |
| 11 | adoration | 叶姊妹 | Mother insists on 中元节 offerings; Ye secretly keeps a temple amulet in her bag "just in case" since her father's death | fear of spirits; not Jesus as a stronger charm but the King whose kingdom has come | 11:20-21 the finger of God; the strong man | 11:22 the stronger one who disarmed him and divides the spoil (Col 2:15) |
| 12 | one step | 苏弟兄 | Siblings fighting over their late parents' flat (分家业); a lawyer's letter; going to court can be right | covetousness inside the family | 12:13-15 「人的生命不在乎家道丰富」 | 12:37 the master who girds himself and serves his servants at table |
| 13 | short prayer | 熊弟兄 | Grandfather dies never having believed; at the funeral a relative asks "Is he in hell?" | speculation vs "strive"; trusting the Judge (Gen 18:25); no universalism, no false comfort | 13:23-24, 29 | 13:34a the hen gathering her chicks: Christ's longing, which went on to Jerusalem |
| 14 | story | 范姊妹 | Son 乐乐 (9) has autism; after stares and a complaint about noise in service, the family stopped coming | the banquet is for those the church finds inconvenient | 14:21 「贫穷的、残废的、瞎眼的、瘸腿的」 | 14:22 「还有空座」 |
| 15 | adoration | 小崔 | Young mother turns her rented flat upside down for her lost wedding ring, then calls her neighbors | do I believe God rejoices over me, not merely tolerates me (do not rebuild the elder brother) | 15:8-9 lamp, broom, "rejoice with me" | 15:10 joy before the angels of God (Heb 12:2 "for the joy set before him") |
| 16 | short prayer | 程弟兄 | Prays for a miracle to convince his skeptical father: "if Dad saw one healing he'd believe" | wanting signs over the Word | 16:29-31 「有摩西和先知的话」 | 16:31 "one rose from the dead": the speaker himself |
| 17 | one step | 侯弟兄 | Recovered after cancer surgery; months of church prayer; back at work, never came back to give thanks | thanksgiving that returns to the person, not repayment (avoid 人情 / owing God) | 17:15-18 「那九个在哪里呢？」 | 17:15-16 glory to God given at Jesus' feet |
| 18 | short prayer | 老董 | Released after five years for embezzlement; can't lift his eyes in the service; restitution and victims line | justification of the ungodly | 18:13 「神啊，开恩可怜我这个罪人」 | 18:14 「这人回家去……倒算为义了」: righteous by another's righteousness |
| 19 | story | 小薛 | Gifted Bible-study leader who stopped after a harsh rebuke; pictures God as 「严厉的人」 | fear of a harsh master buries gifts | 19:20-21 the napkin | 19:38 the king coming to Jerusalem on a borrowed colt to die (not a doxology) |
| 20 | adoration | 康伯伯 | Widower who remarried; at his 80th birthday a relative jokes, "Whose husband will you be in heaven?" | grief, remarriage and resurrection hope | 20:34-36 | 20:38 「因为在他那里，人都是活的」, the risen Christ as firstfruits |
| 21 | story | 田长老 | The church's building of thirty years is demolished in urban redevelopment (拆迁); the congregation meets in a rented hall (no political framing) | grief over loved stones | 21:5-6 | 21:33 「我的话却不能废去」 |
| 22 | short prayer | 石弟兄 | Co-founder and church brother took the clients and left with a warm farewell; safeguarding / legal line | betrayal by a friend at my table | 22:21, 48 | 22:27 「我在你们中间如同服事人的」: he served the betrayer at the same table |
| 23 | story | 邵弟兄 | Left university at 20 to pay his late father's restaurant debts (父债子还) | a cross laid on me by others' choices | 23:26 Simon 「背着跟随耶稣」 | 23:47 「这真是个义人」: the righteous one carried the real cross |
| 24 | adoration | 江弟兄 and wife | Couple walking home in silence after Easter service, a year after their business and hopes collapsed | "we had hoped" and the necessary suffering of Christ | 24:21, 26 | 24:52 「他们就拜他，大大地欢喜」 (Luke's opening joy, 1:14; 2:10, closes) |

Shape count: adoration 7 (00, 02, 07, 11, 15, 20, 24), story 6 (01, 05, 14, 19, 21, 23), one step 6 (03, 06, 08, 10, 12, 17), short prayer 6 (04, 09, 13, 16, 18, 22). Vary prayer openings (Hebrews 06, 07, 09 already use 「主耶稣，……」).

## 5. Names and scenes used (running list: read before writing; add after)

Luke assigned (one surname per chapter, none to reappear):
老顾 (00 engineer's notebook), 姜姊妹 (01 满月酒), 小邓 (02 delivery rider), 老曹 (03 unpaid wages), 谭弟兄 (04 laid off at 35), 小蔡 (05 casino croupier's dinner), 姚阿姨 (06 mother-in-law), 陆弟兄 (07 church-hopper), 小蒋 (08 rehab, going home), 老钟 (09 only son), 小卢 (10 fallen old man), 叶姊妹 (11 amulet, 中元节), 苏弟兄 (12 parents' flat), 熊弟兄 (13 grandfather's funeral), 范姊妹 and 乐乐 (14 autism), 小崔 (15 lost ring), 程弟兄 (16 skeptical father), 侯弟兄 (17 after cancer surgery), 老董 (18 released prisoner), 小薛 (19 study leader rebuked), 康伯伯 (20 remarried widower), 田长老 (21 demolished church), 石弟兄 (22 co-founder's betrayal), 邵弟兄 (23 father's debts), 江弟兄 and wife (24 walk home after Easter).

Already used in other books (do not reuse): surnames 冯, 宋, 李, 郑, 林, 吴, 何, 赵, 黄, 方, 周, 王 (王奶奶); given names 素珍, 秀兰, 小雅; Revelation 00 grandmother and 外孙; Revelation 20 deacon. Avoid 陈 and 刘 (collided in Revelation drafts). Minor characters inside a meditation (a relative, a pastor) stay unnamed. Grep `plans/books/*/*.md` before adding any name.

Scenes taken elsewhere (avoid): New Year wishes, being called unfilial at a funeral, investment fraud, hospital vows, job-form religion line, church stove, choir, wedding seating, group chats, pandemic livestream, a strange city, caring for parents, exams.

## 6. Batches (WORKFLOW section 6)

Two Opus drafters per batch, two chapters each (batch 6: one takes 20-21, the other 22-24 or split 20-22 / 23-24). While a batch is in review, draft the next; keep 3-5 agents running. Each batch's drafters read the finished meditations of earlier batches and this list.

| Batch | Files | Drafter A | Drafter B |
|---|---|---|---|
| 1 | 00-03 | 00, 01 | 02, 03 |
| 2 | 04-07 | 04, 05 | 06, 07 |
| 3 | 08-11 | 08, 09 | 10, 11 |
| 4 | 12-15 | 12, 13 | 14, 15 |
| 5 | 16-19 | 16, 17 | 18, 19 |
| 6 | 20-24 | 20, 21 | 22, 23, 24 |

Per batch: draft → theology → (application ∥ Chinese) → revise → re-review if large → book-publisher (quote check, build in a temporary worktree of HEAD without unreviewed drafts, tests, log rows, commit). After the batch is published, add to section 5 any new names, verses and endings actually used, and add a short "After Luke NN-MM" line to the resume notes for WORKFLOW at release.
