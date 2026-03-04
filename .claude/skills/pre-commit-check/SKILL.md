---
name: pre-commit-check
description: Runs a pre-commit check - tests, linting, and git status. Invoke before committing.
context: fork
agent: Explore
disable-model-invocation: true
allowed-tools: Bash(uv *), Bash(git *)
---

# Pre-Commit Check

You are a subagent running in isolation. You have no conversation history.
Your job is to run a pre-commit check on this repository and return a structured report.

## Steps

1. Run `uv run pytest` and capture the result
2. Run `uv run ruff check .` and capture the result
3. Run `git status -sb` and capture the result
4. Run `git diff --stat HEAD` and capture the result

## Report format

Return a short report with four sections:

- ✅ or ❌ **Tests** — pass/fail, number of tests
- ✅ or ❌ **Lint** — pass/fail, any issues found
- 📋 **Git status** — which files are staged, unstaged, or untracked
- 📊 **Diff stat** — summary of changes since last commit

If anything is ❌, include the specific output so the user knows what to fix.

