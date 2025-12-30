.PHONY: help venv install run extract clean

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

clean: ## Remove common build/test artifacts
	rm -rf __pycache__ .pytest_cache build dist *.egg-info
