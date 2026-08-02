# Verify report template

## Gate (chat)

```markdown
# Verify (gate)

**Scope:** <branch diff | uncommitted>
**Packs checked:** <dotnet, database, ...>

## Drift
| Rule | Skill | Evidence | Note |
|------|-------|----------|------|
| <rule, one line> | `<skill-name>` | `<path>:<line>` | <why Drift, not Gap> |

## Gap
| Rule | Skill | Note |
|------|-------|------|
| ... | ... | acceptable on this batch, or flag for later |

## Style
| Rule | Skill | Evidence |
|------|-------|----------|
| ... | ... | ... |

## Enforced (mechanically covered)
| Rule | Skill | Mechanism | Evidence |
|------|-------|-----------|----------|
| <rule, one line> | `<skill-name>` | <editorconfig\|analyzer\|architecture-test\|regression-test> | `<path>:<line>` (rule id / test name), and confirmation the build/suite is green |

## Verdict
No Drift for this scope. Gap/Style noted above.
| Drift present. Decide before the review pause continues: fix now, accept and log, or ticket.

## Checklist coverage
<n>/<n> skills checked had a `checklist.md`; prose-fallback: <skill-name, skill-name, ...> (or "none - full checklist coverage").
```

Omit empty sections (Drift / Gap / Style / Enforced). Never list Followed / N/A rows in chat; give a count instead: "N rules Followed, N N/A, N Enforced." Omit "Checklist coverage" only when every checked skill had a `checklist.md`.

**`Enforced` is not a fifth flavor of "skipped."** A row lands here only after the subagent confirmed, in *this* target repo, right now, that the named mechanism exists and is currently green (see [`subagent-prompt.md`](subagent-prompt.md) for the exact check). It is mechanically guaranteed, not manually judged - distinct from `Followed` (an LLM read the code and judged it matches) and from `N/A` (the rule doesn't apply here at all). If the mechanism is tagged in the checklist but turns out missing or red in this repo, the row is **not** `Enforced` - it falls back to the normal `Followed`/`Drift`/`Gap`/`Style`/`N/A` judgment, with a note that it was tagged but not wired here.

## Full audit (file or canvas)

Path: `docs/verify/YYYY-MM-DD-<slug>.md` (or the repo's own docs convention).

```markdown
# Pack conformance audit: <slug>

**Date:** YYYY-MM-DD
**Mode:** full audit
**Packs checked:** ...
**Scope:** whole repo | <named area>

## Summary
1-3 sentences. Drift count, Gap count, headline risk.

## Drift
... (same shape as gate, one row per rule)

## Gap
...

## Style
...

## Enforced (mechanically covered)
| Rule | Skill | Mechanism | Evidence |
|------|-------|-----------|----------|
| <rule, one line> | `<skill-name>` | <editorconfig\|analyzer\|architecture-test\|regression-test> | `<path>:<line>` (rule id / test name), and confirmation the build/suite is green |

Count only - same rule as gate: mechanically confirmed present and green in this repo, not re-derived semantically. See [`subagent-prompt.md`](subagent-prompt.md) for the health-check contract and [`rule-extraction.md`](rule-extraction.md) for what each `Enforcement` value means.

## Aligned (Followed highlights)
Short list of what already matches the pack. Keeps the report honest, not only a complaint list.

## Out of scope
...

## Checklist coverage
<n>/<n> skills checked had a `checklist.md`; prose-fallback: <skill-name, skill-name, ...> (or "none - full checklist coverage").

## Verdict
...
```

Chat: paste Summary + Verdict + file path (or canvas path if that surface was chosen).
