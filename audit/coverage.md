# Test Coverage Analysis

## Source Inventory

**File:** `src/ai_workflow_lab/app.py`

| Function | Type | Description |
|---|---|---|
| `create_app()` | Factory | Returns configured Flask application |
| `health()` | Route handler | `GET /health` → `{"status": "ok"}` |
| `version()` | Route handler | `GET /version` → `{"version": "0.1.0"}` |
| `ping()` | Route handler | `GET /ping` → `{"pong": true}` |
| `index()` | Route handler | `GET /` → `"ai-workflow-lab: hello"` |

**File:** `src/ai_workflow_lab/__init__.py` — empty (nothing to test)

---

## Existing Tests

**File:** `tests/test_health.py`

| Test | What it covers |
|---|---|
| `test_health()` | `GET /health` — status 200, JSON body `{"status": "ok"}` |
| `test_ping()` | `GET /ping` — status 200 only |

**File:** `tests/test_version.py`

| Test | What it covers |
|---|---|
| `test_version()` | `GET /version` — status 200, JSON body `{"version": "0.1.0"}` |

---

## Coverage Matrix

| Function / Route | Test Status | Notes |
|---|---|---|
| `create_app()` | Partial | Used indirectly in every test but never asserted as returning a Flask instance |
| `GET /health` | **Covered** | Status code and response body both asserted |
| `GET /version` | **Covered** | Status code and response body both asserted |
| `GET /ping` | **Partial** | Status code asserted; response body `{"pong": true}` is not checked |
| `GET /` (index) | **Missing** | No test exists |

---

## Proposed Test Cases

```python
# tests/test_app_factory.py

from ai_workflow_lab.app import create_app


def test_create_app_returns_flask_instance():
    """Verify that create_app() returns a Flask application instance."""
    ...
```

```python
# tests/test_health.py  (additions)

def test_ping_response_body():
    """Verify GET /ping returns JSON body {"pong": true}."""
    ...
```

```python
# tests/test_index.py

from ai_workflow_lab.app import create_app


def test_index_status():
    """Verify GET / returns HTTP 200."""
    ...


def test_index_body():
    """Verify GET / response body contains the expected greeting text."""
    ...
```
