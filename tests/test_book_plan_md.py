import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from build_book_plan import md_to_html  # noqa: E402


def test_paragraph_then_list_in_one_block():
    html = md_to_html('**1. Two views.** Scholars differ:\n- **A** first\n- **B** second')
    assert html == ('<p><strong>1. Two views.</strong> Scholars differ:</p>\n'
                    '<ul><li><strong>A</strong> first</li><li><strong>B</strong> second</li></ul>')


def test_list_then_closing_paragraph_in_one_block():
    html = md_to_html('Intro:\n- one\n- two\nEither way, the point holds.')
    assert html == '<p>Intro:</p>\n<ul><li>one</li><li>two</li></ul>\n<p>Either way, the point holds.</p>'


def test_plain_paragraph_lines_are_joined():
    assert md_to_html('line one\nline two') == '<p>line one line two</p>'
