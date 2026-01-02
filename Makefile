.PHONY: help venv install run extract populate-verses clean publish

help: ## Show this help message with available targets
	@grep -E '^[a-zA-Z0-9_\-]+:.*?##' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "} {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

venv: ## Create a virtual environment in .venv (if missing)
	@test -d .venv || python3 -m venv .venv

install: venv ## Install dependencies from requirements.txt into .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run: venv ## Run the app server (optional: set PORT environment variable)
	. .venv/bin/activate && PORT=$${PORT:-8000} python -m app.server

extract: venv ## Extract Bible data from PDF to bibleData.json
	.venv/bin/python scripts/extract_bible_data.py
	.venv/bin/python scripts/fix_table_splits.py

fix-tables: venv ## Fix merged tables in bibleData.json
	.venv/bin/python scripts/fix_table_splits.py

populate-verses: venv ## Add verse text from ChineseSimplifiedBible.xml to bibleData.json
	.venv/bin/python scripts/add_verse_text_v2.py

format-llm: venv ## Format all entries using local LLM (requires Ollama running)
	.venv/bin/python scripts/format_content_llm.py --all --model qwen2.5:1.5b

format-heuristic: venv ## Format all entries using heuristic rules (fast, no LLM required)
	.venv/bin/python scripts/apply_formatting.py

publish: venv ## Prepare data for publishing (extract → normalize → fix tables → format → manual fixes → populate verses)
	@echo "📚 Step 1/6: Extracting data from PDF..."
	.venv/bin/python scripts/extract_bible_data.py
	@echo "✓ Extraction complete"
	@echo ""
	@echo "🔢 Step 2/6: Normalizing verse references..."
	.venv/bin/python scripts/normalize_verse_refs.py
	@echo "✓ Normalization complete"
	@echo ""
	@echo "🔧 Step 3/6: Fixing table splits..."
	.venv/bin/python scripts/fix_table_splits.py
	@echo "✓ Table fixes complete"
	@echo ""
	@echo "✨ Step 4/6: Formatting content (heuristic)..."
	.venv/bin/python scripts/apply_formatting.py
	@echo "✓ Formatting complete"
	@echo ""
	@echo "�️  Step 5/6: Applying manual fixes..."
	.venv/bin/python scripts/apply_manual_fixes.py
	@echo "✓ Manual fixes complete"
	@echo ""
	@echo "�📖 Step 6/6: Populating verse text..."
	.venv/bin/python scripts/add_verse_text_v2.py
	@echo "✓ Verse population complete"
	@echo ""
	@echo "✅ Data preparation complete! Run 'make run' to start the server."

clean: ## Remove common build/test artifacts
	rm -rf __pycache__ .pytest_cache build dist *.egg-info
