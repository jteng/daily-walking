#!/usr/bin/env python3
"""
Post-process formatted content to move commentary-box divs to the bottom.
"""

import json
import re
from pathlib import Path


def move_commentary_to_bottom(content):
    """Move <div class="commentary-box">...</div> to the end of content."""
    # Pattern to match the entire commentary-box div
    pattern = r'<div class="commentary-box">.*?</div>\s*'
    
    # Find all commentary boxes
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    if not matches:
        return content
    
    # Extract commentary boxes
    commentary_boxes = [match.group(0) for match in matches]
    
    # Remove them from their current positions
    result = content
    for box in commentary_boxes:
        result = result.replace(box, '', 1)
    
    # Append them at the end
    result = result.rstrip() + '\n\n' + '\n\n'.join(commentary_boxes)
    
    return result


def main():
    """Process all entries in bibleData.json."""
    json_path = Path('bibleData.json')
    
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
    
    # Load data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Processing {len(data)} entries...")
    
    moved_count = 0
    for i, entry in enumerate(data):
        content = entry.get('content', '')
        
        if 'commentary-box' in content:
            new_content = move_commentary_to_bottom(content)
            if new_content != content:
                entry['content'] = new_content
                moved_count += 1
                print(f"✓ [{i+1}/{len(data)}] {entry['day_label']}: Moved commentary to bottom")
    
    # Save
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDone! Moved commentary in {moved_count} entries")


if __name__ == '__main__':
    main()
