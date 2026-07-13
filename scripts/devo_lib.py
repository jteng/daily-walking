#!/usr/bin/env python3
"""
Reusable library for the self-authored devotional overlay plan (plans/devotional.json).

Provides:
- A fast in-memory index of ChineseSimplifiedBible.xml (loaded once).
- Chinese verse-reference parsing (reused from add_verse_text_v2).
- Canonical verse-text lookup + verse_parts population for candidate entries.

All paths are resolved relative to the repo root so the module works from anywhere.
"""

import re
import xml.etree.ElementTree as ET
from pathlib import Path

# Reuse the (large, well-tested) maps + reference parser from the existing pipeline.
from add_verse_text_v2 import (  # noqa: E402
    BOOK_ID_TO_NUMBER,
    CODE_TO_CHINESE_MAP,
    CHINESE_BOOK_MAP,
    parse_verse_reference,
    parse_chinese_number,
    format_verse_reference,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
XML_PATH = REPO_ROOT / 'ChineseSimplifiedBible.xml'
DEVO_PATH = REPO_ROOT / 'plans' / 'devotional.json'
BASE_PATH = REPO_ROOT / 'bibleData.json'

# Patch known gaps/typos in the imported book map so references resolve correctly.
# The upstream map only had the typo '路特记' for Ruth and left bare '路' pointing to
# Luke; add the correct full names (longest-match wins in parse_verse_reference).
CHINESE_BOOK_MAP.setdefault('路得记', 'RUT')
CHINESE_BOOK_MAP.setdefault('路得', 'RUT')

_VERSE_INDEX = None  # {(book_number, chapter, verse): text}
_BASE_WD = None      # {(week, day): base_entry}


def _base_by_week_day():
    """Index the base plan by (week, day) so overlay entries can inherit day_label."""
    global _BASE_WD
    if _BASE_WD is not None:
        return _BASE_WD
    import json
    base = json.load(open(BASE_PATH, encoding='utf-8'))
    _BASE_WD = {(e.get('week'), e.get('day')): e for e in base}
    return _BASE_WD


def base_day_label(week, day):
    """Return the base plan's day_label for a (week, day), or None."""
    e = _base_by_week_day().get((week, day))
    return e.get('day_label') if e else None


def fill_day_labels(entries):
    """Ensure every entry has the correct day_label from the base plan. Returns list
    of (week, day) that could not be resolved."""
    missing = []
    for e in entries:
        if e.get('day_label'):
            continue
        lbl = base_day_label(e.get('week'), e.get('day'))
        if lbl:
            e['day_label'] = lbl
        else:
            missing.append((e.get('week'), e.get('day')))
    return missing


def _build_index():
    global _VERSE_INDEX
    if _VERSE_INDEX is not None:
        return _VERSE_INDEX
    idx = {}
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
    for book in root.iter('book'):
        bnum = int(book.get('number'))
        for chap in book.iter('chapter'):
            cnum = int(chap.get('number'))
            for verse in chap.iter('verse'):
                vnum = int(verse.get('number'))
                txt = (verse.text or '').strip()
                idx[(bnum, cnum, vnum)] = txt
    _VERSE_INDEX = idx
    return idx


def verse_text(book_code, chapter, verse):
    """Return canonical text for a single verse, or None."""
    idx = _build_index()
    bnum = BOOK_ID_TO_NUMBER.get(book_code)
    if bnum is None:
        return None
    return idx.get((bnum, chapter, verse))


def text_for_ref(ref_str):
    """
    Given a Chinese reference like '撒母耳记上十五章廿二节' (or with ranges/commas),
    return (joined_text, verse_parts) where verse_parts is a list of
    {'reference': '撒母耳记上 15:22', 'text': '...'}. Returns (None, []) on failure.
    """
    parsed = parse_verse_reference(ref_str)
    if not parsed:
        return None, []
    all_text = []
    parts = []
    for p in parsed:
        texts = [verse_text(p['book'], p['chapter'], v) for v in p['verses']]
        texts = [t for t in texts if t]
        if not texts:
            return None, []
        joined = ''.join(texts)
        all_text.append(joined)
        parts.append({
            'reference': format_verse_reference(p['book'], p['chapter'], p['verses']),
            'text': joined,
        })
    return ''.join(all_text), parts


# ---- Inline-quote verification helpers -------------------------------------

# Matches an inline citation that follows a Chinese quote, e.g. "(撒上15:22)" or
# "（撒母耳记上 15:22）" or "(腓2:8)". Group 1 = book token, 2 = chapter, 3 = verse(s).
_CITE_RE = re.compile(
    r'[（(]\s*([一-鿿]{1,6}?)\s*'          # book name/abbrev
    r'([0-9零一二三四五六七八九十百廿卅]+)'          # chapter
    r'[:：章]\s*'
    r'([0-9零一二三四五六七八九十百廿卅]+(?:[-至~][0-9零一二三四五六七八九十百廿卅]+)?)'  # verse or range
    r'\s*[节]?\s*[）)]'
)


def resolve_book_token(token):
    """Resolve a possibly-abbreviated Chinese book token to a book code."""
    if token in CHINESE_BOOK_MAP:
        return CHINESE_BOOK_MAP[token]
    # try progressively shorter/longer matches
    for name, code in CHINESE_BOOK_MAP.items():
        if token == name:
            return code
    for name, code in sorted(CHINESE_BOOK_MAP.items(), key=lambda x: -len(x[0])):
        if token.startswith(name) or name.startswith(token):
            return code
    return None


def find_citations(html):
    """Return list of dicts {raw, book, chapter, verses:[..]} for inline citations."""
    out = []
    for m in _CITE_RE.finditer(html):
        book_tok, chap_tok, verse_tok = m.group(1), m.group(2), m.group(3)
        code = resolve_book_token(book_tok)
        if not code:
            continue
        chapter = parse_chinese_number(chap_tok)
        # verse range
        vs = re.split(r'[-至~]', verse_tok)
        try:
            if len(vs) == 2:
                verses = list(range(parse_chinese_number(vs[0]), parse_chinese_number(vs[1]) + 1))
            else:
                verses = [parse_chinese_number(verse_tok)]
        except Exception:
            continue
        out.append({'raw': m.group(0), 'book_token': book_tok,
                    'book': code, 'chapter': chapter, 'verses': verses})
    return out


if __name__ == '__main__':
    # quick self-test
    t, parts = text_for_ref('撒母耳记上十五章廿二节')
    print('lookup ok:', bool(t))
    print(parts)
