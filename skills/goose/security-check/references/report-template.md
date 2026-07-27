# Security-check report template

## Gate (chat)

```markdown
# Security check (gate)

**Scope:** <branch diff | uncommitted | paths>
**Stack notes loaded:** <pack security skill or none>

## Block
- `<path>:<line>` - <finding>. Why exploitable: … Suggested direction: …

## Should-fix
- …

## Needs verification
- …

## FYI
- … (optional, max a couple)

## Verdict
No security blockers for this scope.
| Blockers present - fix before ship (via implement if you want).
```

Omit empty sections. Redact secrets.

## Full audit (file)

Path: `docs/security/YYYY-MM-DD-<slug>.md` (or repo convention).

```markdown
# Security audit: <slug>

**Date:** YYYY-MM-DD
**Mode:** full audit
**Scope:** …

## Summary
1-3 sentences. Blocker count.

## Block
…

## Should-fix
…

## Needs verification
…

## Out of scope / not covered
…

## Verdict
…
```

Chat: paste Summary + Verdict + file path.
