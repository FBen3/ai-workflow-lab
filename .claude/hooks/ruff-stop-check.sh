#!/bin/bash
# ruff-stop-check.sh
# Fires when Claude tries to stop. Blocks if any Python files have ruff violations.

INPUT=$(cat)

# CRITICAL: prevent infinite loop
# If we already triggered a continuation, let Claude stop this time
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0
fi

# Run ruff across the whole src/ directory
RUFF_OUTPUT=$(uv run ruff check src/ 2>&1)
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  exit 0
fi

# Block Claude from stopping; reason is fed back as Claude's next instruction
jq -n --arg output "$RUFF_OUTPUT" '{
  decision: "block",
  reason: ("Ruff violations must be fixed before stopping:\n" + $output)
}'

exit 0

