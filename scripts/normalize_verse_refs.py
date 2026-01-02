#!/usr/bin/env python3
"""
Normalize Bible verse references in bibleData.json from Chinese numbers to Arabic.
Only normalizes references with explicit book names to avoid ambiguity.
Converts: 诗一零二 25 → 诗102:25
Skips: （六 7-8） - ambiguous, needs context
"""

import json
import re
from pathlib import Path

# List of valid book abbreviations
BOOK_NAMES = [
    '创', '出', '利', '民', '申', '书', '士', '得', '撒上', '撒下',
    '王上', '王下', '代上', '代下', '拉', '尼', '斯', '伯', '诗', '箴',
    '传', '歌', '赛', '耶', '哀', '结', '但', '何', '珥', '摩',
    '俄', '拿', '弥', '鸿', '哈', '番', '该', '亚', '玛',
    '太', '可', '路', '约', '徒', '罗', '林前', '林后', '加', '弗',
    '腓', '西', '帖前', '帖后', '提前', '提后', '多', '门', '来', '雅',
    '彼前', '彼后', '约一', '约二', '约三', '犹', '启'
]

def chinese_to_arabic(chinese_num):
    """Convert Chinese numbers to Arabic numerals."""
    char_map = {
        '零': '0', '一': '1', '二': '2', '三': '3', '四': '4',
        '五': '5', '六': '6', '七': '7', '八': '8', '九': '9',
        '十': '10', '廿': '20', '卅': '30'
    }
    
    # Simple single character
    if chinese_num in char_map:
        return char_map[chinese_num]
    
    # Handle 廿六 (26), 卅三 (33)
    if chinese_num.startswith('廿') and len(chinese_num) > 1:
        digit = char_map.get(chinese_num[1], '0')
        return str(20 + int(digit))
    
    if chinese_num.startswith('卅') and len(chinese_num) > 1:
        digit = char_map.get(chinese_num[1], '0')
        return str(30 + int(digit))
    
    # Handle compound numbers with 十 like 九十六 (96)
    if '十' in chinese_num:
        parts = chinese_num.split('十')
        result = 0
        
        # Before 十
        if parts[0]:
            result = int(char_map.get(parts[0], '1')) * 10
        else:
            result = 10  # 十六 = 16
        
        # After 十
        if parts[1]:
            result += int(char_map.get(parts[1], '0'))
        
        return str(result)
    
    # Handle digit-by-digit like 一零二 (102)
    all_digits = all(c in char_map and len(char_map[c]) == 1 for c in chinese_num)
    if all_digits:
        return ''.join(char_map[c] for c in chinese_num)
    
    # Fallback
    return chinese_num

def normalize_verse_references(content):
    """Normalize verse references with explicit book names only."""
    
    # Build pattern with explicit book names only
    book_pattern = '|'.join(BOOK_NAMES)
    # Pattern: optional prefix + book name + chinese chapter + space + verse
    pattern = rf'([（(]?参)?({book_pattern})([一二三四五六七八九十零廿卅]+)\s*(\d+(?:-\d+)?)'
    
    def replace_func(match):
        prefix = match.group(1) or ''
        book = match.group(2)
        chinese_chapter = match.group(3)
        verse = match.group(4)
        
        # Convert Chinese chapter to Arabic
        arabic_chapter = chinese_to_arabic(chinese_chapter)
        
        # Build normalized reference
        normalized_ref = f'{book}{arabic_chapter}:{verse}'
        
        return f'{prefix}{normalized_ref}'
    
    content = re.sub(pattern, replace_func, content)
    
    # Handle single-chapter books: 犹14-15 → 犹1:14-15
    single_chapter_books = ['俄', '门', '约二', '约三', '犹']
    single_chapter_pattern = '|'.join(single_chapter_books)
    single_ref_pattern = rf'({single_chapter_pattern})(\d+(?:-\d+)?)'
    
    def add_chapter_one(match):
        book = match.group(1)
        verses = match.group(2)
        return f'{book}1:{verses}'
    
    content = re.sub(single_ref_pattern, add_chapter_one, content)
    
    return content

def main():
    """Main function to normalize bibleData.json."""
    data_file = Path('bibleData.json')
    
    if not data_file.exists():
        print(f'Error: {data_file} not found')
        return 1
    
    # Load data
    print(f'Loading {data_file}...')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f'Processing {len(data)} entries...')
    print('Only normalizing references with explicit book names')
    
    # Normalize each entry
    normalized_count = 0
    for i, entry in enumerate(data):
        if 'content' in entry and entry['content']:
            original = entry['content']
            
            # Extract book from scripture field for context
            scripture_book = None
            if 'scripture' in entry and entry['scripture']:
                book_pattern = '|'.join(BOOK_NAMES)
                match = re.match(rf'^({book_pattern})', entry['scripture'])
                if match:
                    scripture_book = match.group(1)
            
            # If we have scripture context, normalize standalone chapter references first
            if scripture_book:
                # Pattern for standalone chapter references like （一 10） or （九15）
                # Also handles continuation references like （十二 2，十 三 16，十五4-5）
                standalone_pattern = r'（([一二三四五六七八九十零廿卅\s，、]+?)(\d+(?:-\d+)?(?:[，、]\s*[一二三四五六七八九十零廿卅\s]*\d+(?:-\d+)?)*)）'
                
                def replace_with_context(match):
                    chinese_parts = match.group(1)
                    verses_part = match.group(2)
                    
                    # Split by commas to handle multiple references
                    full_text = chinese_parts + verses_part
                    parts = re.split(r'[，、]\s*', full_text)
                    
                    normalized_parts = []
                    for part in parts:
                        part = part.strip()
                        if not part:
                            continue
                        
                        # Try to match Chinese chapter + verse
                        ref_match = re.match(r'([一二三四五六七八九十零廿卅\s]*?)(\d+(?:-\d+)?)', part)
                        if ref_match:
                            chinese_chapter = ref_match.group(1).replace(' ', '').strip()
                            verse = ref_match.group(2)
                            
                            if chinese_chapter:
                                # Has chapter number
                                arabic_chapter = chinese_to_arabic(chinese_chapter)
                                normalized_parts.append(f'{scripture_book}{arabic_chapter}:{verse}')
                            elif normalized_parts:
                                # No chapter, just verse - use last chapter
                                normalized_parts.append(verse)
                            else:
                                # First reference with no chapter - skip
                                continue
                    
                    if normalized_parts:
                        return f'（{"，".join(normalized_parts)}）'
                    return match.group(0)
                
                original = re.sub(standalone_pattern, replace_with_context, original)
            
            # Then apply normal normalization
            normalized = normalize_verse_references(original)
            
            if original != normalized or entry['content'] != normalized:
                entry['content'] = normalized
                normalized_count += 1
                
                if normalized_count <= 3:  # Show first 3 examples
                    print(f'\nEntry {i} ({entry.get("day_label", "?")}):')
                    # Find what changed
                    for line_orig, line_norm in zip(entry['content'].split('\n'), normalized.split('\n')):
                        if line_orig != line_norm:
                            print(f'  Before: {line_orig[:80]}...')
                            print(f'  After:  {line_norm[:80]}...')
                            break
    
    print(f'\n✓ Normalized {normalized_count} entries')
    
    # Backup original
    backup_file = data_file.with_suffix('.json.bak2')
    print(f'Creating backup: {backup_file}')
    import shutil
    shutil.copy(data_file, backup_file)
    
    # Save normalized data
    print(f'Saving normalized data to {data_file}')
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print('✓ Done!')
    return 0

if __name__ == '__main__':
    exit(main())
