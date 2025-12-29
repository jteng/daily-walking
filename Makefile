.PHONY: help venv install run test pycompile clean

help: ## Show this help message with available targets
	@grep -E '^[a-zA-Z0-9_\-]+:.*?##' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "} {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

venv: ## Create a virtual environment in .venv (if missing)
	@test -d .venv || python3 -m venv .venv

install: venv ## Install dependencies from requirements.txt into .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run: venv ## Run the app server (optional: set PORT environment variable)
	. .venv/bin/activate && PORT=$${PORT:-8000} python -m app.server


extract: venv ## Run app/extract.py (pass ARGS environment variable for arguments)
	. .venv/bin/activate && python app/extract.py $${ARGS}

extract-tables: venv ## Extract tables from FILE (PDF) and append into content; write OUT (defaults to bibleData_with_tables.json). Env: FILE, OUT, USE_HTML (1/0)
	.venv/bin/python scripts/extract_tables.py

pycompile: venv ## Syntax-check Python files with py_compile
	. .venv/bin/activate && python -m py_compile app/server.py tests/test_server_import.py

test: venv ## Run tests with pytest (ensure pytest is in requirements.txt)
	. .venv/bin/activate && pytest -q

clean: ## Remove common build/test artifacts
	rm -rf __pycache__ .pytest_cache build dist *.egg-info
