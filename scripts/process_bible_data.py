
import json
import re

def process_bible_data(json_path):
    print(f"Processing {json_path}...")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 1. Group by Week
    weeks = {}
    for entry in data:
        w = entry['week']
        if w not in weeks:
            weeks[w] = []
        weeks[w].append(entry)
    
    new_data = []
    
    # Process weeks 1 to 52 (or max)
    max_week = max(weeks.keys())
    
    global_day_count = 1
    
    for w in range(1, max_week + 1):
        week_entries = weeks.get(w, [])
        
        # Sort by day
        week_entries.sort(key=lambda x: x['day'])
        
        # Check days 1-6 existence (optional, but good to know)
        existing_days = {e['day'] for e in week_entries}
        
        # Add existing entries to new list, updating labels
        for d in range(1, 8):
            
            # Find entry if exists
            current_entry = next((e for e in week_entries if e['day'] == d), None)
            
            if d == 7:
                if not current_entry:
                    # Create Sabbath Day
                    current_entry = {
                        "day_label": "", # Will set below
                        "week": w,
                        "day": 7,
                        "title": "安息日 (Sabbath Day)",
                        "scripture": "",
                        "content": "<p>今天是安息日，请休息并在主里安息。</p><p>Today is the Sabbath day. Please rest and find peace in the Lord.</p>",
                        "verse": ""
                    }
                else:
                    # Update existing Day 7 if it was somehow there but maybe empty? 
                    # User request: "can we explictly make day 7 the sabbath day? let's add day 7s back in the mix"
                    # If Day 7 exists, we might want to override it or keep it?
                    # The user implies it IS missing ("current plan has a rest day on day 7... let's add day 7s back").
                    # So likely it's missing. If present, we probably shouldn't nuke it unless it's empty.
                    # I'll preserve existing content if meaningful, but ensure title is Sabbath-like if it looks like a placeholder.
                    # Actually, for safety, if there is a Day 7, I'll trust it. 
                    # But based on my check earlier, there were NO Day 7s.
                    pass
            
            if current_entry:
                # Update Label
                # User wants: "Day # of 365"
                # Chinese: "第 # / 365 天"
                current_entry['day_label'] = f"第 {global_day_count} / 365 天"
                
                # Add to new list
                new_data.append(current_entry)
                
                global_day_count += 1
            else:
                # Missing day (not 7), skipping? Or should we fill gap?
                # User didn't ask to fill gaps 1-6. 
                pass

    print(f"Processed {len(new_data)} entries.")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_bible_data("bibleData.json")
