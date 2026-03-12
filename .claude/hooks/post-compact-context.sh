#!/bin/bash
# post-compact-context.sh
# Fires after context compaction. Re-injects project conventions
# that may have been lost in the summary.

cat << 'EOF'
Project conventions reminder (injected after compaction):
- Runtime: use `uv run` for all Python/tool invocations (not bare `python`, `ruff`, `pytest`)
- Linting: `uv run ruff check src/` and `uv run ruff format src/`
- Tests: `uv run pytest`
- Layout: src-layout, package is at src/ai_workflow_lab/
- Commits: conventional commits format (feat:, fix:, chore:, etc.)
- Branch: cc-level-5-hooks
EOF

