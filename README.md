A toy repo to test the various AI development layers / workflows

## Endpoints

- `GET /` returns a plain text greeting.
- `GET /health` returns JSON health status.
- `GET /version` returns JSON package name and version.

## How to Run

Use uv for running the app, tests, and linting. In agent sessions, set `UV_CACHE_DIR=.uv-cache` to avoid sandbox permission issues.

```sh
uv run python -m ai_workflow_lab.app
UV_CACHE_DIR=.uv-cache uv run pytest
UV_CACHE_DIR=.uv-cache uv run ruff check .
```
