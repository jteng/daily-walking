from app import extract


def test_detect_day_on_two_lines():
    # Simulate the two-line pattern from the user's example
    lines = [
        "第  52周  保守你的心  月",
        "第  6、7日  箴言选读  日",
    ]

    # detect starting at index 0 should find week=52 and day_text=6-7 and consume 2 lines
    detected = extract._detect_day_from_lines(lines, 0)
    assert detected is not None
    assert detected["week"] == "52"
    assert detected["day_text"] == "6-7"
    assert detected["consumed"] == 2


def test_detect_day_on_single_line():
    # Both week and day on same line
    lines = ["第  12周 第 3日 标题 经文"]
    detected = extract._detect_day_from_lines(lines, 0)
    assert detected is not None
    assert detected["week"] == "12"
    assert detected["day_text"] == "3"
    assert detected["consumed"] == 1
