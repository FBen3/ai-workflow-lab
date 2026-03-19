#!/bin/bash
# Validates that the subagent only runs pytest or ruff commands.
# Receives JSON via stdin from Claude Code's PreToolUse hook.

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if [ -z "$COMMAND" ]; then
  exit 0
fi

# Allow only uv run pytest and uv run ruff
if echo "$COMMAND" | grep -qE '^uv run (pytest|ruff)'; then
  exit 0
fi

echo "Blocked: only 'uv run pytest ...' and 'uv run ruff ...' are permitted" >&2
exit 2
