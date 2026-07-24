---
name: documentation
description: Write or update durable docs — ADRs before build, and system/API/runbook docs after implementation. Use when the user says "ADR", "document this", "update the docs", or a decision/public surface needs a written trail.
disable-model-invocation: true
metadata:
  area: wip
---

# Documentation

Status: **stub** — fill branches below (inspired by Addy Osmani `documentation-and-adrs`). Project paths/templates live in the target repo (`AGENTS.md`, `docs/`, etc.); this skill owns *when* and *what kind*.

Voice: durable prose — **`write-like-goose`**.

## Branches

Pick one (or both in order on a long feature):

| Branch | When in the lifecycle | Answers |
|--------|----------------------|---------|
| **`adr`** | During **design → plan**, before **implement** | *Why* we chose X (and what we rejected) |
| **`ship-docs`** | During/after **implement**, before **pr-raise** when the public surface changed | *How* it works / how to use it |

```
design → [documentation:adr?] → plan → … → implement → [documentation:ship-docs?] → pr-raise
```

## Branch: adr

_TODO: checklist, minimal ADR shape (context / options / decision / consequences), link from ticket._

Done when: decision is written, discoverable, and referenced from the plan or issue.

## Branch: ship-docs

_TODO: when required (API contract, onboarding, runbook, README surface), what to touch, DoD._

Done when: a newcomer can use or operate the changed surface without reading the PR diff.

## Don't

- Don't write an ADR for reversible trivia.
- Don't write ship-docs that only restate the code line-by-line.
- Don't block every PR on docs — only when the reader-facing or operator-facing surface changed.
