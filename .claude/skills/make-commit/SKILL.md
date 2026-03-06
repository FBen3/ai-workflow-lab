---
name: make-a-commit
description: Stages and commits changes using the conventional commits format. Handles atomic splitting across multiple commits.
allowed-tools: Bash(git *)
---

# Create Commit

## Step 1 - Gather state and Analyze

Consider the following data and reason about what you see:

**What's staged, unstagged, untracked**
!`git status -sb`

**Overall scope of changes**
!`git diff --stat HEAD`

**Exact staged changes**
!`git diff --cached`

**Exact unstaged changes**
!`git diff`

## Step 2 - Plan

Reason about atomicity: should this be one commit or several? 
Do you need to run other git commands to gather more information?
A commit is atomic if it represents one logical change. If staged and unstaged
changes are unrelated, they should be separate commits. If a file has both
staged and unstaged hunks, decide whether the unstaged portion belongs with
this commit or a future one - if the latter, leave it unstaged.

## Step 3 - Execute

Execute the commits in order.
For each commit:
- Stage only the relevant files/hunks (`git add` or `git add -p` if needed)
- Commit with a descriptive message   

## Commit format

Use `<type>(optional-scope): <description>` where description starts with a
capital letter. Keep the subject line under 72 chars. Add a body if the subject
alone doesn't explain the why.

Types: fix, feat, docs, test, refactor, perf, style, build, ci, chore, revert.
Only invent a new type if none of the above fit - this should be rare.

