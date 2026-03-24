# Security Audit

**Project:** ai-workflow-lab
**Date:** 2026-03-24
**Reviewer:** security-reviewer (project-audit team)

---

## Summary

The application is a minimal Flask app with four read-only routes and no user input handling. The attack surface is small. Two medium-severity issues were found related to development defaults that should not reach production. The remaining findings are informational and relevant as the application grows.

| Severity | Count |
|----------|-------|
| Critical | 0 |
| High     | 0 |
| Medium   | 2 |
| Low      | 1 |
| Info     | 4 |

---

## Findings

### 1. Debug Mode Enabled in Dev Server Entry Point

**Severity:** Medium
**File:** `src/ai_workflow_lab/app.py:26`

```python
if __name__ == "__main__":
    create_app().run(debug=True, port=8000)
```

The Werkzeug debugger is enabled via `debug=True`. If this entry point is used in a reachable environment, the interactive debugger allows **arbitrary code execution** from the browser. While guarded by `__main__`, developers may inadvertently use this invocation in non-local environments.

**Recommendation:** Use an environment variable to control debug mode (e.g., `debug=os.environ.get("FLASK_DEBUG", "0") == "1"`), or remove `debug=True` entirely and rely on `flask run --debug` for local development.

---

### 2. No SECRET_KEY Configured

**Severity:** Medium
**File:** `src/ai_workflow_lab/app.py:5`

```python
app = Flask(__name__)
```

Flask's `SECRET_KEY` defaults to `None`. If sessions, flash messages, or any cookie-signing functionality is added, cookies will be unsigned and trivially forgeable.

**Recommendation:** Set `app.secret_key` from an environment variable (e.g., `os.environ["SECRET_KEY"]`) before the app is used in any context that requires signed cookies.

---

### 3. No CSRF Protection

**Severity:** Low
**File:** `src/ai_workflow_lab/app.py` (global)

No CSRF middleware is installed (e.g., Flask-WTF's `CSRFProtect`). All current routes are `GET`-only, so the immediate risk is negligible. However, adding any state-changing (`POST`/`PUT`/`DELETE`) route without CSRF protection would be vulnerable.

**Recommendation:** Install CSRF protection (e.g., `flask-wtf`) before adding any state-changing routes.

---

### 4. Index Route Returns Unescaped Plain Text

**Severity:** Info
**File:** `src/ai_workflow_lab/app.py:21`

```python
@app.get("/")
def index():
    return "ai-workflow-lab: hello"
```

The response is a hardcoded string with no user input, so there is no current XSS risk. Flask sets `Content-Type: text/html` by default for bare string returns. If user-controlled data is ever interpolated into the return value without escaping, this becomes an XSS vector.

**Recommendation:** No action needed now. When adding dynamic content, use `jsonify()` or Jinja2 templates (which auto-escape) instead of raw string returns.

---

### 5. No Input Validation Framework

**Severity:** Info
**File:** N/A

No routes currently accept path parameters, query strings, or request bodies. There is no validation library (e.g., marshmallow, pydantic) integrated. This is fine for the current state but should be addressed before accepting user input.

---

### 6. No Rate Limiting

**Severity:** Info
**File:** N/A

No rate-limiting middleware is configured. For a toy/learning project this is expected, but any publicly exposed deployment should add rate limiting (e.g., `flask-limiter`).

---

### 7. Dependencies — No Known Critical Vulnerabilities

**Severity:** Info
**File:** `pyproject.toml:7-10`

```toml
dependencies = [
    "flask>=3.1.2",
    "mcp>=1.26.0",
]
```

Both runtime dependencies specify modern minimum versions. No known critical CVEs were identified for these versions at the time of this review. The `mcp` package pulls in several transitive dependencies (pydantic, httpx, uvicorn, etc.) — periodic `uv lock --upgrade` and vulnerability scanning (e.g., `pip-audit`) is recommended.

---

## Files Reviewed

| File | Status |
|------|--------|
| `src/ai_workflow_lab/app.py` | Reviewed — all routes and app factory |
| `src/ai_workflow_lab/__init__.py` | Reviewed — empty |
| `pyproject.toml` | Reviewed — dependencies and tool config |
| `.env` / config files | None found |
