#!/usr/bin/env python3
"""
Clean up bibleData.json by removing unwanted HTML wrapper tags.
Removes <!DOCTYPE>, <html>, <head>, <body> tags that the LLM incorrectly added.
"""

import json
import re
from pathlib import Path


def clean_html_content(content):
    """Remove unwanted HTML wrapper tags from content."""
    if not content or not isinstance(content, str):
        return content
    
    original = content
    
    # Remove markdown code blocks if present
    if content.startswith('```html'):
        content = content[7:]
    if content.startswith('```'):
        content = content[3:]
    if content.endswith('```'):
        content = content[:-3]
    content = content.strip()
    
    # Remove DOCTYPE
    content = re.sub(r'<!DOCTYPE[^>]*>', '', content, flags=re.IGNORECASE)
    
    # Extract content from <body> if present
    body_match = re.search(r'<body[^>]*>(.*)</body>', content, re.DOTALL | re.IGNORECASE)
    if body_match:
        content = body_match.group(1).strip()
    
    # Remove <html>, <head>, and their closing tags
    content = re.sub(r'</?html[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<head>.*?</head>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove <title> tags if any leaked through
    content = re.sub(r'<title>.*?</title>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove <meta> tags
    content = re.sub(r'<meta[^>]*>', '', content, flags=re.IGNORECASE)
    
    # Clean up extra whitespace and newlines
    content = content.strip()
    
    # Return cleaned content, or original if something went wrong
    if content and len(content) > 50:
        return content
    else:
        return original


def main():
    """Clean all entries in bibleData.json."""
    json_path = Path('bibleData.json')
    
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
    
    # Load data
    print("Loading bibleData.json...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Processing {len(data)} entries...")
    
    cleaned_count = 0
    
    for i, entry in enumerate(data):
        content = entry.get('content', '')
        
        # Check if content has unwanted tags
        if any(tag in content.lower() for tag in ['<!doctype', '<html', '<head', '<body', '```html']):
            cleaned = clean_html_content(content)
            if cleaned != content:
                entry['content'] = cleaned
                cleaned_count += 1
                print(f"✓ [{i+1}/{len(data)}] {entry['day_label']}: Cleaned")
    
    if cleaned_count > 0:
        # Save cleaned data
        print(f"\nSaving cleaned data...")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Done!")
        print(f"  Cleaned: {cleaned_count} entries")
        print(f"  Unchanged: {len(data) - cleaned_count} entries")
    else:
        print(f"\n✅ No cleanup needed - all entries are already clean!")


if __name__ == '__main__':
    main()
