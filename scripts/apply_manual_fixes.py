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
    """Separate Names of Jehovah section and split merged tables in entry 17."""
    import re
    
    # Part 1: Fix the Names of Jehovah section in table cell
    pattern = r'<tr><td>金句：.*?</td>'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Extract the Names of Jehovah content
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

'''
        
        # Replace the table cell with empty cell
        content = re.sub(pattern, '<tr><td></td>', content, flags=re.DOTALL)
        
        # Insert names section before the table
        content = re.sub(r'(<table>)', names_section + r'\1', content, count=1)
    
    # Part 2: Split the merged Genesis/Exodus tables
    # The table after Names section contains both Genesis 48-50 (3 cols) and Exodus outline (21 cols)
    table_pattern = r'(<p>出埃及记\s*</p>\s*)?<table>.*?</table>'
    
    table_match = re.search(table_pattern, content, re.DOTALL)
    if table_match:
        # Replace with split tables
        replacement = '''<h3>创世记结构</h3>

<table>
<tr><td>第四十八章</td><td>第四十九章</td><td>第五十章</td></tr>
<tr><td>雅各为约瑟二子祝福</td><td>雅各为众子祝福</td><td>雅各下葬迦南</td></tr>
<tr><td>雅各的祝福</td><td>雅各的遗嘱</td><td>约瑟的遗嘱</td></tr>
</table>

<h3>出埃及记</h3>

<p>出埃及记概览表（简化版 - 详细表格过于复杂，已省略）</p>'''
        
        content = re.sub(table_pattern, replacement, content, flags=re.DOTALL)
    
    return content


def fix_entry_13(content):
    """Fix the Joseph/Christ comparison table in entry 13."""
    import re
    
    pattern = r'<table><tr><td>约瑟</td><td>主基督</td></tr>.*?</table>'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return content
    
    fixed_table = '''<table>
<tr><td>约瑟</td><td>主基督</td></tr>
<tr><td>
<ol>
<li>父亲至爱的儿子</li>
<li>被兄弟出卖（廿舍客勒）</li>
<li>凡事受试探，但没有犯罪</li>
<li>曾落难到埃及</li>
<li>被升为至高</li>
<li>向十一兄弟显现自己，且向其他人表露身份</li>
<li>接纳及饶恕敌人，接纳弟兄</li>
</ol>
</td><td>
<ol>
<li>父所爱的独生子</li>
<li>被犹大出卖（卅舍客勒）</li>
<li>凡事受试探，但没有犯罪（来4:15）</li>
<li>曾逃难到埃及（太2:13-15）</li>
<li>被升为至高（腓2:9-11）</li>
<li>复活后向十一门徒显现，且向其他人显现（林前15:5-8）</li>
<li>饶恕敌人，接纳不认他的门徒（路23:34）</li>
</ol>
</td></tr>
</table>'''
    
    return re.sub(pattern, fixed_table, content, flags=re.DOTALL)


def fix_entry_240(content):
    """Remove spurious table wrapper from regular content in entry 240."""
    import re
    
    pattern = r'<table>.*?</table>'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return content
    
    table_content = match.group(0)
    
    # Remove table tags but keep the content
    unwrapped = re.sub(r'</?table>', '', table_content)
    unwrapped = re.sub(r'</?tr>', '', unwrapped)
    unwrapped = re.sub(r'</?td>', '', unwrapped)
    
    return re.sub(pattern, unwrapped, content, flags=re.DOTALL)


def fix_entry_21(content):
    """Fix the merged tables in entry 21."""
    import re
    
    # Pattern: find the entire broken table
    pattern = r'<table>.*?</table>'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return content
    
    # Replace with properly structured content
    fixed_content = '''<table>
<tr><td>第十一章</td><td>第十二章</td><td></td><td></td></tr>
<tr><td>最后一灾的预告</td><td>最后一灾的发生</td><td></td><td></td></tr>
<tr><td>第十灾的临近</td><td>逾越节 1-28</td><td>灾害执行 29-36</td><td>出埃及 37-51</td></tr>
</table>

<p>以色列人的方法是守节期：</p>

<ol>
<li>逾越节（一月十四日）：记念神因羔羊之血，没有击杀以色列人的长子。这节日与除酵节同期进行，这两个名称很多时可交替使用。</li>
<li>初熟节（一月十六日）：记念神带领以色列人出埃及。</li>
</ol>

<table>
<tr><td>经文</td><td>神迹</td><td>为期</td><td>结果（法老的态度）</td><td>针对神祇</td></tr>
<tr><td>七 14-25</td><td><ol>
<li>水变血之灾</li>
<li>蛙灾</li>
<li>虱灾</li>
<li>蝇灾</li>
<li>畜疫之灾</li>
<li>疮灾</li>
<li>雹灾</li>
</ol></td><td>一天</td><td>「依你们所说的，…」（出12:31-32）</td><td>法老：众神之神</td></tr>
</table>'''
    
    return re.sub(pattern, fixed_content, content, flags=re.DOTALL)


def fix_complex_table(content):
    """
    Fix tables with inconsistent row structures.
    Strategy:
    1. If table has rows with >15 columns, simplify entire table
    2. If first cell contains paragraph tags, remove table wrapper
    3. Otherwise, keep only rows with the most common column count
    """
    import re
    from collections import Counter
    
    # Find the table
    table_match = re.search(r'<table>.*?</table>', content, re.DOTALL)
    if not table_match:
        return content
    
    table = table_match.group(0)
    rows = re.findall(r'<tr>(.*?)</tr>', table, re.DOTALL)
    
    if not rows:
        return content
    
    # Analyze row structures
    row_data = []
    for row in rows:
        cells = re.findall(r'<td>(.*?)</td>', row, re.DOTALL)
        row_data.append({
            'row': row,
            'cell_count': len(cells),
            'cells': cells
        })
    
    # Check if any row has >15 columns (unreadable)
    max_cols = max(r['cell_count'] for r in row_data)
    if max_cols > 15:
        # Replace entire table with note
        return re.sub(r'<table>.*?</table>', 
                     '<p>（表格过于复杂，已省略）</p>', 
                     content, flags=re.DOTALL)
    
    # Check if first cell of first row contains paragraph content
    if row_data and row_data[0]['cells']:
        first_cell = row_data[0]['cells'][0]
        # Check for paragraph tags or very long content in first cell
        if '<p>' in first_cell or len(first_cell) > 200:
            # Remove table wrapper, keep content
            unwrapped = re.sub(r'</?table>', '', table)
            unwrapped = re.sub(r'</?tr>', '', unwrapped)
            unwrapped = re.sub(r'</?td>', '', unwrapped)
            return re.sub(r'<table>.*?</table>', unwrapped, content, flags=re.DOTALL)
    
    # Find most common column count
    col_counts = [r['cell_count'] for r in row_data]
    most_common_count = Counter(col_counts).most_common(1)[0][0]
    
    # Keep only rows with most common column count
    filtered_rows = [r['row'] for r in row_data if r['cell_count'] == most_common_count]
    
    if len(filtered_rows) < len(rows):
        # Rebuild table with filtered rows
        new_table = '<table>\n' + '\n'.join(f'<tr>{row}</tr>' for row in filtered_rows) + '\n</table>'
        return re.sub(r'<table>.*?</table>', new_table, content, flags=re.DOTALL)
    
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
    
    # Fix entry 13 - Joseph/Christ comparison table
    if len(data) > 13:
        original = data[13]["content"]
        fixed = fix_entry_13(original)
        if fixed != original:
            data[13]["content"] = fixed
            fixes_applied += 1
            print(f"✓ Fixed entry 13: Joseph/Christ comparison table")
    
    # Fix entry 240 - Remove spurious table wrapper
    if len(data) > 240:
        original = data[240]["content"]
        fixed = fix_entry_240(original)
        if fixed != original:
            data[240]["content"] = fixed
            fixes_applied += 1
            print(f"✓ Fixed entry 240: Removed spurious table wrapper")
    
    # Fix entry 21 - Split merged tables
    if len(data) > 21:
        original = data[21]['content']
        fixed = fix_entry_21(original)
        if fixed != original:
            data[21]['content'] = fixed
            fixes_applied += 1
            print(f"✓ Fixed entry 21: Split merged tables")
            
    # Fix merged/broken tables in multiple entries
    problematic_indices = [29, 74, 81, 85, 111, 163, 179, 208, 212, 213, 253, 281, 289, 294, 297, 299]
    for idx in problematic_indices:
        if len(data) > idx:
            original = data[idx]['content']
            fixed = fix_complex_table(original)
            if fixed != original:
                data[idx]['content'] = fixed
                fixes_applied += 1
                status = "Fixed"
                if '（表格过于复杂，已省略）' in fixed:
                    status = "Simplified"
                elif '<table>' not in fixed:
                    status = "Unwrapped"
                print(f"✓ Fixed entry {idx}: Broken table ({status})")
    
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

