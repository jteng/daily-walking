I reviewed /home/user/daily-walking/plans/books/revelation/01.md (Revelation 1), both ::zh and ::en. The doctrine is sound throughout. The most serious problem is in the meditation: its closing paragraph largely repeats the Hebrews 2 meditation. The body needs a handful of exegetical and consistency fixes, and the file is about 53 KB against a 25–35 KB target.

**Checks run**
- **CUV:** `python3 scripts/check_cuv_quotes.py` reports no NOT FOUND, so every 「」 quotation matches.
- **ESV and references:** I looked up all 70-plus cross-references with `scripts/bible_lookup.py` and every one points where it claims. A script matching every English "..." against the ESV found only three non-matches, all glosses: "belonging to the Lord," "I became dead," and "what is to take place after this" (see C11).

**Items you asked me to confirm**
- **Representatives:** 毕尔 Beale and 包衡 Bauckham for the Holy Spirit reading of 1:4 is correct. 大卫·奥尼 (David Aune, WBC) for seven angels is right as far as I know (seven principal angels). 马太·亨利 for ministers at 1:20 matches his commentary as I remember it. Bauckham on penitent mourning at 1:7 (*Climax of Prophecy*, "conversion of the nations") and on 「在灵里」 marking the structure (1:10; 4:2; 17:3; 21:10) are his published views.
- **1:5:** the present tense (*agapōnti*) and *lusanti* vs *lousanti* (one letter more, "washed") are described correctly.
- **Patmos:** Eusebius *HE* 3.18.1 is right.
- **Didache 14:** right.
- **Ignatius *Magnesians* 9.1:** see C4.
- **Eastern Lightning:** the "Christ returned as a Chinese woman" description is accurate and matches 00 and 05.

---

## MUST-FIX

**M1. The meditation's death paragraph repeats Hebrews 02.**
- **Location:** 默想 / Meditation, last paragraph: 「我们中国人忌讳「死」字。有的楼不设四楼，有的老人家不肯立遗嘱……可是我心底最深的怕，正是死，和死后的审判（来9:27）」 / "We Chinese avoid the word 'death.' Some buildings have no fourth floor…"
- **Problem:** The Hebrews 02 meditation (plans/books/hebrews/02.md, line 96) already uses:
  - the death taboo, the missing 4th floor and avoiding a will;
  - "death and the judgment after it" (9:27);
  - Heb 2:14–15;
  - "拿着死亡和阴间的钥匙（启1:18）" itself.

  WORKFLOW says not to repeat themes.
- **Fix:** Keep the keys ending the brief requires, but drop the taboo frame and Heb 9:27. Go straight from the hidden sin to the keys, staying inside Revelation 1. For example:
  - zh: 「我心底最怕的，是那件事会有最后的话：有一天站在审判台前，它会把我关在门外。可是主在这里说的最后一句话，正是对着这个怕说的：他『拿着死亡和阴间的钥匙』。看透我的那双眼睛，和拿着钥匙的那只手，属于同一位为我死过、现在又活了的主……」
  - en: "My deepest fear is that this thing will have the last word: that on the day of judgment it will shut me out. But the last thing the Lord says here speaks to exactly that fear: he has 'the keys of Death and Hades.' The eyes that see through me and the hand that holds the keys belong to the same Lord who died for me and is alive…"

  Keep the final 「钥匙在他那里。」 / "The keys are with him." Heb 2:14–15 in the 1:17–20 body (point 4) can stay, but the meditation should not lean on it.

## SHOULD-FIX

**S1. The scenario examples and the confession step are used stock.**
- **Location:** 默想 / Meditation, paragraph 1 (报销单 / expense claims; 瞒着配偶的来往 / hidden relationship) and paragraph 3 (confess, then make amends).
- **Problem:**
  - Expense claims already appear in Romans 13 and 2 Timothy 3.
  - "Kickbacks, a wrong relationship" is 2 Peter 02's scenario.
  - "Hidden heart sins and confession" is listed as used (Romans).
  - "Restitution as the freedom of the forgiven" is used in Hebrews 9.
- **Fix:** Pick sins tied to the flaming eyes of the Thyatira title (2:18, 23: "searches mind and heart"). Inner sins nobody can audit fit well: long-held contempt for a co-worker in the church; envy at a friend's blessing; a performed spirituality before the congregation. Keep the restitution line to half a sentence.

**S2. The ongoing hidden affair is met with forgiveness but never told to end.**
- **Location:** 默想 / Meditation, paragraph 3: 「他所看见的每一样，他都已经在十字架上担当了……我可以把那件事照实说出来……能弥补的就去弥补」 / "Everything he sees, he has already borne on the cross…"
- **Problem:** The scenario names a relationship that is 「到今天还没有断干净」 / "still have not fully ended." The response is forgiveness, confession and amends, with no word to break it off. That reads as cheap grace. It is a doctrinal point about repentance, not only a pastoral one.
- **Fix:** If the example stays (S1 suggests replacing it), add: zh 「……求他赦免；若是一段还没有断的关系，就在他的赦免里把它断掉」; en "…and ask his forgiveness; if it is a relationship still going on, end it, standing in his forgiveness." Also make the universal statement clearly for believers: 「凡投靠他的人，他所看见的每一样……」 / "For all who trust him, everything he sees…"

**S3. "He is the Ancient of Days" blurs the Father/Son distinction in Daniel 7.**
- **Location:** 深读 1:12-16 point 6: 「他是亘古常在的神，是大祭司……」 / Going Deeper 1:12–16 point 6: "he is the Ancient of Days, the high priest…"
- **Problem:** In Dan 7:13 the son of man comes *to* the Ancient of Days. Rev 1:14 gives the Son the Ancient of Days' attributes, which shows he shares the divine identity. It does not make him the same person. The English especially invites a modalist reading. WORKFLOW says to guard the Trinity.
- **Fix:**
  - zh: 「他有亘古常在者的荣耀，与父同为神；他是大祭司……」
  - en: "he shares the glory of the Ancient of Days and is God with the Father; he is the high priest…"
- **Optional companion change (point 2, hair):** strengthen the hedge to 「约翰把但以理书描写亘古常在者的话用在人子身上：人子与父有分别，却同享神的荣耀」 / "Daniel distinguishes the Son of Man from the Ancient of Days; John gives the Son the Ancient of Days' own features. The Son is distinct from the Father yet shares his divine glory."

**S4. The worship argument at 1:17 is overread.**
- **Location:** 深读 1:17-20 point 1: 「在人子脚前，主却没有拦阻他。羔羊也和坐宝座的一同受敬拜（5:13）」 / "At the feet of the Son of Man, the Lord does not stop him."
- **Problem:** In 1:17 John falls "as though dead," overcome with fear. The text does not use *proskyneō* (worship), as 19:10 and 22:8 do. Making the contrast the main proof overreads it. The firm evidence is 5:8, 5:14 and 5:13.
- **Fix:**
  - zh: 「第1章的仆倒是惊惧，经文没有说是『拜』；但值得留意的是，约翰后来两次在天使脚前俯伏要拜，天使都说『千万不可！……你要敬拜神』（19:10；22:8-9），而四活物和长老却『俯伏在羔羊面前』（5:8），万物将颂赞归给坐宝座的和羔羊（5:13-14）。」
  - en: "John's falling in 1:17 is terror, and the text does not call it worship; but notice that when he later falls to worship an angel he is told, 'You must not do that!… Worship God' (19:10; 22:8–9), while the living creatures and elders 'fell down before the Lamb' (5:8) and every creature praises 'him who sits on the throne and… the Lamb' (5:13–14)."

**S5. Dan 8:17 is the wrong example, and the closest parallel is underused.**
- **Location:** 深读 1:17-20 point 1: 「但以理『惊慌俯伏在地』（但8:17）」 / "Daniel 'was frightened and fell on my face' (Dan 8:17)"; also point 2.
- **Problem:** In Dan 8:17 Daniel falls before Gabriel. That is an angel, not "God's glory," as the sentence claims. The direct parallel to Rev 1:17 is Dan 10:9–12:
  - he falls face down;
  - a hand touches him;
  - he hears 「不要惧怕」 / "Fear not" (10:12).
- **Fix:**
  - Replace with 但10:9 「一听见就面伏在地沉睡了」 / Dan 10:9 "I fell on my face in deep sleep with my face to the ground."
  - In point 2, add 但10:12 「但以理啊，不要惧怕！」 / "Fear not, Daniel."
  - In point 2, call the figure 「那位天上的使者」 / "the heavenly figure" rather than 「天使」 / "the angel." Point 3 of 1:12–16 applies Dan 10:5–6 to Christ, and some read Dan 10 as a theophany.

**S6. No Old Testament source is given for three images in 1:12–16.**
- **Location:** 深读 1:12-16 point 4 (feet) and point 5 (stars, face).
- **Problem:** The feet 「光明的铜」 come from Dan 10:6 (「手和脚如光明的铜」) and Ezek 1:7. The face "like the sun shining in full strength" echoes Judg 5:31 as well as Matt 17:2. The seven stars have no source and no note. The voice also has Ezek 1:24 and Dan 10:6 behind it, besides Ezek 43:2.
- **Fix:**
  - **Feet:** add 「参但10:6；结1:7」 / "(cf. Dan 10:6; Ezek 1:7)".
  - **Face:** add 「参士5:31『如日头出现，光辉烈烈』」 / "cf. Judg 5:31 'like the sun as he rises in his might'".
  - **Robe (optional):** *podērēs* is the Septuagint word for the high priest's robe (Exod 28:4) and for the man in linen (Ezek 9:2). Some commentators make this point, and it strengthens the priestly reading.
- **Remove:** in point 5, "by it he protects his people" / 「也用这话保护他的百姓」. In Revelation the mouth-sword is consistently judgment (2:12, 16; 19:15, 21).

**S7. The preterist reading of 1:7 is missing.**
- **Location:** 深读 1:4-8 point 5, bullet 「众目要看见」: 「基督再来是公开的、看得见的，是他自己亲身再来」 / "Christ's return will be public and visible…"
- **Problem:** The study's position is fine. But partial preterists (e.g. Kenneth Gentry) read 1:7 as Christ's judgment-coming on Jerusalem in AD 70: "those who pierced him," "the tribes of the land." The draft names preterism at 1:3 and then drops it here. Add one symmetric line.
  - zh: 「部分过去派（如肯尼思·詹特里）认为，这一节主要指主后70年基督藉罗马军队审判耶路撒冷；本研读和多数释经者一样，认为它指向基督将来亲身、可见的再来（参徒1:11），许多过去派也承认这样的再来。」
  - en: "Some partial preterists (e.g. Kenneth Gentry) read the verse mainly of Christ's judgment-coming on Jerusalem in AD 70; this study, with most interpreters, takes it of his future, personal, visible return (cf. Acts 1:11), which many preterists also affirm."
- **Also consider:** Matt 24:30 already joins Dan 7:13 and Zech 12:10; a 「参太24:30」 would help. For the Eastern Lightning sentence, add a brief pointer to 00's pastor/police line: 「（参看导读）」 / "(see the introduction)."

**S8. Use 不定过去时, not 过去式.**
- **Location:** 深读 1:4-8 point 4: 「（英文钦定本所依据的后期抄本作过去式。）」
- **Problem:** WORKFLOW (After 1 John): "Write the aorist as 不定过去时 in ::zh, not 过去式."
- **Fix:**
  - zh: 「作不定过去时（爱了我们）」
  - en: "have an aorist ('loved us')"
- **Parity:** the en bullet on "freed" says "the CUV and the ESV follow"; the zh mentions only CUV. Add 英文标准版 or drop ESV.

**S9. Names and titles differ from 00 and 02.**
- **Location:** 深读 1:17-20 point 5: 「约翰·瓦尔伍德」; 深读 1:9-11 point 4 and 1:17-20 point 5: 「司可福串注圣经」 (no title marks).
- **Problem:** 00 writes 约翰·华尔伏 and 《司可福串珠圣经》; 02 writes 《司可福串注圣经》（1909年）. The three files should agree.
- **Fix:** Choose one form and use it in all three files. I'd suggest 约翰·华尔伏 and 《司可福串注圣经》 with title marks.

**S10. The church-ages bullet needs fixing and largely duplicates 02.**
- **Location:** 深读 1:9-11 point 4, third bullet: 「多数释经者（包括许多采取其他读法的人）」 / "Most interpreters (including many who hold other approaches)".
- **Problems:**
  - The parenthesis is unclear.
  - The church-ages reading is older than Scofield. Some historicists (e.g. Brightman, Vitringa) held it; 02 notes this.
  - For Chinese readers the best-known form is 倪柝声《教会的正统》 (Philadelphia = the Brethren and local-church recovery). It is mentioned nowhere in 00–05.
  - 00 and 02 already treat the question fully.
- **Fix:** Cut 01 to two sentences and leave the discussion to 02. Name Nee there, or here in one clause.
  - zh: 「有人把七个教会看作教会历史的七个时期（如《司可福串注圣经》；华人教会中又以倪柝声《教会的正统》影响最大）；本书和许多释经者一样，认为它们是当时真实的教会，同时向各时代说话（详见第2章）。」
  - en: "Some read the seven as seven periods of church history (e.g. the Scofield Reference Bible; among Chinese churches, most influentially Watchman Nee's *The Orthodoxy of the Church*); this study, with many interpreters, takes them as real churches of John's day that speak to every age (see chapter 2)."

**S11. The second Lord's-day reading has no named holder.**
- **Location:** 深读 1:9-11 point 3: 「少数释经者认为……主的日子」 / "a minority take it to mean…"
- **Problem:** WORKFLOW wants each option labelled symmetrically with names.
- **Fix:** Add a representative, e.g. 「如十九世纪的布林格（E. W. Bullinger）」 / "(e.g. E. W. Bullinger)". If the drafter cannot confirm this, write 「一些时代论的释经者」 / "some dispensational interpreters." A one-line cross-reference would also help the majority view: 1 Cor 11:20 uses the same adjective (*kyriakon deipnon*, 「主的晚餐」).

## CONSIDER

- **C1. Attribution to Bauckham** (深读 1:12-16 point 6: 「许多人（如包衡）指出，这些描写不是要我们画出一幅图来」). I cannot confirm this is Bauckham's published point; it is common in commentaries (Beale says much the same). Use 「有些释经者」 / "some commentators" unless the drafter has a page.
- **C2. Ignatius *Magnesians* 9.1.** Ignatius says "living according to the Lord's [day], on which our life rose." He does not mention gathering, and some manuscripts read "Lord's life." Didache 14.1 is the text about gathering to break bread. Reword:
  - zh: 「《十二使徒遗训》第十四章说信徒在主日聚会擘饼；伊格那丢《致马内夏人书》9.1说信徒不再守安息日，而是『照着主日生活』，因为我们的生命在那日藉着他复活」
  - en: "the *Didache* (14.1) speaks of gathering on the Lord's day to break bread; Ignatius (*Magnesians* 9.1) speaks of living 'according to the Lord's day,' on which our life rose through him."
  - (Quote marks here are for Ignatius, not CUV; per WORKFLOW drop 「」 or use plain text in zh.)
- **C3. Ps 89:37 is about the moon.** In 深读 1:4-8 point 3, 「又说『如天上确实的见证』」 / "speaks of 'a faithful witness in the skies'": the witness is the moon, attesting the covenant, not David's heir. Add 「（指月亮为约作见证）」 / "(the moon as witness to the covenant)" so the echo is not overstated.
- **C4. State the Christological conclusion at 1:17.** In 深读 1:17-20 point 3, after Isa 44:6; 48:12 (add 41:4), say it outright: 「耶稣把耶和华独有的称号用在自己身上」 / "Jesus takes to himself the title the LORD reserves for himself alone." Optionally, at 1:4: the grammatically odd nominative *ho ōn* after "from" echoes Exod 3:14 LXX. Many think this is deliberate; hedge it.
- **C5. Lampstand and stars details.** Zechariah saw one lampstand with seven lamps; John sees seven lampstands. Many commentators note the shift from Israel to the churches. One clause would help. Also in 1:20, 「七灯台在他的面前」 / "the seven lampstands are before him" fits the text better as 「他在灯台中间行走」 / "he walks among the lampstands" (1:13; 2:1).
- **C6. The 1:20 "personification" view has no representative.** Name one (e.g. 「如一些释经者，包括凯尔德 Caird」, if confirmed) or leave it unnamed but parallel in form.
- **C7. The meditation's analogy from 19:10 and 22:8.** Paragraph 4 uses John's falling before angels as a picture of the believer's repeated moral falls, and says 「主并没有因此不再向他说话」. This rests on the 仆倒/跌倒 wordplay. 19:10 is a rebuked act of misplaced worship, and the "Lord kept speaking" point is an inference. A text-grounded alternative is Smyrna: the one "who died and came to life" (2:8) says "Do not fear" to people who will fail and suffer (2:10). Or drop the paragraph's illustration and keep only the word to the one who falls repeatedly, resting on 1:5 ("loves" in the present tense).
- **C8. The "Fear not" pivot is close to 2 Peter 01's ending** (Matt 17:7–8, "Rise, and have no fear"), and the body also cites Matt 17:2. The brief assigns the 1:17 pivot, so keep it. Just don't add a touch or hand image, and keep 「不要惧怕」 as the pivot, not the ending (as now).
- **C9. Two minor 1:19 points.** Some take *ha eisin* as "what they mean" (cf. the same verb in 1:20). Mention it only if space allows. Change the English gloss "what is to take place after this" to the ESV wording "those that are to take place after this."
- **C10. Parity.** The en meditation explains 「四」 sounding like 「死」 and the zh does not. That is natural for each audience; it becomes moot if M1 removes the passage.

## Where to cut (about 53 KB to 30–35 KB)

1. **本章脉络 / Shape, paragraph 2:** shorten the pointer to the introduction to one sentence.
2. **1:1-3 point 3** (the meaning of 「快」): keep the Daniel 2 echo and Beale's inaugurated reading in two sentences, then point to 00.
3. **1:4-8:**
   - Cut the Isa 11 Septuagint "seven" line from the seven-spirits bullet.
   - Trim the 11:17 aside to one clause.
   - Reduce the Eastern Lightning bullet to one sentence plus 「参看导读」.
4. **1:9-11:**
   - Shorten the Patmos persecution-scope sentence to one clause (00 covers it).
   - Cut the 「在灵里」 four-times bullet to one clause (04 treats it).
   - Collapse the three seven-churches bullets to the two-sentence version in S10 (02 treats it fully).
5. **1:12-16 point 6:** reduce to two sentences.
6. **1:17-20 point 5 (1:19):** 00 already sets out both readings; reduce to three lines.
7. **Meditation:** M1 already shortens it. Paragraph 4 (C7) can go.

## Sound, keep

- 1:1: "the revelation of Jesus Christ" as unveiling a person; the *sēmainō* and John 12:33 point; the Daniel 2 echo with "soon" replacing "latter days."
- 1:3: singular reader and plural hearers; all seven beatitude references are correct.
- 1:5–6: the substitutionary gospel is stated plainly (「替我们担当了罪的刑罚」); the textual notes on "loves" and "freed" are accurate; Exod 19:6 and 5:10.
- 1:8 with 22:13: God's title shared by Jesus; 1:17's use of Isa 44:6 and 48:12; 「我成了死的」 (*egenomēn nekros*).
- 1:9: one article governing tribulation, kingdom and endurance, properly hedged.
- 1:10–12: Ezek 3:12 and Exod 19:16 as background.
- The Old Testament background is weighted correctly, and there is no Greco-Roman or Chinese-religion overreach.
- 1:18: Hades as distinct from the lake of fire; Isa 22:22 and 3:7 for keys; Matt 16:18; the Smyrna link (2:8, 10).
- Debated points (seven spirits, wail, Lord's day, 1:19, 1:20) are mostly presented as labelled options with names.
- The meditation follows the brief: fear before the flaming eyes, "Fear not" grounded in who Christ is and his blood (1:5), a word for the one who keeps falling, and an ending on the keys rather than the hand.
- Chinese and English bodies otherwise match closely.

**Verdict:** ready after must-fix items (M1). The should-fix items S1–S11 also need applying before this goes to the application and Chinese reviewers.
