#!/usr/bin/env python3
"""
Auto-format devotional content for better readability.
Adds paragraph breaks, blockquotes, bullet lists, and bold headings.
"""

import json
import re
from pathlib import Path


def build_replacement(content, matches):
    """Helper to build <ol> block for a list of matches."""
    if not matches:
        return None
        
    start_num = int(matches[0].group(1))
    
    list_items = []
    for m in matches:
         # text is group 2
         list_items.append(m.group(2).strip())
         
    start_attr = f' start="{start_num}"' if start_num > 1 else ''
    
    formatted_list = f'<ol{start_attr}>\n' + '\n'.join([f'<li>{item}</li>' for item in list_items]) + '\n</ol>'
    
    return (matches[0].start(), matches[-1].end(), formatted_list)


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
    
    formatted = content
    
    # Pre-process: Ensure numbered lists are on their own lines to help detection
    # This splits "Text. 1. Item" into "Text.\n1. Item"
    # Added support for colon (：) and parens (）) which often precede lists
    content = re.sub(r'([。?？!！：）)])\s*(\d+\.)', r'\1\n\2', content)

    # First, detect and format numbered lists (even if content has some HTML)
    # Pattern: 1.text 2.text 3.text (consecutive numbered items)
    # This works across paragraph boundaries because we use multiline mode
    numbered_list_pattern = r'(?m)^\s*(\d+)\.\s*(.+)$'
    matches = list(re.finditer(numbered_list_pattern, content))
    
    # Logic to identify valid sequences (1, 2, 3...)
    # and group them (splitting if gaps are too large to prevents deleting content)
    
    sequences = []
    current_sequence = []
    expected_num = 1
    
    # 1. Build logical sequences based on numbers
    for m in matches:
        num = int(m.group(1))
        if num == expected_num:
             current_sequence.append(m)
             expected_num += 1
        elif num == 1:
             if current_sequence:
                 sequences.append(current_sequence)
             current_sequence = [m]
             expected_num = 2
        else:
             if current_sequence:
                 sequences.append(current_sequence)
             current_sequence = []
             expected_num = 1
    if current_sequence:
        sequences.append(current_sequence)

    # 2. Process sequences: Check gaps and create replacement actions
    # Action = (start, end, replacement_text)
    replacements = []
    
    GAP_THRESHOLD = 5 # characters (newlines/whitespace are fine, but text implies break)
    
    for seq in sequences:
        # A sequence is like [Item 1, Item 2, Item 3]
        # We need to check gaps between Item 1 end and Item 2 start
        
        # We split this logical sequence into physical chunks
        current_chunk = []
        
        for i, match in enumerate(seq):
            if not current_chunk:
                current_chunk.append(match)
                continue
            
            prev_match = current_chunk[-1]
            gap_text = content[prev_match.end():match.start()]
            
            # If gap contains substantive text (not just whitespace/punctuation), break the chunk
            # We strip whitespace and common punctuation to check for "real" text
            clean_gap = re.sub(r'[\s\n。，\.,]', '', gap_text)
            
            if len(clean_gap) > 0:
                # Close current chunk
                replacements.append(build_replacement(content, current_chunk))
                current_chunk = [match]
            else:
                current_chunk.append(match)
        
        if current_chunk:
            replacements.append(build_replacement(content, current_chunk))
            
    # 3. Apply replacements in reverse order
    # Filter out None (invalid chunks)
    replacements = [r for r in replacements if r is not None]
    replacements.sort(key=lambda x: x[0], reverse=True)
    
    content_modified = False
    for start, end, text in replacements:
        content = content[:start] + text + content[end:]
        content_modified = True

    formatted = content
    
    # Skip if content already has minimal paragraph formatting
    if '<p>' in formatted:
        return content

    # Protection mechanism for blocks that shouldn't be split (like tables)
    protected_blocks = []
    def protect(text):
        token = f'__PROTECTED_BLOCK_{len(protected_blocks)}__'
        protected_blocks.append(text)
        return token

    # 0. Protect existing tables
    # Match <table>...</table> (DOTALL)
    table_pattern = r'(<table>.*?</table>)'
    formatted = re.sub(
        table_pattern,
        lambda m: protect(m.group(1)),
        formatted,
        flags=re.DOTALL
    )

    # 1. Wrap quotes in blockquotes
    # Pattern: text says: 「quote」
    # We want to protect blockquotes as well so they aren't split
    quote_pattern = r'([^。]*说：)「([^」]+)」'
    formatted = re.sub(
        quote_pattern,
        lambda m: f'{m.group(1)}\n{protect(f"<blockquote>「{m.group(2)}」</blockquote>")}\n',
        formatted
    )
    
    # 2. Detect and format question lists
    # Pattern: 若你...？ repeated
    question_pattern = r'(若你[^？]+？)'
    questions = re.findall(question_pattern, formatted)
    
    if len(questions) >= 2:
        # Found multiple questions - create a bullet list
        questions_section = '\n'.join(questions)
        html_list = '<ul style="line-height: 1.8;">\n' + '\n'.join([f'<li>{q}</li>' for q in questions]) + '\n</ul>'
        formatted = formatted.replace(
            questions_section,
            '<p><strong>思考问题：</strong></p>\n' + protect(html_list) + '\n'
        )
    
    # 3. Add paragraph breaks
    # Split on 。and group every 2-3 sentences into a paragraph
    # We first split by existing newlines to respect manual structure
    raw_paras = formatted.split('\n\n')
    final_paras = []
    
    for raw_p in raw_paras:
        if not raw_p.strip():
            continue
            
        sentences = raw_p.split('。')
        current_group = []
        
        for i, sentence in enumerate(sentences):
            sentence = sentence.strip()
            if not sentence:
                continue
                
            # Check if this sentence has a protected token
            if '__PROTECTED_BLOCK_' in sentence:
                if current_group:
                    final_paras.append('。'.join(current_group) + '。')
                    current_group = []
                final_paras.append(sentence) # Treat protected block as its own para (wrapper pending)
                continue
            
            # Check if likely HTML block (skip if already formatted)
            if '<' in sentence and '>' in sentence:
                 if current_group:
                    final_paras.append('。'.join(current_group) + '。')
                    current_group = []
                 final_paras.append(sentence)
                 continue
            
            current_group.append(sentence)
            
            # Create paragraph after 2-3 sentences or at section breaks
            if len(current_group) >= 2 or (sentence and sentence[-1] in '：？'):
                final_paras.append('。'.join(current_group) + '。')
                current_group = []
        
        # Add remaining sentences in this raw para
        if current_group:
            final_paras.append('。'.join(current_group) + '。')
            
    # Wrap paragraphs in <p> tags
    formatted_paragraphs = []
    for para in final_paras:
        para = para.strip()
        if not para:
            continue
            
        # Don't wrap if it's already HTML-like OR if it's a protected block
        # Protected blocks (like tables) should stand alone
        if para.startswith('<') or '__PROTECTED_BLOCK_' in para:
            formatted_paragraphs.append(para)
        else:
            formatted_paragraphs.append(f'<p>{para}</p>')
    
    formatted = '\n\n'.join(formatted_paragraphs)
    
    # Restore protected blocks
    for i, block in enumerate(protected_blocks):
        token = f'__PROTECTED_BLOCK_{i}__'
        formatted = formatted.replace(token, block)

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
