Create a commit that follows the form `<type>(optional-scope): <description>`.

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