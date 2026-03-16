# CLAUDE.md

## Project overview
ai-workflow-lab is a toy Flask app used for learning agentic coding workflows.
Uses a src/ layout with the package at src/ai_workflow_lab/.

## Tools
This project uses `uv` for all dependency management, script running, and environment tasks.
Never use pip, python, or pytest directly — always go through uv.

## Common commands
- Run tests: `uv run pytest`
- Run linter: `uv run ruff check .`
- Run dev server: `uv run python src/ai_workflow_lab/app.py`
- Add a dependency: `uv add <package>`
- Add a dev dependency: `uv add --group dev <package>`

## Workflow rules
- After completing a task, give a short summary of what you did, then run `git status -sb`.
- Before any commit: run `uv run ruff check .` and `uv run pytest`. Fix any issues before committing.

## MCP servers
- `filesystem`: uses `.` (current working directory = project root) — no absolute path needed.

## Code conventions
- Follow existing patterns in the codebase.
- All routes go in app.py inside the create_app() factory.
- Tests use Flask's test_client pattern.

