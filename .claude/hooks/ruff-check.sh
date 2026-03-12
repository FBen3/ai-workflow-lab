#!/bin/bash
# ruff-check.sh
# Runs after Claude edits/writes a file. If ruff finds issues,
# feeds them back to Claude as additional context.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only run on Python files
if [[ "$FILE_PATH" != *.py ]]; then
  exit 0
fi

# Run ruff and capture output
RUFF_OUTPUT=$(uv run ruff check "$FILE_PATH" 2>&1)
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  exit 0
fi

# Feed violations back to Claude as context
jq -n --arg output "$RUFF_OUTPUT" '{
  hookSpecificOutput: {
    hookEventName: "PostToolUse",
    additionalContext: ("ruff found issues in the file you just edited:\n" + $output + "\nPlease fix these before continuing.")
  }
}'

exit 0

