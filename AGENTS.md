# Agent instructions (this repo)

## Voice (always)

Durable prose, chat, and questions use **`write-like-goose`**. Load [`skills/goose/write-like-goose/SKILL.md`](skills/goose/write-like-goose/SKILL.md) before emitting tickets, plans, ADRs, commits, PR text, review comments, code comments, skill bodies, or grill questions.

- Answer first. Short prose with a stance. Fully answers. How-tos: numbered steps, one action each, first line is a doable action. Questions state the decision, each option's consequence, and a recommendation.
- Examples: [`skills/goose/write-like-goose/references/examples.md`](skills/goose/write-like-goose/references/examples.md).
- Do not stack other humanizer skills on the same pass. `write-like-goose` alone.
- Enforced in Cursor via [`.cursor/rules/write-like-goose.mdc`](.cursor/rules/write-like-goose.mdc) (`alwaysApply`).

## Lifecycle (goose/)

Unsure which skill → [`skills/goose/ask/SKILL.md`](skills/goose/ask/SKILL.md).  
How / when map: [`skills/goose/README.md`](skills/goose/README.md). Root README also has a short starter table.

Branch / commit shape → `git-practices`. Open PR → `pr-raise` (never merge to main from the agent).

## Evolving this skills repo

Process for adding / pruning / absorbing skills → [`skills/meta/evolve-goose-skills/SKILL.md`](skills/meta/evolve-goose-skills/SKILL.md) (playbook in that skill’s `references/`). Do not re-teach the ritual in chat.
