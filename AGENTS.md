# Agent instructions (this repo)

## Voice (always)

Durable prose uses **`write-like-goose`** on **ASD-STE100** (Simplified Technical English). Load [`skills/goose/write-like-goose/SKILL.md`](skills/goose/write-like-goose/SKILL.md) before emitting tickets, plans, ADRs, commits, PR text, review comments, code comments, or skill bodies that stay in the tree.

- STE rules: [`skills/goose/write-like-goose/references/ste100.md`](skills/goose/write-like-goose/references/ste100.md). Domain terms: [`technical-names.md`](skills/goose/write-like-goose/references/technical-names.md).
- Do not stack other humanizer skills on the same pass — `write-like-goose` alone.
- Chat one-liners: STE defaults + density is enough; pull the full catalog only for heavy rewrites.
- Enforced in Cursor via [`.cursor/rules/write-like-goose.mdc`](.cursor/rules/write-like-goose.mdc) (`alwaysApply`).

## Lifecycle (goose/)

Unsure which skill → [`skills/goose/ask/SKILL.md`](skills/goose/ask/SKILL.md).  
How / when map: [`skills/goose/README.md`](skills/goose/README.md). Root README also has a short starter table.

Branch / commit shape → `git-practices`. Open PR → `pr-raise` (never merge to main from the agent).

## Evolving this skills repo

Process for adding / pruning / absorbing skills → [`skills/meta/evolve-goose-skills/SKILL.md`](skills/meta/evolve-goose-skills/SKILL.md) (playbook in that skill’s `references/`). Do not re-teach the ritual in chat.
