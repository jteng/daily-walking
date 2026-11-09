import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from verse_refs import add_book_to_refs  # noqa: E402


def test_bare_same_book_reference_gets_book_name():
    assert add_book_to_refs('只在这里（3:3、5）用这个词', '约', 'zh') == '只在这里（约3:3、5）用这个词'


def test_reference_with_book_name_is_unchanged():
    assert add_book_to_refs('（民21:9）', '约', 'zh') == '（民21:9）'


def test_bare_reference_after_other_book_in_list_inherits_it():
    assert add_book_to_refs('（林前9:1；15:8）', '徒', 'zh') == '（林前9:1；林前15:8）'


def test_words_between_references_stop_inheritance():
    assert (add_book_to_refs('(probably Ps 41:9, quoted at 13:18)', 'John', 'en')
            == '(probably Ps 41:9, quoted at John 13:18)')


def test_section_headings_are_left_alone():
    assert add_book_to_refs('## 深读 3:1-21 重生', '约', 'zh') == '## 深读 3:1-21 重生'


def test_english_bare_reference_and_ranges():
    assert add_book_to_refs('(cf. 20:23) and (3:15–16)', 'Acts', 'en') == '(cf. Acts 20:23) and (Acts 3:15–16)'
