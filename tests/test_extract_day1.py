from app import extract


def test_extract_day1_from_text_file():
    # read the provided day1.txt (in tests/)
    with open("tests/day1.txt", "r", encoding="utf-8") as f:
        text = f.read()

    data = extract.extract_from_text(text)
    assert data, "No data extracted"
    day1 = data[0]

    assert day1["title"] == "起初，神创造"
    assert day1["scripture"] == "创一至二章"

    # content should contain the opening question
    assert "创世记讲些什么？简单来说" in day1["content"]

    # key verse (金句)
    assert "创世记一章廿六至廿七节" in day1["verse"]
    assert "二章七节" in day1["verse"]

    # reflection should contain the paragraph starting with 「起初神创造天地」
    assert "起初神创造天地" in day1["reflection"]
