# Agent Instructions

- Plan first before making changes.
- Keep changes minimal and do not change app behavior.
- Do not edit generated files.
- Before finishing, run:
  - `UV_CACHE_DIR=.uv-cache uv run pytest`
  - `UV_CACHE_DIR=.uv-cache uv run ruff check .`
- Show `git diff --stat` at the end of the work.
