---
name: handoff
description: Compact the current conversation into a handoff document so a fresh agent can continue. Use when user says "handoff", "pass to next session", "save context for later", or the session is ending with work in progress.
metadata:
  area: meta
  upstream:
    repo: mattpocock/skills
    path: skills/productivity/handoff
    url: https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff
    synced_at: "2026-06-07"
    commit: be55a7970319ede7965edbb02b5e41cba1ca82c9
---

# Handoff

Write a handoff document summarising the current conversation so a fresh agent can continue the work.

Save to the **OS temp directory** — not the current workspace.

## Document structure

```markdown
# Handoff: {topic}

## Goal
What we're trying to accomplish.

## Done
- [bullets]

## In progress
- [bullets]

## Blocked / open questions
- [bullets]

## Key artifacts
- `path/to/plan.md` — implementation plan
- `path/to/spec.md` — design spec
- PR #42 — https://...

## Suggested skills
Skills the next agent should invoke first:
- `executing-plans` — resume plan at Task 3
- `systematic-debugging` — if blocked on test failure

## Next steps
1. ...
2. ...
```

## Rules

- **Do not duplicate** content already in PRDs, plans, ADRs, issues, commits, or diffs — reference by path or URL.
- **Redact** API keys, passwords, PII.
- If the user passed a focus for the next session, tailor the doc accordingly.
- List skills from **this repo** (`gustavo-santos-swe/skills`) in the suggested skills section.
