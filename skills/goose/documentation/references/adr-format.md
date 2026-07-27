# ADR format (Goose)

Architecture Decision Records for the target repo. Owned by **`documentation`** branch **`adr`**.

Market baseline: [Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (Context / Decision / Consequences) plus optional trade-off sections in the spirit of [MADR](https://adr.github.io/madr/). Goose default is **Nygard-shaped, short**; expand only when the trade-off needs it.

Default path: `docs/adr/` · files `0001-slug.md`, `0002-slug.md`, …  
Create the directory lazily. `AGENTS.md` in the target repo may override the path.

## Default template

```md
# {Short title}

## Status

Accepted

## Context

{What forces the decision? Constraints, problem, who cares.}

## Decision

{What we chose. Imperative, present tense: "We will …"}

## Consequences

{What becomes easier, harder, or forbidden. Include follow-ups if any.}
```

**Status values:** `Proposed` | `Accepted` | `Deprecated` | `Superseded by ADR-NNNN`

## When the trade-off is load-bearing

Add sections (MADR-style) only if they earn their keep:

```md
## Drivers

- {force or constraint that shaped the choice}

## Options considered

### {Option A}
- Good, because …
- Bad, because …

### {Option B}
- Good, because …
- Bad, because …

## Decision

Chosen: **{Option A}**, because {one clear reason tied to drivers}.
```

Skip empty headings. A thin ADR with four Nygard sections beats a hollow MADR skeleton.

## Tiny escape hatch

If the decision is real but tiny, one short file is fine:

```md
# {Title}

**Status:** Accepted

{2–4 sentences: context, decision, why, main consequence.}
```

Still use a numbered file in `docs/adr/`.

## Numbering

Scan `docs/adr/` for the highest `NNNN`; next file is `NNNN+1`.

## When to write an ADR

All three:

1. **Hard to reverse**
2. **Surprising later** without a written why
3. **Real trade-off** among alternatives

### Usually yes

- Architectural shape (boundaries, sync vs events, mono vs multi-repo)
- Lock-in platforms (DB, bus, auth, cloud) — not every library
- Ownership between contexts
- Deliberate deviation from the obvious path
- Constraints invisible in code (compliance, partner SLAs)
- Rejected options that will otherwise keep coming back

### Usually no

- Easy to reverse style choices
- "We did the only sensible thing"
- Implementation detail that belongs in code or ship-docs

Hard decisions that land mid-**brainstorm** hand off here. Ubiquitous-language terms stay in `CONTEXT.md`, not in ADRs.

## Example (filled)

```md
# Use Postgres for the write model

## Status

Accepted

## Context

Order intake must survive process restarts and support reporting within minutes.
We already run Postgres in ops; the team knows it. Event sourcing was proposed
for auditability.

## Decision

We will persist the write model in Postgres with explicit audit rows for money
movements. We will not event-source the write path in v1.

## Consequences

- Simpler operational story and one backup strategy.
- Full temporal rebuild of state is not free; audit tables cover the money path.
- Revisit if multi-region active-active becomes a hard requirement.
```
