# Theology review: Revelation 06 and 07 (drafts)

Reviewer: theology-reviewer (Carson/Packer-style lens; a model, not the scholars themselves). Date: 2026-11-26.
Files: plans/books/revelation/06.md, plans/books/revelation/07.md. Checked against 00-05, the brief and WORKFLOW.

## Verdicts
- **06.md: ready after must-fix items** (1 must-fix, 3 should-fix, 5 consider)
- **07.md: ready after must-fix items** (1 must-fix, 4 should-fix, 5 consider)

## Mechanical checks
- `check_cuv_quotes.py`: 06 flags only 「罗马的和平」 (a gloss: remove the 「」 or write 罗马和平（*Pax Romana*）), 「第几印已经揭开了」 (slogan, keep), and meditation speech (keep). 07 flags only meditation speech. No real CUV misquotes.
- ESV: every English quotation of 3+ words was matched against EnglishESVBible.xml; only non-biblical speech and the gloss "come out of the great tribulation" (07 meditation, a paraphrase in quote marks, see 07-C5) fail to match.
- All verse references checked with bible_lookup.py point where they claim, except Zech 4:5 (07-S2).
- Attributions verified:
  - Irenaeus *AH* 4.21.3 does apply Rev 6:2 ("he went forth conquering, that he should conquer") to Christ. The hedge "seems" is fine.
  - Victorinus (white horse = the preaching of the gospel / word sent with the Spirit) and Hendriksen (*More Than Conquerors*: the conquering Christ) are correct.
  - Walvoord (the rider is the future world ruler, the Antichrist, who comes with a seemingly peaceful conquest) and Beale (satanic forces parodying Christ; NIGTC) are correct.
  - Irenaeus *AH* 5.30.2 (Dan omitted because the Antichrist comes from Dan, citing Jer 8:16) is correct.
  - Bauckham's 144,000 as the messianic army (census, Num 1:3) is correct (*Climax of Prophecy*, "The Apocalypse as a Christian War Scroll").
  - Structure: Victorinus, Hendriksen and Beale for recapitulation and Walvoord for telescoping are sound. Ladd and Osborne as "between the two" is fair only with "broadly"/"大致" (kept). Ladd also leans toward the seventh seal containing the trumpets, and Osborne toward progressive recapitulation.

---

## 06.md

### MUST-FIX

**06-M1. The sixth seal is called "God's final judgment" on both views. This contradicts the file's own sequential reading.**
- Location: 深读 6:12-17 §1 / Going Deeper 6:12–17 §1.
- Text: 「这两种看法都同意：这里描写的是「忿怒的大日」（6:17），就是神最后的审判。」 / "Both views agree that this is 'the great day of their wrath' (6:17), God's final judgment."
- Problem: the sequential/telescoping reading set out in 本章脉络 (Walvoord) makes the seals the first part of the tribulation. On that reading the sixth seal cannot be the final judgment: it is the onset of the wrath, and the trumpets and bowls follow. A disputed point is stated as agreed.
- Fix (zh): 「两种看法都同意，地上的人在这里认出「忿怒的大日」已经临到（6:17）。重述的读法认为这就是最后的审判；先后发生的读法（例如约翰·华尔伏）则认为这是神忿怒的开始，七号、七碗还要接着倾倒。主耶稣也用同样的话说到他的再来（太24:29-30）。」
- Fix (en): "Both views agree that people on earth here recognize that 'the great day of their wrath has come' (6:17). Recapitulation readers take this as the last judgment itself; sequential readers (e.g. John Walvoord) take it as the onset of God's wrath, which the trumpets and bowls go on to pour out. Jesus used the same words of his own coming (Matt 24:29–30)."

### SHOULD-FIX

**06-S1. The "oil and wine" explanation is stated as fact.**
- Location: 深读 6:3-8 §2 / Going Deeper 6:3–8 §2.
- Text: 「橄榄树和葡萄树根深，不像麦子那样容易受旱灾影响。这是一场有限度的饥荒」 / "olive trees and vines have deep roots… This is a limited famine".
- Problem: this is one explanation among several. Others: the irony that luxuries stay while staples fail (the rich untouched, the poor starving); or an allusion to Domitian's vine edict of AD 92 (Suetonius, *Domitian* 7.2), which some commentators link to it and others doubt. The "limited famine" conclusion holds on any reading.
- Fix (zh): 「「油和酒不可糟蹋」有几种解释：橄榄树和葡萄树根深，不像麦子那样容易受旱灾影响；也有人认为这是讽刺，穷人买不起面包，富人的油和酒却照样有。无论哪一种，这都是一场有限度的饥荒，神为它定了界限。」
- Fix (en): "'Do not harm the oil and wine' is explained in several ways: olive trees and vines have deep roots and suffer from drought less quickly than grain; or, some suggest, it is an irony, with bread beyond the poor while the oil and wine of the better-off remain. Either way, this is a limited famine, with bounds set by God."

**06-S2. The meditation should say plainly whose wrath the Lamb bore.**
- Location: 默想 ¶3 / Meditation ¶3.
- Text: 「人要躲避的「羔羊的忿怒」，他自己已经在十字架上替信靠他的人承担了」 / "The 'wrath of the Lamb' that people flee, he himself bore on the cross for all who trust him".
- Problem: 6:17 says "their wrath", that of the One on the throne and of the Lamb. Saying only that the Lamb bore "the wrath of the Lamb" can read as Christ absorbing his own anger, apart from the Father's just wrath against sin. Packer-style precision on penal substitution wants the divine wrath named. 2 Cor 5:21 speaks of sin-bearing, not wrath, so the link needs one clause.
- Fix (zh): 「人要躲避的，是坐宝座者和羔羊的忿怒（6:16-17）；这位羔羊却已经在十字架上，替信靠他的人担当了神向罪所发的忿怒：「神使那无罪的，替我们成为罪，好叫我们在他里面成为神的义。」（林后5:21）」
- Fix (en): "What people flee is the wrath of the One on the throne and of the Lamb (6:16–17); yet this Lamb has already borne, on the cross, God's wrath against sin for all who trust him: 'For our sake he made him to be sin who knew no sin, so that in him we might become the righteousness of God' (2 Cor 5:21)."

**06-S3. The meditation calls Golgotha a "hill / 山".**
- Location: 默想 last ¶ / Meditation last ¶.
- Text: 「已经在城外的山上为我们倒下了」 / "on a hill outside the city".
- Problem: Scripture places the cross "outside the gate" (Heb 13:12; John 19:20) but never calls it a hill. The mountain/hill contrast with 6:16 rests on tradition, not on the text, and the meditation's contrast depends on it.
- Fix (zh): 「已经在城门外为我们倒下了（来13:12）」
- Fix (en): "outside the city gate (Heb 13:12)"
- Alternatively keep the image and drop 山 / "hill": 「在城外的十字架上」 / "on a cross outside the city".

### CONSIDER

**06-C1. Name a representative for the gospel view of the white rider among modern futurists.** Ladd (1972 commentary) took the first rider as the proclamation of the gospel. Adding him shows the gospel view is not only amillennial, which keeps the labels symmetric. zh: 「……威廉·亨德里克森也认为这是得胜的基督；历史前千禧年派的乔治·赖德则认为这是福音的传扬。」 en: "…and William Hendriksen as the conquering Christ; the historic premillennialist George Eldon Ladd also took it as the proclamation of the gospel."

**06-C2. 6:11 textual note.** "Should be complete" (*plērōthōsin*) has a variant, *plērōsōsin* ("complete [their course]"). It is optional and probably cut for length; mention it only if space allows.

**06-C3. 「罗马的和平」.** Remove the 「」 (it is a gloss, not CUV): 罗马和平（*Pax Romana*）.

**06-C4. The 6:9 bullet on the intermediate state.** The point is sound, but say what the text supports: *anapauō* "rest" (6:11; cf. 14:13) and souls conscious enough to cry out. It already says "许多释经者"; no change is required.

**06-C5. The meditation could close on Ps 32:7** ("You are a hiding place for me" / 「你是我藏身之处」). That would give "be my only hiding place" a scriptural anchor. Check the CUV first.

### Length cuts for 06 (36.9 KB, target ≤35 KB; about 2.5 KB to remove)
1. 深读 6:3-8 §4: merge the two bullets into one sentence and leave date-setting to 00. zh: 「这几匹马所代表的事在每一个世代都可能出现；不要把新闻当作时间表（见导读），也不要以为与自己无关。」 This saves about 0.7 KB across both languages.
2. 深读 6:1-2 §2, the Parthian view: cut to one sentence, e.g. 「也有学者认为，最初的读者会想起罗马东边以骑射闻名的帕提亚人。」 Saves about 0.4 KB.
3. 深读 6:3-8 §1: drop the *Pax Romana* sentence. The *sphazō* link to 5:6 and 6:9 is the stronger point. Saves about 0.5 KB.
4. 深读 6:9-11 §2: drop the 8:3-5 forward pointer, since chapter 8 will make it. Saves about 0.4 KB.
5. 深读 6:12-17 §1: shorten the two imagery bullets to one line each after 06-M1 is applied. Saves about 0.5 KB.
Do not cut the safeguarding lines in the meditation (gambling help, police, the wife not signing for debts).

---

## 07.md

### MUST-FIX

**07-M1. The 7:4-8 要点 says "not one tribe is left out", but the list omits Dan, as §1 has just said.**
- Location: 深读 7:4-8, 要点 / The point.
- Text: 「神没有忘记他对以色列的应许，一个支派、一个人都没有漏掉。」 / "God has not forgotten his promise to Israel; not one tribe, not one person, is left out."
- Problem: this is a factual contradiction inside the section. Dan is missing and Ephraim is absent by name. The line also states the "same people" identification as settled after two views were just set out.
- Fix (zh): 「> 要点：受印的人一个支派一个支派、一个一个都被数算过，神没有忘记属他的任何一个人。许多释经者认为，他对以色列的应许在羔羊里成就，结果是一群数不过来的人。」
- Fix (en): "> The point: The sealed are counted tribe by tribe, one by one; God forgets none who are his. Many interpreters see here his promise to Israel fulfilled in the Lamb, in a people no one can number."

### SHOULD-FIX

**07-S1. Zechariah 6:5 is claimed in English to call the chariots "the four winds of heaven". The ESV does not say this.**
- Location: Going Deeper 7:1–3 §1 (en only; zh is fine because the CUV reads 「这是天的四风」).
- Text: "the four chariots in Zechariah are also 'the four winds of heaven' (Zech 6:5)".
- Problem: the ESV reads "These are going out to the four winds of heaven". The words in quotation marks are ESV words, but the claim reverses the ESV's sense. The Hebrew *ruchot* can be read either way, which is why CUV and ESV differ. As written, this is a parity mismatch and misstates the ESV.
- Fix (en): "in Zechariah the four chariots are 'going out to the four winds of heaven' (Zech 6:5; the Hebrew can also be read 'these are the four winds/spirits')". The zh can stay, or add 「（原文也可译作「往天的四方去」）」 for parity.

**07-S2. Zech 4:5 is not a parallel to "Sir, you know".**
- Location: 深读 7:13-17 §1 / Going Deeper 7:13–17 §1.
- Text: 「撒迦利亚也曾这样回答天使（亚4:5）。」 / "Zechariah answered an angel the same way (Zech 4:5)."
- Problem: Zech 4:5 is 「主啊，我不知道」 / "No, my lord." The verbal parallel is Ezek 37:3, 「主耶和华啊，你是知道的」 / "O Lord GOD, you know." Many commentators cite it.
- Fix (zh): 「以西结被问「这些骸骨能复活吗」的时候，也这样回答：「主耶和华啊，你是知道的。」（结37:3；参亚4:5）」
- Fix (en): "Ezekiel answered the same way when asked whether the dry bones could live: 'O Lord GOD, you know' (Ezek 37:3; cf. Zech 4:5)."

**07-S3. "The New Testament often calls believers… the true Israel" overstates, and cites two disputed texts as plain.**
- Location: 深读 7:4-8 §2, second bullet / Going Deeper 7:4–8 §2.
- Text: 「新约也常把信基督的人……称为真以色列或亚伯拉罕的后裔（罗2:28-29；加3:29；6:16；腓3:3；雅1:1）」 / "The New Testament often calls those who believe in Christ, Jew and Gentile, the true Israel or Abraham's offspring (…)".
- Problem: Gal 6:16 ("the Israel of God") is debated: the church as a whole, or Jewish believers. Jas 1:1 is debated too, and James 00 sets out both views. Phil 3:3 says "we are the circumcision", not "Israel". The point stands, but it needs hedging and accurate wording.
- Fix (zh): 「新约有时把信基督的人，无论是犹太人还是外邦人，称为亚伯拉罕的后裔、真受割礼的人（罗2:28-29；加3:29；腓3:3）；许多释经者也这样理解加拉太书6:16的「神的以色列民」和雅各书1:1的「十二个支派」，不过这两处都有争议。」
- Fix (en): "The New Testament at times calls those who believe in Christ, Jew and Gentile, Abraham's offspring and 'the circumcision' (Rom 2:28–29; Gal 3:29; Phil 3:3); many read 'the Israel of God' (Gal 6:16) and 'the twelve tribes' (Jas 1:1) the same way, though both are debated."
- Build note: the zh puts 6:16 bare after 加3:29, which is fine for the build, but naming the book in the new wording avoids any ambiguity.

**07-S4. The 7:4-8 interpretation omits the preterist option and the non-dispensational ethnic-remnant option.**
- Location: 深读 7:4-8 §2 / Going Deeper 7:4–8 §2.
- Problem: this is the book's main 144,000 section, and the brief asks for options with names. As written, it is "dispensational vs everyone else". Some preterists (e.g. Kenneth Gentry, David Chilton) take the 144,000 as Jewish Christians preserved through AD 70. Some non-dispensational interpreters take them as a believing remnant of ethnic Israel within the church, without a pre-tribulation rapture.
- Add one bullet. zh: 「**犹太信徒中的余民：** 也有释经者认为，这是教会中信主的犹太人。过去派（例如肯尼斯·詹特里）认为，这是公元70年耶路撒冷被毁时蒙保守的犹太基督徒；另一些人则认为，这是末世以色列中归主的余民，但不必先有灾前被提。」 en: "**A remnant of Jewish believers:** some take them as Jewish believers within the church. Preterists (e.g. Kenneth Gentry) see the Jewish Christians preserved through the fall of Jerusalem in AD 70; others see an end-time believing remnant of Israel, without requiring a pre-tribulation rapture." Change 「两种」/"two main views" to 「几种」/"several views".

### CONSIDER

**07-C1. "As the introduction noted, John often hears one thing, then turns and sees another."** 00 makes this point only for 5:5-6; 05 §4 develops it. Write 「第5章说过」 / "As chapter 5 noted (5:5–6)", and soften "often", e.g. 「约翰有时先听见……」 / "John sometimes hears…". 1:10-12 (he hears a voice, turns, sees) is a second example if wanted.

**07-C2. Answering the Jehovah's Witnesses: add the strongest textual point.** JW literature reads "before the throne" and "in his temple" of the earthly courts. The word in 7:15 is *naos*, which elsewhere in Revelation is the heavenly sanctuary (11:19; 14:15, 17; 15:5-8). That makes the "multitude is in heaven" bullet harder to evade. zh: 「「殿」这个词在启示录别处指的是天上的圣所（11:19；15:5）。」 en: "the word for 'temple' (*naos*) elsewhere in Revelation is the heavenly sanctuary (11:19; 15:5)."

**07-C3. 7:14 "great tribulation": a preterist line.** Add for symmetry: 「过去派则认为这指公元66-70年的犹太战争（参太24:21）。」 / "Preterists take it as the Jewish War of AD 66–70 (cf. Matt 24:21)." Also, 1:9 has the article too (ἐν τῇ θλίψει). This supports the church-age reading and could replace "using the same word" with "the same word, also with the article".

**07-C4. Meditation, the son: 「他的罪，羔羊已经担当了」 / "the Lamb has already carried his sin".** This is stated unconditionally of a teenager whose faith is not mentioned. Add the faith clause, keeping gospel before command: 「他可以把那句话带到羔羊面前，承认它，哭出来；凡信靠他的，他的罪羔羊已经担当了。」 / "…for all who trust him, the Lamb has already carried their sin." This matches 06's "for all who trust him".

**07-C5. Meditation ¶2: 「从大患难中出来的」 / "come out of the great tribulation".** The English puts a paraphrase in quotation marks; the ESV reads "coming out of the great tribulation". Use the ESV wording or remove the quote marks. The zh is verbatim CUV.

### Length cuts for 07 (37.1 KB, target ≤35 KB; about 2.5-3 KB to remove, more if 07-S4 is added)
1. 深读 7:9-12 §4, "What it means for Chinese churches today": cut it, or fold one clause into the 要点. 05 already makes the "not a foreign religion" point at 5:9. Saves about 0.8 KB.
2. 深读 7:1-3 §3, the mark-of-the-beast bullet: reduce to one sentence ("The beast's mark (13:16) imitates this seal; chapter 13 returns to it"). Saves about 0.4 KB.
3. 深读 7:13-17 §4, "Now or later?": reduce to one sentence ("Those who have died are before the throne now; all this is fully realized in the new creation, 21:3-4"). Saves about 0.5 KB.
4. 深读 7:4-8 §1: merge the Judah and Levi/Joseph bullets into one "unusual order" bullet. Saves about 0.4 KB.
5. 深读 7:4-8 §3, JW rebuttal: merge "the multitude is in heaven too" and "one people" into one bullet (keep 07-C2's *naos* point). Saves about 0.4 KB.
6. 深读 7:1-3 §2: shorten the description of what ancient seals meant to one clause. Saves about 0.2 KB.

---

## Language parity
- 06: zh and en match point for point. The only real divergence is the Zech 1:8 and 6:5 handling: zh paraphrases 1:8 and quotes 6:5 CUV, en quotes the ESV of both. That is acceptable.
- 07: 07-S1 (Zech 6:5 sense differs between zh and en). Otherwise the bodies match, including the safeguarding and compensation lines in the meditation.

## Sound and to be kept
- 06 sets out the seals/trumpets/bowls question once, symmetrically, with correct names, and points later chapters back. It is consistent with 00 §structure and 04's throne-centered framing.
- The white rider options are well balanced: arguments are given for each side, Irenaeus is properly hedged, and there is a note that evil imitates Christ.
- The divine passive (「赐给他」, 6:2, 4, 8; 13:7) and the limits on judgment (1/4, then 1/3, then the bowls) are good exegesis that rightly honors God's sovereignty.
- 6:9-11 reads the altar and Lev 4:7 with Paul's drink-offering, and presents the cry for justice as a plea for God's holiness, not private revenge.
- The chain from Gen 3:8 to 6:16 to 22:4 (the face hidden from and the face seen) and "Who can stand?" answered by 7:9 and 7:14 with Rom 5:9 are excellent salvation-historical reading.
- The 06 meditation: gospel before steps; a word to the one who relapsed; full safeguarding for the wife; it ends on the Lamb as hiding place, as the brief asks. With 06-S2 applied, the substitution is stated plainly.
- 07: the seal as belonging and protection from wrath, not from suffering, read with Ezek 9 and Eph 1:13. The hear/see reading is set beside Walvoord's strongest arguments. Future mercy for Israel (Rom 11:26) is acknowledged on the other view. The JW answer is gentle and starts from who Jesus is.
- 7:10 and 7:14 keep salvation wholly God's and the Lamb's. The robes washed white in the blood are stated plainly. The Lamb-shepherd reading is grounded in Isa 49:10, Ezek 34:23 and John 10:11. The 7:15 *skēnoō* link to John 1:14 and 21:3 is accurate.
- The 07 meditation: grief is not hurried; justice-seeking is not unspiritual; it does not pronounce on the unknown dead; it ends on 7:17 as the brief assigns.

## Summary counts
- 06: must-fix 1, should-fix 3, consider 5
- 07: must-fix 1, should-fix 4, consider 5
