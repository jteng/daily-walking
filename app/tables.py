"""Utilities to detect tables in PDFs and append them to extracted content.

This module uses pdfplumber's table detection to find tables on each page,
convert them to Markdown or HTML, and append them into the `content` field
of the extracted devotional data. It uses the same header-detection helper from
`app.extract` to map pages to day entries.
"""

from typing import List, Dict, Any, Optional
import html

import pdfplumber

from app.extract import _detect_day_from_lines, _normalize_text


def find_tables_in_pdf(
    pdf_path: str, table_settings: Optional[dict] = None
) -> Dict[int, List[List[List[str]]]]:
    """Return tables found on each page of the PDF.

    Returns a mapping: page_number (0-based) -> list of tables, where each table
    is a list of rows and each row is a list of cell strings.
    """
    if table_settings is None:
        table_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "lines",
            "intersection_tolerance": 5,
            "snap_tolerance": 3,
            "join_tolerance": 3,
        }

    page_tables: Dict[int, List[List[List[str]]]] = {}
    with pdfplumber.open(pdf_path) as pdf:
        for pno, page in enumerate(pdf.pages):
            tables = []
            found = page.find_tables(table_settings=table_settings)
            for table in found:
                try:
                    rows = table.extract()
                except Exception:
                    # fallback to page.extract_table for this table
                    rows = page.extract_table()
                if rows:
                    # normalize cell values to strings
                    norm_rows = [[(cell or "").strip() for cell in row] for row in rows]
                    tables.append(norm_rows)
            if tables:
                page_tables[pno] = tables
    return page_tables


def table_to_markdown(table: List[List[str]]) -> str:
    """Convert a 2D table (list of rows) to GitHub-flavored Markdown table.

    If the table has at least one row, use the first row as header.
    """
    if not table:
        return ""
    rows = table

    # Escape pipes in content
    def esc(s: str) -> str:
        return s.replace("|", "\\|")

    header = rows[0]
    md = "| " + " | ".join(esc(c) for c in header) + " |\n"
    md += "|" + " --- |" * len(header) + "\n"
    for r in rows[1:]:
        md += "| " + " | ".join(esc(c) for c in r) + " |\n"
    return md


def table_to_html(table: List[List[str]]) -> str:
    """Convert a 2D table to simple HTML table string."""
    if not table:
        return ""
    html_parts = ["<table>"]
    # header
    header = table[0]
    html_parts.append(
        "  <thead>\n    <tr>"
        + "".join(f"<th>{html.escape(c)}</th>" for c in header)
        + "</tr>\n  </thead>"
    )
    html_parts.append("  <tbody>")
    for r in table[1:]:
        html_parts.append(
            "    <tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in r) + "</tr>"
        )
    html_parts.append("  </tbody>")
    html_parts.append("</table>")
    return "\n".join(html_parts)


def append_tables_to_content(
    pdf_path: str,
    data: List[Dict[str, Any]],
    use_html: bool = True,
    table_settings: Optional[dict] = None,
) -> List[Dict[str, Any]]:
    """Find tables in `pdf_path` and append them into `data` content fields.

    The function maps page -> first day found on that page (if any) using the
    same `_detect_day_from_lines` helper. Tables on a page are appended to the
    content of that day. If no day exists on the page, tables are appended to
    the last day found before that page.

    Args:
        pdf_path: path to PDF file
        data: list of day dicts produced by extract_devotional_data
        use_html: if True, append HTML tables; otherwise append Markdown tables
        table_settings: optional pdfplumber table_settings

    Returns the modified `data` (same list instance returned for convenience).
    """
    page_tables = find_tables_in_pdf(pdf_path, table_settings=table_settings)
    if not page_tables:
        return data

    # Build mapping of page -> day_index by scanning pages for day headers
    page_to_day_idx: Dict[int, Optional[int]] = {}
    day_idx = 0
    with pdfplumber.open(pdf_path) as pdf:
        for pno, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            lines = text.split("\n")
            found_day_on_page = False
            for i, _ in enumerate(lines):
                if _detect_day_from_lines(lines, i):
                    page_to_day_idx[pno] = day_idx
                    day_idx += 1
                    found_day_on_page = True
                    break
            if not found_day_on_page:
                page_to_day_idx[pno] = None

    # Now assign tables to days.
    # NOTE: per user request, only include tables if the page contains a
    # day header (i.e. mapped -> not None). Tables on pages without a day
    # header are skipped rather than attached to the previous day.
    for pno in sorted(page_tables.keys()):
        mapped = page_to_day_idx.get(pno)
        if mapped is None:
            # skip tables on pages that don't have an explicit day header
            continue

        target_idx = mapped
        if target_idx >= len(data):
            # out-of-range day index
            continue

        for table in page_tables[pno]:
            # Remove overlapping plain-text snippets from the day's content
            # if they match table cell texts. This is a best-effort dedupe:
            # for each non-empty cell string, remove exact occurrences from
            # the content before appending the table markup.
            content = data[target_idx].get("content", "") or ""
            for row in table:
                for cell in row:
                    cell_text = (cell or "").strip()
                    if not cell_text:
                        continue
                    # remove exact occurrences; replace with a single space
                    if cell_text in content:
                        content = content.replace(cell_text, " ")

            # normalize cleaned content and put it back
            content = _normalize_text(content)
            data[target_idx]["content"] = content

            # build markup and append
            if use_html:
                markup = table_to_html(table)
            else:
                markup = table_to_markdown(table)

            # append with separators then normalize
            data[target_idx]["content"] = _normalize_text(
                (data[target_idx].get("content", "") or "") + " \n\n " + markup
            )
            data[target_idx]["reflection"] = _normalize_text(
                data[target_idx].get("reflection", "")
            )

    return data
