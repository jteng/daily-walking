"""List 「」 quotations in the ::zh body of Book Study files that are not verbatim CUV.

Usage: python3 scripts/check_cuv_quotes.py plans/books/1corinthians/07.md ...
Hits are either real misquotes (fix them) or deliberate non-Scripture phrases
(glosses, slogans, prayers) that may stay. Text in 『』 and ellipses is split
and each fragment of 4+ characters is checked.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tree = ET.parse(ROOT / 'ChineseSimplifiedBible.xml').getroot()
cuv = ''.join(re.sub(r'\s', '', v.text or '') for v in tree.iter('verse'))

for f in sys.argv[1:]:
    zh = open(f, encoding='utf-8').read().split('::en')[0]
    for q in re.findall(r'「([^「」]*)」', zh):
        q2 = re.sub(r'\s', '', q).replace('『', '…').replace('』', '…')
        for part in re.split(r'……|…', q2):
            part = part.strip('。，；！？：')
            if len(part) >= 4 and part not in cuv:
                print(Path(f).name, 'NOT FOUND:', q)
                break
