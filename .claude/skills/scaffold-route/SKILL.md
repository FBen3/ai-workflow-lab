---
name: scaffold-route
description: Scaffolds a new Flask route in app.py and a matching test. Use by invoking /scaffold-route <method> <path>, e.g. /scaffold-route GET /users
argument-hint: [method] [path]
disable-model-invocation: true
allowed-tools: Read, Grep
---

# Scaffold Route

You are scaffolding a new Flask route. The arguments are:
- Method: $ARGUMENTS[0]
- Path: $ARGUMENTS[1]

## Phase 1 — Analyse (read-only)

Use Read to examine `src/ai_workflow_lab/app.py` and `tests/test_health.py`.
Understand the existing patterns: how routes are structured, how tests are written.
Do not write anything yet.

## Phase 2 — Implement

1. Add the new route to `app.py` inside `create_app()`, following existing patterns exactly.
2. Add a corresponding test inside `tests/` that asserts a 200 status code. If the logic naturally falls into any of the current testing modules, then add it there. Otherwise create a new test file.
3. Keep it minimal — match the style of the existing `/health` and `/version` routes.

## Phase 3 — Confirm

After writing both files, report:
- What route was added
- What test was added
- Remind the user to run `uv run pytest` to verify

