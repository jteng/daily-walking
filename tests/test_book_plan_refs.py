"""Every book-prefixed verse reference in plans/books.json must exist.

A bare reference in a chapter (e.g. "（22:27）" meaning Psalm 22) gets the
chapter's own book added at build time, so it can silently point at a verse
that does not exist ("约22:27") and the app shows no tooltip.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from verse_refs import ZH_ABBR_LIST  # noqa: E402

# Verses missing from ChineseSimplifiedBible.xml; the references are correct.
KNOWN_ZH_GAPS = {'约7:53'}


@lru_cache(maxsize=None)
def verse_counts(xml_name):
    root = ET.parse(ROOT / xml_name).getroot()
    return {(int(b.get('number')), int(c.get('number'))): len(c.findall('verse'))
            for b in root.iter('book') for c in b.findall('chapter')}


def exists(counts, book, chapter, verse):
    n = counts.get((book, chapter))
    return n is not None and 1 <= verse <= n


def entries():
    return json.loads((ROOT / 'plans' / 'books.json').read_text(encoding='utf-8'))['entries']


def test_zh_references_exist():
    counts = verse_counts('ChineseSimplifiedBible.xml')
    num = {a: i + 1 for i, a in enumerate(ZH_ABBR_LIST)}
    abbrs = sorted(ZH_ABBR_LIST, key=len, reverse=True)
    pat = re.compile('(' + '|'.join(map(re.escape, abbrs)) + r')(\d+):(\d+)')
    bad = []
    for e in entries():
        for m in pat.finditer(e['content']):
            a, c, v = m.group(1), int(m.group(2)), int(m.group(3))
            if m.group(0) not in KNOWN_ZH_GAPS and not exists(counts, num[a], c, v):
                bad.append(f"{e.get('toc')}: {m.group(0)}")
    assert not bad, 'references to verses that do not exist:\n' + '\n'.join(bad)


def test_en_own_book_references_exist():
    # Build-time prefixes always use the chapter's own book, so checking those catches the bug.
    counts = verse_counts('EnglishESVBible.xml')
    books = {}
    for f in (ROOT / 'plans' / 'books').glob('*/book.json'):
        j = json.loads(f.read_text(encoding='utf-8'))
        books[j['name_en']] = j['number']
    names = sorted(books, key=len, reverse=True)
    pat = re.compile(r'(?<![A-Za-z0-9] )(' + '|'.join(map(re.escape, names)) + r') (\d+):(\d+)')
    bad = []
    for e in entries():
        for m in pat.finditer(e.get('content_en', '')):
            if not exists(counts, books[m.group(1)], int(m.group(2)), int(m.group(3))):
                bad.append(f"{e.get('toc_en')}: {m.group(0)}")
    assert not bad, 'references to verses that do not exist:\n' + '\n'.join(bad)
