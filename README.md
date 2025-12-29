# WalkWithGod — Python project wrapper

This repository was converted to a minimal Python project. It contains a tiny
HTTP server (no external dependencies) that can serve the existing `index.html`
from the repository root.

How to run (macOS / Linux):

1. From the repository root run:

    python3 -m app.server

2. Open http://localhost:8000/ in your browser. The existing `index.html` at
   the project root will be served.

Files added:

- `app/server.py` — tiny server using Python standard library.
- `app/__init__.py` — package init for `app`.
- `tests/test_server_import.py` — minimal import test.
- `requirements.txt` — placeholder for dependencies (empty for now).
- `pyproject.toml` — minimal project metadata.

Suggested next steps:

- Add tests and CI (GitHub Actions) to run tests automatically.
- If you want a real web framework, add `Flask` or `FastAPI` to
  `requirements.txt` / `pyproject.toml` and extend `app.server` accordingly.
