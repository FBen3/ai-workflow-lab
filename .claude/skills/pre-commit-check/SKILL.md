---
name: pre-commit-check
description: Runs a pre-commit check - tests, linting, and git status. Invoke before committing.
context: fork
agent: Explore
disable-model-invocation: true
allowed-tools: Bash(uv *), Bash(git *)
---

# Pre-Commit Check

You are a subagent running in isolation. The following data was collected before
you were invoked. You did not run these commands — they were pre-processed.

## Collected data

**Test results:**
!`uv run pytest --tb=short 2>&1`

**Lint results:**
!`uv run ruff check . 2>&1`

**Git status:**
!`git status -sb`

**Diff stat:**
!`git diff --stat HEAD`

## Your task

Analyse the data above and return a short report:

- ✅ or ❌ **Tests** — pass/fail, number of tests
- ✅ or ❌ **Lint** — pass/fail, any issues found
- 📋 **Git status** — staged, unstaged, untracked files
- 📊 **Diff stat** — summary of changes since last commit

If anything is ❌, include the specific output so the user knows what to fix.

