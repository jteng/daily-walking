#!/usr/bin/env python3
"""
Verify a candidate devotional entries file (or the whole overlay) against the XML.

Checks, per entry:
  1. verse_parts text matches canonical CUNP text for its reference.
  2. Every inline citation in `content` like (撒上15:22) resolves to a real verse,
     and — when the citation is immediately preceded by a 「...」 quote — the quoted
     text is a near-match to the canonical verse text (whitespace/punctuation-tolerant).

Usage:
  python scripts/devo_verify.py path/to/candidate.json
  python scripts/devo_verify.py            # verifies plans/devotional.json
Exit code 1 if any hard errors (unresolvable refs / verse_parts mismatch).
"""
import json
import re
import sys
from devo_lib import DEVO_PATH, text_for_ref, find_citations, verse_text, BOOK_ID_TO_NUMBER


def norm(s):
    return re.sub(r'[\s，。、；：！？「」『』（）()·,.!?;:"\'\-]', '', s or '')


def canonical_for_citation(c):
    texts = [verse_text(c['book'], c['chapter'], v) for v in c['verses']]
    texts = [t for t in texts if t]
    return ''.join(texts) if texts else None


# find a 「...」 quote ending right before position `start`
def preceding_quote(html, start):
    seg = html[:start]
    m = re.search(r'[「『]([^「」『』]{2,120})[」』]\s*$', seg)
    return m.group(1) if m else None


def verify_entry(e):
    errors, warns = [], []
    lbl = e.get('day_label', '?')
    # 1. verse_parts consistency
    ref = (e.get('verse') or '').strip()
    if ref and e.get('verse_parts'):
        txt, parts = text_for_ref(ref)
        if txt is None:
            errors.append(f'{lbl}: verse ref unresolvable: {ref!r}')
        else:
            got = ''.join(p['text'] for p in e['verse_parts'])
            if norm(got) != norm(txt):
                errors.append(f'{lbl}: verse_parts text != canonical for {ref!r}')
    # 2. inline citations
    html = e.get('content', '')
    for c in find_citations(html):
        canon = canonical_for_citation(c)
        if canon is None:
            errors.append(f'{lbl}: citation {c["raw"]} does not resolve to a verse')
            continue
        idx = html.find(c['raw'])
        q = preceding_quote(html, idx) if idx >= 0 else None
        if q:
            nq, nc = norm(q), norm(canon)
            # quote should be a substring-ish of canonical (allow partial quotes)
            if nq not in nc and nc not in nq:
                # allow small edit distance for partial quotations
                overlap = sum(1 for ch in nq if ch in nc)
                if overlap < 0.75 * len(nq):
                    warns.append(f'{lbl}: quote before {c["raw"]} may not match text\n'
                                 f'      quoted: {q}\n      canon : {canon}')
    return errors, warns


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else str(DEVO_PATH)
    data = json.load(open(path, encoding='utf-8'))
    entries = data['entries'] if isinstance(data, dict) and 'entries' in data else data
    all_err, all_warn = [], []
    for e in entries:
        er, wn = verify_entry(e)
        all_err += er; all_warn += wn
    print(f'Verified {len(entries)} entries. Errors: {len(all_err)}  Warnings: {len(all_warn)}')
    for e in all_err:
        print('  ERROR  ', e)
    for w in all_warn:
        print('  WARN   ', w)
    if all_err:
        sys.exit(1)


if __name__ == '__main__':
    main()
