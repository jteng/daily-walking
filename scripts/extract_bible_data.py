
import pdfplumber
import re
import json
import sys
import os

def get_headers(page):
    """
    Returns list of dicts: {'y': float, 'type': 'week'|'day', 'text': str, 'match': match_obj}
    """
    headers = []
    
    # Patterns
    # Relaxed patterns to match text extracted from `extract_words`
    # or just use `extract_text` lines and find their Y? 
    # extract_text lines logic is reliable for content, finding their Y is the trick.
    # get_headers_with_offset logic I wrote earlier using extract_words is good.
    
    week_pattern = re.compile(r'第\s*(\d+)\s*周')
    day_pattern = re.compile(r'第\s*([\d、,]+)\s*日')
    
    words = page.extract_words()
    if not words: return []
    
    # helper to sort/group lines
    lines = []
    current_line = [words[0]]
    for w in words[1:]:
        if abs(w['top'] - current_line[-1]['top']) < 3:
            current_line.append(w)
        else:
            lines.append(current_line)
            current_line = [w]
    lines.append(current_line)
    
    for line_words in lines:
        text = "".join([w['text'] for w in line_words])
        y = line_words[0]['top']
        
        # Check patterns
        wm = week_pattern.search(text)
        if wm:
             # Look for Title in week header
             title = ""
             # Attempt to extract title from text "第1周Title月"
             # Regex: 第\s*\d+\s*周\s*(.*?)\s*(?:月)?$
             tm = re.search(r'周\s*(.*?)\s*(?:月)?$', text)
             if tm: title = tm.group(1).strip()
             
             headers.append({
                 'y': y, 
                 'type': 'week', 
                 'num': int(wm.group(1)),
                 'title': title,
                 'text': text
             })
             continue
             
        dm = day_pattern.search(text)
        if dm:
             # Extract scripture
             # Text: "第5日创十二至十四章日" -> script: "创十二至十四章"
             scripture = re.sub(r'(日|月)$', '', day_pattern.sub('', text)).strip()
             
             day_str = dm.group(1)
             day_num_match = re.search(r'\d+', day_str)
             day_num = int(day_num_match.group(0)) if day_num_match else 0
             
             headers.append({
                 'y': y, 
                 'type': 'day', 
                 'num': day_num,
                 'label_str': day_str,
                 'scripture': scripture,
                 'text': text
             })
             continue
             
    # Sort by Y
    headers.sort(key=lambda x: x['y'])
    return headers

def extract_data(pdf_path, output_path):
    print(f"Opening {pdf_path}...")
    
    entries = []
    
    # Global state machine
    current_week = 0
    current_week_title = ""
    current_entry = None
    
    verse_pattern = re.compile(r'金句\s*[:：]\s*(.*)')
    
    parsed_count = 0

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"Total pages: {total_pages}")
        
        for i, page in enumerate(pdf.pages):
            # 1. Identify Headers on this page
            page_headers = get_headers(page)
            
            # Define Zones
            # [0, h1.y), [h1.y, h2.y), ... [hn.y, height)
            
            # Safe bounding boxes
            # Crop at h.y - epsilon? 
            # Actually, we want the header to be IN the crop starting at h.y
            
            cuts = [0] + [h['y'] for h in page_headers] + [page.height]
            
            # We align cuts with headers. 
            # Zone 0 corresponds to "Before first header" -> belongs to previous `current_entry`.
            # Zone k (k>0) corresponds to Header k-1.
            
            for k in range(len(cuts) - 1):
                top = cuts[k]
                bottom = cuts[k+1]
                
                if bottom <= top: continue
                
                # Crop zone
                # BBox: (x0, top, x1, bottom)
                crop_rect = (0, top, page.width, bottom)
                zone = page.crop(crop_rect)
                
                # Identify context for this zone
                header_info = None
                if k > 0:
                    header_info = page_headers[k-1]
                
                # Update State if entering a new header zone
                if header_info:
                    if header_info['type'] == 'week':
                        current_week = header_info['num']
                        if header_info['title']:
                            current_week_title = header_info['title']
                        # Week Header doesn't start a new entry usually, 
                        # but it might finish the previous one?
                        # No, usually "Week X" is just a label.
                        # We continue adding to `current_entry`? 
                        # Or does Week Header imply end of previous day?
                        # Yes, visually it breaks the flow.
                        # But technically the previous day might have finished content.
                        # Let's assume Week Header belongs to "General Context" or "New Week Context".
                        # If we have an active `current_entry`, should we close it?
                        # Usually yes. But we close entry when we push it to list.
                        # We push to list when we start a NEW Day Entry.
                        pass
                        
                    elif header_info['type'] == 'day':
                        # New Day!
                        # Push old entry
                        if current_entry:
                            entries.append(current_entry)
                            parsed_count += 1
                        
                        # Create new entry
                        current_entry = {
                            "day_label": f"第{current_week}周 第{header_info['num']}日",
                            "week": current_week,
                            "day": header_info['num'],
                            "title": current_week_title, 
                            "scripture": header_info['scripture'],
                            "content": "",
                            "verse": ""
                        }



                # Extract content from Zone
                
                # 1. Tables in Zone
                zone_tables = zone.find_tables()
                valid_tables = []
                
                if zone_tables:
                    for t_idx, table in enumerate(zone_tables):
                        data = table.extract()
                        if not data: continue
                        
                        # Filter 1x1
                        if len(data) == 1 and len(data[0]) == 1:
                            if len(str(data[0][0])) > 50:
                                continue
                        
                        # Filter Header Text
                        table_str = str(data)
                        if re.search(r'第\s*\d+\s*周', table_str) or re.search(r'第\s*[\d、,]+\s*日', table_str):
                             continue

                        valid_tables.append(table)

                # 2. Text in Zone
                # Filter out text belonging to VALID tables
                def not_inside_tables(obj):
                    # obj and table.bbox are BOTH ABSOLUTE coordinates.
                    x0, top, x1, bottom = obj['x0'], obj['top'], obj['x1'], obj['bottom']
                    mid_x = (x0 + x1) / 2
                    mid_y = (top + bottom) / 2
                    
                    for t in valid_tables:
                        tx0, ttop, tx1, tbottom = t.bbox
                        if tx0 <= mid_x <= tx1 and ttop <= mid_y <= tbottom:
                            return False
                    return True

                filtered_zone = zone.filter(not_inside_tables)
                zone_text = filtered_zone.extract_text()
                
                # 3. Assemble Content (Sort by Y)
                content_items = []
                
                # Add Tables
                for t in valid_tables:
                    content_items.append({
                        'y': t.bbox[1],
                        'type': 'table',
                        'data': t.extract()
                    })
                    
                # Add Text
                if zone_text:
                    # Get Y of text block
                    words = filtered_zone.extract_words()
                    if words:
                        text_top = words[0]['top']
                        content_items.append({
                            'y': text_top,
                            'type': 'text',
                            'text': zone_text
                        })
                
                # Sort
                content_items.sort(key=lambda x: x['y'])
                
                # Process items
                for item in content_items:
                    if item['type'] == 'text':
                        z_lines = item['text'].split('\n')
                        for line in z_lines:
                            line = line.strip()
                            if not line: continue
                            
                            # Check Verse
                            vm = verse_pattern.search(line)
                            if vm:
                                 if current_entry:
                                     current_entry['verse'] = vm.group(1).strip()
                                     current_entry['verse'] = vm.group(1).strip()
                            else:

                                 # Skip header lines
                                 # Relaxed regex to catch "第 周", "第 日" artifacts safely
                                 if re.match(r'第\s*[\d\s]*周', line) or re.match(r'第\s*[\d\s、,]*日', line):
                                     continue
                                 
                                 if current_entry:
                                     # Use space instead of newline to avoid literal \n in content
                                     current_entry['content'] += (" " + line) if current_entry['content'] else line
                                     
                    elif item['type'] == 'table':
                        data = item['data']
                        merged = False
                        
                        # Aggressive Merge: If previous content ends with table, append rows
                        if current_entry and current_entry['content'].strip().endswith('</table>'):
                             # Remove last </table>
                             # Find the last </table>
                             last_close_idx = current_entry['content'].rfind('</table>')
                             if last_close_idx != -1:
                                 # Check if it looks close enough?
                                 # Assume yes for now as they are adjacent in sequence
                                 
                                 # Strip trailing whitespace/newlines before </table> is hard on string
                                 # We slice string up to last_close_idx
                                 base_content = current_entry['content'][:last_close_idx]
                                 
                                 # Construct new rows
                                 new_rows_html = ""
                                 for row in data:
                                    new_rows_html += "<tr>"
                                    for cell in row:
                                        cell_text = str(cell).replace('\n', ' ') if cell else ""
                                        # Check for verse pattern in table cells
                                        if cell and current_entry and not current_entry.get('verse'):
                                            vm = verse_pattern.search(str(cell))
                                            if vm:
                                                current_entry['verse'] = vm.group(1).strip()
                                        new_rows_html += f"<td>{cell_text}</td>"
                                    new_rows_html += "</tr>"
                                 
                                 current_entry['content'] = base_content + new_rows_html + "</table>"
                                 merged = True
                        
                        if not merged:
                            html = "<table>"
                            for row in data:
                                html += "<tr>"
                                for cell in row:
                                    cell_text = str(cell).replace('\n', ' ') if cell else ""
                                    # Check for verse pattern in table cells
                                    if cell and current_entry and not current_entry.get('verse'):
                                        vm = verse_pattern.search(str(cell))
                                        if vm:
                                            current_entry['verse'] = vm.group(1).strip()
                                    html += f"<td>{cell_text}</td>"
                                html += "</tr>"
                            html += "</table>"
                            if current_entry:
                                # Add space before table
                                current_entry['content'] += " " + html

    if current_entry:
        entries.append(current_entry)
        parsed_count += 1
        
    print(f"Extracted {parsed_count} entries.")
    

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    pdf_path = "daily-walk-with-God.pdf"
    output_path = "bibleData.json"
    extract_data(pdf_path, output_path)
