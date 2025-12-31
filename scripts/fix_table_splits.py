#!/usr/bin/env python3
"""
Fix table splits in bibleData.json.
Some tables in the PDF are incorrectly merged and need to be split.
"""

import json
from pathlib import Path


def split_week2_day1_tables(entry):
    """Split the merged table in Week 2 Day 1."""
    content = entry['content']
    split_marker = '<td>考验内容</td>'
    
    if split_marker not in content:
        return False
    
    # Split the table at this point
    parts = content.split('<tr>')
    new_parts = []
    found_split = False
    
    for i, part in enumerate(parts):
        if split_marker in part and not found_split:
            # Close previous table and start new one
            new_parts.append('</table>')
            new_parts.append('<table>')
            new_parts.append('<tr>')
            new_parts.append(part)
            found_split = True
        else:
            if i > 0:  # Add <tr> back (except for first part)
                new_parts.append('<tr>')
            new_parts.append(part)
    
    entry['content'] = ''.join(new_parts)
    return True


def main():
    """Fix table splits in bibleData.json."""
    json_path = Path('bibleData.json')
    
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
    
    # Load data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Processing {len(data)} entries...")
    
    fixed_count = 0
    
    # Week 2 Day 1 (index 6)
    if len(data) > 6:
        if split_week2_day1_tables(data[6]):
            fixed_count += 1
            print(f"✓ Week 2 Day 1: Split tables")
    
    # Add more table fixes here as needed
    # if len(data) > X:
    #     if fix_some_other_table(data[X]):
    #         fixed_count += 1
    
    if fixed_count > 0:
        # Save
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Done! Fixed {fixed_count} table(s)")
    else:
        print(f"\n✅ No table fixes needed")


if __name__ == '__main__':
    main()
