
import json
import re

# List of inspirational Sabbath messages (Cycling)
SABBATH_MESSAGES = [
    {
        "title": "安息日：安息与更新 (Rest and Renewal)",
        "content": """
        <div class="sabbath-message">
            <h3>安息与更新</h3>
            <p>「你们要休息，要知道我是神。」(诗篇 46:10)</p>
            <p>今天是安息日，是由神所设立的礼物。在这忙碌的一周之后，请停下脚步，在主的同在里得着安息。</p>
            <p>建议：</p>
            <ul>
                <li>回顾过去一周神的恩典。</li>
                <li>选择一卷你最喜爱的经文细细品读。</li>
                <li>为着下周的挑战向神祷告。</li>
            </ul>
            <p><em>"Be still, and know that I am God." (Psalm 46:10)</em></p>
            <p>Today is the Sabbath, a gift from God. After a busy week, pause and find rest in His presence.</p>
        </div>
        """
    },
    {
        "title": "安息日：记念神的创造 (Remembering Creation)",
        "content": """
        <div class="sabbath-message">
            <h3>记念神的创造</h3>
            <p>「因为六日之内，耶和华造天、地、海，和其中的万物，第七日便安息了。」(出埃及记 20:11)</p>
            <p>安息日让我们记念神伟大的创造工作。看看窗外的天空、树木，或此时此刻的宁静，感谢神创造的美好。</p>
            <p>建议：</p>
            <ul>
                <li>走到户外，欣赏神的创造。</li>
                <li>为着生命的奇妙献上赞美。</li>
            </ul>
            <p><em>The Sabbath reminds us of God's great work of creation. Look at the sky and nature, and thank Him for His beauty.</em></p>
        </div>
        """
    },
    {
        "title": "安息日：在主里得自由 (Freedom in Him)",
        "content": """
        <div class="sabbath-message">
            <h3>在主里得自由</h3>
            <p>「主耶和华的灵在我身上……报告被掳的得释放，被囚的出监牢。」(以赛亚书 61:1)</p>
            <p>安息日不仅仅是身体的休息，更是心灵的释放。放下心中的重担、焦虑和罪咎，在基督里得着完全的自由。</p>
            <p>今天，你可以自由地敬拜祂，单单享受祂的爱。</p>
            <p><em>The Sabbath is not just physical rest, but spiritual freedom. Lay down your burdens and find freedom in Christ.</em></p>
        </div>
        """
    },
    {
        "title": "安息日：属灵的加油站 (Spiritual Refuelling)",
        "content": """
        <div class="sabbath-message">
            <h3>属灵的加油站</h3>
            <p>「得力在乎平静安稳。」(以赛亚书 30:15)</p>
            <p>就像汽车需要加油，我们的灵人也需要补给。不要急着奔跑，先在神的面前重新得力。</p>
            <p>建议今天花更多时间敬拜和赞美。</p>
            <p><em>"In quietness and in confidence shall be your strength." (Isaiah 30:15) Recharge your spirit in God's presence today.</em></p>
        </div>
        """
    },
    {
        "title": "安息日：数算恩典 (Count Your Blessings)",
        "content": """
        <div class="sabbath-message">
            <h3>数算恩典</h3>
            <p>「我的心哪，你要称颂耶和华！不可忘记他的一切恩惠！」(诗篇 103:2)</p>
            <p>这一周，神在你身上做了什么？有没有什么微小的事情显明了祂的看顾？</p>
            <p>花一点时间，写下三件你要感谢神的事情。</p>
            <p><em>"Bless the LORD, O my soul, and forget not all his benefits!" (Psalm 103:2) Take a moment to list three things you are grateful for this week.</em></p>
        </div>
        """
    },
        {
        "title": "安息日：专注于神 (Focus on God)",
        "content": """
        <div class="sabbath-message">
            <h3>专注于神</h3>
            <p>「你们要思念上面的事，不要思念地上的事。」(歌罗西书 3:2)</p>
            <p>世界充满了噪音和干扰。安息日是一个将频道调回「神」的机会。</p>
            <p>关掉不必要的电子设备，打开圣经，聆听祂微小的声音。</p>
            <p><em>"Set your minds on things above, not on earthly things." (Colossians 3:2) Tune out the noise of the world and tune in to God.</em></p>
        </div>
        """
    }
]

def process_bible_data(json_path):
    print(f"Processing {json_path} with Sabbath messages...")
    
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
        week_entries.sort(key=lambda x: x['day'])
        
        # Determine Sabbath Message for this week (Cycle through list)
        msg_index = (w - 1) % len(SABBATH_MESSAGES)
        sabbath_msg = SABBATH_MESSAGES[msg_index]
        
        # Ensure Day 7 exists and update it
        # First, filter out existing Day 7 if we are going to overwrite/ensure it matches our spec
        # Actually, let's find it.
        day7_entry = next((e for e in week_entries if e['day'] == 7), None)
        
        if not day7_entry:
            day7_entry = {
                "week": w,
                "day": 7,
                "scripture": "",
                "verse": ""
            }
            week_entries.append(day7_entry)
        
        # FORCE Update Day 7 content
        day7_entry['title'] = sabbath_msg['title']
        day7_entry['content'] = sabbath_msg['content']
        # Maybe add a generic "Read your favorite chapter" Note if not implicit
        
        # Re-sort because we might have appended
        week_entries.sort(key=lambda x: x['day'])
        
        # Add to new_data with updated labels
        for d in range(1, 8):
            current_entry = next((e for e in week_entries if e['day'] == d), None)
            
            if current_entry:
                # Update Label
                current_entry['day_label'] = f"第 {global_day_count} / 365 天"
                new_data.append(current_entry)
                global_day_count += 1

    print(f"Processed {len(new_data)} entries.")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_bible_data("bibleData.json")
