#!/usr/bin/env python3
"""
Apply manual formatting fixes to specific entries in bibleData.json.
This script handles special cases that need custom formatting beyond
what the heuristic formatter can handle.
"""

import json
from pathlib import Path


def fix_angel_of_the_lord(content):
    """Format the 'Angel of the Lord' section in entry 12."""
    old_text = '耶和华的使者（ The Angel of the Lord）是谁？ 1.有时他是耶和华自己 a.创世记十六章七至九节、十三节 b.出埃及记十三章廿一至廿二节，十四章十九、二十、廿四节 c.民数记十四章十四节，廿章十六节 d.创世记卅一章十一至十三节 e.创世记四十五章五节，四十八章十五至十六节等 2.有时他有一独特位格，与耶和华不同： a.创世记廿四章七节 b.民数记二十章十六节 c.撒迦利亚书一章十二至十三节 3.他乃是道成肉身前之主基督。'
    
    new_text = '''<strong>耶和华的使者（The Angel of the Lord）是谁？</strong>
<ol>
<li>有时他是耶和华自己
<ol type="a">
<li>创16:7-9、13</li>
<li>出13:21-22，14:19、20、24</li>
<li>民14:14，20:16</li>
<li>创31:11-13</li>
<li>创45:5，48:15-16等</li>
</ol>
</li>
<li>有时他有一独特位格，与耶和华不同：
<ol type="a">
<li>创24:7</li>
<li>民20:16</li>
<li>亚1:12-13</li>
</ol>
</li>
<li>他乃是道成肉身前之主基督。</li>
</ol>'''
    
    if old_text in content:
        return content.replace(old_text, new_text)
    return content


def fix_entry_17(content):
    """Separate Names of Jehovah section from table in entry 17."""
    import re
    
    # Find the problematic table cell content
    # The issue is that "耶和华在旧约中的名字..." is inside a table cell
    # We need to extract it and place it before the table
    
    # Pattern to find the table with the problematic content
    pattern = r'(<tr><td>金句： 创世记四十八章廿一节.*?耶和华洛斐.*?的意思。</p>\s*<p>出埃及记)'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return content
    
    # Extract the Names of Jehovah content (without the golden verse since it's in the verse field)
    names_section = '''<h4>耶和华在旧约中的名字</h4>
<ol>
<li>耶和华：原从希伯来文「他是」的字根而来，有关「他是」的意义，请参本书出埃及记三至五章之「默想」部份</li>
<li>耶和华以勒（JHWH-Jireh，创22:14）：就是「耶和华必预备、医治」的意思。</li>
<li>耶和华尼西（JHWH-Nissi，出17:15-16）：就是「耶和华是我旌旗」的意思。</li>
<li>耶和华沙龙（JHWH-Shalom，士6:23-24）：就是「耶和华是我平安」的意思。</li>
<li>耶和华沙玛（JHWH-Shammah，结48:35）：就是「耶和华要再来」的意思。</li>
<li>耶和华士基路（JHWH-Tsidkenu，耶23:6）：就是「耶和华是我的义」的意思。</li>
<li>耶和华洛斐（JHWH-Rapha，出15:26）：就是「耶和华是我医治者」的意思。</li>
</ol>

<p>出埃及记'''
    
    # Replace the table cell content with just "出埃及记" to start the table properly
    content = re.sub(pattern, names_section, content, flags=re.DOTALL)
    
    return content


def apply_manual_fixes(data):
    """Apply all manual formatting fixes to the data."""
    fixes_applied = 0
    
    # Fix entry 12 - Angel of the Lord section
    if len(data) > 12:
        original = data[12]['content']
        fixed = fix_angel_of_the_lord(original)
        if fixed != original:
            data[12]['content'] = fixed
            fixes_applied += 1
            print(f"✓ Fixed entry 12: Angel of the Lord section")
    
    # Fix entry 17 - Golden verse and Names of Jehovah
    if len(data) > 17:
        original = data[17]['content']
        fixed = fix_entry_17(original)
        if fixed != original:
            data[17]['content'] = fixed
            fixes_applied += 1
            print(f"✓ Fixed entry 17: Golden verse and Names of Jehovah section")
    
    # Note: Scripture reference spacing is handled by normalize_verse_refs.py
    # No need for manual spacing fixes here
    
    # Add more manual fixes here as needed
    
    return fixes_applied


def main():
    """Main function to apply manual fixes."""
    data_file = Path('bibleData.json')
    
    if not data_file.exists():
        print(f'Error: {data_file} not found')
        return 1
    
    # Load data
    print('Loading bibleData.json...')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f'Applying manual formatting fixes to {len(data)} entries...')
    
    # Apply fixes
    fixes_applied = apply_manual_fixes(data)
    
    if fixes_applied > 0:
        # Save updated data
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f'\n✓ Applied {fixes_applied} manual fix(es)')
    else:
        print('\nNo manual fixes needed (already applied or not found)')
    
    return 0


if __name__ == '__main__':
    exit(main())
