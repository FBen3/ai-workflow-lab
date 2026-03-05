# AGENTS.md

## Cursor Cloud specific instructions

This is a minimal Python Flask application managed with `uv`. There are no databases, Docker services, or external dependencies.

### Quick reference

- **Python version:** 3.13 (specified in `.python-version`)
- **Package manager:** `uv` (lockfile: `uv.lock`)
- **Lint:** `uv run ruff check .` (config in `pyproject.toml` — rules: E, F, I, UP, B)
- **Tests:** `uv run pytest`
- **Run dev server:** `uv run python -m ai_workflow_lab.app` (port 8000, debug mode)
- **CI definition:** `.github/workflows/ci.yml`

### Notes

- The repo has pre-existing ruff `I001` (import sorting) violations. These are not regressions.
- `uv` auto-installs the required Python version (3.13) if missing, so no separate Python install step is needed after `uv` is available.
