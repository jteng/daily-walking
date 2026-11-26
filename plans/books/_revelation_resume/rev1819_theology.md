# Theology review: Revelation 18 and 19 (theology-reviewer)

Files: plans/books/revelation/18.md, plans/books/revelation/19.md
Checked against: 00.md, 06.md, 14.md, 16.md, 17.md (draft), 20.md (draft), the brief, and the CUV/ESV XML (scripts/bible_lookup.py, scripts/check_cuv_quotes.py, and an ESV substring script).

## Verdicts
- **18.md: ready after must-fix items** (1 must-fix, 2 should-fix, 4 consider)
- **19.md: ready after must-fix items** (2 must-fix, 3 should-fix, 5 consider)

## Quotation check
- CUV: check_cuv_quotes.py flags only 「你不干，有的是人干。」 (18.md meditation, the boss's words: not Scripture). Keep it as is, or use “ ” in place of 「」. 19.md is clean.
- ESV: every ESV quotation in both files matches the XML. The script's only "not found" hits were glosses or slogans ("matching", "souls of men", "fighting hard", "labor costs", "output per head", "Lord, I love you", "costs", "God will avenge", "has begun to reign", "divine passive", "by grace she was given to wear"). These are not presented as ESV text. Note that the ESV of 18:2 has "a haunt for every unclean and detestable beast", which the CUV lacks (a textual variant). Each language quotes its own Bible correctly; no change needed.
- Every verse reference I checked points where it claims, including Jer 51:45, 51:63-64, 25:10, 16:18; Isa 40:2, 47:7-8, 21:9, 34:10, 63:3, 11:4, 61:10, 25:6; Ezek 27:13, 43:2, 39:17-20, 1:1; Exod 3:7, 21:32; Matt 26:15, 23:35, 22:10-12, 8:11; 1 Tim 1:10; 2 Thess 2:8; Eph 2:10, 5:25-27; Phil 2:7, 2:13; John 2:1-2; Rev 17:1/21:9, 12:3, 13:1, 16:14/19:19/20:8. The count of beatitudes (19:9 is the fourth of seven: 1:3; 14:13; 16:15; 19:9; 20:6; 22:7; 22:14), "the only Hallelujahs in the NT" (19:1, 3, 4, 6), the last appearance of the elders and living creatures (19:4), the six "no more"s in 18:21-23, and the first appearance of the lake of fire (19:20) are all correct.

## Attributions the drafter asked about
- **Chilton, 19:11-16 as gospel conquest:** This matches David Chilton, *The Days of Vengeance* (1987), who reads the Rider as Christ's ongoing conquest through the Word and not as the Second Coming. The better-known representative of this postmillennial reading is B. B. Warfield, "The Millennium and the Apocalypse" (1904), who takes 19:11-21 as the gospel's victory in this age. 20.md already names 华腓德. Name both and hedge with "主要" / "chiefly" (see S-19-2).
- **Caird, the robe's blood as the martyrs':** Correct. G. B. Caird (*The Revelation of St. John the Divine*, 1966) argued that the blood on the Rider's robe is the martyrs' blood, which he made his own. Keep it. The zh form 乔治·凯尔德 is acceptable (George Bradford Caird). It is new in the book, so consider adding (G. B. Caird) after it at first mention.
- **Beale, "double" (18:6) as equivalent repayment:** Correct. In his NIGTC commentary (1999), Beale argues, following Meredith Kline ("Double Trouble," *JETS* 32, 1989), that *diplous* here means a "duplicate", that is, a matching or equivalent payment. The draft's "倾向认为 / lean toward" is fair. You may add Kline (consider C-18-2).
- **Walvoord, religious Babylon (17) vs economic Babylon (18):** Correct. In *The Revelation of Jesus Christ* (1966), Walvoord treats ch. 17 as ecclesiastical/religious Babylon and ch. 18 as political and commercial Babylon. The problem is that 17.md does not mention this, so 18's "第17章已经列出" is inaccurate (see S-18-1).
- Others checked: Bauckham's essay "The Economic Critique of Rome in Revelation 18" is in *The Climax of Prophecy* (1993). Correct. Charles Dyer, *The Rise of Babylon* (1991). Correct. Eusebius, *Church History* 3.5.3 (Pella). Correct.
- One I am less sure of: on 19:13, Grant Osborne as representative of "enemies' blood". I believe Osborne leans this way, but the case is less clear-cut than Walvoord's or Mounce's. Consider C-19-1.

---

## MUST-FIX

### M-18-1 (18.md, 默想 / Meditation): "my people" is loosened from faith in Christ, and the gospel ground is not stated plainly
- zh: 「在神的口中，他们是可以被称为「我的民」的人。」 and 「神并没有把这样的人划出「我的民」以外。」
- en: "in God's mouth, they are people who can be called 'my people.'" and "God has not ruled us out of 'my people.'"
- **Problem:** In 18:4 "my people" are those who already belong to God. The meditation applies the title to the collapsed young man and to the unrepentant manager simply because they are treated as cargo. That blurs the line between God's care for every human being (Exod 3:7 is about his covenant people) and belonging to him through faith in Christ. The closing paragraph also says Christ "let himself be entered on Babylon's cargo list, so that those treated as cargo could be called God's people", but it never says he died for sin in our place. Repentance and faith are not named. WORKFLOW requires substitution and the ground of forgiveness to be stated plainly.
- **Fix (zh):** In paragraph 3, replace 「在巴比伦的账本上，那个晕倒的年轻人是一项成本，这位主管也是一项成本；在神的口中，他们是可以被称为「我的民」的人。」 with:
  「在巴比伦的账本上，那个晕倒的年轻人是一项成本，这位主管也是一项成本；神却不是这样看人。」
  In paragraph 4, replace 「如果我们像这位主管一样，曾经把人当作数字，甚至在别人倒下的时候只想到进度，神并没有把这样的人划出「我的民」以外。他呼召我们出来，是要我们离开她的罪，不是要我们先把自己洗干净才能回来。」 with:
  「如果我们像这位主管一样，曾经把人当作数字，甚至在别人倒下的时候只想到进度，这是真实的罪，不是一句「行业就是这样」可以带过的。可是神没有说，这样的人永远不配被称为「我的民」。凡悔改、信靠基督的，罪都得赦免，就属于他。他呼召我们出来，是要我们离开她的罪，不是要我们先把自己洗干净才能回来。」
  In paragraph 5, after 「（腓2:7）」, change the clause to:
  「……「取了奴仆的形象」（腓2:7），被人用一个奴仆的价钱卖了，又被钉在十字架上，「义的代替不义的」（彼前3:18），担当了我们这些把人当货物的人的罪，好叫那些被当作货物的人，和那些把人当作货物的人，都可以因信被神称为自己的百姓。」
- **Fix (en):** Paragraph 3: "In Babylon's ledger, the young man who collapsed is a cost, and so is the manager; but God does not see people that way."
  Paragraph 4: "If, like this manager, we have treated people as figures, and even thought only of schedules when someone fell, that is real sin, not something to wave away with 'that's just the industry.' But God has not said that such a person can never be called 'my people.' Everyone who repents and trusts in Christ is forgiven and belongs to him. He calls us out of her sins; he does not require us to wash ourselves first before we may come."
  Paragraph 5: "...took 'the form of a servant' (Phil 2:7), was sold for the price of a slave, and was nailed to a cross, 'the righteous for the unrighteous' (1 Pet 3:18), bearing the sins of people like us who treat others as cargo, so that both those treated as cargo and those who treated them so could be called, through faith, God's own people."
  (1 Pet 3:18 quotes verified: CUV 「义的代替不义的」, ESV "the righteous for the unrighteous". Check the WORKFLOW used-verse lists. If 1 Pet 3:18 is taken, use Gal 3:13 or 1 Pet 2:24, but not 5:9 "ransomed", per the brief.)

### M-19-1 (19.md, 深读 19:17-21, point 4): a disputed reading of 19:13 is used as settled fact
- zh: 「那流过血的衣服，就是他愿意接纳罪人的凭据。」
- en: "and the robe dipped in blood is the pledge that he is willing to receive sinners."
- **Problem:** Point 3 of 19:11-16 rightly gives three readings of the blood on the robe (enemies', Christ's own, martyrs'), and the majority reading is the enemies' blood (Isa 63:3). Point 4 then builds the gospel appeal on the minority reading as though it were settled.
- **Fix (zh):** 「那将来要审判列国的道，今天仍在呼召人悔改；他曾在十字架上为罪人流血（1:5；5:9），这就是他愿意接纳罪人的凭据。」
- **Fix (en):** "The Word who will judge the nations still calls people to repent today; and the blood he shed on the cross for sinners (1:5; 5:9) is the pledge that he is willing to receive them."

### M-19-2 (19.md, 深读 19:17-21, point 2): overstated Ezekiel claim, and it disagrees with 20.md
- zh: 「这三处的「争战」在原文都带冠词（*ton polemon*），又都用了以西结书第38-39章歌革的画面」
- en: "...'the battle' carries the article in the Greek in all three places (*ton polemon*), and all three draw on Ezekiel's picture of Gog (Ezek 38–39)"
- **Problem:** 16:12-16 does not use Ezekiel's Gog imagery; only 19:17-21 and 20:8-9 do. 20.md correctly says 「第19章和第20章都引用以西结书第38-39章（19:17-18；20:8-9）」. The article point is accurate for all three verses.
- **Fix (zh):** 「……这三处的「争战」在原文都带冠词（*ton polemon*），而19:17-18和20:8-9又都用了以西结书第38-39章歌革的画面，所以认为它们是从不同角度描写主再来时同一场最后的争战。」
- **Fix (en):** "...point out that 'the battle' carries the article in the Greek in all three places (*ton polemon*), and that 19:17–18 and 20:8–9 both draw on Ezekiel's picture of Gog (Ezek 38–39); so they take them as different views of the same final battle at the Lord's return."

---

## SHOULD-FIX

### S-18-1 (18.md, 本章脉络 / Shape): the recap does not match 17.md
- zh: 「巴比伦指的是什么，第17章已经列出几种主要的看法：」 followed by four bullets. The last bullet ends 「约翰·华尔伏则把第17章读作宗教的巴比伦，第18章读作政治和经济的巴比伦。」
- **Problem:** 17.md names Bauckham, Beale *and Osborne* for Rome. It lists "rebuilt Babylon (Dyer) or a worldwide religious/economic system (other dispensationalists)". It does not mention Walvoord's 17/18 split at all. Presenting new material as "already set out in ch. 17" is inaccurate. Rewriting the list as a one-line pointer also saves about 1.3 KB per language (see Cuts).
- **Fix (zh):** Replace the sentence and its four bullets with:
  「巴比伦指的是什么，第17章已经列出几种主要的看法：一世纪的罗马（多数释经者）、背道的耶路撒冷（一些过去派）、教皇的罗马（许多宗教改革时期的历史派），以及将来重建的巴比伦城或末日的世界体系（一些时代论者）。这里只补充一点：有些时代论者（例如约翰·华尔伏）把两章分开，第17章读作宗教的巴比伦，第18章读作政治和经济的巴比伦。」
  Keep the following sentence 「本研读和多数释经者一样，认为第17、18章说的是同一座城……」. Supporting reasons for unity can be given in one clause: both chapters use the same "great city" (17:18; 18:10), the same dress (17:4; 18:16) and the same "one hour" (17:12; 18:10).
- **Fix (en):** "Chapter 17 has already set out the main views of what Babylon is: first-century Rome (most interpreters), apostate Jerusalem (some preterists), papal Rome (many Reformation-era historicists), and a rebuilt city of Babylon or an end-time world system (some dispensationalists). One addition here: some dispensationalists (e.g. John Walvoord) separate the two chapters, reading chapter 17 as religious Babylon and chapter 18 as political and economic Babylon." Then keep "With most interpreters, this study takes chapters 17 and 18 as the same city…".

### S-18-2 (18.md, 深读 18:4-8, point 3): a Babel allusion stated as the meaning; the closer background is left out
- zh: 「「滔天」原文的意思是罪一层层堆起来，直堆到天上，令人想起巴别塔（创11:4）。」
- en: "The picture is of sins stacked layer on layer until they reach heaven, which recalls the tower of Babel (Gen 11:4)."
- **Problem:** The verb (*ekollēthēsan*) means "clung / were joined together". The ESV's "heaped high" is a fair rendering, but "layer on layer" overreads it. The direct background is Jer 51:9, in John's main source chapter: 「她受的审判通于上天」. Babel is a possible secondary echo and should be hedged.
- **Fix (zh):** 「「滔天」是说她的罪一直连到天上，这句话来自耶利米书论巴比伦的话：「她受的审判通于上天，达到穹苍」（耶51:9）；也有人联想到巴别塔「塔顶通天」（创11:4）。」
- **Fix (en):** "Her sins have 'clung together' or piled up as high as heaven. The words come from Jeremiah's oracle against Babylon, 'her judgment has reached up to heaven and has been lifted up even to the skies' (Jer 51:9); some also hear an echo of Babel's 'tower with its top in the heavens' (Gen 11:4)."

### S-19-1 (19.md, 深读 19:6-10, point 5): guard the deity of Christ where the angel refuses worship; the 00 cross-reference is overstated in zh
- zh: 「本研读的导读（第00章）已经详细讨论过。……连最荣耀的天使也只是和约翰「同是作仆人的」，敬拜只归给神。」
- en: "the introduction to this study (chapter 00) has discussed it. … worship belongs to God alone."
- **Problem:** 19:10 is a favourite proof-text for groups that deny Christ's deity ("only God is worshipped, so not Jesus"). Revelation itself answers this: the Lamb receives the same worship as the one on the throne (5:8-14). One sentence closes the gap. In addition, 00 mentions 19:10 only in its meditation, so 「详细讨论过」 is overstated, and the en already lacks "in detail" (a parity gap).
- **Fix (zh):** 「这件事在22:8-9又发生了一次，导读（第00章）的默想已经提过。……连最荣耀的天使也只是和约翰「同是作仆人的」，敬拜只归给神。可是羔羊却和坐宝座的一同受敬拜（5:8-14）：天使不敢领受的敬拜，羔羊理当领受，因为他是神。」
- **Fix (en):** "The same thing happens again in 22:8–9, and the meditation in the introduction (chapter 00) has touched on it. … worship belongs to God alone. Yet the Lamb is worshiped together with the one seated on the throne (5:8–14): the worship the angel dares not receive is rightly given to the Lamb, because he is God."

### S-19-2 (19.md, 深读 19:11-16, point 1): name the main postmillennial representative and hedge
- zh: 「也有些过去派和后千禧年派的释经者（例如大卫·齐尔顿）认为，这段经文描写的是基督藉着福音得胜列国。」
- **Problem:** The attribution to Chilton is accurate (see above). Warfield is the classic and better-known representative, and 20.md already names him. "Some preterist and postmillennial" should also not suggest that all of them read it this way. Gentry, for example, holds a real future Second Coming.
- **Fix (zh):** 「也有些后千禧年派和过去派的释经者（例如华腓德、大卫·齐尔顿）认为，这段经文主要描写基督藉着福音在历史中得胜列国。」
- **Fix (en):** "some postmillennial and preterist interpreters (e.g. B. B. Warfield, David Chilton) read it chiefly as Christ conquering the nations through the gospel in history."

### S-19-3 (19.md, 深读 19:6-10, point 4): an interpretation stated as fact
- zh: 「新妇和被请的客人，看起来是两群人，其实是同一群人从两个角度来看」
- en: "The Bride and the invited guests look like two groups, but they are the same people seen from two angles"
- **Problem:** This is the majority reading. Some dispensationalists (e.g. Walvoord) distinguish the Bride (the church) from the guests (OT saints / tribulation saints). It should be labelled as a reading.
- **Fix (zh):** 「新妇和被请的客人，看起来是两群人；许多释经者认为，其实是同一群人从两个角度来看：……（有些时代论者，例如约翰·华尔伏，则认为新妇是教会，客人是旧约的圣徒等其他的人。）」
- **Fix (en):** "The Bride and the invited guests look like two groups; many interpreters take them as the same people seen from two angles … (some dispensationalists, such as John Walvoord, distinguish the Bride, the church, from the guests, such as Old Testament saints.)"

---

## CONSIDER

- **C-18-1 (18.md, 18:9-19 point 4):** John's 「人口」 / *psychas anthrōpōn* is the very phrase of LXX Ezek 27:13 (the verse already cited). Saying so strengthens the point: 「「人口」原文是人的魂（*psychas anthrōpōn*），正是七十士译本以西结书27:13的说法」 / "'souls of men' (*psychas anthrōpōn*), the very phrase of the Greek Old Testament at Ezek 27:13".
- **C-18-2 (18.md, 18:4-8 point 4):** Optionally: 「也有学者（例如毕尔，跟随梅雷迪思·克莱恩）……」 / "Some scholars (e.g. Beale, following Meredith Kline)…". The attribution as it stands is accurate.
- **C-18-3 (18.md, 18:20-24 point 4):** Matt 23:35 is also a main text for the Jerusalem reading of Babylon (17.md cites Matt 23:37 for it). A clause keeps it from being used one-sidedly: 「主张巴比伦是耶路撒冷的人也常引这句话；不过……」 / "Those who read Babylon as Jerusalem also cite this; but…". Alternatively, leave it out to save space.
- **C-18-4 (18.md, 18:9-19 要点 / The point):** 「已经被称了，显出亏欠」 / "weighed … and found wanting" quotes Dan 5:27 without citing it, and it is the CUV wording. Add （但5:27） / (Dan 5:27).
- **C-19-1 (19.md, 19:11-16 point 3):** For "enemies' blood", 「例如约翰·华尔伏、格兰特·奥斯本」 / "e.g. John Walvoord, Grant Osborne" is a safer pair. Walvoord certainly holds this view. Optionally add (G. B. Caird) after 乔治·凯尔德 at first mention.
- **C-19-2 (19.md, 19:1-5 point 2):** 「对那些在罗马的竞技场里、在各地的监牢里受苦的信徒来说」 / "for believers suffering in Roman arenas and prisons". This is slightly overstated for Asia c. AD 95 (00 warns against overstating Domitian's persecution). Use 「对那些被下在监里、甚至被杀害的信徒来说（2:10、13）」 / "for believers thrown into prison or even killed (2:10, 13)".
- **C-19-3 (19.md, 19:6-10 point 3, last line):** 「大淫妇的衣服是她用别人的血换来的（18:13、24）」 / "The prostitute's clothing was bought with other people's blood". This is a rhetorical overreach of 18:13, 24. Use 「大淫妇的华丽，是靠买卖人口、流圣徒的血得来的（18:13、24）；新妇的衣服却是白白赐给她的。」 / "The prostitute's splendor was built on trading in human lives and shedding the saints' blood (18:13, 24); the Bride's clothing is given to her freely."
- **C-19-4 (19.md, 19:11-16 point 2):** 「新约中只有约翰的著作这样称呼耶稣（约1:1、14）」. Add 约一1:1 / 1 John 1:1 for completeness ("the word of life").
- **C-19-5 (19.md, 默想 / Meditation):** The gospel ground is present (7:14, Eph 2:10, Phil 2:13). One plain clause would make substitution explicit: 「……是因为羔羊为她的冷淡和谎言流了血，她「曾用羔羊的血把衣裳洗白净了」（7:14）」 / "because the Lamb shed his blood for her coldness and her lies". The reading of the parable in Matt 22 is properly hedged ("many interpreters"). Keep it.

---

## Recommended cuts (target 30-35 KB; 18.md is 37.3 KB and 19.md is 39.5 KB)

**18.md (cut about 3-4 KB):**
1. Shape: replace the four Babylon bullets with the one-sentence pointer in S-18-1 (about 1.3 KB per language, 2.5 KB total). This also fixes the inconsistency.
2. 18:9-19 point 3 (cargo list): drop the five category bullets, which only repeat 18:12-13. Keep one sentence: 「约翰把客商的货物一样一样列出来（18:12-13），共有二十几种：从金银珠宝、丝绸香料，到牛羊车马，最后是「奴仆、人口」。」 Then keep the Bauckham sentence (about 0.8 KB per language).
3. 18:1-3: merge point 1 (glory) and point 3 (desolation) into a single short point, or drop point 3's last sentence (about 0.4 KB per language).
4. Meditation paragraph 4: shorten the three-example "coming out" list to two, keeping the labour-law sentence for those who are exploited (about 0.3 KB per language).

**19.md (cut about 5 KB):**
1. 19:6-10 point 2 (Bride): keep Isa 54:5 and Eph 5:25-27 and drop Hos 2:19, 2 Cor 11:2 and Matt 22:2/25:10. 2 Cor 11:2 was already used in 14.md (about 0.6 KB per language).
2. 19:6-10 point 5 (19:10): after adding S-19-1, drop the phrase about the two readings of "testimony of Jesus" (00 covers the verse). Net about 0.2 KB per language.
3. 19:1-5 point 1: shorten the Hallel / Mark 14:26 excursus to one clause (about 0.4 KB per language).
4. 19:11-16 point 2: merge the "names" bullets with point 3, and drop the 「除了他自己没有人知道」 bullet's gloss (about 0.4 KB per language).
5. 19:17-21: merge point 4 (sword) into point 3 (end of the beast), keeping the corrected M-19-1 sentence and 22:17. The sword-from-the-mouth material is already in 19:11-16 point 4 (about 0.6 KB per language).
6. Shape: shorten the "two women / two suppers" bullets to one sentence each (about 0.3 KB per language).

---

## Sound and should be kept
- 18: the 18:4 insight 「神还没有说「出来」，就先说「我的民」」, which is grounded in the text and pastorally rich. "Come out" read as moral separation without withdrawal, with Jer 29:7 as balance. 18:6 framed so that vengeance belongs to God (Rom 12:19). The lament structure from Ezek 27. The handling of *sōmata* / *psychas anthrōpōn* with the ESV's epexegetical "that is". The hedged slavery statistic. The 18:20 "not gloating" note, linked back to 6:10. Thirty pieces of silver = the price of a slave (Exod 21:32). The labour-law and safeguarding-style sentence for those who are exploited.
- 19: hedged aorist points (19:6 with 11:17). The *edothē* divine passive and *dikaiōmata* plural, with three readings fairly set out and the order of grace kept clear (blood and gift first, then deeds that are themselves God's gift; Eph 2:10). The symmetric amil/idealist vs dispensational/historic-premil treatment of 19:19-21, which points ahead to ch. 20. The sword from the mouth = the word (Isa 11:4; 2 Thess 2:8). The solemn handling of 19:21 with 22:17's invitation. The meditation's "invitation, not inspection" and its careful reading of Matt 22:10-12. The ending on "Faithful and True" (per the brief).
- Both files agree with 00 (structure 17:1-19:10 / 19:11-20:15), 06 (white horse), 14 (14:8 prophetic aorist) and 16 (one final battle offered as a possibility).

Verdict: 18.md ready after must-fix items; 19.md ready after must-fix items.

## Applied (reviser)
- M-18-1: applied in zh/en (paragraphs 3-5: "神却不是这样看人"; sin named, repent and trust in Christ, forgiven; 1 Pet 3:18 substitution clause). 1 Pet 3:18 kept: 1 Peter 03 used a different clause ("to bring us to God") and theme.
- M-19-1: applied (blood shed on the cross, 1:5; 5:9, as the pledge), zh/en.
- M-19-2: applied (Gog imagery only 19:17-18 and 20:8-9), zh/en.
- S-18-1: applied (one-sentence pointer plus Walvoord as "one addition"; unity reasons 17:18/18:10, 17:4/18:16, 17:12/18:10 in one clause), zh/en.
- S-18-2: applied (Jer 51:9 as background, Babel hedged), zh/en.
- S-19-1: applied (00 meditation "touched on"; Lamb worshiped with the one on the throne, 5:8-14), zh/en.
- S-19-2: applied (华腓德/B. B. Warfield and Chilton, "chiefly"), zh/en.
- S-19-3: applied (labelled as a reading; Walvoord's distinction added), zh/en.
- C-18-1: applied (LXX Ezek 27:13). C-18-2: applied (following Meredith Kline). C-18-3: not applied, to save space. C-18-4: applied (Dan 5:27).
- C-19-1: applied (Walvoord + Osborne; G. B. Caird after 乔治·凯尔德). C-19-2: applied (2:10, 13). C-19-3: applied. C-19-4: applied (1 John 1:1). C-19-5: applied (the Lamb shed his blood for her coldness and lies), reworded so the subject is "she", not "the saints".
- Quote check: boss's words now in “ ” instead of 「」; also “行业就是这样”.
- Cuts 18: all four applied (Babylon bullets, cargo bullets, 18:1-3 point 3 last line, meditation examples 3 → 2), and also: lament bullets merged, 18:3 bullets merged, minor trims in 18:1, 18:7-8, 18:11, 18:16, 18:23.
- Cuts 19: all six applied (Hos 2:19 / 2 Cor 11:2 / Matt 22:2; 25:10 dropped; "testimony of Jesus" readings dropped; Hallel/Mark 14:26 shortened; names merged and the gloss dropped; 19:17-21 point 4 merged into point 3; shape bullets shortened), and also: Ezek 1:1 and Isa 25:6 dropped, rod/winepress bullet reduced to references, 19:2, 19:3, 19:4, 19:8, 19:20 and meditation trims.
- Final sizes: 18.md 35,836 bytes; 19.md 35,784 bytes. check_cuv_quotes clean on both; build OK; pytest 37 passed; plans/books.json restored.
