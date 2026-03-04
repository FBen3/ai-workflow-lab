---
name: make-a-commit
description: Looks at staged and unstaged changes and makes 1 (or more) atomic commits, following the  `<type>(optional-scope): <description>` format for the commit message.
allowed-tools: Bash(git *), Bash(gh *)
---

# Strategy

- Check if there are any staged changes. If there are then evaluate whether it makes sense to commit all of them in 1 commit, or whether to split them.
- Check if there are any unstaged changes. If there are, evaluate whether they should all be in 1 commit, or if you need to stage and commit them separately.

# Format

Create a commit that follows the form `<type>(optional-scope): <description>`. The <description> should start with a capital letter, e.g. `feat: Add version/ endpoint`.

Typical types:
- fix: a bug fix
- feat: a new feature
- docs: documentation only
- test: add/fix tests
- refactor: restructure code, no behavior change
- perf: performance improvement
- style: formatting (e.g. whitespace, lint fixes), no behavior change
- build: build system/deps
- ci: CI config/scripts
- chore: maintenance work
- revert: revert a previous commit

If the change does not fall into any of above categories, you're allowed to make your own short type tag, but this is discouraged and should only be done when absolutely necessary.

The message should be descriptive and impertaive (e.g. "Fix ...") and follow the form:
```
Add a short commit message (<=72 chars) 

Optional, more detailed explanatory text. Wraped 
to 72 characters. The blank line separating the 
summary from the body is critical (unless you omit 
the body entirely).

Further paragraphs come after blank lines.

- Bullet points are okay, too.
- Typically a hyphen or asterisk is used for the bullet, followed by a
single space. Use a hanging indent.
```
