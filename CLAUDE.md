# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

"每天与主同行" (Daily Walk With The Lord) — a Chinese devotional Bible reading PWA. It combines a vanilla JS frontend with a Python data processing pipeline that converts a PDF into structured JSON data served by the app.

## Commands

```bash
# Setup
make venv        # Create Python virtual environment (.venv)
make install     # Install dependencies (pdfplumber, requests)

# Development
make run         # Start HTTP server on port 8000 (or PORT=XXXX make run)
python -m pytest tests/   # Run tests

# Data pipeline
make publish     # Full pipeline: extract → normalize → fix → format → apply-fixes → populate
make extract     # Extract Bible data from PDF to bibleData.json
make fix-tables  # Fix merged tables in bibleData.json
make populate-verses  # Add verse text from ChineseSimplifiedBible.xml
make format-heuristic # Pattern-based formatting (fast)
make format-llm  # LLM-based formatting via Ollama (qwen2.5:1.5b, slower but ~95% accuracy)
```

## Architecture

### Frontend (PWA)
- **index.html** — entry point, Chinese-language mobile-first layout
- **js/reader.js** — core app logic: swipe navigation between days, Chinese number parsing (e.g. "廿" → 20), 66-book Bible mapping, verse display
- **sw.js** — service worker with cache-first for assets, network-first for `bibleData.json`; cache key `wwg-v3`
- **manifest.json** — PWA manifest for installability

### Data
- **bibleData.json** — the main data file (~1.1MB), 365 daily entries with fields: `day`, `week`, `title`, `scripture`, `content` (HTML), `verse`, `verse_text`, `verse_parts`
- **ChineseSimplifiedBible.xml** — full Chinese Bible source used to populate `verse_text`

### Python Backend & Pipeline
- **app/server.py** — stdlib HTTP server, serves the repo root at port 8000
- **scripts/** — data processing pipeline run in order by `make publish`:
  1. `extract_bible_data.py` — PDF extraction with `pdfplumber`
  2. `normalize_verse_refs.py` — clean scripture references
  3. `fix_table_splits.py` — repair rows split across PDF pages
  4. `apply_formatting.py` / `format_content_llm.py` — format HTML content
  5. `apply_manual_fixes.py` — handcrafted corrections
  6. `add_verse_text_v2.py` — populate verse text from XML

### Deployment
- GitHub Actions (`.github/workflows/pages-deploy.yml`) auto-deploys the full repo to `gh-pages` on push to `main`.

## gstack

Use the `/browse` skill from gstack for all web browsing. Never use `mcp__claude-in-chrome__*` tools.

Available skills: `/office-hours`, `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/design-consultation`, `/review`, `/ship`, `/land-and-deploy`, `/canary`, `/benchmark`, `/browse`, `/qa`, `/qa-only`, `/design-review`, `/setup-browser-cookies`, `/setup-deploy`, `/retro`, `/investigate`, `/document-release`, `/codex`, `/careful`, `/freeze`, `/guard`, `/unfreeze`, `/gstack-upgrade`.
