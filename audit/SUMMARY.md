# Audit Summary

**Project:** ai-workflow-lab
**Date:** 2026-03-24
**Auditors:** security-reviewer, test-analyst, architecture-critic

---

## Overall Assessment

The project is in good shape for a toy/learning app. The foundation is correct: proper `src/` layout, Flask app factory, CI pipeline, and a clean `CLAUDE.md` contract. The attack surface is minimal (four GET-only routes, no user input, no database). The issues found are not crises — they are the predictable debt of a project that hasn't needed production hardening yet.

---

## Cross-Cutting Themes

### 1. Hardcoded / Duplicated Data

Three separate findings from two auditors converge on the same pattern:

| Finding | Source | Severity |
|---|---|---|
| Version string `"0.1.0"` duplicated across `app.py` and `pyproject.toml` | Architecture | Inconsistency |
| `list_routes()` in MCP server hardcodes 3 routes; app defines 4 (`/ping` missing) | Architecture | Inconsistency |
| `debug=True` hardcoded in `app.py:26` | Security | Medium |

**Root cause:** No pattern for externalising configuration or deriving metadata dynamically. The MCP and version issues are the same mistake at different scales.

**Fix:** Read version from `importlib.metadata`; replace hardcoded MCP route list with `create_app().url_map` introspection; replace `debug=True` with an env-var toggle.

---

### 2. Missing Production-Readiness Scaffolding

The security and architecture auditors both noted the absence of standard safety scaffolding that is cheap to add now and expensive to retrofit later:

| Gap | Security Impact | Architecture Impact |
|---|---|---|
| No `SECRET_KEY` | Unsigned cookies if sessions added | — |
| No CSRF protection | Vulnerable if POST routes added | — |
| No config layer (dev/test/prod) | No place to put env-specific secrets | Developers will improvise |
| No input validation framework | — | No pattern to follow when routes accept parameters |
| No rate limiting | Denial-of-service exposure | — |

None of these are emergencies today. All become blockers the moment the app grows beyond its current toy scope.

---

### 3. Test Coverage Is Nearly Complete — With One Structural Issue

Test coverage is better than average for a small project, but two gaps were identified:

| Gap | Risk |
|---|---|
| `GET /` has no test | A regression on the index route would go undetected |
| `GET /ping` body not asserted | A silent change to the response shape would pass CI |

The deeper issue (noted by architecture): every test file independently calls `create_app()` and `test_client()`. Without a `conftest.py` shared fixture, this boilerplate will be copy-pasted into every new test file, and a future change to the factory signature will require touching every file.

---

## Prioritised Action List

Items are ordered by effort-to-impact ratio — quick wins first, architectural investments last.

| Priority | Action | Effort | Addresses |
|---|---|---|---|
| 1 | Replace `debug=True` with env-var toggle in `app.py:26` | Trivial | Security (Medium) |
| 2 | Set `SECRET_KEY` from env var in `create_app()` | Trivial | Security (Medium) |
| 3 | Add `conftest.py` with a shared `client` fixture | Low | Architecture, Test Coverage |
| 4 | Add tests for `GET /` and `GET /ping` response body | Low | Test Coverage |
| 5 | Read version from `importlib.metadata` in `/version` route | Low | Architecture |
| 6 | Make `list_routes()` dynamic via `url_map` introspection | Low | Architecture |
| 7 | Standardise `GET /` to return JSON (or document the exception) | Low | Architecture |
| 8 | Install CSRF protection before adding any state-changing routes | Low | Security (Low) |
| 9 | Add Blueprints before route count exceeds ~10 | Medium | Architecture (scale) |
| 10 | Add `config.py` with env-based config classes | Medium | Security + Architecture (scale) |
| 11 | Establish a service layer pattern before adding business logic | Medium | Architecture (scale) |

---

## Audit File Index

| File | Contents |
|---|---|
| [`audit/security.md`](security.md) | Full security findings with severity labels and file:line references |
| [`audit/coverage.md`](coverage.md) | Coverage matrix and proposed test stubs |
| [`audit/architecture.md`](architecture.md) | Strengths, inconsistencies, scale risks, and 8 recommendations |
