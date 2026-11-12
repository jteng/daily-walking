#!/usr/bin/env python3
"""Build the Book Study plan (plans/books.json) from authored Markdown.

Layout:
    plans/books/<book>/book.json   {"number": 43, "name": "约翰福音",
                                    "name_en": "John", "abbr": "约"}
    plans/books/<book>/00.md       book introduction (optional)
    plans/books/<book>/NN.md       one file per chapter

Each .md file has a small front-matter block, then a Chinese body and an
English body:

    ---
    title: 太初有道
    title_en: In the Beginning Was the Word
    key: 1:1, 1:14
    ---
    ::zh
    ## 本章脉络
    paragraph text with **bold** and *italic*
    ::en
    ## The Shape of the Chapter
    ...

Body syntax (deliberately tiny): "## " heading -> section title, "> " lines
-> blockquote, "- " lines -> bullet list, anything else -> paragraph.
Blank lines separate blocks.

Same-book references written bare ("（3:3）") get the book name added at build
time (see verse_refs.py) so the app's verse tooltip recognizes them.

Key-verse text is filled in from ChineseSimplifiedBible.xml so the key-verse
card and memorize button work exactly as they do for the daily plans.

Run:  python scripts/build_book_plan.py
"""
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verse_refs import add_book_to_body  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BOOKS_DIR = ROOT / 'plans' / 'books'
OUT = ROOT / 'plans' / 'books.json'
XML = ROOT / 'ChineseSimplifiedBible.xml'

CN_DIGITS = '零一二三四五六七八九'


def to_chinese_number(n):
    """1 -> 一, 12 -> 十二, 21 -> 廿一, 30 -> 三十 (matches the app's parser)."""
    if n < 10:
        return CN_DIGITS[n]
    tens, ones = divmod(n, 10)
    if n < 20:
        head = '十'
    elif tens == 2:
        head = '廿'
    else:
        head = CN_DIGITS[tens] + '十'
    return head + (CN_DIGITS[ones] if ones else '')


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    return text


def md_to_html(src):
    out = []
    for block in re.split(r'\n\s*\n', src.strip()):
        lines = [l.rstrip() for l in block.strip().split('\n') if l.strip()]
        if not lines:
            continue
        if lines[0].startswith('## ') and len(lines) == 1:
            out.append(f'<div class="section-title">{inline(lines[0][3:].strip())}</div>')
        elif all(l.startswith('>') for l in lines):
            body = ' '.join(l.lstrip('>').strip() for l in lines)
            out.append(f'<blockquote>{inline(body)}</blockquote>')
        elif all(l.startswith('- ') for l in lines):
            items = ''.join(f'<li>{inline(l[2:].strip())}</li>' for l in lines)
            out.append(f'<ul>{items}</ul>')
        else:
            if lines[0].startswith('## '):
                out.append(f'<div class="section-title">{inline(lines[0][3:].strip())}</div>')
                lines = lines[1:]
            # A paragraph followed directly by "- " lines (no blank line
            # between) is a paragraph plus a list, not one long paragraph.
            para, items = [], []
            for l in lines:
                if l.startswith('- '):
                    if para:
                        out.append(f'<p>{inline(" ".join(para))}</p>')
                        para = []
                    items.append(f'<li>{inline(l[2:].strip())}</li>')
                else:
                    if items:
                        out.append(f'<ul>{"".join(items)}</ul>')
                        items = []
                    para.append(l)
            if para:
                out.append(f'<p>{inline(" ".join(para))}</p>')
            if items:
                out.append(f'<ul>{"".join(items)}</ul>')
    return '\n'.join(out)


def parse_md(path):
    text = path.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.S)
    if not m:
        raise ValueError(f'{path}: missing front matter')
    meta = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
    body = m.group(2)
    parts = re.split(r'^::(zh|en)\s*$', body, flags=re.M)
    bodies = {parts[i]: parts[i + 1] for i in range(1, len(parts) - 1, 2)}
    if 'zh' not in bodies:
        raise ValueError(f'{path}: missing ::zh body')
    return meta, bodies


class Bible:
    def __init__(self, path):
        self.root = ET.parse(path).getroot()

    def verses(self, book, chapter, start, end):
        b = self.root.find(f".//book[@number='{book}']")
        ch = b.find(f"chapter[@number='{chapter}']") if b is not None else None
        if ch is None:
            raise ValueError(f'chapter not found: {book} {chapter}')
        out = []
        for v in range(start, end + 1):
            el = ch.find(f"verse[@number='{v}']")
            if el is None or not el.text:
                raise ValueError(f'verse not found: {book} {chapter}:{v}')
            out.append(re.sub(r'\s+', '', el.text))
        return ''.join(out)


def key_parts(bible, book, key_field):
    parts = []
    for ref in [r.strip() for r in key_field.split(',') if r.strip()]:
        m = re.fullmatch(r'(\d+):(\d+)(?:-(\d+))?', ref)
        if not m:
            raise ValueError(f'bad key ref {ref!r}')
        c, s = int(m.group(1)), int(m.group(2))
        e = int(m.group(3)) if m.group(3) else s
        rng = f'{c}:{s}' + (f'-{e}' if e != s else '')
        parts.append({
            'reference': f"{book['name']} {rng}",
            'reference_en': f"{book['name_en']} {rng}",
            'text': bible.verses(book['number'], c, s, e),
        })
    return parts


def build_book(bible, book_dir):
    book = json.loads((book_dir / 'book.json').read_text(encoding='utf-8'))
    files = sorted(p for p in book_dir.glob('*.md'))
    chapter_files = [p for p in files if p.stem != '00']
    total = book.get('chapters', len(chapter_files))
    entries = []
    for path in files:
        meta, bodies = parse_md(path)
        n = int(path.stem)
        if n == 0:
            scripture, scripture_en = f"{book['abbr']}一章", f"{book['name_en']} 1"
            label, label_en = f"{book['name']} · 导读", f"{book['name_en']} · Introduction"
            toc, toc_en = f"{book['name']} 导读", f"{book['name_en']}: Introduction"
        else:
            scripture = f"{book['abbr']}{to_chinese_number(n)}章"
            scripture_en = f"{book['name_en']} {n}"
            label = f"{book['name']} · 第 {n} / {total} 章"
            label_en = f"{book['name_en']} · Chapter {n} of {total}"
            toc, toc_en = f"{book['name']} {n} 章", f"{book['name_en']} {n}"
        parts = key_parts(bible, book, meta['key']) if meta.get('key') else []
        entry = {
            'book': book['number'],
            'chapter': n,
            'day_label': label,
            'day_label_en': label_en,
            'toc': toc,
            'toc_en': toc_en,
            'title': meta['title'],
            'title_en': meta.get('title_en', ''),
            'scripture': scripture,
            'scripture_en': scripture_en,
            'verse': '，'.join(p['reference'] for p in parts),
            'verse_en': '; '.join(p['reference_en'] for p in parts),
            'verse_parts': [{'reference': p['reference'], 'text': p['text']} for p in parts],
            'verse_text': ''.join(p['text'] for p in parts),
            'content': md_to_html(add_book_to_body(bodies['zh'], book['abbr'], 'zh')),
        }
        if 'en' in bodies:
            entry['content_en'] = md_to_html(add_book_to_body(bodies['en'], book['name_en'], 'en'))
        entries.append(entry)
    return book, entries


def main():
    bible = Bible(XML)
    all_entries, books = [], []
    dirs = [d for d in BOOKS_DIR.iterdir() if (d / 'book.json').exists()]
    built = [build_book(bible, d) for d in dirs]
    built.sort(key=lambda be: be[0]['number'])
    for book, entries in built:
        books.append({'number': book['number'], 'name': book['name'],
                      'name_en': book['name_en'], 'entries': len(entries)})
        all_entries.extend(entries)
    out = {
        'id': 'books',
        'name': '逐卷研读版',
        'name_en': 'Book Study Edition',
        'books': books,
        'entries': all_entries,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'wrote {OUT.relative_to(ROOT)}: {len(books)} book(s), {len(all_entries)} entries')


if __name__ == '__main__':
    sys.exit(main())
