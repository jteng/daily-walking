# Theology review: plans/books/revelation/20.md (Revelation 20 draft)

Reviewer: theology-reviewer (Carson/Packer-style exegesis and doctrine). Date: 2026-11-26.

## Verdict

**ready after must-fix items** (2 must-fix, 3 should-fix, 7 consider)

The doctrine is sound throughout. The four millennial views are labelled symmetrically, each with named representatives, and they agree with 00.md. Common ground is stated plainly: the Lord's real bodily return, the resurrection, the judgment, and the new creation. Substitution is plain in the meditation. "Judged by works, saved by the book of life" is put carefully, with Eph 2:8-10 read through v. 10. All CUV and ESV quotations were checked with scripts/bible_lookup.py and match. check_cuv_quotes.py flags only the preacher's invented sentence in the meditation, which is not a Bible quotation and is correctly in 「」 as speech. I simulated scripts/verse_refs.py over the file, and every bare reference resolves to the intended book (no wrong inheritance).

---

## Must-fix

### M1. 20:4: "two kinds of people" stated as fact, and the English presents the ESV as reading two groups
- **Location:** 深读 20:4-6, point 1 / Going Deeper 20:4–6, point 1.
  - zh: 「约翰特别看见两种人的灵魂：「因为给耶稣作见证，并为神之道被斩者」，以及「没有拜过兽与兽像」、没有受兽印记的人（20:4）。」
  - en: "John sees the souls of two kinds of people in particular: "those who had been beheaded for the testimony of Jesus and for the word of God," and those who "had not worshiped the beast or its image" or received its mark (20:4)."
- **Problem:** The Greek *kai hoitines* can mark a second group (all faithful believers who refused the beast; the CUV reads it this way, 「和那……之人的灵魂」). It can also describe the same martyrs a second way, and the ESV reads it so ("the souls of those who had been beheaded … and who had not worshiped"). The English inserts "those who" outside the quotation marks, which makes the ESV appear to say something it does not. This is a disputed point stated as settled.
- **Fix:**
  - zh: 「约翰看见「那些因为给耶稣作见证，并为神之道被斩者的灵魂」，又说到「那没有拜过兽与兽像」、没有受兽印记的人（20:4）。和合本读作两种人：殉道者，以及所有不肯拜兽的信徒（例如毕尔）；英文标准版读作同一群人，就是殉道者，从两方面来描写。」
  - en: "John sees "the souls of those who had been beheaded for the testimony of Jesus and for the word of God, and who had not worshiped the beast or its image and had not received its mark" (20:4). The CUV reads two groups here: the martyrs, and all believers who refused the beast (so Beale). The ESV reads one group, the martyrs, described in two ways."
  - (If space is tight, keep the quotation and add only the last sentence in each language.)

### M2. 20:8: "the same expression in Greek as in 16:14 and 19:19" is inaccurate for 19:19
- **Location:** 深读 20:4-6, point 3, amillennial bullet / Going Deeper 20:4–6, point 3, "Amillennial."
  - zh: 「20:8的「聚集争战」，原文和16:14、19:19是同一个说法，而且都带定冠词」
  - en: ""to gather them for battle" in 20:8 is the same expression in Greek as in 16:14 and 19:19, each time with the article ("the battle")"
- **Problem:** 20:8 and 16:14 share the same phrase (*synagagein autous eis ton polemon*). 19:19 uses a different construction ("gathered to make *the* war", *synēgmena poiēsai ton polemon*). What the three places share is the verb "gather" and the noun with the article, *ton polemon*, which is how 19.md (§19:19) states it. As written, the claim overstates the evidence and is out of step with 19.md.
- **Fix:**
  - zh: 「20:8的「聚集争战」和16:14在原文是同一个说法，19:19的说法也很接近；三处都说「聚集」，「争战」一词都带定冠词（*ton polemon*），好像是同一场最后的争战（参第19章）」
  - en: ""to gather them for battle" in 20:8 is the same Greek phrase as in 16:14, and 19:19 is very close; all three speak of gathering, and each time "battle" carries the article (*ton polemon*), as if it were the same final battle (see chapter 19)"

---

## Should-fix

### S1. The postmillennial bullet gives no exegesis of Revelation 20 itself
- **Location:** 深读 20:4-6, point 3, 「后千禧年派」 / "Postmillennial."
- **Problem:** The brief asks for each view's strongest exegetical case on this text. The other three views engage 20:1-6 (ezēsan, the binding, the 19→20 sequence). The postmillennial bullet cites only Matt 13, Hab 2:14 and 1 Cor 15:25, so this view looks less textually grounded than the others. That is an imbalance of presentation, not a fault in the view.
- **Fix:** add before 「所以他们盼望……」 / "So they look for…":
  - zh: 「他们把20:3「使它不得再迷惑列国」读作福音在列国中越来越得胜：撒但越来越不能拦阻万民归主，基督藉着他的道和圣灵，从天上治理地上的教会。」
  - en: "They read 20:3, "so that he might not deceive the nations any longer," as the gospel's growing triumph among the nations: Satan is less and less able to keep the peoples from Christ, who rules his church on earth from heaven by his word and Spirit."

### S2. Meditation: the "film" fear is answered with the book of life, but not with what God says about forgiven sin
- **Location:** 默想, para. 2 / Meditation, para. 2.
  - zh: 「她没有记错：案卷是真实的。神的审判不会把罪说成没有发生过」
  - en: "She is not mistaken: the books are real. God's judgment will not pretend sin never happened"
- **Problem:** The paragraph rightly refuses to deny the sin. But "she is not mistaken", followed by silence on what happens to forgiven sins, can leave the reader thinking that her fear of the scene being "played" is confirmed. Reformed writers differ on whether believers' sins are disclosed at the judgment (cf. 1 Cor 4:5). All agree that God does not hold forgiven sins against those in Christ (Heb 8:12; Isa 43:25). One sentence would close the gap without overclaiming. Heb 8:12 is expounded in Hebrews 08 but is not used in a meditation there.
- **Fix:** after 「她父亲所受的苦，神也都看见了。」 / "God saw what her father suffered, too." add:
  - zh: 「可是对在基督里的人，神也说过：「我要宽恕他们的不义，不再记念他们的罪愆」（来8:12）。不是全知的神会忘记，而是他不再向她追讨。」
  - en: "Yet to those in Christ God has also said, "I will be merciful toward their iniquities, and I will remember their sins no more" (Heb 8:12). The God who knows all things does not forget; he will not hold it against her."

### S3. "Many historic premillennialists" for the all-people reading of 20:12, and the link to Matt 25
- **Location:** 深读 20:11-15, point 2 / Going Deeper 20:11–15, point 2.
  - zh: 「所有的人（无千禧年派，许多历史前千禧年派和改革宗信条）」
  - en: "All people (amillennialists, many historic premillennialists and the Reformed confessions)"
- **Problem:** I cannot confirm that "many" historic premillennialists identify the great white throne with the judgment of all people in Matt 25. Premillennial readers who follow the sequence of chapters 19-20 usually take "the dead" of 20:12 as mainly "the rest of the dead" (20:5). Some include believers who died during the millennium. Naming Hoekema keeps the attribution safe and matches the symmetric-label rule.
- **Fix:**
  - zh: 「所有的人（无千禧年派，例如安东尼·胡克玛；改革宗信条；也有一些历史前千禧年派）」
  - en: "All people (amillennialists such as Anthony Hoekema, the Reformed confessions, and some historic premillennialists)"

---

## Consider

### C1. 20:4: who sits on the thrones?
- zh: 「第6章祭坛底下的灵魂曾呼求伸冤（6:9-10），在这里，他们坐在宝座上。」 / en: "here they sit on thrones."
- The identity of "those seated" is debated: the martyrs themselves, the saints of Dan 7:22, or the apostles or the twenty-four elders. Suggest:
  - zh: 「……在这里，许多释经者认为，坐在宝座上的正是他们（也有人认为是使徒或二十四位长老）。」
  - en: "here, many interpreters hold, they are the ones seated on the thrones (others think of the apostles or the twenty-four elders)."

### C2. 20:4-6: the premillennial reply to Augustine's "new birth" reading
- Premillennialists, and many amillennialists who follow Hoekema rather than Augustine, note that those who "came to life" had already been beheaded, so the new birth fits poorly. This is a real exegetical point and explains why Hoekema adopts the intermediate-state reading. Suggest one clause at the end of the "spiritual life" bullet:
  - zh: 「前千禧年派回应说，这些人是被斩以后才「复活」的，所以不像是指重生；胡克玛的读法也正是要回应这一点。」
  - en: "Premillennialists reply that these people "came to life" after being beheaded, which does not fit the new birth; Hoekema's reading is partly an answer to this."

### C3. 20:10 "where the beast and the false prophet were"
- The Greek has no verb here (the ESV supplies "were"). Amillennialists reply that this can mean the devil joins them at the same final moment, not afterwards. Optional in the historic premillennial bullet:
  - zh: 「（原文这里没有动词，无千禧年派认为也可以理解为同时发生。）」
  - en: "(The Greek has no verb here; amillennialists take it as possibly simultaneous.)"

### C4. "on one day" (Acts 24:15)
- zh: 「新约别处也多把死人复活和审判放在同一个日子（约5:28-29；徒24:15）」 / en: "usually puts the resurrection of the dead and the judgment on one day"
- Acts 24:15 speaks of one resurrection "of both the just and the unjust" but names no day; John 5:28 says "an hour". Suggest:
  - zh: 「……多把义人和不义之人的复活说成同一件事（约5:28-29「时候要到」；徒24:15）」
  - en: "…usually speaks of the resurrection of the just and the unjust as one event (John 5:28–29, "an hour is coming"; Acts 24:15)"

### C5. Col 2:14: the subject is God
- zh: 「那「攻击我们、有碍于我们的字据」，他已经「钉在十字架上」（西2:14）。」 follows 「他亲口说过」 (Jesus), so "he" reads as the Son. In Col 2:13-14 the subject is most naturally God ("God made alive together with him"). Suggest:
  - zh: 「神已经把那「攻击我们、有碍于我们的字据」「钉在十字架上」（西2:14）。」
  - en: "And God has set aside "the record of debt that stood against us," "nailing it to the cross" (Col 2:14)."

### C6. Justin, *Dialogue* 80
- The citation is accurate. For balance, note that Justin, in the same chapter, also counts "right-minded Christians on all points" as holding the millennium, so his concession is real but limited. This is optional.

### C7. Meditation shape close to Revelation 12's (for the application reviewer)
- 12.md's meditation also features an older woman who serves in the church, carries a secret sin from her youth, has confessed it repeatedly, and is haunted by a 「案卷」. 20.md follows the brief's assignment (fear of the judgment and the books) and ends correctly on 21:27, without the keys of Death and Hades or 3:5. Still, the two scenarios are close enough that the application reviewer should judge whether to vary 20's (for example, a believer whose fear comes from fear-driven preaching rather than a single hidden act).

---

## Sound, keep

- The symmetric four-view section, with named representatives (Augustine/Hoekema/Beale; Ladd/Justin/Irenaeus; Walvoord; Edwards/Boettner/Warfield), is consistent with 00.md §5 and 19.md §19:19.
- *ezēsan* in 20:4-5 is handled accurately (aorist of *zaō*; "came to life"). Alford's remark is fairly paraphrased. Augustine, *City of God* 20.6, and Hoekema's intermediate-state reading are correctly distinguished, and John 5:25 / 28-29 is used fairly.
- Matt 12:29 / Rev 20:2: the same verb (*deō*) is correctly stated. The future-binding reply (sealed pit; 2 Cor 4:4) is given fairly.
- The common-ground paragraph affirms the bodily return, the resurrection, the judgment, Satan's end and the new creation, with a pastoral word for dispensational-shaped Chinese churches.
- On the lake of fire, the majority view (Augustine; WCF 33) is distinguished from conditional immortality (Stott, "tentatively"), which is accurate and not overstated.
- The great white throne is handled in Trinitarian terms (Father and Son; John 5:22; Acts 17:31; 22:3), which guards the deity of the Son. On works versus the book of life, Eph 2:8-10 is read through v. 10, and works are presented as evidence, not ground.
- The Scofield note on Ezekiel 38 is correctly reported, and date-setting is warned against.
- In the meditation, substitution is stated plainly ("on the cross bore God's judgment for sinners"). Heidelberg Q52 is accurately summarized. The gospel is offered to the unsure reader (John 3:18, 5:24). Making amends is explicitly "not the price". The meditation ends on 21:27 and grace, as assigned.
- Chinese/English parity is good; I found no claim present in one body and missing from the other.

## Applied (reviser)

- M1 applied (zh/en): full CUV/ESV 20:4 quotation; CUV two groups (Beale) vs ESV one group described two ways.
- M2 applied (zh/en): 20:8 = 16:14, 19:19 very close; shared "gather" + articular *ton polemon*, see ch. 19.
- S1 applied (zh/en): postmillennial reading of 20:3 as the gospel's growing triumph added.
- S2 applied (zh/en): Heb 8:12 (CUV/ESV verbatim) added after "God saw what her father suffered"; removed the second 「可是」 in zh.
- S3 applied (zh/en): "amillennialists such as Hoekema, the Reformed confessions, and some historic premillennialists".
- C1 applied (zh/en): "many interpreters hold" they sit on the thrones; apostles / 24 elders named as alternative.
- C2 applied (zh/en): premillennial reply (came to life after beheading) and Hoekema's reading as partly an answer.
- C3 applied (zh/en): parenthesis that the Greek has no verb in 20:10; amillennial "simultaneous" reading.
- C4 applied (zh/en): "resurrection of the just and the unjust as one event (John 5:28-29 'an hour is coming'; Acts 24:15)".
- C5 applied (zh/en): God made the subject of Col 2:14.
- C6 not applied: optional; space (file had to be cut to ~36 KB).
- C7 not applied: left for the application reviewer, as the report suggests.
- Also: removed English "came to life" from ::zh (20:4-6 point 2); Rev 20:12 named explicitly after Heb 8:12 in the meditation.
- Cuts for size (both languages): shorter chapter-shape bullets; 20:1-3 quote shortened to 20:1-2; two 要点 lines (20:1-3, 20:7-10) dropped; Col 2:15, Matt 13:31, Dan 7:22 and Dan 12:1 quotations, Matt 16:27 / Rev 22:12 refs, Dan 7:9 quote reduced to ref, redundant closing sentences in 20:6, 20:7-8, 20:11, 20:14 removed; common-ground and Gog/Magog sentences tightened. Size ~37 KB -> 36.3 KB (after additions).
