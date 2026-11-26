# Theology review: Revelation 12 and 13 (drafts of 2026-11-26)

Reviewer: theology-reviewer (Carson/Packer lens; a model applying their published emphases, not the men themselves).
Files: plans/books/revelation/12.md, plans/books/revelation/13.md.
Checks run: scripts/check_cuv_quotes.py (both files clean); ESV quotes checked against EnglishESVBible.xml with a phrase-match script (all ESV quotations verbatim; the only non-matches are deliberate non-ESV text: the KJV "the Lamb slain from the foundation of the world", the WCF wording, the CUV-based variant gloss at 13:10, "Who is like God?", and the friend's words in the 12 meditation). Spot-checked cross-references with scripts/bible_lookup.py.

## Verdicts

- **12.md: ready after must-fix items** (2 must-fix, 6 should-fix, 4 consider)
- **13.md: ready after must-fix items** (3 must-fix, 5 should-fix, 4 consider)

The doctrine is sound in both files. The atonement is stated plainly: "the Lamb has borne their penalty", "the Lamb's blood has paid for this very thing". The deity of Christ is protected, the debated readings are mostly set out symmetrically, and the 00 framework is respected. The must-fix items are the cross-chapter rulings the caller asked for (13 meditation scenario, 12 name, 12 pointing back to 11) and three factual points (the "three times" claim against the CUV in 12:9, the Westminster revision date, and the 616 evidence).

---

## 12.md

### Must-fix

**M12-1. Rename 秀兰 (also used in 21).**
- Location: 12.md, 默想 / Meditation, throughout.
- Problem: 秀兰 / Xiulan is also the meditation character in 21.md. The 06-22 run must not repeat names.
- Fix: rename to **素珍 / Suzhen** throughout both bodies. I grepped plans/books for 素珍 and Suzhen and found neither. 「秀兰姊妹」→「素珍姊妹」; "Sister Xiulan" → "Sister Suzhen"; every later 秀兰/Xiulan → 素珍/Suzhen.

**M12-2. 12:9 "thrown down three times" is false of the CUV.**
- Location: 12.md, 深读 12:7-9, point 3. zh: 「这一节里『被摔』接连出现了三次，是被动的说法」.
- Problem: the Greek has the passive three times (ἐβλήθη, ἐβλήθη, ἐβλήθησαν), and so does the ESV. The CUV of 12:9 has 被摔 only twice (「它被摔在地上，它的使者也一同被摔下去」), so a Chinese reader will count two and conclude the claim is wrong. The English sentence is fine.
- Fix (zh only): 「这一节原文里「被摔」这个动词（*eblēthē*）出现了三次（和合本译出两次），都是被动的说法：不是龙自己离开，而是被神赶出去。」 Leave the English as is, or optionally write "in this verse the Greek verb 'thrown down' (*eblēthē*) occurs three times".

### Should-fix

**S12-1. Point the 1,260 days back to 11.md instead of re-surveying them (cross-chapter ruling 3; also saves about 1 KB).**
- Location: 12.md, 深读 12:1-6, point 6 (「第11章已经介绍过几种读法：毕尔、威廉·亨德里克森等认为……过去派（例如肯尼斯·詹特里）连于主后66-70年的犹太战争。」 / "Chapter 11 has already set out the main readings: … (preterists such as Kenneth Gentry).").
- Problem: the draft says 11 has set out the readings and then repeats all four. 11.md (深读 11:2-3) is the home of this survey and states that the study leans to the church-age reading. 12 should point back to it and repeat neither the list nor the names.
- Replacement zh (from 「一千二百六十天，就是四十二个月」 up to 「是神量定的。」):
  「这段日子和两个见证人传道的日子相同（11:3），又称为「一载二载半载」（12:14）。几种主要的读法，第11章已经介绍过（参11:2-3的讨论）；本研读在那里倾向把它看作从基督升天到再来的整个教会时代。无论采取哪一种看法，这段时间都是有限的，是神量定的。」
- Replacement en: "This is the same period as the two witnesses' prophesying (11:3), also called "a time, and times, and half a time" (12:14). The main readings are set out at 11:2–3; there this study leans toward taking it as the whole church age from Christ's ascension to his return. On any view the time is limited and measured out by God."
- Keep the Elijah, wilderness and manna sentences that follow.
- Related fix in 13.md: 深读 13:5-10, point 1, 「（参12:6的讨论）」 / "(see the discussion at 12:6)" should become 「（参11:2-3的讨论）」 / "(see the discussion at 11:2–3)".

**S12-2. 12:10 "now": a disputed reading is stated as fact right after the options were listed.**
- Location: 深读 12:10-12, point 1. zh: 「「现在」不是指世界末了，而是指羔羊被杀、复活、升天以后的这个时候。神的国度和基督的权柄，已经在十字架上开始了」. en: ""Now" is not the end of the world, but the time after the Lamb has been slain, raised and exalted. God's kingdom and the authority of his Christ have already begun at the cross".
- Problem: section 12:7-9 point 2 has just set out a futurist (Walvoord) reading that puts this in a future tribulation. Point 1 then settles the matter without a label. I agree with the inaugurated reading, and the text supports it: the child is caught up in 12:5 and conquers "by the blood of the Lamb" in 12:11. But it has to be labeled as a reading.
- zh: 「按许多释经者（例如毕尔、包衡）的读法，「现在」不是指世界末了，而是指羔羊被杀、复活、升天以后的这个时候：神的国度和基督的权柄，已经借着十字架和复活开始了（参诗2:2、8）；未来派则把这首诗歌连于将来的大灾难。」
- en: "On the reading many take (for example Beale and Bauckham), "now" is not the end of the world but the time after the Lamb has been slain, raised and exalted: God's kingdom and the authority of his Christ have already been inaugurated through the cross and resurrection (cf. Ps 2:2, 8). Futurists link the song to a future tribulation."

**S12-3. Michael is not Christ: add one guarding sentence (deity of Christ, Chinese context).**
- Location: 深读 12:7-9, point 1, after 「这里打仗的是米迦勒，不是基督自己」 / "It is Michael who fights here, not Christ himself".
- Problem: the draft rightly distinguishes Michael from Christ but gives no reason. Some older Protestant interpreters identified Michael with Christ. Jehovah's Witnesses, who are active among Chinese speakers and are already answered in 07, teach that Jesus is Michael the archangel, a creature. One sentence here protects the deity of the Son.
- zh: 「有些较早的释经者认为米迦勒就是基督；耶和华见证人更教导耶稣就是天使长米迦勒，是受造的。可是圣经称米迦勒为「天使长」（犹1:9）、「大君中的一位」（但10:13），而子是「神的使者都要拜他」的那一位（来1:6）。」
- en: "Some older interpreters took Michael to be Christ, and Jehovah's Witnesses teach that Jesus is the archangel Michael, a created being. But Scripture calls Michael "the archangel" (Jude 9) and "one of the chief princes" (Dan 10:13), while of the Son it says, "Let all God's angels worship him" (Heb 1:6)."
- These quotations are verified against the CUV and ESV. 「大君中的一位」 is verbatim CUV of Dan 10:13.

**S12-4. Safeguarding in the marriage-breakdown lines (WORKFLOW safeguarding points).**
- Location: 默想, paragraph 3. zh: 「如果你是在暴力和危险中离开的，离开危险不是罪。」 en: "If you left because of violence and danger, leaving danger is not sin."
- Problem: the line is good, but the WORKFLOW points that apply here are missing: reporting violence to the police is right, and a victim need not return to someone unsafe. The draft also says nothing to the spouse who was left, whom the accuser also targets.
- zh: 「如果你是在暴力和危险中离开的，离开危险不是罪；向警方求助是对的（罗13:4），你也不必回到一个不安全的人身边。如果你是被离弃的一方，控告者也许会说都是你的错；被人离弃，本身不是你的罪。」
- en: "If you left because of violence and danger, leaving danger is not sin; going to the police is right (Rom 13:4), and you need not go back to someone unsafe. If you were the one who was left, the accuser may tell you it was all your fault; being abandoned is not in itself your sin."
- The abortion care itself is sound, and I would keep it. It names the act as real sin, confessed with tears ("everything written in the file is true"). It says that sin is answered by the Lamb's blood, not denied. It refuses to speculate about the child beyond God's justice (Gen 18:25). It names her being wronged (abandonment, family pressure) without turning that into an excuse. It distinguishes the Spirit's conviction from the accuser's charges. And it warns the church not to "speak for the accuser".

**S12-5. The Lord's Supper element repeats a used theme (1 Corinthians: "feeling too unworthy for the Lord's Supper").**
- Location: 默想, paragraph 1 「所以她不敢领圣餐」, paragraph 3 「控告者却把人从圣餐桌前赶开」, paragraph 4 「下一个主日，秀兰领了饼和杯。」 and the matching English.
- Problem: WORKFLOW's used-theme list has this resolution already. The application reviewer will flag it too. Tie the accusation to her own ministry of visiting the sick instead, which is already in the scene.
- Paragraph 1, replace 「所以她不敢领圣餐，也从来不敢在姊妹会里分享。」 with 「所以她每次在病床边为人祷告，心里都有一个声音说：你也配为别人求生命吗？她也从来不敢在姊妹会里分享。」
  en: replace "So she does not dare take the Lord's Supper, and she has never dared share at the women's meeting." with "So every time she prays at a bedside, a voice inside says: you, of all people, ask God for someone's life? And she has never dared share at the women's meeting."
- Paragraph 3: 「控告者却把人从圣餐桌前赶开」→「控告者却叫人觉得自己不配服事」. en: "the accuser drives her away from the Lord's Table" → "the accuser tells her she is unfit to serve".
- Paragraph 4: 「下一个主日，秀兰领了饼和杯。」→「下一周，素珍去医院探访一位早产的年轻妈妈，为她和孩子祷告的时候，声音没有再发抖。」 en: "The next Sunday Xiulan took the bread and the cup." → "The next week Suzhen visited a young mother whose baby had come early, and when she prayed for the mother and child her voice did not shake."

**S12-6. "Often" overstates what comes from the dragon's mouth.**
- Location: 深读 12:13-17, point 2. zh: 「从龙的口中出来的，在启示录里常常是迷惑人的话（参16:13）」. en: "in Revelation what comes from the dragon's mouth is often deceiving speech (cf. 16:13)".
- Problem: the dragon's mouth appears only here and in 16:13-14, where unclean spirits perform signs. "Often" overreads the evidence.
- zh: 「16:13-14也说，从龙口中出来的是污秽的灵，行奇事迷惑人。」 en: "In 16:13–14 too, what comes from the dragon's mouth is unclean spirits that deceive by signs."

### Consider

**C12-1. Fold the 12:18 / 12:17 versification and the KJV variant into the overview, and drop point 4 of 深读 12:13-17 (saves about 0.9 KB).** The ESV XML has no 12:18; its 12:17 ends "And he stood on the sand of the sea". The CUV numbers this line 12:18, as NA28 does. The KJV reads "I stood" (later manuscripts) and places it at 13:1. The draft's text-critical claim is right: P47, Sinaiticus and Alexandrinus read ἐστάθη, "he stood". One detail is missing: the KJV puts the line in 13:1.
- zh overview, replace the paragraph beginning 「和合本的12:18」 with: 「和合本的12:18「那时龙就站在海边的沙上」（英文标准版把这句放在12:17末了；英文钦定本按较后期的抄本作我站在，指约翰，放在13:1），把我们带到第13章：龙不能再上天，就站在海边，等着那兽从海中上来，借着地上的权势作工。」
- en overview: "The last line of 12:17 in the ESV, "And he stood on the sand of the sea" (12:18 in the Chinese Union Version; the KJV, following later manuscripts, reads "I stood," meaning John, and places it at 13:1), leads into chapter 13: barred from heaven, the dragon stands at the shore, waiting for the beast to rise from the sea and work through earthly power."
- Then delete point 4 and move the 要点 line up.

**C12-2. Marian reading: make it precise and keep the tone even.** The facts are right. Hippolytus, *On Christ and Antichrist* 61, does take the woman as the church. The Roman Missal's first reading for the Mass of the day of the Assumption is Rev 11:19a; 12:1-6a, 10ab. Two optional tweaks: (a) 「诵读这一段经文」 → 「以这一段（11:19；12:1-6、10）为第一篇读经」 / "uses this passage (11:19; 12:1–6, 10) as the first reading". (b) The closing 「我们不必轻看她，却也不向她祷告」 / "we need not belittle her, though we do not pray to her" reads as a polemical aside in an otherwise symmetric survey. It could become 「福音派尊敬她，也学习她的信心，但只向三一神祷告」 / "Evangelicals honor her and learn from her faith, while praying to the triune God alone".

**C12-3. John 16:8 is about the world.** The 深读 12:10-12 point 2 bullet ("Accusation is not conviction") applies John 16:8, which speaks of the Spirit convicting "the world", to believers' confession. That is a fair extension, but it could be marked: 「（这节首先是说世人，也适用于信徒）」 / "(said first of the world, but true for believers too)". Or it could cite John 16:13-14 alongside.

**C12-4. Trims for length (12 is 37.6 KB).** S12-1 saves about 1.3 KB and C12-1 about 0.9 KB, while S12-3 and S12-4 add about 1.0 KB. More cuts:
- (a) In 深读 12:13-17 point 2, drop the Ps 124:4 / Isa 43:2 sentence (about 0.5 KB).
- (b) Drop the 深读 12:7-9 要点 line, which 12:10-12's 要点 repeats (about 0.4 KB).
- (c) Shorten the 12:11 "Loving not their lives" bullet to one sentence with 2:10 only, since 03 already uses 12:11 (about 0.3 KB).
- (d) Compress view 1 of "When is this war?" to one sentence (about 0.3 KB).
- (e) Optionally trim 本章脉络's three bullets to one line each (about 0.6 KB).
- That brings the file to about 34 KB.

---

## 13.md

### Must-fix

**M13-1. Replace the meditation scenario (cross-chapter ruling 1): falsified inspection reports repeat 11's quality inspector, and 陈 is already used in 06, 09, 10, 15 and 17.**
- Location: 13.md, 默想 / Meditation, paragraphs 1, 2 and 4.
- Ruling: give him the surname 郑 (Xiao Zheng). I grepped the Revelation folder and found no 郑 or Zheng. Give him a compromise that is closer to 13:16-17 than any fraud: livelihood tied to worship, the very pressure Asia's trade guilds put on Christians (guild feasts and patron gods). In Chinese business life the direct parallel is the shop-opening rite of burning incense to 财神. It is not tax fraud (Romans), investment fraud (17), the 996 workplace (18) or false inspection (11). It also lets the 666 thread make a sharper point: he hunts for the mark in chips and health codes while he is asked to bow, which is exactly what 13:16 and 14:9 are about.
- The draft's paragraph 4 also needs a guard. Its assurance for someone who has already compromised is right, but without a sentence on 14:9-11 a careful reader may ask whether the warning there is real. One sentence is enough. I have avoided "Peter by the fire", which is used in 2 Corinthians.
- (An alternative if the 财神 scene is thought too close to 1 Thess 01's household idols: a medical-device sales rep told that the promotion depends on paying kickbacks (回扣) to hospital doctors. I prefer the 财神 scene because it carries the worship dimension of 13:16-17 and 14:9.)

New paragraph 1 (zh), after the verse quote:
「小郑在一家连锁餐饮公司做店长，在教会的小组里是出了名的启示录专家。他能讲清楚尼禄该撒怎样算成六百六十六，也知道六百一十六的抄本问题；疫情那几年，他常在群里转发文章，提醒大家留意哪一种芯片、哪一种码可能就是兽的印记。这个月，公司要派他去开一家新店，升区域经理的事也有了眉目。老板只有一个规矩：每家新店开业那天，店长要带着全体员工给财神上香、磕头，说是图个吉利，从来没有人例外。上司私下对他说：「你不拜，别的店长会怎么想？这个位置有的是人要。」周四晚上他还在小组里讲兽的数目；开业前一天晚上，他站在那尊还盖着红布的财神像前，心里算的不是六百六十六，而是房贷和孩子的学费。」
(The quote marks around the supervisor's words are a quoted saying, which WORKFLOW permits; if the Chinese reviewer prefers, use a colon without 「」.)

New paragraph 1 (en), after the verse quote:
"Xiao Zheng manages a branch of a restaurant chain, and in his church small group he is known as the "Revelation expert." He can explain exactly how "Nero Caesar" adds up to 666, and he knows about the manuscripts that read 616; during the pandemic years he kept forwarding articles to the group chat warning which chip or which code might be the mark of the beast. This month the company wants him to open a new branch, and a promotion to regional manager is in sight. The owner has one rule: on the day a new branch opens, the manager leads all the staff in burning incense and bowing to the god of wealth, "for luck," and no one has ever been excused. His supervisor tells him quietly, "If you won't bow, what will the other managers think? Plenty of people want this job." On Thursday night he was explaining the number of the beast in his small group; the night before the opening he stands in front of the god of wealth, still under its red cloth, and the sum in his head is not 666 but his mortgage and his child's school fees."

New paragraph 2 (zh):
「约翰最初的读者，住在推雅推喇、别迦摩这样的城里，生意常和行会的宴席、守护神的节期连在一起：不去赴席，就接不到生意。兽的印记先写在人敬拜的心里，然后才在手所做的事上显出来。小郑一直在芯片和手机里找兽的印记，却差一点在开业那天，在全店的人面前向别的神弯下腰。我也许不像他那样懂六百六十六，也不一定有人叫我上香，可是我知道，为了一个职位、一张执照、一笔生意，我曾经怎样一点一点地让步。」

New paragraph 2 (en):
"John's first readers lived in cities like Thyatira and Pergamum, where trade was bound up with guild feasts and the festivals of patron gods: stay away from the feast and the contracts dry up. The mark of the beast is written first on the heart's worship, and only then shows itself in what the hand does. Xiao Zheng had been searching chips and phones for the mark of the beast, yet on opening day he nearly bowed to another god in front of his whole staff. I may not know as much about 666 as he does, and no one may ask me to burn incense, but I know how, for a position, a licence or a deal, I have given way little by little."

Paragraph 3: keep as drafted (Luke 4:6-8; John 19:15).

New paragraph 4 (zh):
「那个周四，小郑第一次没有在小组里讲六百六十六，而是讲了开业的事。他也承认，去年另一家店开张的时候，他虽然没有磕头，却站在老板旁边替他点了香。小组里没有人指着他说他受了兽的印记；大家一起读13:8，名字记在「被杀之羔羊生命册上」的人，不是靠自己的刚强站立的。他们为他祷告，也说好，如果他因此丢了这个位置，大家一同承担。小郑去见老板，客气地说明自己是基督徒，不能上香磕头，开业的其他事他都会尽心办好。他不知道结果会怎样。启示录14:9-11严厉警告那些拜兽、受印记的人，那是到底甘心归属兽的人；一个曾经软弱、又回转悔改的门徒，羔羊并没有因为去年那一炷香把他的名字划掉。主耶稣的国不是赏给从来没有屈过膝的人，而是赐给那些屈过膝、又被他的血带回来的人。」

New paragraph 4 (en):
"That Thursday, for the first time, Xiao Zheng did not talk about 666 at small group. He talked about the opening. He also admitted that when another branch opened last year, though he had not bowed, he had stood beside the owner and lit the incense for him. No one pointed at him and said he had taken the mark of the beast. Together they read 13:8: those whose names are written "in the book of life of the Lamb that was slain" do not stand by their own strength. They prayed for him, and agreed that if he lost the position over this, they would carry it with him. Xiao Zheng went to the owner and explained politely that as a Christian he could not burn incense or bow, and that he would do everything else for the opening with all his heart. He does not know how it will turn out. Revelation 14:9–11 warns in the strongest terms those who worship the beast and receive its mark, people who give themselves to the beast to the end; but the Lamb has not crossed out the name of a disciple who was weak and has turned back, not over last year's incense. The Lord Jesus does not give his kingdom as a prize to those who have never bent the knee. He gives it to those who bent the knee and have been brought back by his blood."

Paragraph 5 (prayer and Luke 12:32 ending): keep. Change 「我却常常为了一点点好处就弯了腰」 only if the Chinese reviewer wants; it now echoes the scene well.

**M13-2. Westminster Confession 25.6: state the American revision accurately.**
- Location: 深读 13:1-4, point 5, historicist bullet. zh: 「后来有些长老会（例如二十世纪初美国的长老会）删去了这一句」. en: "some Presbyterian churches later removed the clause (for example in America in the early twentieth century)".
- Problem: "in America" reads as though all American Presbyterians acted together. The deletion was the Presbyterian Church in the U.S.A.'s 1903 revision of the Confession, which also amended 16.7 and 22.3 and added chapters 34-35. The bodies descended from it use the revised text of 25.6 ("Nor can the Pope of Rome, in any sense, be head thereof."). The quoted original wording ("that Antichrist, that man of sin, and son of perdition") is correct. So are the 2 Thessalonians source and the 1646 date (completed December 1646; proof texts 1647). The original proof texts include Rev 13:6 as well as 2 Thess 2:3-4, 8-9, so placing it under the beast is fair. "Reformation era" is loose for the 1640s.
- Also add one clause so the survey is symmetric: some confessional Reformed believers still hold the original wording.
- zh replacement (from 「这是在宗教改革时期」 to the end of the bullet): 「这是在经历了一个多世纪的逼迫和激烈对立之后写成的。美国长老会（PCUSA）在1903年修订信条时删去了这一句，许多长老会今天采用修订后的文字；许多福音派信徒也不再这样认定，不过也有一些改革宗信徒仍持守原文。」
- en replacement: "It was written after more than a century of persecution and bitter conflict. The Presbyterian Church in the U.S.A. struck the clause in its 1903 revision, and many Presbyterian churches today use the revised text; many evangelicals no longer make the identification, though some Reformed believers still hold the original wording."
- My confidence: high on the 1903 PCUSA revision including 25.6. If the reviser cannot confirm it independently, "the Presbyterian Church in the U.S.A., early in the twentieth century" is the safe fallback, still naming the body.

**M13-3. The 616 evidence: name the papyrus and hedge its date; the hōs esphagmenēn claim needs the right form.**
- (a) Location: 深读 13:16-18, point 3, Nero bullet. zh: 「现存的一些抄本也有这个读法，包括一份三世纪的蒲草纸残片」. en: "some surviving manuscripts also read it, including a third-century papyrus fragment".
  - Problem: the fragment is P115 (P.Oxy. 66.4499). Its editors date it to the later third century, and the INTF list gives third/fourth century, so "third-century" is slightly firm. The other main witness, the fifth-century Codex Ephraemi Rescriptus (C), should be named. Irenaeus, *Against Heresies* 5.30.1, is correctly cited: he knew copies reading 616 and blamed scribal error, against "all the most approved and ancient copies". *Lateinos* at 5.30.3 is correct: he lists Euanthas, Lateinos and Teitan and declines to decide. The gematria (נרון קסר = 666; without the final nun, 616) is correct.
  - zh: 「现存的抄本中也有这个读法，主要是一份约三世纪的蒲草纸残片（P115，即俄克喜林库斯蒲草纸4499号）和五世纪的以法莲抄本。」
  - en: "surviving manuscripts also have it, chiefly a papyrus fragment from about the third century (P115, P.Oxy. 4499) and the fifth-century Codex Ephraemi."
- (b) Location: 深读 13:1-4, point 3. zh: 「用的是同一个说法（*hōs esphagmenēn*）」. en: "the same expression (*hōs esphagmenēn*)".
  - Problem: 5:6 has the neuter ὡς ἐσφαγμένον (agreeing with ἀρνίον); 13:3 has the feminine ὡς ἐσφαγμένην (agreeing with μίαν [κεφαλήν]) plus εἰς θάνατον. It is the same participle, but not the same form.
  - zh: 「用的是同一个分词（5:6作*hōs esphagmenon*，13:3作*hōs esphagmenēn*）」. en: "the same participle (*hōs esphagmenon* in 5:6, *hōs esphagmenēn* in 13:3)".

### Should-fix

**S13-1. Overview: "as the Father gives the scroll to the Lamb (5:7)" overreads 5:7.**
- Location: 本章脉络 / Shape, paragraph 2. zh: 「龙把权柄给兽，像父把书卷交给羔羊（5:7）」. en: "as the Father gives the scroll to the Lamb (5:7)".
- Problem: in 5:7 the Lamb takes the scroll. It is not handed to him. The text that actually matches 13:2/4 is the Son's received authority.
- zh: 「龙把权柄给兽，像子从父领受权柄（2:27「像我从我父领受的权柄一样」）」. en: "The dragon gives his authority to the beast, as the Son receives authority from the Father ("even as I myself have received authority from my Father," 2:27)". Both quotations are verified.
- Also add one Trinitarian guard, since this is a "counterfeit trinity": 「这只是模仿的外形，不是说三一神有任何可以被比拟的缺欠」 is optional. A shorter alternative is to add after 「撒但不能创造，只能模仿」 the words 「而且模仿得永远不像」 / "and the imitation is never a likeness".

**S13-2. 13:8: "most modern translations" needs the NIV exception.**
- Location: 深读 13:5-10, point 3. zh: 「多数现代译本采用前一种读法」. en: "Most modern translations take the first reading."
- Problem: the ESV, NASB, RSV and NRSV attach the phrase to "written", but the NIV (1984 and 2011) reads "the Lamb who was slain from the creation of the world". The draft is right that the Greek word order favors "slain".
- zh: 「许多现代译本（例如英文标准版）采用前一种读法，也有一些（例如新国际版）采用后一种。」 en: "Many modern translations (e.g. ESV, NRSV) take the first reading; some (e.g. NIV) take the second."

**S13-3. Bauckham and Beale on church insiders: hedge the attribution.**
- Location: 深读 13:11-15, point 3, first-century bullet. zh: 「许多学者（例如包衡、毕尔）认为，地中的兽代表推动皇帝崇拜的地方祭司和城中的权贵，甚至也包括教会里那些劝信徒随从的人」. en: "Many scholars (for example Bauckham and Beale) think … and even for those in the churches who urged believers to go along".
- Problem: the local priests and elites reading is widely held, Bauckham's included. Extending the beast to false teachers inside the church is especially Beale's emphasis. As written, the sentence attributes it to both.
- zh: 「……地中的兽代表推动皇帝崇拜的地方祭司和城中的权贵；有些学者（例如毕尔）认为，也包括教会里那些劝信徒随从的人……」. en: "…stands for the local priests and city elites who promoted the imperial cult; some (for example Beale) extend it to those in the churches who urged believers to go along…".

**S13-4. Hand and forehead: hedge the symbolism.**
- Location: 深读 13:16-18, point 1. zh: 「额关乎人所认信的，手关乎人所做的。」 en: "The forehead concerns what a person confesses; the hand concerns what a person does."
- Problem: this is a common homiletic reading but not stated by the text. Mark it as such.
- zh: 「许多人认为，额关乎人所认信的，手关乎人所做的。」 en: "Many take the forehead to stand for what a person confesses and the hand for what a person does."

**S13-5. Point 1 of 13:5-10 should send readers to 11, not 12 (from S12-1).** 「（参12:6的讨论）」→「（参11:2-3的讨论）」; "(see the discussion at 12:6)" → "(see the discussion at 11:2–3)".

### Consider

**C13-1. Ephesus imperial temple.** 「以弗所在多米田时也有皇帝的庙」 / "Ephesus had an imperial temple under Domitian" is stated more firmly than 00 does ("many scholars think"). The Temple of the Sebastoi (c. AD 89/90) is well attested, so this is acceptable. For consistency, write 「以弗所在多米田时也建了皇帝的庙（参看导读）」 or keep 00's hedge.

**C13-2. Cullmann.** "As Oscar Cullmann argued" is accurate. Adding the title helps a reader check it: 《新约中的国家》 / *The State in the New Testament* (1956).

**C13-3. Murabba'at spelling.** Optionally add to the Nero bullet that the Hebrew spelling נרון קסר is attested in a first-century Aramaic document from Wadi Murabba'at. This answers the common objection that the spelling is contrived. Keep it hedged ("an Aramaic document from about the time").

**C13-4. Trims for length (13 is 39.2 KB).** The new meditation is roughly the same size as the old one. Cuts:
- (a) 深读 13:1-4 point 3: reduce the three wound bullets to one sentence each, and leave the Nero legend detail (Tacitus, Suetonius) to 17, which "returns to it" (about 0.9 KB).
- (b) Point 5 "Who is the beast?": 00 already sets out the four schools. Keep only the historicist bullet (with the M13-2 fix) and the eclectic sentence, and reduce the preterist, futurist and idealist bullets to one line: 「过去派（詹特里）、未来派（华尔伏）、理想派（亨德里克森）的读法，参看导读。」 / "For the preterist (Gentry), futurist (Walvoord) and idealist (Hendriksen) readings, see the Introduction." (about 0.7 KB).
- (c) Move the *Lateinos* bullet into the historicist bullet of point 5 as one clause and delete it from 13:18 (about 0.5 KB).
- (d) Shorten point 6 (Romans 13 / Revelation 13) by dropping 1 Pet 2:17 and the tax sentence (about 0.5 KB).
- (e) Fold point 4 "A word about pastors" into the end of point 2 as one sentence (about 0.4 KB).
- (f) In 13:18 point 4, cut the sentence about Irenaeus urging restraint, since 00 has it with the citation (about 0.3 KB).
- That brings the file to about 35 KB.

---

## What is sound and should be kept

- 12: the three readings of the woman, each with representatives (Beale/Bauckham plus Hippolytus 61; Walvoord; the Catholic liturgical use), and the fair concession on Mary; the Gen 3:15 thread through 12:4-5 and 12:17; *diadēma* against *stephanos*; the three readings of the war in heaven and the harmonizing note; Isa 14 and Ezek 28 rightly qualified; the accuser who uses true charges (Zech 3) answered by penal substitution and Rom 8:33-34; the distinction between accusation and conviction; the wrath of a defeated enemy (12:12); the exodus background (Exod 19:4; 15:12).
- 12 meditation: careful, honest and gospel-grounded treatment of abortion. Sin is named, the woman is not crushed, the child is entrusted to God without speculation, the wrong she suffered is acknowledged, and the church is warned against gossip. It ends as the brief asks, on the 12:10 announcement.
- 13: the counterfeit-trinity frame; Dan 7 composite beast; Luke 4:6 linked to 13:2; the parody of Exod 15:11 and the name Michael; the divine passive in 13:5-7 hedged as "many"; the 13:8 and 13:10 textual and syntactic notes, with the shared sense drawn out; Deut 13:1-3 as the test of signs; the mark as counterfeit of the seal, tied to worship (14:9), so "not taken unknowingly" (which pastorally defuses vaccine and chip fears, consistent with 00); the four 666 readings with the harmonizing "these views can stand together"; the Romans 13 / Revelation 13 balance; the faithful-pastor note.
- 13 meditation ending: Christ's refusal of the dragon's offer (Luke 4:6-8) and the gift of the Father's kingdom (Luke 12:32).

## Summary count

- 12.md: 2 must-fix, 6 should-fix, 4 consider. Verdict: ready after must-fix items.
- 13.md: 3 must-fix, 5 should-fix, 4 consider. Verdict: ready after must-fix items.
