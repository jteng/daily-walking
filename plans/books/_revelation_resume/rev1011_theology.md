# Theology review: Revelation 10 and 11 (drafts)

Reviewer: theology-reviewer (Carson/Packer-style lens; independent of drafter). Date: 2026-11-26.
Files: /home/user/daily-walking/plans/books/revelation/10.md, /home/user/daily-walking/plans/books/revelation/11.md

## Verdicts

- **10.md: ready** (no must-fix; apply the should-fix items, chiefly F3-F6, per WORKFLOW step 4).
- **11.md: ready after must-fix items** (F1, plus the label and balance fixes F7-F9 and the ~6 KB cuts in F10).

Quote checks: `check_cuv_quotes.py` flags only meditation dialogue in both files (10: one line; 11: four lines), which is fine. A script check of every English quotation of 3+ words against EnglishESVBible.xml found no misquotes (the misses were the KJV gloss "there should be time no longer", the "day for a year" principle, and dialogue). Spot checks with `bible_lookup.py` (5:2 "strong angel", 10:1, 10:8, 11:7, 11:13, 14:7, 16:9, Mark 13:20, Luke 9:54-55, Heb 1:4, Col 2:2) all match.

Doctrine: no errors. Christ's deity, the cross and the blood (1 John 1:7; Mark 15:31), grace before the task, and the authority of Scripture ("the book he wrote is the word of God") are all stated clearly. The findings are about exegesis, labels, attributions and cross-chapter fit.

---

## MUST-FIX

### F1. 11.md, 深读 11:3-6 §4 / Going Deeper 11:3–6 §4, preterist bullet: Peter and Paul were not killed in Jerusalem
- zh: 「一些过去派的学者认为，他们是耶路撒冷被毁以前在那里作见证的人；有人认为是彼得和保罗，也有人认为泛指当时作见证的教会。」
- en: "some preterist scholars take them as those who bore witness in Jerusalem before its fall; some suggest Peter and Paul, others the witnessing church of that time in general."
- **Problem:** Tradition places the martyrdoms of Peter and Paul in Rome under Nero, not in Jerusalem, so the sentence contradicts itself. The Peter-and-Paul reading (e.g. Johannes Munck, 1950) ties 11:8 to Rome, and it is a minority view that is not usually called preterist in the Gentry/Chilton sense. The bullet also has no named representative, unlike every other bullet (WORKFLOW: symmetric labels).
- **Fix (zh):** 「**一世纪的见证人：** 一些过去派的释经者（如肯尼斯·詹特里、大卫·奇尔顿）认为，这是耶路撒冷被毁以前，教会在那城中向以色列所作的先知性见证。另有少数学者认为是在尼禄手下殉道的彼得和保罗。」
- **Fix (en):** "**First-century witnesses:** some preterist interpreters (e.g. Kenneth Gentry, David Chilton) take them as the church's prophetic witness to Israel in Jerusalem before its fall. A few scholars have instead suggested Peter and Paul, martyred under Nero."
- Hedge: I am confident of Chilton (*The Days of Vengeance*, 1987) in substance. If Gentry's exact view of the witnesses cannot be checked, name Chilton only, or write 「一些过去派的释经者」 / "some preterist interpreters" with no name. Since §4 is also a place to cut (F10), you may simply drop the Peter-and-Paul clause.

---

## SHOULD-FIX

### F2. Both files: "lean" sentences must match 00's eclectic framing, and labels must be symmetric
00 (zh l.86 / en l.196) says the study 「采取综合的读法」 / "reads eclectically": written to seven real churches, speaking to every age, and pointing to a real end still to come. In 11 the study "leans" three times toward the church/whole-age reading (temple, 42 months, two witnesses) and also gives the world-city reading most room. That is a legitimate choice (Beale and Bauckham, both named in 00, read these that way), but two things need fixing:
- **(a) Asymmetric adjectives.** 「将来真实的三年半」 / "A literal future three and a half years" (the en is fine; the zh 真实 implies the symbolic view is not real) and 「将来两位真实的先知」 / "Two real prophets in the future" both suggest the church reading is less real.
  - Fix: zh 「将来字面的三年半」, 「将来两位个别的先知」; en "Two individual prophets in the future".
- **(b) Tie the first lean back to 00 and keep the future end in view.** At the first "lean" (11:1-2) add:
  - zh: 「这符合导读所说的综合读法：经文写给一世纪的教会，也向每个时代的教会说话；而且许多持这种读法的人（如毕尔、威廉·亨德里克森）也认为，兽对见证人最后的攻击（11:7）指向基督再来以前一次最后的、更猛烈的逼迫。」
  - en: "This fits the eclectic reading set out in the Introduction: the text addressed first-century churches and speaks to the church in every age. Many who hold this view (e.g. Beale, William Hendriksen) also see in the beast's final attack (11:7) a last, intensified persecution before Christ returns."
- Do not label the Beale/Bauckham bullets "idealist" (the draft rightly does not). 08 and 09 use 理想派 for Hendriksen/Beale bullets; in 11 the descriptive labels ("God's people, the church"; "A symbol of the whole church age") are better and should stay.

### F3. 11.md, 深读 11:2-3 §2 / Going Deeper 11:2–3 §2: a major futurist view is missing
- The futurist option is given only as dispensational (Walvoord). Many non-dispensational futurists and historic premillennialists take the 42 months / 1,260 days as a final period of tribulation just before the return, whose length may be symbolic (the "Ladd/Osborne mixed" position the brief names for the series question).
- **Fix:** widen the first bullet.
  - zh: 「**将来末了的一段日子：** 时代论的学者（例如约翰·华尔伏）认为，这是但以理第七十个七的后半，就是将来大灾难中字面的三年半；另一些未来派学者（例如乔治·赖德）也认为这是基督再来以前末了的一段苦难时期，但长度可能是象征的。」
  - en: "**A future final period:** dispensational scholars (e.g. John Walvoord) take it as the second half of Daniel's seventieth week, a literal three and a half years within the future tribulation; other futurists (e.g. George Ladd) also see a final period of tribulation before Christ's return, though its length may be symbolic."
- (Optional) dispensationalists differ on whether the witnesses' 1,260 days are the first or second half of the week. One clause is enough, or leave it out.

### F4. 10.md, 深读 10:5-7 §4 "成全" bullet: overstated John 19:30 link, and the "It is finished" overlap with 14
- zh: 「这个动词（*teleō*）和约翰福音19:30耶稣在十字架上所说的「成了」，是同一个字根。许多释经者看见两者的关联」
- en: "this verb (*teleō*) shares its root with 'It is finished,' Jesus' word on the cross (John 19:30). Many interpreters see the connection"
- **Problem:** (1) It is the same verb, not only the same root (ἐτελέσθη / τετέλεσται). (2) "Many interpreters" overstates the case. Commentators on Revelation seldom make this link; it is a canonical, devotional connection, not a standard exegetical one. (3) The link Revelation itself makes is to the same verb in 11:7 (「作完见证」 / "finished their testimony") and 15:1 (「发尽了」 / "is finished").
- **Fix (zh):** 「**「成全」：** 这个动词（*teleō*）在启示录里也用在见证人「作完见证」（11:7）和神的大怒在七灾中「发尽了」（15:1）。神所定的事，没有一件会半途而止。」
- **Fix (en):** "**'Fulfilled':** Revelation uses the same verb (*teleō*) when the witnesses have 'finished their testimony' (11:7) and when 'the wrath of God is finished' in the last plagues (15:1). Nothing God has purposed stops halfway."
- If you want to keep the cross, add a hedged clause: 「有些读者也会想起主耶稣在十字架上所说的「成了」（约19:30），原文是同一个动词。」 / "Some readers also hear an echo of 'It is finished' (John 19:30), the same verb." I recommend dropping it, so that 14 owns the theme (F5).

### F5. Cross-chapter: "It is finished" (John 19:30) should be kept in 14 and removed from 10's meditation
- 14's meditation builds a whole paragraph on 「成了」: Christ's finished work goes before ours, and rest follows. That is its structural pivot, so it should stay in 14. In 10 it is one sentence near the end.
- 10.md, 默想 last paragraph:
  - zh: 「这佳音的中心，是那位在十字架上说「成了」的主；到了第七号吹响的时候，神的奥秘必要成全。」
  - en: "At the center of that good news is the Lord who said 'It is finished' on the cross; when the seventh trumpet sounds, the mystery of God will be fulfilled."
- **Replacement (Col 2:2, "God's mystery, which is Christ"; this ties 10:7's "mystery" to Christ and is not in WORKFLOW's used lists. Heb 6:17-18's oath and 2 Cor 1:20 are already used.)**
  - zh: 「故事不需要由她来讲完。保罗说，神的奥秘「就是基督」（西2:2）：那位为她流血、也仍在呼唤那个离开的孩子的主，就是这奥秘的中心。到了第七号吹响的时候，神的奥秘必要成全。天地的创造主、直活到永远的神，已经为此起了誓。」
  - en: "The story does not have to be finished by her. Paul speaks of 'God's mystery, which is Christ' (Col 2:2): the Lord who shed his blood for her, and who is still calling the boy who left, is the heart of it. When the seventh trumpet sounds, the mystery of God will be fulfilled. The Creator of heaven and earth, who lives forever, has sworn it."
- The meditation still ends on the oath (10:6-7), as the brief assigns. Avoid "shed his blood for the boy": the replacement says "still calling" so as not to imply anything about the boy's standing.

### F6. 10.md, 深读 10:1-4 §2: guard against reading "angel" as "created angel" if the angel is Christ
- The Beale bullet ("this angel is probably Christ") is accurately attributed. Beale (NIGTC, 1999) identifies the figure as the divine Angel of the LORD, i.e. Christ. Bauckham and Osborne take him as an angel; Bauckham links him to the revealing angel of 1:1, which you could add. In a Chinese context, where Jehovah's Witnesses equate Christ with Michael, readers need one clause.
- **Add to the Beale bullet:**
  - zh: 「即使采用这种看法，「使者」也只是指奉差遣而来，不是说基督是受造的天使；神的儿子「远超过天使」（来1:4）。」
  - en: "Even on this view, 'angel' means one who is sent, not that Christ is a created angel; the Son is 'as much superior to angels as the name he has inherited is more excellent than theirs' (Heb 1:4)."

### F7. 10.md, 深读 10:8-11 §1: the diminutive argument is overread; Beale is understated
- zh: 「有些释经者（如大卫·奥尼）认为，原文用的是指小词（*biblaridion*），这是另一卷书」; 「毕尔也认为两者关系密切」
- en: "some interpreters (e.g. David Aune) note the diminutive (*biblaridion*)"; "Beale also sees the two as closely linked"
- **Problems:** (1) In 10:8 the better-attested Greek text has the ordinary *biblion*, not the diminutive. That is why the ESV has "the scroll" in 10:8 while the CUV, following the later text, has 「小书卷」. This is the main reply to Aune and also explains the zh/en difference in the quotation. In Koine the diminutive often carries little sense of "small". (2) Beale does identify the little scroll with the ch. 5 scroll, not merely "closely link" it. The Aune attribution (WBC 52B: a distinct scroll whose content is roughly 11:1-13) is sound as worded.
- **Fix (zh), same-scroll bullet:** 「包衡和毕尔都认为是同一卷书：第5章封严的书卷由羔羊揭开以后，现在「是展开的」（10:2）……而且10:8较早的抄本用的是普通的「书卷」一词（和合本依照后来的抄本作「小书卷」），所以指小词未必有多大分量。」 (No English words inside ::zh.)
- **Fix (en):** "Bauckham and Beale both identify it with the chapter 5 scroll... and in 10:8 the better manuscripts use the ordinary word *biblion* (hence the ESV's 'the scroll'), so the diminutive may carry little weight."

### F8. 10.md, 深读 10:5-7 §2-3: "no more delay" against the 1,260 days of ch. 11
- 10 says "nothing will any longer hold back God's purpose", and 11 then sets out a 1,260-day period. Readers will ask how "no more delay" fits a further three and a half years. Daniel's oath (Dan 12:7, which the draft cites) answered with "a time, times, and half a time", the very period that returns in 11:2-3 and 12:14.
- **Add to §3:**
  - zh: 「但以理听见的「一载、二载、半载」，在第11-12章又出现了（11:2-3；12:14）。有释经者（如包衡）因此认为，「不再有时日」不是说中间再没有任何时间，而是说神所量定的最后一段日子不再推迟，已经开始了。」
  - en: "Daniel's 'time, times, and half a time' reappears in chapters 11–12 (11:2–3; 12:14). Some interpreters (e.g. Bauckham) therefore take 'no more delay' to mean not that no interval remains, but that the final period God has measured will be postponed no longer; it has begun."
- Hedge: if Bauckham's page cannot be confirmed, write 「有释经者」 / "some interpreters".

### F9. Cross-chapter pointers for the recapitulation question
- 10 Shape: 「这个问题在导读和第8章已经介绍过」 / "The Introduction and chapter 8 set out that question"; 11:19 §4: 「参看导读和第8章的讨论」 / "see the Introduction and chapter 8".
- 06 (zh l.17 / en l.104) first sets out the recapitulation question for the series, and 08 repeats it for the trumpets. Point to both, briefly: zh 「导读和第6、8章」; en "the Introduction and chapters 6 and 8". Nothing more is needed; 10 and 11 rightly do not re-argue it.

### F10. 11.md is 41.0 KB: specific cuts (~6.3 KB, both languages)
Sizes (zh+en): Shape 2.6; 11:1-2 4.5; 11:2-3 4.8; 11:3-6 7.1; 11:7-14 8.8; 11:15-19 6.4; Meditation 6.6.
1. **11:2-3 §3 "不要拿这些数字来推算 / Do not use these numbers to calculate":** cut it to one sentence and append it to §2. 10 §6 and 00 already carry this warning. zh 「这些数字是要告诉受苦的教会，苦难的日子是神所量定的，不是叫我们推算日期（可13:32；参看导读）。」 / en "These numbers tell a suffering church that its days of suffering are measured by God, not to set us calculating dates (Mark 13:32; see the Introduction)." (saves ~0.9 KB)
2. **11:2-3 §1:** drop the Dan 9:27 clause and the Luke 4:25 sentence; keep Dan 7:25; 12:7. (~0.5 KB)
3. **11:3-6 §4:** drop the Beale Smyrna/Philadelphia sentence (see attribution note below) and apply F1's shorter preterist bullet. (~0.8 KB)
4. **11:3-6 §1:** drop the Luke 10:1 sentence. (~0.2 KB)
5. **11:7-14 §3:** quote only 11:9b-10a (「不许把尸首放在坟墓里……互相馈送礼物」 / "refuse to let them be placed in a tomb... exchange presents"); the full quote repeats the Shape and the meditation opening. (~0.8 KB)
6. **11:7-14 §5:** cut the sentence 「时代论的学者把这一节读作……公开为他忠心的百姓伸冤。」 / "Dispensational scholars read this verse... at the end." The views were already set out in §4. (~0.5 KB)
7. **11:15-19 §1:** drop the Dan 2:44 sentence, and shorten the 「他要作王」 / "He shall reign" bullet to a pointer: 「单数的「他」，参第5章的讨论」 / "the singular 'he' (see chapter 5)". This also removes a slight overreading; many take "he" simply as God. (~0.6 KB)
8. **Meditation:** cut the Ezek 37:23 sentence (third paragraph, last sentence). It brings in a second OT text after the 11:11 point and slightly misdescribes the bones, which in Ezek 37:9 are "slain". Trim the church backstory in the first paragraph to one sentence (「那间小教会经过一场纷争，现在只剩八九个人，镇上的人说「那个教会早就散了」」 / matching en). Drop 「更不需要求「火从天上降下来」（路9:54）」 / "still less to 'tell fire...' (Luke 9:54)", since the body already makes the point. (~1.5 KB)
9. **Shape:** merge 11:7-10 and 11:11-14 into one bullet ("11:7–14, killed, raised, taken up"). (~0.4 KB)
Total ≈ 6.2-6.5 KB, which brings the file to about 34.5-35 KB.

---

## CONSIDER

### C1. 10.md, 10:3-4 §5, Bauckham bullet: Mark 13:20 muddles Bauckham's argument
- 「主耶稣也说过，主为选民的缘故，「将那日子减少了」（可13:20）」 / "The Lord Jesus also said that 'for the sake of the elect... he shortened the days' (Mark 13:20)."
- Bauckham's point (*The Climax of Prophecy*, 1993, ch. 9) is that the thunders are cancelled because judgment alone does not bring repentance. Mark 13:20 is about shortening tribulation for the elect's sake, which is a different rationale, and it reads as if it were Bauckham's. Drop it, or mark it as the study's own cross-reference ("cf.").

### C2. 10.md, 10:3-4 §5: the sealing contrast is clearer with Daniel
- Daniel was told to "seal the book, until the time of the end" (Dan 12:4); 22:10 reverses this. Add 「参但12:4」 / "(cf. Dan 12:4)" to the 22:10 sentence.

### C3. 11.md, 11:13 §6, closing line overreaches the second view
- 「无论哪一种看法，这节经文都显明：神的心意不只是审判，也是叫人回转。」 On the "acknowledgment under fear" view this is not what the verse shows. Suggest: zh 「无论哪一种看法，神的见证人所传的，终要叫连仇敌也承认天上的神。」 / en "On either view, the witness of God's people at last brings even their enemies to acknowledge the God of heaven." Bauckham's 11:13 reading (reversal of 1 Kgs 19:18 and the tithe of judgment; "give glory" as repentance language, 14:7; 16:9) is accurately attributed. For the second bullet, a Dan 4:34 (Nebuchadnezzar) parallel would strengthen it. Name a representative only if verified (Walvoord is likely but unchecked here).

### C4. 11.md, 11:8 §2: who holds the world-city view
- "many scholars (e.g. Beale, Bauckham)": Beale certainly holds it. I am less certain Bauckham argues 11:8 specifically in these terms, so consider "e.g. Beale". For symmetry, name a preterist (Gentry) beside Walvoord in the Jerusalem bullet.

### C5. 11.md, 11:1-2 §1: measuring can also mark judgment
- Measuring sometimes marks destruction (2 Kgs 21:13; Lam 2:8; Amos 7:7-9). Most read 11:1 as protection, so one clause is enough: 「（旧约有时也用丈量表示审判，如哀2:8，但这里多数人认为是保守）」 / "(measuring can also mark judgment, e.g. Lam 2:8, but most take it here as protection)". Within the church reading, Hendriksen-type readers take the outer court as the nominal church or the world, rather than believers' bodily vulnerability. An optional half-sentence.

### C6. 11.md, 11:19 §4
- "each time more intensely": cite 4:5 as the baseline (lightning, sounds, thunder), then 8:5 (+earthquake), 11:19 (+hail), 16:18-21 (great earthquake, great hail). This is Bauckham's observation.
- The ark: 「圣殿被毁以后」 / "After the temple was destroyed" should say the first temple (Babylon, 586 BC). Jewish tradition that Jeremiah hid the ark until God gathers his people (2 Macc 2:4-8) is apt background (write 《马加比二书》2.4-8 so the build does not read it as a Revelation verse).
- 11:17: the KJV adds "and art to come" (later manuscripts). An optional clause, since readers using 英文钦定本 will notice.

### C7. 10.md, 10:11 §4
- 「「指着」原文的介词」: fine. You could add that ἐπί + dative most likely means "about/concerning" here (ESV), with "against" possible given the judgments that follow. Keep it hedged as now.

---

## Attribution check (as requested)

- **Beale, 10:1 angel = Christ:** correct (Beale, NIGTC 1999, the divine "Angel of the LORD"). Keep, adding F6.
- **Beale, two lampstands = Smyrna and Philadelphia:** this agrees with my knowledge of Beale's commentary, where it is a secondary suggestion after Deut 19:15 and Zech 4. I cannot confirm the page here. If kept, hedge it as 「毕尔还提出一个可能的次要原因」 / "Beale also suggests, as a secondary reason". It is better cut (F10 #3).
- **Aune, little scroll as a separate scroll:** correct (WBC 52B). See F7 for the 10:8 *biblion* counterpoint.
- **Hippolytus, Enoch and Elijah:** correct (*On Christ and Antichrist* 43; Tertullian, *On the Soul* 50, likewise). "some early church writers (e.g. Hippolytus)" is well hedged. An optional citation: 希坡律陀《论基督与敌基督》43 / Hippolytus, *On Christ and Antichrist* 43 (period form for the build).
- **Bauckham, sealed seven thunders as cancelled judgments; 11:13 as repentance:** both correct (*Climax of Prophecy*, ch. 9, "The Conversion of the Nations"). Remove the Mark 13:20 mixing (C1).
- **Bauckham, 11:17 omission of "who is to come":** correct (*Theology of the Book of Revelation*).
- **Gentry (preterist):** correct for the temple standing before AD 70 as an early-date argument, and for the 42 months as the Jewish War of AD 67-70 (*Before Jerusalem Fell*). For the two witnesses, see F1.
- **Walvoord (dispensational):** correct for the future rebuilt temple, the second half of the 70th week, two individual future prophets (he does not insist on Moses/Elijah, and the draft does not say he does), and the great city as Jerusalem.
- **E. B. Elliott (historicist):** correct (*Horae Apocalypticae*, 1844; Anglican, English; day-year, papal 1,260 years).
- **Hendriksen and Beale, 1,260 days = the church age:** correct.

---

## Sound and should be kept

- 10: the OT background of the angel (1:7, 1:16, 4:3, Exod 13:21); sea and land answering the beasts of ch. 13; Dan 12:6-7 behind the oath; *chronos* = "delay" with 2:21 and 6:11; the explicit "this is not a date" and the Eastern Lightning pointer; *euangelizō* in 10:7; Ezek 2-3 and Jer 15:16 for eating the scroll; the reversed sweet/bitter order; 10:11 "kings" replacing "tribes"; "John's commission was unique; the book he wrote is the word of God".
- 10 meditation: honest scenario, legitimate bitterness separated from sin, 1 John 1:7 before any step, rest without dismissal ("the One who sends her is also the One who feeds her").
- 11: Zech 4 background and the change from one lampstand to two; fire from the mouth as the word (Jer 5:14) with Luke 9:54-55 against violence; Ezek 37 behind 11:11; 1,260 days against 3½ days; the Psalm 2 background of 11:15 and the aorist hedged as proleptic; 11:18 as a table of contents for the rest of the book.
- 11 meditation: the witnesses lying "where their Lord was crucified" linked to Mark 15:31; confession without hiding; no retaliation; prayer for the mockers; ending on 11:15 in a short prayer.
- Language parity is close throughout. The only zh/en difference in a quotation is 10:8 「小书卷」 vs "the scroll", which F7 explains.

**Verdict line:** 10.md ready; 11.md ready after must-fix items (F1, with the F2/F3 labels and F10 cuts applied).
