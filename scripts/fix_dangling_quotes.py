#!/usr/bin/env python3
import json
import re
from pathlib import Path

def fix_dangling_quotes():
    json_path = Path('bibleData.json')
    if not json_path.exists():
        print("Error: bibleData.json not found")
        return

    print("Loading bibleData.json...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Pattern: </p> followed by <p> containing only quote, then </blockquote>
    # Matches: </p>\n\n<p>」</blockquote>
    pattern = r'</p>\s*<p>([」』])\s*</blockquote>'
    
    count = 0
    fixed_indices = []

    for entry in data:
        content = entry['content']
        if re.search(pattern, content):
            # Replace with just the quote and closing blockquote
            # This effectively merges it into the previous paragraph context
            # (or leaves it at the end of the text block inside the blockquote)
            new_content = re.sub(pattern, r'\1</blockquote>', content)
            
            if new_content != content:
                entry['content'] = new_content
                count += 1
                fixed_indices.append(entry['day_label'])

    if count > 0:
        print(f"Fixing {count} entries with dangling quotes...")
        for label in fixed_indices:
            print(f"  - {label}")
            
        print("Saving back to bibleData.json...")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Done!")
    else:
        print("No dangling quotes found.")

if __name__ == '__main__':
    fix_dangling_quotes()
