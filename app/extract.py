import pdfplumber
import re
import json
from typing import List, Optional, Dict


def _normalize_text(s: str) -> str:
    """Normalize whitespace in extracted text: collapse runs of whitespace (including newlines)
    into single spaces and strip leading/trailing space.
    """
    if not s:
        return ""
    # replace any run of whitespace (spaces, tabs, newlines) with a single space
    return re.sub(r"\s+", " ", s).strip()


def _detect_day_from_lines(lines: List[str], i: int) -> Optional[Dict]:
    """Detect a 'day' header starting at lines[i].

    Handles cases where the week and day appear on the same line or on two
    consecutive lines. Returns a dict with keys: week (str), day_text (str),
    consumed (int) — number of lines consumed (1 or 2). Returns None if no
    day header detected.
    """
    week_pattern = re.compile(r"第\s*(\d+)\s*周")
    day_pattern = re.compile(r"第\s*([\d、]+)\s*日")

    line = lines[i].strip()
    week_match = week_pattern.search(line)
    day_match = day_pattern.search(line)

    # Case A: both week and day on the same line
    if week_match and day_match:
        week = week_match.group(1)
        day_text = day_match.group(1).replace("、", "-")
        # text between week and day is likely the title
        title_between = line[week_match.end() : day_match.start()].strip()
        title = title_between or None
        # text after day may contain scripture (remove trailing 日/月 markers)
        after = line[day_match.end() :].strip()
        scripture = after.rstrip("日月 ") or None
        return {
            "week": week,
            "day_text": day_text,
            "consumed": 1,
            "header_title": title,
            "header_scripture": scripture,
        }

    # Case B: week on this line, day on next line
    if week_match and i + 1 < len(lines):
        next_line = lines[i + 1].strip()
        next_day_match = day_pattern.search(next_line)
        if next_day_match:
            week = week_match.group(1)
            day_text = next_day_match.group(1).replace("、", "-")
            # title likely follows the week on the current line
            title_after_week = line[week_match.end() :].strip()
            # remove trailing month marker if present
            if title_after_week.endswith("月"):
                title_after_week = title_after_week[:-1].strip()
            header_title = title_after_week or None
            # scripture likely after the day on the next line; strip trailing 日/月
            after = next_line[next_day_match.end() :].strip()
            header_scripture = after.rstrip("日月 ") or None
            return {
                "week": week,
                "day_text": day_text,
                "consumed": 2,
                "header_title": header_title,
                "header_scripture": header_scripture,
            }

    # Case C: day on this line (without week) — sometimes PDFs split week elsewhere
    if day_match and i - 1 >= 0:
        prev_line = lines[i - 1].strip()
        prev_week_match = week_pattern.search(prev_line)
        if prev_week_match:
            week = prev_week_match.group(1)
            day_text = day_match.group(1).replace("、", "-")
            after = line[day_match.end() :].strip()
            header_scripture = after.rstrip("日月 ") or None
            # title may be on previous line after the week
            title_between = prev_line[prev_week_match.end() :].strip()
            if title_between.endswith("月"):
                title_between = title_between[:-1].strip()
            header_title = title_between or None
            return {
                "week": week,
                "day_text": day_text,
                "consumed": 1,
                "header_title": header_title,
                "header_scripture": header_scripture,
            }

    return None


def extract_devotional_data(pdf_path: str) -> List[Dict]:
    all_days: List[Dict] = []
    current_day: Optional[Dict] = None

    verse_pattern = re.compile(r"金句：(.*)")

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = text.split("\n")

            i = 0
            while i < len(lines):
                line = lines[i].strip()
                # detect new day header using helper
                detected = _detect_day_from_lines(lines, i)
                if detected:
                    # save previous day
                    if current_day:
                        # normalize content/reflection before saving
                        current_day["content"] = _normalize_text(
                            current_day.get("content", "")
                        )
                        current_day["reflection"] = _normalize_text(
                            current_day.get("reflection", "")
                        )
                        all_days.append(current_day)

                    week = detected["week"]
                    day_text = detected["day_text"]
                    consumed = detected["consumed"]
                    header_title = detected.get("header_title")
                    header_scripture = detected.get("header_scripture")

                    # title and scripture are expected to follow after the header
                    title_idx = i + consumed
                    scripture_idx = i + consumed + 1
                    # prefer header values when available
                    if header_title:
                        title = header_title
                    else:
                        title = (
                            lines[title_idx].strip() if title_idx < len(lines) else ""
                        )

                    if header_scripture:
                        scripture = header_scripture
                    else:
                        scripture = (
                            lines[scripture_idx].strip()
                            if scripture_idx < len(lines)
                            else ""
                        )

                    current_day = {
                        "day_label": f"第{week}周 第{day_text}日",
                        "title": title,
                        "scripture": scripture,
                        "content": "",
                        "reflection": "",
                        "verse": "",
                    }
                    # advance index: skip header lines plus any title/scripture lines
                    skip = consumed
                    if not header_title:
                        skip += 1
                    if not header_scripture:
                        skip += 1
                    i += skip
                    continue

                if not current_day:
                    i += 1
                    continue

                # 2. detect verse
                verse_match = verse_pattern.search(line)
                if verse_match:
                    current_day["verse"] = verse_match.group(1)
                    # collect subsequent lines as reflection until next day header,
                    # skipping any prompt lines like those starting with "请用" or
                    # containing prompt keywords (思考/提醒/意义)
                    j = i + 1
                    while j < len(lines):
                        nl = lines[j].strip()
                        # stop if a new day header starts here
                        if _detect_day_from_lines(lines, j):
                            break
                        if not nl:
                            j += 1
                            continue
                        if nl.startswith("请用") or any(
                            k in nl for k in ("思考", "提醒", "意义")
                        ):
                            j += 1
                            continue
                        current_day["reflection"] += nl + "\n"
                        j += 1
                    i = j
                    continue

                # 3. previously we treated explicit prompts as reflection, but
                # prompts like "请用"/"思考"/"提醒"/"意义" should be ignored.

                # 4. otherwise append to content (filter out page headers)
                if (
                    line
                    and "PAGE" not in line
                    and line != current_day["title"]
                    and line != current_day["scripture"]
                ):
                    current_day["content"] += line + "\n"

                i += 1

        # append last day
        if current_day:
            current_day["content"] = _normalize_text(current_day.get("content", ""))
            current_day["reflection"] = _normalize_text(
                current_day.get("reflection", "")
            )
            all_days.append(current_day)

    return all_days


def extract_from_text(text: str) -> List[Dict]:
    """Extract devotional data from plain text (useful for tests or text inputs).

    The text should be the concatenated pages of the document; the function
    will split into lines and reuse the same parsing logic as the PDF extractor.
    """
    all_days: List[Dict] = []
    current_day: Optional[Dict] = None

    verse_pattern = re.compile(r"金句：(.*)")

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        detected = _detect_day_from_lines(lines, i)
        if detected:
            if current_day:
                # normalize content/reflection before saving
                current_day["content"] = _normalize_text(current_day.get("content", ""))
                current_day["reflection"] = _normalize_text(
                    current_day.get("reflection", "")
                )
                all_days.append(current_day)

            week = detected["week"]
            day_text = detected["day_text"]
            consumed = detected["consumed"]
            header_title = detected.get("header_title")
            header_scripture = detected.get("header_scripture")

            title_idx = i + consumed
            scripture_idx = i + consumed + 1

            if header_title:
                title = header_title
            else:
                title = lines[title_idx].strip() if title_idx < len(lines) else ""

            if header_scripture:
                scripture = header_scripture
            else:
                scripture = (
                    lines[scripture_idx].strip() if scripture_idx < len(lines) else ""
                )

            current_day = {
                "day_label": f"第{week}周 第{day_text}日",
                "title": title,
                "scripture": scripture,
                "content": "",
                "reflection": "",
                "verse": "",
            }
            # advance index: skip header lines plus any title/scripture lines
            skip = consumed
            if not header_title:
                skip += 1
            if not header_scripture:
                skip += 1
            i += skip
            continue

        if not current_day:
            i += 1
            continue

        verse_match = verse_pattern.search(line)
        if verse_match:
            current_day["verse"] = verse_match.group(1)
            # collect subsequent lines as reflection until next day header,
            # skipping any prompt lines like those starting with "请用" or
            # containing prompt keywords (思考/提醒/意义)
            j = i + 1
            while j < len(lines):
                nl = lines[j].strip()
                # stop if a new day header starts here
                if _detect_day_from_lines(lines, j):
                    break
                if not nl:
                    j += 1
                    continue
                if nl.startswith("请用") or any(
                    k in nl for k in ("思考", "提醒", "意义")
                ):
                    j += 1
                    continue
                current_day["reflection"] += nl + "\n"
                j += 1
            i = j
            continue

        if (
            line
            and "PAGE" not in line
            and line != current_day["title"]
            and line != current_day["scripture"]
        ):
            current_day["content"] += line + "\n"

        i += 1

    if current_day:
        current_day["content"] = _normalize_text(current_day.get("content", ""))
        current_day["reflection"] = _normalize_text(current_day.get("reflection", ""))
        all_days.append(current_day)

    return all_days


# If run as a script, run extraction using a default file name
if __name__ == "__main__":
    pdf_file = "daily-walk-with-God.pdf"
    data = extract_devotional_data(pdf_file)

    # write JSON
    with open("bibleData.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"成功提取了 {len(data)} 天的内容！已保存至 bibleData.json")
