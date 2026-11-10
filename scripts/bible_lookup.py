"""Print CUV and ESV text for verses, to quote accurately while drafting.

Usage: python3 scripts/bible_lookup.py 46:13:4,5,6 43:3:16
       (book number : chapter : comma-separated verses; book numbers 1-66)
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZH = ET.parse(ROOT / 'ChineseSimplifiedBible.xml').getroot()
EN = ET.parse(ROOT / 'EnglishESVBible.xml').getroot()


def verse(root, b, c, v, strip):
    bk = root.find(f".//book[@number='{b}']")
    ch = bk.find(f"chapter[@number='{c}']") if bk is not None else None
    e = ch.find(f"verse[@number='{v}']") if ch is not None else None
    if e is None or not e.text:
        return '—'
    return re.sub(r'\s+', '', e.text) if strip else e.text.strip()


for arg in sys.argv[1:]:
    b, c, vs = arg.split(':')
    for v in vs.split(','):
        print(f"{b}:{c}:{v} {verse(ZH, b, c, v, True)} | {verse(EN, b, c, v, False)}")
