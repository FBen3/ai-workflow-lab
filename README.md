A toy repo to test the various AI development layers / workflows

## How to Run

Use uv for running tests and linting. In agent sessions, set `UV_CACHE_DIR=.uv-cache` to avoid sandbox permission issues.

```sh
UV_CACHE_DIR=.uv-cache uv run pytest
UV_CACHE_DIR=.uv-cache uv run ruff check .
```
