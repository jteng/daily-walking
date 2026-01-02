#!/usr/bin/env python3
"""
Extract verse text from ChineseSimplifiedBible.xml and add to bibleData.json
This version is self-contained and does not depend on add_verse_text.py.
"""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

# Book number to name mapping (for the new XML format)
BOOK_NUMBER_MAP = {
    # Old Testament (1-39)
    1: 'GEN', 2: 'EXO', 3: 'LEV', 4: 'NUM', 5: 'DEU',
    6: 'JOS', 7: 'JDG', 8: 'RUT', 9: '1SA', 10: '2SA',
    11: '1KI', 12: '2KI', 13: '1CH', 14: '2CH', 15: 'EZR',
    16: 'NEH', 17: 'EST', 18: 'JOB', 19: 'PSA', 20: 'PRO',
    21: 'ECC', 22: 'SNG', 23: 'ISA', 24: 'JER', 25: 'LAM',
    26: 'EZK', 27: 'DAN', 28: 'HOS', 29: 'JOL', 30: 'AMO',
    31: 'OBA', 32: 'JON', 33: 'MIC', 34: 'NAM', 35: 'HAB',
    36: 'ZEP', 37: 'HAG', 38: 'ZEC', 39: 'MAL',
    # New Testament (40-66)
    40: 'MAT', 41: 'MRK', 42: 'LUK', 43: 'JHN', 44: 'ACT',
    45: 'ROM', 46: '1CO', 47: '2CO', 48: 'GAL', 49: 'EPH',
    50: 'PHP', 51: 'COL', 52: '1TH', 53: '2TH', 54: '1TI',
    55: '2TI', 56: 'TIT', 57: 'PHM', 58: 'HEB', 59: 'JAS',
    60: '1PE', 61: '2PE', 62: '1JN', 63: '2JN', 64: '3JN',
    65: 'JUD', 66: 'REV'
}

# Reverse mapping: USFX ID to book number
BOOK_ID_TO_NUMBER = {v: k for k, v in BOOK_NUMBER_MAP.items()}

# Common Chinese book abbreviations/names to ID mapping
CHINESE_BOOK_MAP = {
    '创世记': 'GEN', '创': 'GEN',
    '出埃及记': 'EXO', '出': 'EXO',
    '利未记': 'LEV', '利': 'LEV',
    '民数记': 'NUM', '民': 'NUM', '民数': 'NUM',
    '申命记': 'DEU', '申': 'DEU',
    '约书亚记': 'JOS', '书': 'JOS', '约书亚': 'JOS',
    '士师记': 'JDG', '士': 'JDG',
    '路特记': 'RUT', '路': 'RUT', '路特': 'RUT',
    '撒母耳记上': '1SA', '撒上': '1SA', '撒母耳上': '1SA',
    '撒母耳记下': '2SA', '撒下': '2SA', '撒母耳下': '2SA',
    '列王纪上': '1KI', '王上': '1KI', '列王上': '1KI',
    '列王纪下': '2KI', '王下': '2KI', '列王下': '2KI',
    '历代志上': '1CH', '代上': '1CH', '历代上': '1CH',
    '历代志下': '2CH', '代下': '2CH', '历代下': '2CH',
    '以斯拉记': 'EZR', '拉': 'EZR', '以斯拉': 'EZR',
    '尼希米记': 'NEH', '尼': 'NEH', '尼希米': 'NEH',
    '以斯帖记': 'EST', '斯': 'EST', '以斯帖': 'EST',
    '约伯记': 'JOB', '伯': 'JOB',
    '诗篇': 'PSA', '诗': 'PSA',
    '箴言': 'PRO', '箴': 'PRO',
    '传道书': 'ECC', '传': 'ECC',
    '雅歌': 'SNG', '歌': 'SNG',
    '以赛亚书': 'ISA', '赛': 'ISA', '以赛亚': 'ISA',
    '耶利米书': 'JER', '耶': 'JER', '耶利米': 'JER',
    '耶利米哀歌': 'LAM', '哀': 'LAM',
    '以西结书': 'EZK', '结': 'EZK', '以西结': 'EZK',
    '但以理书': 'DAN', '但': 'DAN', '但以理': 'DAN',
    '何西阿书': 'HOS', '何': 'HOS', '何西阿': 'HOS',
    '约珥书': 'JOL', '珥': 'JOL', '约珥': 'JOL',
    '阿摩司书': 'AMO', '摩': 'AMO', '阿摩司': 'AMO',
    '俄巴底亚书': 'OBA', '俄': 'OBA', '俄巴底亚': 'OBA',
    '约拿书': 'JON', '拿': 'JON', '约拿': 'JON',
    '弥迦书': 'MIC', '弥': 'MIC', '弥迦': 'MIC',
    '那鸿书': 'NAM', '鴻': 'NAM', '那鸿': 'NAM',
    '哈巴谷书': 'HAB', '哈': 'HAB', '哈巴谷': 'HAB',
    '西番雅书': 'ZEP', '番': 'ZEP', '西番雅': 'ZEP',
    '哈该书': 'HAG', '该': 'HAG', '哈该': 'HAG',
    '撒迦利亚书': 'ZEC', '亚': 'ZEC', '撒迦利亚': 'ZEC',
    '玛拉基书': 'MAL', '玛': 'MAL', '玛拉基': 'MAL',
    '马太福音': 'MAT', '太': 'MAT', '马太': 'MAT',
    '马可福音': 'MRK', '可': 'MRK', '马可': 'MRK',
    '路加福音': 'LUK', '路': 'LUK', '路加': 'LUK',
    '约翰福音': 'JHN', '约': 'JHN', '约翰': 'JHN',
    '使徒行传': 'ACT', '徒': 'ACT',
    '罗马书': 'ROM', '罗': 'ROM',
    '哥林多前书': '1CO', '林前': '1CO',
    '哥林多后书': '2CO', '林后': '2CO',
    '加拉太书': 'GAL', '加': 'GAL',
    '以弗所书': 'EPH', '弗': 'EPH',
    '腓立比书': 'PHP', '腓': 'PHP',
    '歌罗西书': 'COL', '西': 'COL',
    '帖撒罗尼迦前书': '1TH', '帖前': '1TH',
    '帖撒罗尼迦后书': '2TH', '帖后': '2TH',
    '提摩太前书': '1TI', '提前': '1TI', '提摩太前': '1TI',
    '提摩太后书': '2TI', '提后': '2TI', '提摩太后': '2TI',
    '提多书': 'TIT', '多': 'TIT', '提多': 'TIT',
    '腓利门书': 'PHM', '门': 'PHM', '腓利门': 'PHM',
    '希伯来书': 'HEB', '来': 'HEB', '希伯来': 'HEB',
    '雅各书': 'JAS', '雅': 'JAS',
    '彼得前书': '1PE', '彼前': '1PE',
    '彼得后书': '2PE', '彼后': '2PE',
    '约翰一书': '1JN', '约一': '1JN',
    '约翰二书': '2JN', '约二': '2JN',
    '约翰三书': '3JN', '约三': '3JN',
    '犹大书': 'JUD', '犹': 'JUD', '犹大': 'JUD',
    '启示录': 'REV', '启': 'REV',
}


# Canonical Chinese Book Names for Display
CODE_TO_CHINESE_MAP = {
    'GEN': '创世记', 'EXO': '出埃及记', 'LEV': '利未记', 'NUM': '民数记', 'DEU': '申命记',
    'JOS': '约书亚记', 'JDG': '士师记', 'RUT': '路得记', '1SA': '撒母耳记上', '2SA': '撒母耳记下',
    '1KI': '列王纪上', '2KI': '列王纪下', '1CH': '历代志上', '2CH': '历代志下', 'EZR': '以斯拉记',
    'NEH': '尼希米记', 'EST': '以斯帖记', 'JOB': '约伯记', 'PSA': '诗篇', 'PRO': '箴言',
    'ECC': '传道书', 'SNG': '雅歌', 'ISA': '以赛亚书', 'JER': '耶利米书', 'LAM': '耶利米哀歌',
    'EZK': '以西结书', 'DAN': '但以理书', 'HOS': '何西阿书', 'JOL': '约珥书', 'AMO': '阿摩司书',
    'OBA': '俄巴底亚书', 'JON': '约拿书', 'MIC': '弥迦书', 'NAM': '那鸿书', 'HAB': '哈巴谷书',
    'ZEP': '西番雅书', 'HAG': '哈该书', 'ZEC': '撒迦利亚书', 'MAL': '玛拉基书',
    'MAT': '马太福音', 'MRK': '马可福音', 'LUK': '路加福音', 'JHN': '约翰福音', 'ACT': '使徒行传',
    'ROM': '罗马书', '1CO': '哥林多前书', '2CO': '哥林多后书', 'GAL': '加拉太书', 'EPH': '以弗所书',
    'PHP': '腓立比书', 'COL': '歌罗西书', '1TH': '帖撒罗尼迦前书', '2TH': '帖撒罗尼迦后书',
    '1TI': '提摩太前书', '2TI': '提摩太后书', 'TIT': '提多书', 'PHM': '腓利门书', 'HEB': '希伯来书',
    'JAS': '雅各书', '1PE': '彼得前书', '2PE': '彼得后书', '1JN': '约翰一书', '2JN': '约翰二书',
    '3JN': '约翰三书', 'JUD': '犹大书', 'REV': '启示录'
}


def parse_chinese_number(chn_num_str):
    """Convert Chinese number string to integer."""
    if not chn_num_str:
        return 0
    if chn_num_str.isdigit():
        return int(chn_num_str)
        
    chn_map = {
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
        '百': 100, '千': 1000,
        '廿': 20, '卅': 30  # Common in Chinese Bible references
    }
    
    result = 0
    temp = 0
    
    # Handle special single chars directly
    if len(chn_num_str) == 1 and chn_num_str in chn_map:
        return chn_map[chn_num_str]

    for char in chn_num_str:
        val = chn_map.get(char)
        if val is None:
            continue
            
        if val >= 10:
            if val == 20 or val == 30: # Handle 廿, 卅 acting like 20, 30
                 if temp == 0:
                     result += val
                 else:
                     result += temp + val # e.g. unlikely usage
                     temp = 0
            elif temp == 0:
                temp = 1 # for '十' at start
                result += temp * val
                temp = 0
            else:
                result += temp * val
                temp = 0
        else:
            temp = val
            
    result += temp
    return result


def parse_verse_reference(ref_str):
    """
    Parse a verse reference string like "创世记一章1节" or "创世记十五章六节，十七章一节" into components.
    Returns a LIST of dicts: [{'book': 'GEN', 'chapter': 1, 'verses': [1]}, ...]
    """
    if not ref_str:
        return []
        
    ref_str = ref_str.strip()
    results = []
    
    # 1. Identify Initial Book
    # We strip the book name from the start, but remember it for context
    current_book = None
    book_len = 0
    
    for name, code in CHINESE_BOOK_MAP.items():
        if ref_str.startswith(name):
            if len(name) > book_len:
                book_len = len(name)
                current_book = code
                
    if not current_book:
        print(f"Warning: Could not parse book from '{ref_str}'")
        return []
        
    # Content after book name
    remaining = ref_str[book_len:].strip()
    
    # 2. Split into segments by separators (comma, semicolon, etc.)
    # We want to split by commonly used separators: ， , ； ; 、
    # Note: '、' is often used for verses within same chapter (1, 3), but logic handles it fine if we treat as segment
    segments = re.split(r'[,，;；、]', remaining)
    
    current_chapter = None
    
    for segment in segments:
        segment = segment.strip()
        if not segment: continue
        
        # Check for Book change (rare in this dataset, but possible)
        # (Skipping book change check for now as usually it's one book per entry, 
        #  but if needed we'd check if segment starts with a book name)
        
        # Check for Chapter change
        # Look for "章" or "篇" - include 廿 and 卅 for numbers like 廿六 (26)
        chapter_match = re.search(r'([零一二三四五六七八九十百廿卅\d]+)[章篇]', segment)
        
        verses_to_parse = segment
        
        if chapter_match:
            # Found a new chapter
            chapter_str = chapter_match.group(1)
            current_chapter = parse_chinese_number(chapter_str)
            # Verses are after the chapter marker
            verses_to_parse = segment[chapter_match.end():]
        elif current_chapter is None:
            # No chapter found yet and no current chapter context
            print(f"Warning: No chapter found in segment '{segment}' and no context")
            continue
            
        # Parse Verses in this segment
        # Format: "1节", "1-3节", "1至3"
        clean_verses_str = re.sub(r'[节\s]', '', verses_to_parse)
        
        if not clean_verses_str:
            continue
            
        parsed_verses = []
        
        # Ranges: "1-3" or "1至3"
        if '-' in clean_verses_str or '至' in clean_verses_str:
            separator = '-' if '-' in clean_verses_str else '至'
            parts = clean_verses_str.split(separator, 1)
            if len(parts) == 2 and parts[0] and parts[1]:
                start = parse_chinese_number(parts[0])
                end = parse_chinese_number(parts[1])
                parsed_verses.extend(range(start, end + 1))
        else:
            # Single verse
            val = parse_chinese_number(clean_verses_str)
            if val > 0:
                parsed_verses.append(val)
                
        if parsed_verses:
            results.append({
                'book': current_book,
                'chapter': current_chapter,
                'verses': parsed_verses
            })
            
    return results


def format_verse_reference(book_id, chapter, verses):
    """Format reference standardized like '创世记 1:1-3'"""
    # Use Chinese name if available, else Capitalized ID
    book_name = CODE_TO_CHINESE_MAP.get(book_id, book_id.capitalize())
    
    verses_str = ""
    # Simplified logic: if continuous, use range
    if not verses:
        return f"{book_name} {chapter}"
        
    # Group into ranges
    result_verses = []
    if not verses:
        pass
    else:
        # Simple range compression
        start = verses[0]
        prev = verses[0]
        
        for v in verses[1:]:
            if v == prev + 1:
                prev = v
            else:
                if start == prev:
                    result_verses.append(str(start))
                else:
                    result_verses.append(f"{start}-{prev}")
                start = v
                prev = v
        # Add last
        if start == prev:
            result_verses.append(str(start))
        else:
            result_verses.append(f"{start}-{prev}")
            
    verses_str = ",".join(result_verses)
    
    return f"{book_name} {chapter}:{verses_str}"


def extract_verses_from_simplified_xml(xml_path, book_id, chapter, verses):
    """Extract verse text from ChineseSimplifiedBible.xml file."""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Convert book ID to book number
        book_number = BOOK_ID_TO_NUMBER.get(book_id)
        if book_number is None:
            print(f"Warning: Book ID {book_id} not found in mapping")
            return None
        
        # Find the book by number attribute
        book = root.find(f".//book[@number='{book_number}']")
        if book is None:
            print(f"Warning: Book number {book_number} not found in XML")
            return None
        
        # Find the chapter
        chapter_elem = book.find(f".//chapter[@number='{chapter}']")
        if chapter_elem is None:
            print(f"Warning: Chapter {chapter} not found in book {book_number}")
            return None
        
        # Collect verse texts
        verse_texts = []
        for verse_num in verses:
            verse_elem = chapter_elem.find(f".//verse[@number='{verse_num}']")
            if verse_elem is not None and verse_elem.text:
                verse_texts.append(verse_elem.text.strip())
        
        return ''.join(verse_texts) if verse_texts else None
        
    except Exception as e:
        print(f"Error extracting verses: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    """Main function to add verse text to bibleData.json"""
    xml_path = Path('ChineseSimplifiedBible.xml')
    json_path = Path('bibleData.json')
    
    if not xml_path.exists():
        print(f"Error: {xml_path} not found")
        return
    
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
    
    # Load JSON data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Processing {len(data)} entries...")
    
    # Process each entry
    success_count = 0
    for i, entry in enumerate(data):
        verse_ref = entry.get('verse', '').strip()
        
        if not verse_ref:
            continue
        
        # Parse reference (returns a list)
        parsed_list = parse_verse_reference(verse_ref)
        if not parsed_list:
            continue
        
        # Extract verse text from all references
        all_verse_texts = []
        verse_parts = []
        
        for parsed in parsed_list:
            verse_text = extract_verses_from_simplified_xml(
                xml_path,
                parsed['book'],
                parsed['chapter'],
                parsed['verses']
            )
            if verse_text:
                all_verse_texts.append(verse_text)
                # Generate individual reference for this part
                individual_ref = format_verse_reference(
                    parsed['book'],
                    parsed['chapter'],
                    parsed['verses']
                )
                verse_parts.append({
                    'reference': individual_ref,
                    'text': verse_text
                })
        
        # Store the results
        if all_verse_texts:
            entry['verse_text'] = ''.join(all_verse_texts)
            # Store them separately for proper display with standardized references
            if len(verse_parts) > 0:
                entry['verse_parts'] = verse_parts
            success_count += 1
            print(f"✓ [{i+1}/{len(data)}] {entry['day_label']}: {verse_ref[:40]}...")
        else:
            print(f"✗ [{i+1}/{len(data)}] {entry['day_label']}: Failed to extract")
    
    # Save updated JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDone! Successfully added verse text to {success_count}/{len(data)} entries")


if __name__ == '__main__':
    main()
