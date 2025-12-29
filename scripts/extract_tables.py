#!/usr/bin/env python3
"""Script wrapper to extract devotional data and append detected tables.

Reads environment variables:
  FILE - path to PDF (default: daily-walk-with-God.pdf)
  OUT  - output JSON (default: bibleData_with_tables.json)
  USE_HTML - '0' for markdown, otherwise HTML (default: '1')

This script is designed to be run from the Makefile using the venv's python
to ensure required packages in the venv are used.
"""

import os
import json
import sys
from pathlib import Path

# Ensure repo root is on sys.path so `from app import ...` works when running
# the script with the venv python (similar to tests/conftest.py).
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main():
    pdf = os.environ.get("FILE", "daily-walk-with-God.pdf")
    out = os.environ.get("OUT", "bibleData_with_tables.json")
    use_html = os.environ.get("USE_HTML", "1") != "0"

    try:
        from app import extract, tables
    except Exception:
        print(
            "Failed to import app modules (is the venv active and dependencies installed?)",
            file=sys.stderr,
        )
        raise

    data = extract.extract_devotional_data(pdf)
    data = tables.append_tables_to_content(pdf, data, use_html=use_html)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Wrote", out)


if __name__ == "__main__":
    main()
