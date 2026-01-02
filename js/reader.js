/**
 * Swipeable Bible Reader Logic
 * Handles scripture parsing, XML fetching, and Swipe UI management.
 */

const Reader = {
    // Book abbreviation map (Chinese -> ID 1-66)
    bookMap: {
        '创': 1, '出': 2, '利': 3, '民': 4, '申': 5,
        '书': 6, '士': 7, '得': 8, '撒上': 9, '撒下': 10,
        '王上': 11, '王下': 12, '代上': 13, '代下': 14, '拉': 15,
        '尼': 16, '斯': 17, '伯': 18, '诗': 19, '箴': 20,
        '传': 21, '歌': 22, '赛': 23, '耶': 24, '哀': 25,
        '结': 26, '但': 27, '何': 28, '珥': 29, '摩': 30,
        '俄': 31, '拿': 32, '弥': 33, '鸿': 34, '哈': 35,
        '番': 36, '该': 37, '亚': 38, '玛': 39,
        '太': 40, '可': 41, '路': 42, '约': 43, '徒': 44,
        '罗': 45, '林前': 46, '林后': 47, '加': 48, '弗': 49,
        '腓': 50, '西': 51, '帖前': 52, '帖后': 53, '提前': 54,
        '提后': 55, '多': 56, '门': 57, '来': 58, '雅': 59,
        '彼前': 60, '彼后': 61, '约一': 62, '约二': 63, '约三': 64,
        '犹': 65, '启': 66
    },

    // Convert Chinese number string to Integer
    chineseToArabic: function(cnNum) {
        if (!cnNum) return 0;
        const map = {
            '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, 
            '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
            '十': 10, '廿': 20, '卅': 30, '百': 100
        };
        
        let result = 0;
        let temp = 0; // For handling units like '百' if needed, but simplified here
        
        // Simple parsing for 1-99 range common in chapter numbers
        if (cnNum.startsWith('百')) return 100 + this.chineseToArabic(cnNum.substring(1));
        
        // Handle standard format: 
        // 一 (1), 十 (10), 十一 (11), 二十 (20), 廿一 (21), 一百 (100)
        
        let sum = 0;
        let i = 0;
        while (i < cnNum.length) {
            let val = map[cnNum[i]];
            
            if (val === 10 || val === 20 || val === 30) {
                 // if it's 10, 20, 30
                 if (i === 0) {
                     sum += val;
                 } else {
                     // Check if previous was a multiplier? 
                     // Usually format is "二十一" -> 二(2) 十(10) 一(1). 
                     // But simplified bible often uses "廿" for 20.
                     // Our map handles 廿 as 20.
                     // If we have "二十", Chinese logic: 2*10. This simplistic function might fail on "二十". 
                     // Let's use a simpler known strategy for Bible chapters.
                 }
            } 
            i++;
        }
        
        // Re-implementing a robust version based on common patterns
        // Patterns:
        // 1-10: 一..十
        // 11-19: 十一..十九
        // 20-99: 廿..廿九, 卅..卅九 OR 二十..九十九
        // 100+: 一百..
        
        let total = 0;
        
        // Check for hundred
        if (cnNum.indexOf('百') > -1) {
            let parts = cnNum.split('百');
            let hundreds = map[parts[0]] || 1; // "一百" vs "百"
            total += hundreds * 100;
            cnNum = parts[1];
            if (!cnNum) return total;
        }
        
        // Handle 廿, 卅 special chars
        if (cnNum.startsWith('廿')) {
            total += 20;
            cnNum = cnNum.substring(1);
        } else if (cnNum.startsWith('卅')) {
            total += 30;
            cnNum = cnNum.substring(1);
        }
        
        // Handle 十
        if (cnNum.indexOf('十') > -1) {
            let parts = cnNum.split('十');
            let tens = parts[0] ? map[parts[0]] : 1; // "二十" -> 2, "十" -> 1
            total += tens * 10;
            cnNum = parts[1];
        }
        
        if (cnNum) {
            total += map[cnNum] || 0;
        }
        
        return total;
    },

    /**
     * Parse scripture string into object
     * @param {string} scripture e.g. "创一至二章", "创48:21", "诗102"
     * @returns {object|null} { bookId: number, startChapter: number, endChapter: number }
     */
    parseScripture: function(scripture) {
        if (!scripture) return null;
        
        // 1. Identify Book
        // Sort keys by length desc to match "撒母耳记上" before "撒"
        const books = Object.keys(this.bookMap).sort((a, b) => b.length - a.length);
        let bookAbbr = null;
        let remaining = scripture;
        
        for (const book of books) {
            if (scripture.startsWith(book)) {
                bookAbbr = book;
                remaining = scripture.substring(book.length).trim();
                break;
            }
        }
        
        if (!bookAbbr) return null; // Can't identify book
        const bookId = this.bookMap[bookAbbr];
        
        // 2. Parse Chapter/Range
        let startChap = 1;
        let endChap = 1;
        
        // Case A: Arabic Numbers (e.g. "1-2", "48:21", "102")
        // Check if starts with digit
        if (/^\d/.test(remaining)) {
            // Regex for: Start([:.]Verse)? (- End([:.]Verse)?)?
            const match = remaining.match(/^(\d+)(?:[:\.]\d+)?(?:-(\d+)(?:[:\.]\d+)?)?/);
            if (match) {
                startChap = parseInt(match[1]);
                if (match[2]) {
                    endChap = parseInt(match[2]);
                } else {
                    endChap = startChap;
                }
            }
        } 
        // Case B: Chinese Numbers (e.g. "一至二章", "一章", "一百一十九篇")
        else {
            // Remove "章", "篇" suffix
            remaining = remaining.replace(/[章篇]/g, '');
            
            // Split by "至" (to)
            const parts = remaining.split('至');
            startChap = this.chineseToArabic(parts[0].trim());
            
            if (parts.length > 1) {
                endChap = this.chineseToArabic(parts[1].trim());
            } else {
                endChap = startChap;
            }
        }
        
        return {
            bookId: bookId,
            bookName: bookAbbr,
            startChapter: startChap,
            endChapter: endChap
        };
    },

    // Initialization
    init: function() {
        this.track = document.getElementById('reader-track');
        this.dots = document.querySelectorAll('.nav-dot');
        this.currentPanel = 0; // 0: Bible, 1: Devotional
        
        // Touch handling
        let startX = 0;
        let currentX = 0;
        const threshold = 50;
        
        const container = document.querySelector('.reader-container');
        
        if (container) {
            container.addEventListener('touchstart', (e) => {
                startX = e.touches[0].clientX;
            }, {passive: true});
            
            container.addEventListener('touchend', (e) => {
                const diff = startX - e.changedTouches[0].clientX;
                if (Math.abs(diff) > threshold) {
                    if (diff > 0) {
                        // Swipe Left: Next Panel
                        this.goToPanel(Math.min(this.currentPanel + 1, 1));
                    } else {
                        // Swipe Right: Prev Panel
                        this.goToPanel(Math.max(this.currentPanel - 1, 0));
                    }
                }
            }, {passive: true});
        }
        
        console.log("Reader initialized.");
    },
    
    // Switch panels
    goToPanel: function(index) {
        if (!this.track) this.init();
        
        this.currentPanel = index;
        // Panel 0: 0%, Panel 1: -50% (since width is 200%)
        // Wait, width is 200%. Panel 0 is first 50%. Panel 1 is second 50%.
        // To show Panel 0: input 0 -> translateX(0)
        // To show Panel 1: input 1 -> translateX(-50%)
        const translate = index * -50;
        this.track.style.transform = `translateX(${translate}%)`;
        
        // Update dots
        this.dots.forEach((dot, i) => {
            if (i === index) dot.classList.add('active');
            else dot.classList.remove('active');
        });
        
        // Scroll to top of panel?
        // document.getElementById(index === 0 ? 'bible-panel' : 'devotional-panel').scrollTop = 0;
    },
    
    // Render Bible Text
    renderBible: async function(scriptureStr) {
        const container = document.getElementById('full-scripture-content');
        if (!container) return;
        
        container.innerHTML = '<div style="color:#666; padding:20px; text-align:center;">加载中...</div>';
        
        const parsed = this.parseScripture(scriptureStr);
        if (!parsed) {
            container.innerHTML = `<div style="padding:20px; color:#666;">无法解析经文: ${scriptureStr}</div>`;
            return;
        }
        
        const xml = await window.loadBibleXML(); // Assume global function exists
        if (!xml) {
            container.innerHTML = '<div style="color:red;">无法加载圣经数据XML</div>';
            return;
        }
        
        let html = '';
        const bookNode = xml.querySelector(`book[number="${parsed.bookId}"]`);
        
        if (!bookNode) {
            container.innerHTML = `<div style="color:red;">未找到书卷 ID: ${parsed.bookId}</div>`;
            return;
        }
        
        // Loop through chapters
        for (let c = parsed.startChapter; c <= parsed.endChapter; c++) {
            const chapterNode = bookNode.querySelector(`chapter[number="${c}"]`);
            if (chapterNode) {
                html += `<div class="bible-chapter">
                    <h3>${parsed.bookName} 第${c}章</h3>`;
                
                const verses = chapterNode.querySelectorAll('verse');
                verses.forEach(v => {
                    const num = v.getAttribute('number');
                    const text = v.textContent;
                    html += `<div class="bible-verse">
                        <span class="verse-num">${num}</span>${text}
                    </div>`;
                });
                
                html += `</div>`;
            }
        }
        
        container.innerHTML = html || '<div>未找到经文内容</div>';
    }
};

// Expose to window
window.Reader = Reader;
