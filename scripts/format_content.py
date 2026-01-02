#!/usr/bin/env python3
"""
Auto-format devotional content for better readability.
Adds paragraph breaks, blockquotes, bullet lists, and bold headings.
"""

import json
import re
from pathlib import Path


def format_content(content):
    """
    Format content with improved structure.
    
    Rules:
    1. Detect quotes with 「」or 『』and wrap in blockquote
    2. Detect question patterns (若你...？) and create bullet lists
    3. Detect sequential events and create bullet lists
    4. Add paragraph breaks after every 2-3 sentences
    5. Bold section headers (text ending with ：)
    6. Detect numbered lists and format as <ol>
    """
    
    # First, detect and format numbered lists (even if content has some HTML)
    # Pattern: 1.text 2.text 3.text (consecutive numbered items)
    # This works across paragraph boundaries
    numbered_list_pattern = r'(\d+)\.\s*([^。\n<]+(?:。)?)'
    matches = list(re.finditer(numbered_list_pattern, content))
    
    content_modified = False
    if len(matches) >= 3:  # Require at least 3 items for a list
        # Find the longest consecutive sequence starting from 1
        # (there might be multiple numbered lists in the content)
        best_sequence = []
        current_sequence = []
        expected_num = 1
        
        for m in matches:
            num = int(m.group(1))
            if num == expected_num:
                current_sequence.append(m)
                expected_num += 1
            elif num == 1:
                # Start of a new sequence
                if len(current_sequence) > len(best_sequence):
                    best_sequence = current_sequence
                current_sequence = [m]
                expected_num = 2
            else:
                # Sequence broken
                if len(current_sequence) > len(best_sequence):
                    best_sequence = current_sequence
                current_sequence = []
                expected_num = 1
        
        # Check final sequence
        if len(current_sequence) > len(best_sequence):
            best_sequence = current_sequence
        
        if len(best_sequence) >= 3:
            # Found a numbered list with at least 3 items
            list_items = []
            for m in best_sequence:
                item_text = m.group(2).strip()
                # Remove trailing period if present
                if item_text.endswith('。'):
                    item_text = item_text[:-1]
                list_items.append(item_text)
            
            # Find the span of text containing all list items
            first_match_start = best_sequence[0].start()
            last_match_end = best_sequence[-1].end()
            
            # Build the formatted list
            formatted_list = '<ol>\n' + '\n'.join([f'<li>{item}</li>' for item in list_items]) + '\n</ol>'
            
            # Replace in content
            content = content[:first_match_start] + formatted_list + content[last_match_end:]
            content_modified = True
    
    # If we modified the content (added numbered list), return it
    if content_modified:
        return content
    
    formatted = content
    
    # Skip if content already has HTML formatting
    if '<p>' in content or '<ul>' in content or '<blockquote>' in content:
        return content
    
    # 1. Wrap quotes in blockquotes
    # Pattern: text says: 「quote」
    quote_pattern = r'([^。]*说：)「([^」]+)」'
    formatted = re.sub(
        quote_pattern,
        r'\1\n<blockquote>「\2」</blockquote>\n',
        formatted
    )
    
    # 2. Detect and format question lists
    # Pattern: 若你...？ repeated
    question_pattern = r'(若你[^？]+？)'
    questions = re.findall(question_pattern, formatted)
    
    if len(questions) >= 2:
        # Found multiple questions - create a bullet list
        questions_section = '\n'.join(questions)
        formatted = formatted.replace(
            questions_section,
            '<p><strong>思考问题：</strong></p>\n<ul style="line-height: 1.8;">\n' +
            '\n'.join([f'<li>{q}</li>' for q in questions]) +
            '\n</ul>\n'
        )
    
    # 3. Add paragraph breaks
    # Split on 。and group every 2-3 sentences into a paragraph
    sentences = formatted.split('。')
    paragraphs = []
    current_para = []
    
    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if not sentence:
            continue
            
        # Check if this sentence has HTML tags (skip if already formatted)
        if '<' in sentence and '>' in sentence:
            if current_para:
                paragraphs.append('。'.join(current_para) + '。')
                current_para = []
            paragraphs.append(sentence)
            continue
        
        current_para.append(sentence)
        
        # Create paragraph after 2-3 sentences or at section breaks
        if len(current_para) >= 2 or (sentence and sentence[-1] in '：？'):
            paragraphs.append('。'.join(current_para) + '。')
            current_para = []
    
    # Add remaining sentences
    if current_para:
        paragraphs.append('。'.join(current_para) + '。')
    
    # Wrap paragraphs in <p> tags (skip if already has tags)
    formatted_paragraphs = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if para.startswith('<'):
            formatted_paragraphs.append(para)
        else:
            formatted_paragraphs.append(f'<p>{para}</p>')
    
    formatted = '\n\n'.join(formatted_paragraphs)
    
    # 4. Bold section headers (text ending with ：)
    header_pattern = r'<p>([^<>]+：)</p>'
    formatted = re.sub(
        header_pattern,
        r'<p><strong>\1</strong></p>',
        formatted
    )
    
    # 5. Detect and format "注释：" sections
    # Handle both standalone paragraphs and inline commentary
    if '注释：' in formatted:
        # Split content at "注释："
        parts = formatted.split('注释：', 1)
        if len(parts) == 2:
            main_content = parts[0].strip()
            commentary_content = parts[1].strip()
            
            # Remove any incomplete paragraph tags from commentary
            commentary_content = re.sub(r'^</p>', '', commentary_content)
            commentary_content = re.sub(r'<p>$', '', commentary_content)
            
            # Clean up main content
            main_content = main_content.strip()
            
            # Create commentary box
            commentary_box = f'''<div class="commentary-box">
<h5>注释</h5>
{commentary_content}
</div>'''
            
            # Combine: main content + commentary at bottom
            formatted = main_content + '\n\n' + commentary_box
    
    return formatted


def preview_formatting(json_path, sample_indices):
    """
    Preview formatting on sample entries.
    
    Args:
        json_path: Path to bibleData.json
        sample_indices: List of indices to preview
    
    Returns:
        List of dicts with before/after content
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    previews = []
    for idx in sample_indices:
        if idx >= len(data):
            continue
        
        entry = data[idx]
        original = entry['content']
        formatted = format_content(original)
        
        previews.append({
            'index': idx,
            'day_label': entry['day_label'],
            'title': entry['title'],
            'original': original,
            'formatted': formatted,
            'changed': original != formatted
        })
    
    return previews


def main():
    """Generate preview of formatted content."""
    json_path = Path('bibleData.json')
    
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
    
    # Sample indices to preview (various weeks)
    sample_indices = [0, 5, 10, 20, 50, 100, 150, 200]
    
    previews = preview_formatting(json_path, sample_indices)
    
    # Save preview to file
    preview_path = Path('content_formatting_preview.json')
    with open(preview_path, 'w', encoding='utf-8') as f:
        json.dump(previews, f, ensure_ascii=False, indent=2)
    
    print(f"Generated preview for {len(previews)} entries")
    print(f"Saved to: {preview_path}")
    
    # Print summary
    changed_count = sum(1 for p in previews if p['changed'])
    print(f"\nSummary:")
    print(f"  Total previewed: {len(previews)}")
    print(f"  Would be changed: {changed_count}")
    print(f"  Already formatted: {len(previews) - changed_count}")
    
    # Show which entries would change
    print(f"\nEntries that would be formatted:")
    for p in previews:
        if p['changed']:
            print(f"  - {p['day_label']}: {p['title']}")


if __name__ == '__main__':
    main()
