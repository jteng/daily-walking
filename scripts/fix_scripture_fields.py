#!/usr/bin/env python3
"""
Normalize 'scripture' fields in bibleData.json.
Ensures all scripture references start with a book abbreviation.
If a book name is missing (e.g., "七至九章"), it infers it from the 'verse' field or context.
"""

import json
import re
from pathlib import Path

# Valid book abbreviations (Single char or distinct start)
BOOK_ABBRS = [
    '创', '出', '利', '民', '申', '书', '士', '得', '撒上', '撒下',
    '王上', '王下', '代上', '代下', '拉', '尼', '斯', '伯', '诗', '箴',
    '传', '歌', '赛', '耶', '哀', '结', '但', '何', '珥', '摩',
    '俄', '拿', '弥', '鸿', '哈', '番', '该', '亚', '玛',
    '太', '可', '路', '约', '徒', '罗', '林前', '林后', '加', '弗',
    '腓', '西', '帖前', '帖后', '提前', '提后', '多', '门', '来', '雅',
    '彼前', '彼后', '约一', '约二', '约三', '犹', '启'
]

# Map full book names to abbreviations
FULL_TO_ABBR = {
    '创世记': '创', '出埃及记': '出', '利未记': '利', '民数记': '民', '申命记': '申',
    '约书亚记': '书', '士师记': '士', '路得记': '得', '撒母耳记上': '撒上', '撒母耳记下': '撒下',
    '列王纪上': '王上', '列王纪下': '王下', '历代志上': '代上', '历代志下': '代下',
    '以斯拉记': '拉', '尼希米记': '尼', '以斯帖记': '斯', '约伯记': '伯', '诗篇': '诗', '箴言': '箴',
    '传道书': '传', '雅歌': '歌', '以赛亚书': '赛', '耶利米书': '耶', '耶利米哀歌': '哀',
    '以西结书': '结', '但以理书': '但', '何西阿书': '何', '约珥书': '珥', '阿摩司书': '摩',
    '俄巴底亚书': '俄', '约拿书': '拿', '弥迦书': '弥', '那鸿书': '鸿', '哈巴谷书': '哈',
    '西番亚书': '番', '哈该书': '该', '撒迦利亚书': '亚', '玛拉基书': '玛',
    '马太福音': '太', '马可福音': '可', '路加福音': '路', '约翰福音': '约', '使徒行传': '徒',
    '罗马书': '罗', '哥林多前书': '林前', '哥林多后书': '林后', '加拉太书': '加', '以弗所书': '弗',
    '腓立比书': '腓', '歌罗西书': '西', '帖撒罗尼迦前书': '帖前', '帖撒罗尼迦后书': '帖后',
    '提摩太前书': '提前', '提摩太后书': '提后', '提多书': '多', '腓利门书': '门', '希伯来书': '来',
    '雅各书': '雅', '彼得前书': '彼前', '彼得后书': '彼后', '约翰一书': '约一', '约翰二书': '约二',
    '约翰三书': '约三', '约翰壹书': '约一', '约翰贰书': '约二', '约翰叁书': '约三', '犹大书': '犹', '启示录': '启'
}

def get_book_from_verse(verse_text):
    """Extract book abbreviation from verse text (e.g., '阿摩司书八章十一节' -> '摩')."""
    if not verse_text:
        return None
    for full, abbr in FULL_TO_ABBR.items():
        if verse_text.startswith(full):
            return abbr
    # Try finding abbreviation directly if it matches significantly? 
    # Usually verse field starts with Full Name.
    return None

def normalize_scripture(data):
    """Normalize scripture fields."""
    count = 0
    last_book = None
    
    for i, entry in enumerate(data):
        scripture = entry.get('scripture', '').strip()
        if not scripture:
            continue
            
        # Check if scripture starts with a valid book abbreviation
        # We sort BOOK_ABBRS by length descending to match longest first (e.g., 撒上 before 撒)
        sorted_abbrs = sorted(BOOK_ABBRS, key=len, reverse=True)
        
        has_book = False
        for abbr in sorted_abbrs:
            if scripture.startswith(abbr):
                has_book = True
                last_book = abbr
                break
        
        if not has_book:
            # Try to infer from verse field
            verse = entry.get('verse', '').strip()
            inferred_book = get_book_from_verse(verse)
            
            if inferred_book:
                print(f"Entry {i}: '{scripture}' -> '{inferred_book}{scripture}' (inferred from verse '{verse}')")
                entry['scripture'] = f"{inferred_book}{scripture}"
                last_book = inferred_book
                count += 1
            elif last_book:
                 # Fallback to last book if reasonable? 
                 # Risk: Might be wrong if context changed.
                 # But 'Seven to Nine Chapters' without book implies continuation.
                 # Let's verify with context if possible, but for now simple inference.
                 print(f"Entry {i}: '{scripture}' -> '{last_book}{scripture}' (inferred from previous '{last_book}')")
                 entry['scripture'] = f"{last_book}{scripture}"
                 count += 1
            else:
                 print(f"Warning: Entry {i} '{scripture}' has no book and cannot infer.")

    return count

def main():
    json_path = Path('bibleData.json')
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
        
    print(f"Loading {json_path}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    fixed_count = normalize_scripture(data)
    
    if fixed_count > 0:
        print(f"Saving {fixed_count} fixes to {json_path}...")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Done.")
    else:
        print("No changes needed.")

if __name__ == '__main__':
    main()
