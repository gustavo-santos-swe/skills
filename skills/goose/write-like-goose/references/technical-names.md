# Technical names (Goose / skills domain)

ASD-STE100 lets you use **technical names** for domain terms not in the STE dictionary. Use these consistently. Do not swap synonyms for the same item in one document.

## Lifecycle and artifacts

| Use | Not |
|-----|-----|
| skill | playbook (when meaning Agent Skill), capability |
| agent | assistant, bot (in skill prose) |
| repository | repo (in PR/ticket/plan prose; `repo` ok in commit, branch, and chat text) |
| pull request | PR (in PR/ticket/plan prose, prefer "pull request" on first use; `PR` ok in chat, tables, and commit/branch text) |
| commit | check-in |
| branch (git) | — (see also skill-meta `branch` below for the unrelated "skill path" sense) |
| ticket | issue (match the target repo's tracker term — Linear says ticket, GitHub Issues says issue; pick one per document) |
| plan | roadmap (when meaning implementation plan) |
| ADR | architecture decision record (define once, then ADR) |
| brainstorm | ideation session |
| Briefing | PR/ticket/plan opening section: what + why (1-3 sentences, descriptive STE shape) |

## Code and stack

| Use | Not |
|-----|-----|
| test | spec (when meaning automated test) |
| endpoint | route (pick one per API doc) |
| database | DB (in formal prose) |
| migration | schema change (when meaning EF/flyway migration) |
| module | package (when meaning code module; match the codebase) |

**`-ing` state/process nouns** (exempt from the STE `-ing` ban, see [ste100.md](./ste100.md)): loading, caching, routing, testing, pending. Use as plain nouns/adjectives (`the loading state`, `still pending`), not tacked on as fake-depth fluff.

## Skill-meta vocabulary

These terms come from `writing-great-skills`. They are technical names in this repo:

| Term | Meaning |
|------|---------|
| leading word | Compact concept that anchors skill behavior |
| completion criterion | Checkable condition that marks a step done |
| context pointer | Link that loads reference on demand |
| branch | Distinct path through a skill (not the git `branch` above unless stated) |
| premature completion | Ending a step before the criterion is met |
| context load | Tokens a skill description adds every turn |

## Project glossary

Product/domain terms live in the target repo's **`CONTEXT.md`**, not here. Load that file for ubiquitous language when writing app tickets, plans, or ADRs.

## Adding names

When a new domain term repeats across skills and is not STE-approved:

1. Add it here with a short definition.
2. Use the same term everywhere (Rule 1.11).
3. Do not add generic English words — use the STE dictionary for those.
