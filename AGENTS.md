# Agent instructions (this repo)

## Voice (always)

Durable prose uses **`write-like-goose`**. Load [`skills/goose/write-like-goose/SKILL.md`](skills/goose/write-like-goose/SKILL.md) before emitting tickets, plans, ADRs, commits, PR text, review comments, or code comments that stay in the tree.

- Do not stack other humanizer skills on the same pass — `write-like-goose` alone.
- Chat one-liners: skill Defaults + density is enough; pull the full catalog only for heavy rewrites.
- Enforced in Cursor via [`.cursor/rules/write-like-goose.mdc`](.cursor/rules/write-like-goose.mdc) (`alwaysApply`).

## Lifecycle (goose/)

Unsure which skill → [`skills/goose/ask/SKILL.md`](skills/goose/ask/SKILL.md).  
How / when map: [`skills/goose/README.md`](skills/goose/README.md). Root README also has a short starter table.

Branch / commit shape → `git-practices`. Open PR → `pr-raise` (never merge to main from the agent).
