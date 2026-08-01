---
name: verify
description: Iterate every active pack SKILL.md against real code (gate on a diff, or full audit on an existing codebase); classify each rule as Drift, Gap, or Style. Use after implement, as a pr-review guidelines pass, or when asked to audit an existing repo against the packs.
metadata:
  area: goose
---

# Verify

Goose handbook for **checking code against the pack skills it should follow** - one line per rule, not a vibe check. Fills the done gate `ask` flagged after `implement`.

Voice: **`write-like-goose`**.

## When to use

- End of an **`implement`** batch, before the review pause (**gate**)
- **`pr-review`** Guidelines axis, instead of eyeballing pack conformance
- User asks to audit an existing / inherited repo against the packs (**full audit**)

## When not to

- Design still open → **brainstorm** / **research**
- Trust-boundary depth → **security-check** (this skill defers security findings there, doesn't repeat them)
- Correctness / logic bugs in a PR → **pr-review** other axes
- Pack **how-to** itself (what the rule should be) → the pack skill, not this one

## Hard rules

1. **Read every active `SKILL.md` fresh.** Do not judge from memory of what a skill says. Memory is what drifted in the first place.
2. **One row per rule, not per skill.** A skill with eight checkable rules produces up to eight rows. Collapsing to "mostly follows X" is premature completion.
3. **Target repo wins stays live.** A rule a pack states as a *greenfield default* is not Drift if the repo already documents a deliberate alternative. Ask when it is unclear whether a variance is deliberate or missed.
4. **Report only.** Fixes flow back through **implement** after the engineer decides. This skill never edits code.
5. **Gate Drift blocks the implement review pause.** Full-audit Drift does not block anything by itself. It is a backlog input, not a rewrite order.
6. **Defer security to `security-check`.** Route auth/secrets/injection findings there; note the row here as "see security-check" instead of scoring it twice.
7. **Never grade in the orchestrating context.** The agent that just implemented (or is reviewing) the code is a biased judge of it. Dispatch one subagent per skill (or per cluster) to do the actual grading; the orchestrator only dispatches, collects, and gates. Mechanics: [`references/subagent-dispatch.md`](references/subagent-dispatch.md).
8. **Discover skills by glob, not memory.** "Which skills are in this pack" is a `find <pack>/dotnet -name SKILL.md` fact, run fresh every time, never an LLM guess from a README skim or a prior run. Full audit dispatches every skill the glob returns; gate may filter that universe by touched paths but never invents or drops from it by feel.
9. **Checklist before prose.** If a skill ships `references/checklist.md`, that file is the rule list - no re-derivation from prose. Only fall back to reading the skill's prose (via `rule-extraction.md`) when the checklist is missing, and say so in the report so the gap is visible.

## Modes

| Mode | Scope | Trigger | Deliverable |
|------|-------|---------|--------------|
| **Gate** | Branch diff or uncommitted change, against the pack(s) already loaded | End of `implement`, or `pr-review` Guidelines axis | Chat report; **Drift blocks the review pause** until the engineer decides |
| **Full audit** | Whole repo (or a named area) against every applicable pack | User asks to audit an existing / inherited codebase | Report on the surface they pick (chat / markdown / canvas) |

Default is whichever mode the trigger implies. Ask only when genuinely ambiguous.

## Classification

| Label | Meaning | Blocks gate? |
|-------|---------|---------------|
| **Drift** | Code does what a pack rule (hard rule, "Don't", or stated default) forbids, with no documented local override | Yes |
| **Gap** | Pack area not implemented yet (acceptable on a POC or early slice) | No |
| **Style** | Cosmetic mismatch (naming, ordering) with no behavior cost | No |
| **Followed** | Rule checked; code matches | - |
| **Enforced** | Rule's checklist `Enforcement` tag (`editorconfig`/`analyzer`/`architecture-test`/`regression-test`) is confirmed present and green in this repo right now - mechanically guaranteed, not manually judged | - |
| **N/A** | Rule does not apply to this repo, stack, or slice | - |

Drift vs Gap is the call that matters. **Drift**: did something the rule forbids. **Gap**: has not done the thing yet. Don't inflate a Gap into a Drift to sound thorough.

**`Enforced` is a cheap-verification path, not a skipped check.** A row only earns it after the subagent confirms - in this run, against this repo - that the named tool/test actually exists and is currently green; it never comes from trusting a checklist tag at face value. A tagged rule whose mechanism is missing or red here still gets the full Followed/Drift/Gap/Style/N/A judgment, exactly as if it had no tag. Mechanics: [`references/subagent-prompt.md`](references/subagent-prompt.md) step 3a, tag semantics: [`references/rule-extraction.md`](references/rule-extraction.md).

## Steps

### Gate

1. **Scope** - branch diff vs base, or uncommitted tree. Confirm which pack(s) `implement` already loaded, or detect from touched paths with the pack README maps.
2. **Enumerate + filter** - glob every `SKILL.md` in the active pack(s) (never from memory); filter that list against touched paths using the pack README's map to get the touched-skill subset.
3. **Resolve + dispatch** - resolve absolute paths (skill files, `rule-extraction.md`, repo root, touched-path hints); fan out one subagent per touched skill, all in one message. Mechanics + prompt: [`references/subagent-dispatch.md`](references/subagent-dispatch.md) + [`references/subagent-prompt.md`](references/subagent-prompt.md).
4. **Collect** - wait for every subagent; concatenate their tables; sanity-check each `Counts:` line against its rows; re-dispatch on mismatch or malformed output.
5. **Report** in chat, using [`references/report-template.md`](references/report-template.md). Omit no rule row; only omit whole skills with zero surface in the diff.
6. **Gate** - Drift present: tell the engineer and wait for a decision (fix now / accept and log / ticket) before the `implement` review pause continues. Gap and Style never block.

### Full audit

1. **Scope** - whole repo, or a named area if the user narrows it.
2. **Detect packs** - which stack pack(s) apply (same table `implement` uses).
3. **Enumerate, no filter** - glob every `SKILL.md` in each detected pack; dispatch all of them, exhaustively, no relevance filtering. If a pack has more skills than the per-skill default covers comfortably, ask the granularity question in [`references/subagent-dispatch.md`](references/subagent-dispatch.md) (per-skill vs per-cluster) - the exhaustiveness itself is never up for debate, only the batching.
4. **Resolve + dispatch** - same mechanics as gate step 3, scoped to the whole codebase (or named area) instead of a diff.
5. **Collect** - same as gate step 4.
6. **Ask surface** - chat, markdown doc, or canvas. No silent default; ask.
7. **Report** using [`references/report-template.md`](references/report-template.md); canvas via [`references/canvas-layout.md`](references/canvas-layout.md) + [`references/verify-canvas.template.tsx`](references/verify-canvas.template.tsx) if chosen.
8. **Next** - Drift items: engineer decides fix-now vs ticket (**create-tickets**, which dedups rows by root cause into slices - this skill reports one row per rule on purpose and never collapses them itself). Gap items: candidate backlog, not urgent by default.

Stop when a rule's applicability is genuinely unclear (stack mismatch, ambiguous local override). Ask; don't guess a classification.

**Done when:** every rule of every active pack has a row (Enforced / Followed / Drift / Gap / Style / N/A) with evidence; gate Drift has an explicit engineer decision before the review pause continues.

## Guardrails

1. Report only. Never edit code from this skill.
2. Read pack `SKILL.md` files fresh every run. No cached memory of "what the dotnet pack says."
3. Exhaustive at the rule level. A skipped rule is a bug in the run, not an acceptable shortcut.
4. Never grade in the orchestrating context - dispatch, don't self-judge. Same rule applies recursively: a subagent checks one skill and nothing it just wrote.
5. Security findings route to **security-check**, not scored here.
6. Gap is not Drift. Don't punish a POC for work it has not reached yet.

## References

- [`references/rule-extraction.md`](references/rule-extraction.md) - checklist-first, prose-fallback method for turning a skill into checkable rows
- [`references/subagent-dispatch.md`](references/subagent-dispatch.md) - granularity, path resolution, collecting, failure handling
- [`references/subagent-prompt.md`](references/subagent-prompt.md) - the literal prompt every dispatched subagent gets
- [`references/report-template.md`](references/report-template.md) - fixed report shape (gate + full audit)
- [`references/canvas-layout.md`](references/canvas-layout.md) - canvas surface for full audit
- [`references/verify-canvas.template.tsx`](references/verify-canvas.template.tsx) - copy-paste canvas

## Related

- Build → **implement** (calls this skill at the done bar)
- PR guidelines axis → **pr-review**
- Trust boundary depth → **security-check**
- Drift needing a ticket → **create-tickets**
- Voice → **write-like-goose**
