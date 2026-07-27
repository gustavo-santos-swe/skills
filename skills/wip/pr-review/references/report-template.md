# PR review report template

**Keep these headings** (same names) on every generation - chat, markdown, or canvas content mapping. Omit a findings subsection only when it has zero items.

```markdown
# PR review: <repo>#<number> - <title>

**Verdict:** Approve | Comment | Request changes
**CI:** pass | fail | pending | unknown - <one line>
**Spec / SoT:** <path or URL> | none provided

## Summary
2-4 sentences. What the PR does and the review outcome. No filler.

## Human review guide
(Required - follow human-walk-guide.md exactly)

### Inferred structure
…

### Suggested read order
1. …
2. …

### Why this order
…

## Findings

### Block
- **<axis>** - `<path>:<line>` - <what's wrong>. <why it matters>.

### Should-fix
- …

### Nit
- … (≤2 total)

## Axes without findings
One short line listing axes checked with nothing to report, e.g. `Correctness, security: nothing high-confidence.`

## Next
- Author: **pr-iterate** if changes needed
- Optional: **security-check** if …
- Post to GitHub? (ask) - suggest: request changes | comment | approve-only-if-asked
```

### Mapping rules

- **Chat:** full template; keep Summary + Human review guide + Findings above the fold.
- **Markdown file:** identical body; path `docs/reviews/YYYY-MM-DD-pr-<n>.md` unless repo convention differs.
- **Canvas:** same information in the fixed canvas sections (see canvas-layout.md) - do not rename axes or verdict labels.
