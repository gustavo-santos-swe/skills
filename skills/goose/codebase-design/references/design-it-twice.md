# Design it twice

Explore alternate interfaces for one deepening candidate (Ousterhout). Vocabulary from the parent skill.

## 1. Frame the problem space

Before sub-agents: constraints any interface must meet, dependency category ([deepening.md](deepening.md)), a rough sketch that grounds constraints (not a proposal). Show the user, then spawn agents while they read.

## 2. Spawn 3+ parallel designs

Each agent gets a different constraint, e.g.:

1. Minimize interface (1–3 entry points); max leverage per entry
2. Maximise flexibility / many use cases
3. Optimise the most common caller (default case trivial)
4. (If needed) Ports & adapters for cross-seam deps

Brief each with file paths, coupling, dependency category, what sits behind the seam, plus this vocabulary and `CONTEXT.md` terms.

Each returns: interface (types + invariants/errors), caller usage example, what implementation hides, dependency/adapter strategy, trade-offs (where leverage is high vs thin).

## 3. Compare

Present side by side on **depth**, **locality**, and **seam** placement. Recommend one; note what you’d steal from the losers. User picks before any production code.
