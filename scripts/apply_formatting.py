#!/usr/bin/env python3
"""
Apply auto-formatting to all entries in bibleData.json
"""

import json
from pathlib import Path
from format_content import format_content


def main():
    """Apply formatting to all entries."""
    json_path = Path('bibleData.json')
    
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
    
    # Load data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Processing {len(data)} entries...")
    
    # Format each entry
    formatted_count = 0
    skipped_count = 0
    
    for i, entry in enumerate(data):
        original = entry['content']
        formatted = format_content(original)
        
        if formatted != original:
            entry['content'] = formatted
            formatted_count += 1
            print(f"✓ [{i+1}/{len(data)}] {entry['day_label']}: Formatted")
        else:
            skipped_count += 1
    
    # Save updated data
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDone!")
    print(f"  Formatted: {formatted_count}")
    print(f"  Skipped (already formatted): {skipped_count}")
    print(f"  Total: {len(data)}")


if __name__ == '__main__':
    main()
