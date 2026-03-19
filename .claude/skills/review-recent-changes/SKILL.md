---
name: review-recent-changes
description: Reviews all Python files changed in the last commit using the python-code-reviewer agent
context: fork
agent: python-code-reviewer
---

# Review Recent Changes

Run this command first to identify which files changed:
!`git diff --name-only HEAD~1 HEAD -- '*.py'`

Review each Python file listed above for code quality, clarity, and adherence 
to project conventions. Report findings by severity.
