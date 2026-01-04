
import json
import re
import statistics

def clean_html(text):
    """Strip HTML tags to measure raw text length."""
    return re.sub(r'<[^>]+>', '', text)

def analyze_paragraphs():
    with open('bibleData.json', 'r') as f:
        data = json.load(f)

    total_entries = len(data)
    has_p_wrapper = 0
    paragraph_lengths = []
    max_para_lengths = []
    broken_html_count = 0

    print(f"Analyzing {total_entries} entries...\n")

    for i, entry in enumerate(data):
        content = entry.get('content', '')
        
        # Check 1: Does it start with <p>?
        if content.strip().startswith('<p>'):
            has_p_wrapper += 1
        
        # Check 2: Paragraph Lengths
        # Split by <p>...</p> or \n\n if plain text
        if '<p>' in content:
            # Extract content inside <p> tags
            paras = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
            # Also count non-p text blocks if mixed? simpler to just clean html and split by \n\n maybe?
            # Let's stick to <p> contents for HTML entries
        else:
            paras = content.split('\n\n')

        # Clean and measure
        lengths = [len(clean_html(p).strip()) for p in paras if p.strip()]
        
        if lengths:
            entry_max = max(lengths)
            entry_avg = statistics.mean(lengths)
            paragraph_lengths.extend(lengths)
            max_para_lengths.append((i, entry_max))
        
        # Check 3: Broken HTML (Simple check for unbalanced simple tags)
        # Count open/close p tags
        p_open = content.count('<p>')
        p_close = content.count('</p>')
        if p_open != p_close:
            broken_html_count += 1
            if i < 5: # Print first few
                print(f"[Warn] Entry {i} ({entry.get('day_label')}) has unbalanced <p> tags: {p_open} open vs {p_close} close")

    # Stats
    print("\n--- Summary ---")
    print(f"Entries with <p> wrapper: {has_p_wrapper}/{total_entries} ({has_p_wrapper/total_entries*100:.1f}%)")
    print(f"Entries with unbalanced <p> tags: {broken_html_count}")
    
    if max_para_lengths:
        max_overall = max(max_para_lengths, key=lambda x: x[1])
        print(f"\nLongest Paragraph: {max_overall[1]} chars (Entry {max_overall[0]})")
        
        # Distribution
        over_500 = len([x for x in max_para_lengths if x[1] > 500])
        print(f"Entries with a paragraph > 500 chars: {over_500}")
        over_1000 = len([x for x in max_para_lengths if x[1] > 1000])
        print(f"Entries with a paragraph > 1000 chars: {over_1000}")
    
    print("\nTop 5 entries with longest paragraphs:")
    sorted_max = sorted(max_para_lengths, key=lambda x: x[1], reverse=True)[:5]
    for idx, length in sorted_max:
        print(f"- Entry {idx} ({data[idx].get('day_label')}): {length} chars")

    # Specific check for Index 1 and 2
    print(f"\n--- Specific Check ---")
    print(f"Entry 1 starts with <p>: {data[1].get('content').strip().startswith('<p>')}")
    print(f"Entry 2 starts with <p>: {data[2].get('content').strip().startswith('<p>')}")

if __name__ == "__main__":
    analyze_paragraphs()
