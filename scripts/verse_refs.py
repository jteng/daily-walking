"""Add the book name to same-book verse references in Book Study text.

Authors write same-book references bare: "（3:3、5）" or "(3:3, 5)". The
app's verse tooltip only recognizes references that start with a book name,
so at build time every bare chapter:verse gets the chapter's own book
prefixed ("约3:3" / "John 3:3").

Rules:
- A reference already preceded by a book name is left alone.
- Inside parentheses, a bare reference that directly follows another
  book's reference in a list inherits that book, so "（林前9:1；15:8）"
  keeps 15:8 in 1 Corinthians; with other words between them ("Ps 41:9,
  quoted at 13:18") it gets the chapter's own book.
- Section headings ("## 深读 3:1-21") are left alone.
"""
import re

ZH_ABBRS = sorted(
    '创 出 利 民 申 书 士 得 撒上 撒下 王上 王下 代上 代下 拉 尼 斯 伯 诗 箴 传 歌 赛 耶 哀 '
    '结 但 何 珥 摩 俄 拿 弥 鸿 哈 番 该 亚 玛 太 可 路 约 徒 罗 林前 林后 加 弗 腓 西 '
    '帖前 帖后 提前 提后 多 门 来 雅 彼前 彼后 约一 约二 约三 犹 启'.split(),
    key=len, reverse=True)

EN_BOOKS = sorted([
    'Genesis', 'Gen', 'Exodus', 'Exod', 'Ex', 'Leviticus', 'Lev', 'Numbers', 'Num',
    'Deuteronomy', 'Deut', 'Joshua', 'Josh', 'Judges', 'Judg', 'Ruth',
    '1 Samuel', '2 Samuel', '1 Sam', '2 Sam', '1 Kings', '2 Kings', '1 Kgs', '2 Kgs',
    '1 Chronicles', '2 Chronicles', '1 Chr', '2 Chr', 'Ezra', 'Nehemiah', 'Neh',
    'Esther', 'Esth', 'Job', 'Psalms', 'Psalm', 'Ps', 'Proverbs', 'Prov',
    'Ecclesiastes', 'Eccl', 'Song of Solomon', 'Song', 'Isaiah', 'Isa',
    'Jeremiah', 'Jer', 'Lamentations', 'Lam', 'Ezekiel', 'Ezek', 'Daniel', 'Dan',
    'Hosea', 'Hos', 'Joel', 'Amos', 'Obadiah', 'Obad', 'Jonah', 'Micah', 'Mic',
    'Nahum', 'Nah', 'Habakkuk', 'Hab', 'Zephaniah', 'Zeph', 'Haggai', 'Hag',
    'Zechariah', 'Zech', 'Malachi', 'Mal', 'Matthew', 'Matt', 'Mark', 'Luke',
    'John', 'Acts', 'Romans', 'Rom', '1 Corinthians', '2 Corinthians', '1 Cor', '2 Cor',
    'Galatians', 'Gal', 'Ephesians', 'Eph', 'Philippians', 'Phil', 'Colossians', 'Col',
    '1 Thessalonians', '2 Thessalonians', '1 Thess', '2 Thess', '1 Timothy', '2 Timothy',
    '1 Tim', '2 Tim', 'Titus', 'Philemon', 'Phlm', 'Hebrews', 'Heb', 'James', 'Jas',
    '1 Peter', '2 Peter', '1 Pet', '2 Pet', '1 John', '2 John', '3 John', 'Jude',
    'Revelation', 'Rev',
], key=len, reverse=True)

REF_RE = re.compile(r'\d+:\d+')
# What may sit between two references for the second to inherit the first's book.
LIST_GAP_RE = re.compile(r'[\s；;，,、\d\-–]*(?:(?:and|cf\.|see|和|及|与|参|见)[\s]*)?')
OPENS, CLOSES = '（(', '）)'


def _book_before(text, i, lang):
    """The book name ending right before text[i], or None."""
    if lang == 'zh':
        for a in ZH_ABBRS:
            if text.endswith(a, 0, i):
                return a
        return None
    for b in EN_BOOKS:
        start = i - len(b) - 1
        if start >= 0 and text[start:i] == b + ' ' and (start == 0 or not text[start - 1].isalnum()):
            return b
    return None


def add_book_to_refs(line, book_name, lang):
    if line.lstrip().startswith('## '):
        return line
    out, last, pos, depth, inherited, prev_end = [], 0, 0, 0, book_name, 0
    for m in REF_RE.finditer(line):
        i = m.start()
        for ch in line[pos:i]:
            if ch in OPENS:
                depth += 1
                inherited = book_name
            elif ch in CLOSES:
                depth = max(0, depth - 1)
                inherited = book_name
        pos = i
        gap_ok = LIST_GAP_RE.fullmatch(line[prev_end:i]) is not None
        prev_end = m.end()
        if i > 0 and (line[i - 1].isdigit() or line[i - 1] in ':–-'):
            continue
        named = _book_before(line, i, lang)
        if named:
            if depth:
                inherited = named
            continue
        prefix = inherited if (depth and gap_ok) else book_name
        out.append(line[last:i])
        out.append(prefix if lang == 'zh' else prefix + ' ')
        last = i
    out.append(line[last:])
    return ''.join(out)


def add_book_to_body(body, book_name, lang):
    return '\n'.join(add_book_to_refs(l, book_name, lang) for l in body.split('\n'))
