# ADR format

Formats for the target repo. Owned by **`documentation`** branch **`adr`**. Adapted from Matt Pocock domain-modeling (see skill `inspired_by`).

Default path: `docs/adr/` with sequential names `0001-slug.md`, `0002-slug.md`, …  
Create the directory lazily on the first ADR. Repo `AGENTS.md` may override the path.

## Template

```md
# {Short title of the decision}

{1–3 sentences: context, what we decided, and why.}
```

A single paragraph is enough. Value is recording *that* a decision happened and *why*, not filling sections.

## Optional sections

Only when they earn their keep:

- **Status** (`proposed` | `accepted` | `deprecated` | `superseded by ADR-NNNN`) when decisions get revisited
- **Considered options** when rejected alternatives are worth remembering
- **Consequences** when non-obvious downstream effects matter

## Numbering

Scan `docs/adr/` for the highest number; increment by one.

## When to write an ADR

All three must hold:

1. **Hard to reverse** — changing your mind later is costly
2. **Surprising without context** — a future reader will wonder why
3. **Real trade-off** — genuine alternatives, picked for specific reasons

Skip if easy to reverse, obvious, or there was no real alternative.

### What usually qualifies

- Architectural shape (monorepo, event-sourced write model, etc.)
- Integration between contexts (events vs sync HTTP)
- Lock-in tech (DB, bus, auth, deploy target), not every library
- Boundary / ownership (“Customer data lives here; others use IDs only”)
- Deliberate deviation from the obvious path
- Constraints invisible in code (compliance, partner latency)
- Non-obvious rejected alternatives (so they are not re-proposed forever)

Hard decisions that crystallize mid-**brainstorm** hand off here; don’t duplicate the triple gate.
