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
    
    # Continue with formatting even if we added a numbered list
    formatted = content
    
    # Store protected blocks to prevent them from being split by paragraph formatting
    protected_blocks = []
    
    def protect(text):
        token = f'__PROTECTED_BLOCK_{len(protected_blocks)}__'
        protected_blocks.append(text)
        return token
    
    # Pre-process: Merge dangling closing quotes with previous line
    # Fixes issue where 」 appears on a new line: "text\n」" or "text\n\n」" -> "text」"
    # Using regex to handle multiple newlines/spaces
    formatted = re.sub(r'\s+([」』])', r'\1', formatted)

    # Only run main formatting if not already formatted
    # (Note: we bypass this check for the protection logic to work correctly if we want to support re-runs,
    # but for now we keep the check to avoid double-processing text, assuming input is raw text)
    if not ('<p>' in formatted or '<ul>' in formatted or '<blockquote>' in formatted):
        
        # 0. Detect and format numbered lists (Pattern: 1.text 2.text)
        numbered_list_pattern = r'(\d+)\.\s*([^。\n<]+(?:。)?)'
        matches = list(re.finditer(numbered_list_pattern, formatted))
        
        if len(matches) >= 3:
            # Find the longest consecutive sequence starting from 1
            best_sequence = []
            current_sequence = []
            expected_num = 1
            
            for m in matches:
                num = int(m.group(1))
                if num == expected_num:
                    current_sequence.append(m)
                    expected_num += 1
                elif num == 1:
                    if len(current_sequence) > len(best_sequence):
                        best_sequence = current_sequence
                    current_sequence = [m]
                    expected_num = 2
                else:
                    if len(current_sequence) > len(best_sequence):
                        best_sequence = current_sequence
                    current_sequence = []
                    expected_num = 1
            
            if len(current_sequence) > len(best_sequence):
                best_sequence = current_sequence
            
            if len(best_sequence) >= 3:
                list_items = []
                for m in best_sequence:
                    item_text = m.group(2).strip()
                    if item_text.endswith('。'):
                        item_text = item_text[:-1]
                    list_items.append(item_text)
                
                first_match_start = best_sequence[0].start()
                last_match_end = best_sequence[-1].end()
                
                html_list = '<ol>\n' + '\n'.join([f'<li>{item}</li>' for item in list_items]) + '\n</ol>'
                
                # Replace with protected block
                formatted = formatted[:first_match_start] + protect(html_list) + formatted[last_match_end:]

        # 1. Wrap quotes in blockquotes
        # Pattern: text says: 「quote」
        quote_pattern = r'([^。]*说：)「([^」]+)」'
        formatted = re.sub(
            quote_pattern,
            lambda m: f'{m.group(1)}\n{protect(f"<blockquote>「{m.group(2)}」</blockquote>")}\n',
            formatted
        )
        
        # 2. Detect and format lettered lists (a．text b．text c．text)
        # Note: using full-width dot ．
        letter_list_pattern = r'([a-z])．\s*([^a-z．。\n<]+(?:。)?)'
        letter_matches = list(re.finditer(letter_list_pattern, formatted))
        
        if len(letter_matches) >= 2:
             # Basic check if sequential 'a' start
             if letter_matches[0].group(1) == 'a':
                 items = []
                 expected_char = 'a'
                 for m in letter_matches:
                     char = m.group(1)
                     if char == expected_char:
                         items.append(m.group(2).strip())
                         expected_char = chr(ord(expected_char) + 1)
                     else:
                         break
                
                 if len(items) >= 2:
                     first_start = letter_matches[0].start()
                     last_end = letter_matches[len(items)-1].end()
                     
                     html_parts = ['<ol type="a" style="margin-left: 20px;">']
                     
                     for i, m in enumerate(letter_matches[:len(items)]):
                         current_item = items[i]
                         current_end = m.end()
                         gap_content = ""
                         consumed_gap = False
                         
                         if i < len(items) - 1:
                             next_start = letter_matches[i+1].start()
                             if next_start > current_end:
                                 gap_content = formatted[current_end:next_start]
                                 clean_gap = gap_content.strip()
                                 # Heuristic: merge scripture ref
                                 if clean_gap.startswith('（') and clean_gap.endswith('）') and len(clean_gap) < 30:
                                     current_item += " " + clean_gap
                                     consumed_gap = True
                         else:
                             # Last item
                             suffix_match = re.match(r'\s*（[^）\n]+）', formatted[current_end:])
                             if suffix_match:
                                 ref_text = suffix_match.group(0)
                                 current_item += " " + ref_text.strip()
                                 last_end += len(ref_text)
                                 
                         html_parts.append(f'<li>{current_item}</li>')
                         
                         if not consumed_gap and gap_content:
                             html_parts.append('</ol>')
                             # If gap content matches a protected block token (unlikely but possible if recursive), it's fine
                             html_parts.append(gap_content) 
                             html_parts.append('<ol type="a" style="margin-left: 20px;" start="' + chr(ord('a') + i + 1) + '">')
                     
                     html_parts.append('</ol>')
                     html_list = '\n'.join(html_parts)
                     
                     formatted = formatted[:first_start] + protect(html_list) + formatted[last_end:]
        
        # 2b. Detect and format question lists
        question_pattern = r'(若你[^？]+？)'
        questions = re.findall(question_pattern, formatted)
        
        if len(questions) >= 2:
            questions_section = '\n'.join(questions)
            html_list = '<ul style="line-height: 1.8;">\n' + '\n'.join([f'<li>{q}</li>' for q in questions]) + '\n</ul>'
            formatted = formatted.replace(
                questions_section,
                '<p><strong>思考问题：</strong></p>\n' + protect(html_list) + '\n'
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
            
            # Since HTML is protected, we don't need to check for < anymore, 
            # unless there are stray tags not protected. 
            # But let's check for __PROTECTED_BLOCK_ match to keep block as its own para
            if '__PROTECTED_BLOCK_' in sentence:
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
        
        # Wrap paragraphs in <p> tags
        formatted_paragraphs = []
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            
            # If paragraph is JUST a protected block, don't wrap in <p> yet (or wrap and strip later)
            # Actually, we wrap everything in <p> and then strip if it contains ONLY block
            if para.startswith('<') and not '__PROTECTED_BLOCK_' in para: # Existing HTML tags logic
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
        if '注释：' in formatted:
            parts = formatted.split('注释：', 1)
            if len(parts) == 2:
                main_content = parts[0].strip()
                commentary_content = parts[1].strip()
                
                commentary_content = re.sub(r'^</p>', '', commentary_content)
                commentary_content = re.sub(r'<p>$', '', commentary_content)
                
                main_content = main_content.strip()
                
                commentary_box = f'''<div class="commentary-box">
    <h5>注释</h5>
    {commentary_content}
    </div>'''
                
                # Protect commentary box? It's adding HTML at the end.
                # Assuming main_content is already processed/protected.
                formatted = main_content + '\n\n' + commentary_box
    
    # Final cleanup: Restore protected blocks
    # We loop backwards to ensure nested blocks are restored correctly (e.g. List containing Quote)
    for i, block in reversed(list(enumerate(protected_blocks))):
        token = f'__PROTECTED_BLOCK_{i}__'
        # If token is wrapped in <p>, remove <p>
        # e.g. <p>__PROTECTED_BLOCK_0__</p> -> block
        # e.g. <p>Some text __PROTECTED_BLOCK_0__</p> -> <p>Some text </p> block (break p)
        
        # Robust unwrap:
        # 1. Exact match <p>token</p>
        if f'<p>{token}</p>' in formatted:
             formatted = formatted.replace(f'<p>{token}</p>', block)
        elif f'<p>{token}。</p>' in formatted: # Sometimes . might be appended
             formatted = formatted.replace(f'<p>{token}。</p>', block)
        else:
             formatted = formatted.replace(token, block)

    # Double-check closing quotes cleanup (in case they were not protected, though quotes ARE protected)
    # This might still be needed for text not in protected blocks
    formatted = re.sub(r'</p>\s*<p>\s*([」』])', r'\1', formatted)
            
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
