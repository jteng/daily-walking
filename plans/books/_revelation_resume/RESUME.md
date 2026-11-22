# Revelation 00-05: resume notes (delete this folder before publishing)

User request: run the Book Study workflow for Revelation, **stop after chapters 1-5** (plus 00 intro). Publish to branch `claude/there-8j0kr7` via book-publisher, then **ask the user before merging** (book incomplete). Do not release/bump versions for a partial book unless the user says so.

Shared drafting brief (framework, names, meditation assignments): `plans/books/_revelation_resume/revelation_brief.md`
Book-wide name forms: 约翰·华尔伏 (Walvoord), 《司可福串注圣经》, 毕尔 (Beale), 包衡 (Bauckham), 大卫·奥尼 (Aune), 肯尼斯·詹特里 (Gentry), 乔治·赖德, 安东尼·胡克玛, 威廉·亨德里克森, 罗兰·贝特纳（Loraine Boettner）. Osborne: pick one (00 has 葛兰·奥斯本, 02 has 格兰特·奥斯本) — use 格兰特·奥斯本 everywhere.

## Status per file (as of commit 9a5cc6f)

| File | Theology | Application | Chinese |
|---|---|---|---|
| 00 | passed (review + recheck, all applied) | done, applied (commit 0cca22a) | done: no must-fix, 7 should-fix (`rev00_chinese.md`); applying |
| 01 | review done (`plans/books/_revelation_resume/rev01_theology.md`); drafter was applying fixes and was **cut off mid-edit** — diff committed in 9a5cc6f; finish applying, then theology recheck | — | — |
| 02, 03 | review done (summary below); **not yet applied** | — | — |
| 04, 05 | review done (`plans/books/_revelation_resume/rev0405_theology.md`); drafter **cut off mid-edit** — partial diff committed; finish applying, then recheck | — | — |

Then: application + Chinese reviews for 01-05; apply; book-publisher (quote check, build, tests, REVIEW_LOG rows per reviewer, commit, push); add Revelation 00-05 meditation themes to WORKFLOW.md; delete this file; ask user about merging.

Cross-chapter from 00 Chinese review: 04 uses 图密善 → change to 多米田; 02/03 first mention of Osborne must be full 格兰特·奥斯本.

## Revelation 00 application review — to apply (should-fix 1 + consider 2-6)
1. Meditation pivot/ending too close to 2 Thessalonians 00 ("not a chart/date but a person", "the Lord who loves us"). Paragraph 2: replace 「幔子拉开，先显出来的不是一张图表，而是一个人。」 with zh 「那时众人一同听见的第一句话，是「耶稣基督的启示」（1:1）。幔子拉开，先听见的是一句称颂：约翰刚问完安，就忍不住说：「他爱我们，用自己的血使我们脱离罪恶……」（1:5-6）」 / en "And the first words those gathered hearers heard were 'the revelation of Jesus Christ' (1:1). When the curtain is drawn back, the first thing heard is praise: John has barely finished his greeting before he breaks out, 'To him who loves us and has freed us from our sins by his blood…' (1:5–6)." Last paragraph: drop the "chart on the wall" phrase and the repeated 1:5 clause; zh 「那卷叫外婆害怕了三十多年的书，最后落在的不是一只兽，而是耶稣亲口报出自己的名字。在一切的号声和碗以先，他已经在那里。晨星升起的时候，夜还没有完全过去，可是看见它的人已经知道：天要亮了。先升起来的，是他。」 / en "The book that frightened Grandma for more than thirty years does not end on a beast; it ends with Jesus speaking his own name. Before every trumpet and every bowl, he is already there. When the morning star rises the night is not yet over, but whoever sees it knows the day is coming. He is the one who rises first."
2. Paragraph 3: don't tie 22:10 to John's failure; zh 「约翰看错了方向，天使没有丢下他，只把他的眼目转回来：「你要敬拜神」，因为「预言中的灵意乃是为耶稣作见证」（19:10）。这卷书也仍要敞开，念给众教会听（22:10）。」 / en "John looked the wrong way, and the angel did not abandon him; he turned his eyes back: 'Worship God,' for 'the testimony of Jesus is the spirit of prophecy' (19:10). And the book itself stays open, to be read to the churches (22:10)."
3. After 「……本来是在教会里念给大家一同听的。」 add zh 「我自己呢？也许我像外婆，也许像孙子，也许两样都有一点：怕的时候就跳过，好奇的时候就一个人去拆。」 / en "And me? Perhaps I am like Grandma, perhaps like her grandson, perhaps a little of both: skipping the book when I am afraid, taking it apart alone when I am curious."
4. What This Book Is About ¶2: after 「因为它必要倾倒」 add 「；羔羊所要给的，远比它更好（3:18；21:2）」 / en ", and what the Lamb gives is far better (3:18; 21:2)".
5. Key Verses 1: start from the blessing: zh 「……遵守，是从这福来的：启示录是要人听进去、活出来的话：……」 / en "…Keeping flows from this blessing: Revelation is a word to be taken in and lived out: …"
6. 外婆 + 孙子 mismatch: use 外孙 (or 奶奶) consistently in zh (let Chinese reviewer confirm).
WORKFLOW notes: 22:16 morning star is now 00's ending (later chapters, esp. 22, must not end on it); 19:10/22:8-9 and 7:14 used in a meditation; three end-times meditations now (1 Thess 5, 2 Thess 00, Rev 00) — Rev 01-05 must not rebuild them.

## Revelation 02-03 theology review — to apply (verdict: ready after must-fix)
MUST-FIX
1. 03 §3:19 pt 1: phileō vs agapaō overread. Replace with en "Where the Greek Old Testament of Prov 3:12 has *agapaō*, John writes *phileō*; some see extra warmth in the change, though the two verbs overlap so widely that the point should not be pressed. Either way, his rebuke is not rejection; it is a father's love." / zh 「箴言3:12的七十士译本用的是 *agapaō*，这里约翰用的是 *phileō*；有人认为这更带亲密的情感，不过这两个词的意思大量重叠，不宜推得太远。无论如何，他的责备不是厌弃，而是父亲的爱。」
2. 03 same point: aorist "decisive turn" overread. en "Many take the present imperative 'be zealous' as calling for ongoing zeal, alongside the summons to repent." / zh 「许多人认为，「发热心」用现在式的命令，带有持续的意思；同时主也呼召他们悔改。」 Drop "decisive turn".
3. 03 §3:14-18 pt 5: eye salve contradicts own hedge. en "…targets things the city was known for (the eye remedy is the least certain of the three) … the region was linked with a Phrygian eye remedy, but the Lord says they are blind…" / zh 「主所开的药方，正对着这城出名的东西（其中眼药一项最不确定）……这一带和一种弗吕家眼药有关，主却说他们是瞎眼的……」
4. 02 §2:18-29 pt 5: "bed" wordplay. en "(the Greek says simply 'bed', *klinē*; many commentators see irony here: the couch of immorality, or the dining couch of the guild feasts, becomes a bed of sickness)" / zh 「（原文只说「床」，这个词也可以指宴席上斜靠的榻；许多解经家认为这里带着讽刺：淫乱的床或偶像宴席的榻，要变成病床）」
5. 02 "What are the seven churches?": Scofield unfair (his note gives local/all churches/personal/prophetic). Best: replace paragraph with two sentences + "see chapter 1": dispensational reading (《司可福串注圣经》1909) accepts real churches with a message for all, but adds that the seven also foreshadow periods of church history; mapping (e.g. Philadelphia = revival/missions) is later popular form. 01 already treats it (and may name 倪柝声《教会的正统》).
SHOULD-FIX
6. Name forms across 00-05 (Walvoord, Osborne) — see top.
7. 02 §2:1-7 pt 4 "Both": name Osborne only (or "some commentators"); optionally add Beale's reading: lost love = fading witness (lampstand removal). zh 「也有人（如毕尔）把它和见证的热心衰退连在一起，因为主警告要挪去的是灯台。」
8. 02 §2:8-11 pt 4: "Smyrna often called crown of Asia" overstated → en "Ancient writers spoke of the ring of buildings on Smyrna's hill as its 'crown', and some scholars (e.g. Ramsay) hear an allusion." / zh 「古代作者曾把士每拿山上环绕的建筑比作城的冠冕，有学者（如拉姆齐）认为这里可能暗指此事。」
9. 02 Thyatira "smallest" → 「名气最小、地位最不显要的一个」 / "least known and least important".
10. 02 Thyatira: add en "The name must not become a label for women who speak up or for those who raise concerns; the sin named here is false teaching that leads God's servants into idolatry and immorality." / zh 「「耶洗别」这个名字不可以拿来给敢于说话的姊妹或提出投诉的人贴标签；这里所责备的，是引诱神仆人拜偶像、行淫乱的假教导。」 And say once that applying 2:20 to sexual abuse of spiritual authority is by analogy.
11. 03 §3:1-6 pt 6: cite (13:8; 17:8), lean on 17:8 (13:8 syntax ambiguous); Arminian bullet may cite Exod 32:33; Rev 22:19.
12. 03 §3:7-13 pt 6 (3:10): pre-trib side add en "They stress that the promise is to keep them from the *hour*, the period itself, not only from the trial." / zh 「他们强调，主应许保守他们免去的是那「时候」本身，不只是试炼。」 Optional preterist line.
13. 03 §3:7-13 pt 5 (3:9): 「大概以外邦人为主」 / "probably largely Gentile"; add en "This does not mean God has cast off his ancient people (Rom 11:1–2, 28–29)." / zh 「这不是说神已经弃绝了他的古民（罗11:1-2、28-29）。」; bowing: "some see hope of conversion here, others a final acknowledgment" / 「有人认为…也有人认为这是末日被迫的承认」 (drop "many scholars").
14. Meditation endings: 02 should end on the tree of life (not "being loved"; avoid "hand"): e.g. zh 「……有一天，他要把神乐园中生命树的果子赐给我吃。」; 03 ending: use 3:19 not 3:9: en "…but because he has said to people like me, 'Those whom I love' (3:19)." / zh 「……而是因为他对我这样的人说过：「凡我所疼爱的」（3:19）。」
15. 02 meditation: cut the Martha paragraph (used in 1 Thess 4 / John 11; saves ~1.2 KB per language).
CONSIDER
16. 02 2:9: Satan = "adversary" (accuser in court, 12:10); "devil" v10 = slanderer, matching v9 "slander"; hedge protection point "many scholars think".
17. 02 Pergamum: add Dio Cassius 51.20.6-7 for 29 BC temple.
18. 02 Nicolaitans: Clement of Alexandria *Stromateis* 3.4 defends Nicolaus; optional etymology "conqueror of the people" ≈ Balaam.
19. 02 Polycarp: *Martyrdom* 16.1 (fire didn't consume him; stabbed); John link via Irenaeus to Florinus (Eusebius *Church History* 5.20.6).
20. 03 Sardis: Croesus is historical: 「以富有闻名的」 / "proverbially rich"; attribute "living on its past" (Ramsay, Hemer); add Matt 24:43.
21. 03 3:4 & 19:8: add "granted righteousness that shows in deeds".
22. 03 Philadelphia: "In the years after the earthquake of AD 17…"; "the holy one, the true one" (3:7) = God's title in 6:10 → Christ's deity; Flavia rename.
23. 03 3:14: add 2 Cor 1:20; optional Arians/Prov 8:22 LXX; John 1:3.
24. 03 3:20 Holman Hunt: cut bullet, or add "his knock is his voice… (John 10:27; cf. Acts 16:14)".
25. 03 meditation: "hung naked" → "stripped of his garments (John 19:23–24)" / 「被剥去衣服（约19:23-24）」; keep 「不要欠人情」 brief.
26. 03 Laodicea water: link Rudwick–Green with 3:19 so they don't contradict.
CUTS (02 51 KB, 03 48 KB → ~35 KB): 02: seven-churches para to 2 sentences; Martha para; Pergamum city + Satan's-throne views to one sentence each; white stone to one line; shorten Thyatira background. 03: cut "doorway to the throne" (§3:19-22 pt 4); cut Holman Hunt; trim "seven letters together"; condense Laodicea city + water into one paragraph; trim 3:12 bullets.
KEEP: synagogue-of-Satan care; Thyatira safeguarding + faithful-pastor balance; 3:5 symmetric labels; 3:10 Walvoord vs Ladd/Beale/Osborne + John 17:15; 3:14 vs JW; 3:20 church context; meditations' gospel-first shape.
