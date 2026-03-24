# Architecture Review

## Strengths

- **Correct src/ layout**: The project uses `src/ai_workflow_lab/` with an installable package (`[tool.uv] package = true`), which prevents accidental imports of the source tree and is the recommended Python packaging layout.
- **App factory pattern**: `create_app()` in `app.py` follows Flask best practice, making the app testable and configurable.
- **Consistent test pattern**: Tests use Flask's `test_client()` and assert on both status codes and JSON bodies. Test files are clearly named after the routes they cover.
- **CI pipeline**: GitHub Actions runs both `ruff check` and `pytest` on push/PR to main, matching the workflow described in CLAUDE.md.
- **Ruff configuration**: `pyproject.toml` selects a focused ruleset (`E, F, I, UP, B`) with a reasonable line length (100). All tooling config lives in one file.
- **CLAUDE.md as source of truth**: Documents commands, conventions, and workflow rules in a single place. The codebase currently adheres to these conventions.
- **MCP server**: `scripts/mcp_server.py` exposes project metadata as tools, enabling agentic workflows without touching the Flask app.

## Inconsistencies

### 1. MCP route list is stale
`scripts/mcp_server.py:list_routes()` hardcodes three routes (`/health`, `/version`, `/`) but `app.py` defines four — `/ping` is missing. Any time a route is added to `app.py`, the MCP server must be manually updated.

### 2. Version string duplicated
`"0.1.0"` appears in both `pyproject.toml` (line 3) and `app.py:version()` (line 13). On a version bump, one will inevitably be missed. The canonical version should live in `pyproject.toml` only, and the route should read it at runtime (e.g., via `importlib.metadata`).

### 3. Index route returns plain text; all others return JSON
`GET /` returns a bare string (`"ai-workflow-lab: hello"`), while `/health`, `/version`, and `/ping` all return `jsonify(...)`. This is a minor content-type inconsistency that could confuse API consumers.

### 4. No shared test fixtures
Each test file independently calls `create_app()` and `app.test_client()`. There is no `conftest.py` with a shared `client` fixture. With only 2 test files this is fine, but it's already showing repetition.

### 5. Test file grouping doesn't match route grouping
`test_health.py` tests both `/health` and `/ping`, while `test_version.py` tests `/version`. There is no test for the index route (`/`). The grouping is somewhat arbitrary.

## Scale Risks

### Monolithic app.py (High)
All routes live inside the `create_app()` function body as nested closures. At 4 routes this is clean; at 40 it becomes unnavigable. Flask Blueprints are the standard solution — group related routes into modules (e.g., `routes/health.py`, `routes/api.py`) and register them in the factory.

### No configuration management (Medium)
There is no `config.py`, no environment-based config switching (dev/test/prod), and no use of `app.config`. As soon as the app needs a database URL, API key, or feature flag, there is no pattern to follow. Developers will improvise, leading to inconsistency.

### No service/model layer (Medium)
Routes currently return static data, so there's no business logic to separate. But when routes start doing real work (database queries, external API calls), having no service layer means business logic will accumulate inside route handlers. This makes routes hard to test in isolation and creates tight coupling.

### Test setup duplication (Low)
Without a `conftest.py`, every new test file will repeat the `create_app()` + `test_client()` boilerplate. At 20+ test files, changing the app factory signature means updating every file.

### Stale MCP metadata pattern (Low)
The hardcoded route list in the MCP server will silently drift from reality as routes are added or removed. At scale, this becomes a source of incorrect tooling output for any agent consuming the MCP server.

## Recommendations

Listed in priority order:

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | **Add `conftest.py`** with a `client` fixture to eliminate repeated test setup | Low | Medium |
| 2 | **Read version from `importlib.metadata`** in the `/version` route to eliminate duplication | Low | Medium |
| 3 | **Add a test for `GET /`** to close the coverage gap | Low | Low |
| 4 | **Make `list_routes()` dynamic** — introspect `create_app().url_map` instead of hardcoding | Low | Medium |
| 5 | **Make `GET /` return JSON** for content-type consistency, or document the intentional difference | Low | Low |
| 6 | **Introduce Blueprints** when route count exceeds ~8-10, splitting by domain | Medium | High (at scale) |
| 7 | **Add a config layer** (`config.py` with dev/test/prod classes) before adding any external dependencies | Medium | High (at scale) |
| 8 | **Establish a service layer pattern** before adding business logic to routes | Medium | High (at scale) |

Items 1-5 are quick wins for the current codebase. Items 6-8 are architectural preparations that should be done *before* the codebase grows, not after.
