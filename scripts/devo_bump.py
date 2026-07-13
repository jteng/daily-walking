#!/usr/bin/env python3
"""
Bump the service-worker cache version (sw.js CACHE_NAME 'wwg-vN') and the app's
APP_SW_VERSION ('vN') in index.html so returning users pick up new plan content.

Usage: python scripts/devo_bump.py
"""
import re
from devo_lib import REPO_ROOT

SW = REPO_ROOT / 'sw.js'
INDEX = REPO_ROOT / 'index.html'


def bump_sw():
    s = SW.read_text(encoding='utf-8')
    m = re.search(r"CACHE_NAME = 'wwg-v(\d+)'", s)
    n = int(m.group(1)) + 1
    s = s[:m.start()] + f"CACHE_NAME = 'wwg-v{n}'" + s[m.end():]
    SW.write_text(s, encoding='utf-8')
    return n


def bump_index():
    s = INDEX.read_text(encoding='utf-8')
    m = re.search(r"APP_SW_VERSION = 'v(\d+)'", s)
    n = int(m.group(1)) + 1
    s = s[:m.start()] + f"APP_SW_VERSION = 'v{n}'" + s[m.end():]
    INDEX.write_text(s, encoding='utf-8')
    return n


if __name__ == '__main__':
    print(f"sw.js CACHE_NAME -> wwg-v{bump_sw()}")
    print(f"index.html APP_SW_VERSION -> v{bump_index()}")
