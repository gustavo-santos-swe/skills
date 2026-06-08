# ADR Format

ADRs live in `docs/adr/` with sequential numbering: `0001-slug.md`, `0002-slug.md`, etc.

Create `docs/adr/` lazily — only when the first ADR is needed.

## Template

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

An ADR can be a single paragraph. Record *that* a decision was made and *why*.

## Optional sections

Only when they add value:

- **Status** frontmatter (`proposed | accepted | deprecated | superseded by ADR-NNNN`)
- **Considered Options** — when rejected alternatives are worth remembering
- **Consequences** — when non-obvious downstream effects matter

## Numbering

Scan `docs/adr/` for the highest existing number and increment by one.

## When to offer an ADR

All three must be true:

1. **Hard to reverse**
2. **Surprising without context**
3. **Result of a real trade-off**

### What qualifies

- Architectural shape, integration patterns between contexts
- Technology choices with lock-in (DB, auth, deployment)
- Boundary and scope decisions
- Deliberate deviations from the obvious path
- Constraints not visible in code
- Rejected alternatives when rejection is non-obvious
