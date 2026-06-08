---
name: zoom-out
description: Zoom out and map how unfamiliar code fits the bigger picture — modules, callers, domain vocabulary. Use when user says "zoom out", "big picture", "how does this fit", or is lost in an unfamiliar area of the codebase.
metadata:
  area: engineering
  upstream:
    repo: mattpocock/skills
    path: skills/engineering/zoom-out
    url: https://github.com/mattpocock/skills/tree/main/skills/engineering/zoom-out
    synced_at: "2026-06-07"
    commit: be55a7970319ede7965edbb02b5e41cba1ca82c9
---

# Zoom Out

The user doesn't know this area of code well. Go up a layer of abstraction.

## Steps

1. Read `CONTEXT.md` (or relevant context from `CONTEXT-MAP.md`) for domain vocabulary.
2. Map the relevant modules, their responsibilities, and who calls whom.
3. Use the project's domain glossary — not generic terms like "service" or "component".
4. Present as a concise map, not a file-by-file dump.

## Output shape

```markdown
## Context
[1-2 sentences: what this area does in the system]

## Modules
- **ModuleName** — responsibility; called by X; calls Y

## Flow
[How data/control moves through the area]

## Where to look next
[2-3 entry points if the user wants to dive in]
```

Keep it short. The goal is orientation, not documentation.
