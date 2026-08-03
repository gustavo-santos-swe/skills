# Verify: prevention over post-hoc audit

**Date:** 2026-08-02  
**Status:** draft  
**Branch intent:** reshape Goose lifecycle so pack conformance happens during build, not as a costly after-the-fact gate

## Goal

Cut the implement → verify → fix → re-verify loop by making the builder follow pack checklists while coding, and reserve `verify` for audits the engineer asks for.

## Why the current flow is expensive

### Causal chain (today)

```text
implement loads full pack (read once)
  → agent codes (rules leave attention)
    → done bar runs verify gate (mandatory)
      → N subagents (one per touched skill), report-only
        → Drift found → pause for engineer decision
          → implement fixes → verify again
            → (often) pr-review Guidelines runs verify again
```

Four cost drivers stack:

| Driver | What burns money / time | Why it exists today |
|--------|-------------------------|---------------------|
| **A. Post-hoc detection** | Drift is written first, then found | Conformance is a gate after the build, not a constraint during it |
| **B. Isolation tax** | One `generalPurpose` subagent per skill; re-dispatch on bad shape | Hard rule: never grade in the orchestrating context |
| **C. Report-only loop** | Verify cannot edit; engineer must decide; then re-run | Hard rule: report only; gate blocks until decision |
| **D. Double pass** | Same pack check at implement done bar and at `pr-review` | Both skills call verify for Guidelines / gate |

The pain you feel (“lots of back and forth”) is mostly **A + C**. The token bill is mostly **B + D**. Fixing only B (cheaper verify) leaves the fix loop. Fixing only A without changing when verify runs still pays B on every slice.

### What “do it right the first time” means here

The agent must treat pack `checklist.md` rows for skills that apply to this slice as **build constraints**, the same way it treats acceptance criteria. Misses get fixed in the same implement turn, before any pause. An independent audit is optional later, not the way every slice discovers basic pack mistakes.

## Approach (how the suggestion actually solves it)

**Move the conformance work into `implement`. Demote `verify` from a mandatory done-bar gate to an on-request / full-audit tool.**

| Concern | Who owns it after the change | Mechanism |
|---------|------------------------------|-----------|
| Follow pack rules while coding | **`implement`** | Live checklist for touched skills; fix before pause |
| Independent audit of a repo or PR | **`verify`** | Same rigor as today (subagents, report-only), but only when asked or as optional PR Guidelines |
| Correctness / SoT / security-in-diff | Unchanged | `implement` self-check, `pr-review` other axes, `security-check` |

### Before vs after (one slice)

```text
BEFORE (costly loop)
  build → verify fan-out → Drift report → you decide → fix → verify again → pause

AFTER (prevention)
  pick touched skills → code against those checklists → self-check + fix in-turn → pause
  verify only if you ask, or optional PR Guidelines, or full-repo audit
```

### Why each driver shrinks

| Driver | After the change |
|--------|------------------|
| **A. Post-hoc** | Checklist is open during build. Self-check runs before pause and **may edit**. Drift that the builder can see dies in the same turn. |
| **B. Isolation tax** | Daily slice: no subagent fan-out. Parent already loaded the pack; it walks checklist rows for touched skills only. |
| **C. Report-only loop** | Daily slice: no separate report-only skill in the middle. No mandatory “wait for engineer on every Drift” before fix. |
| **D. Double pass** | Default: verify once at most (PR Guidelines if you keep it), or zero times for small work. Full audit stays explicit. |

### Honest trade-off

Self-check is a **biased** judge (same agent that wrote the code). That is the price of killing the loop.

Mitigation (pick one in Task 5; default below):

1. **Default:** keep `verify` as the optional / on-request independent judge (`/verify`, full audit, or `pr-review` Guidelines when the engineer wants rigor).
2. **Stricter:** `pr-review` always runs verify Guidelines (independent once per PR, not per implement pause).
3. **Cheapest:** verify only when the human types `/verify` or asks for a full audit.

Recommended default for Goose: **(1) on-request + full audit; (2) only if the engineer opts into a strict PR Guidelines pass** — not automatic on every implement done bar.

## Assumptions

- Pack skills already ship `references/checklist.md` for almost all `dotnet` skills (25/26 today; `resilience` still missing). Checklist-first is the contract.
- “Touched skills” can be derived from the pack README map + paths/concerns in the batch (same idea verify gate already uses for filter). Exact mapping rules land in Task 2.
- Context cost of “load every `SKILL.md` at implement start” stays for now. This plan does not thin the pack load; it stops paying a second full audit machine after every build.
- Mutation testing and other slow CI gates stay out of the local loop (separate guidance already in `testing`).

## File map

| Action | Path | Role |
|--------|------|------|
| Modify | `skills/goose/implement/SKILL.md` | Live checklist during build; replace mandatory verify gate with in-turn self-check |
| Modify | `skills/goose/implement/references/done-checklist.md` | Done bar matches new gate |
| Create | `skills/goose/implement/references/pack-conformance.md` | How to pick touched skills, walk checklists, self-check, when to call verify |
| Modify | `skills/goose/verify/SKILL.md` | Remove “end of implement” as default trigger; keep full audit + on-request (+ optional PR) |
| Modify | `skills/goose/verify/references/subagent-dispatch.md` | Gate mode wording: only when verify actually runs |
| Modify | `skills/goose/ask/SKILL.md` | Main-flow diagram and table: verify no longer mandatory after every implement |
| Modify | `skills/goose/pr-review/SKILL.md` | Guidelines: call verify only when engineer asks or when a “strict guidelines” flag is set (see Task 5) |
| Modify | `skills/goose/pr-review/references/review-axes.md` | Guidelines axis: default = pack smell skim / checklist spot-check; verify = optional deep pass |
| Modify | `skills/goose/create-tickets/SKILL.md` | Keep verify full-audit report as backlog input; drop implication that every implement ends in verify |
| Modify | `skills/goose/README.md` | Lifecycle map matches ask |
| Create | `skills/goose/implement/dotnet/resilience/references/checklist.md` | Close the only missing checklist so prose-fallback is not a silent hole |
| Test | Manual dry-run on a toy slice (Task 7) | Prove one implement pause with no verify fan-out |

## Tasks

### Task 1: Freeze the new ownership model in prose

**Files:** this plan (already); then `ask/SKILL.md` lifecycle table as the source of truth for “when verify runs”

**Acceptance:**

- Documented triggers for `verify` are only: (a) user asks, (b) full audit of an existing/inherited repo, (c) optional PR Guidelines deep pass per Task 5 decision.
- Documented owner of daily pack conformance is `implement` via checklists.
- One sentence in `ask` states: implement must not call verify as a mandatory done-bar gate.

**Verify:** Read `ask` main-flow table; no arrow that implies verify after every implement batch.

### Task 2: Write `implement/references/pack-conformance.md`

**Files:** create `skills/goose/implement/references/pack-conformance.md`

**Content that must be in the file (no placeholders):**

1. **When:** after pack load, before feature code; again at done bar before review pause.
2. **Pick touched skills:**
   - Start from the glob of `SKILL.md` under the loaded pack(s) (filesystem fact, not memory).
   - Keep a skill if the batch touches its concern (use pack README map + paths + ticket keywords).
   - Always keep core skills that apply to every feature change in that pack when the README marks them as such (for `dotnet`: at least `solution-structure`, `testing`, `code-style` when any production code or test changes; add `application-layer` / `domain-modeling` / `db-integration` / `validation` / `error-handling` / `endpoint-conventions` when those layers appear in the diff or ticket).
   - Cap is not a skip list: if unsure whether a skill applies, include it.
3. **Load checklists:** for each touched skill, read `references/checklist.md`. If missing, say so and extract hard rules from that skill’s body once (same spirit as verify’s prose fallback), then prefer backfilling the checklist later.
4. **During build:** treat `verify`-enforcement rows as constraints while writing code. Prefer fixing a miss immediately when noticed.
5. **Done-bar self-check (same agent, may edit):**
   - Walk every checklist row for touched skills against the dirty tree / branch diff.
   - Rows tagged `editorconfig` / `analyzer` / `architecture-test` / `regression-test`: confirm mechanism exists and is green in this repo (same health idea as verify’s Enforced lane). If mechanism missing, judge the code manually for that row.
   - On miss: **fix now** in this turn when the fix is in batch scope. If out of scope or needs a product decision: note Gap / accept-and-log / ticket — do not invent a verify report ceremony.
6. **When to call `verify` anyway:** engineer asks; full-repo audit; optional strict PR Guidelines (Task 5).
7. **What this is not:** not a second copy of verify’s subagent protocol; not report-only; not one row per rule pasted into chat by default. Chat gets a short conformance note: skills checked, misses fixed, open Gaps.

**Acceptance:** File exists; an agent can follow it without opening `verify/SKILL.md`.

**Verify:** Dry-read: every step is imperative and ≤20 words per procedure sentence (Goose voice).

### Task 3: Rewire `implement` done bar

**Files:** `skills/goose/implement/SKILL.md`, `skills/goose/implement/references/done-checklist.md`

**Changes:**

- Hard rule / steps: after Load pack(s), add “Open pack conformance” pointing at `pack-conformance.md`.
- Done bar: replace “Run `verify` (gate)…” with “Run pack-conformance self-check; fix in-batch misses before pause.”
- Self-check section: pack conformance is implement’s job via checklists; `verify` is on-request / audit.
- Related: verify is no longer “part of the done bar, not optional.”
- `done-checklist.md`: same wording; remove mandatory verify checkbox; add pack-conformance self-check checkbox.

**Acceptance:** Grep of `implement/` shows no “mandatory” / “not optional” verify gate on the done bar.

**Verify:** `rg -n 'verify' skills/goose/implement/SKILL.md skills/goose/implement/references/done-checklist.md` and confirm each hit matches the new model.

### Task 4: Narrow `verify` triggers

**Files:** `skills/goose/verify/SKILL.md`, `skills/goose/verify/references/subagent-dispatch.md` (and report template only if it says “end of implement”)

**Changes:**

- `When to use`: remove “End of an implement batch, before the review pause” as a default. Keep full audit; keep “user asks”; keep optional PR Guidelines deep pass.
- `When not to`: add “Routine end of implement — use implement pack-conformance self-check.”
- Modes table: Gate mode becomes “diff-scoped audit when verify was invoked (user / PR deep pass),” not “always after implement.”
- Hard rule “Gate Drift blocks the implement review pause”: reword to “When verify runs as a gate the engineer requested, Drift blocks until they decide.” Implement’s own pause is no longer owned by verify.
- Keep: report-only, subagent isolation, checklist-first, glob discovery — these stay valuable for real audits.

**Acceptance:** An agent that only reads `verify/SKILL.md` will not start a fan-out at the end of a normal implement batch.

**Verify:** Description frontmatter + When to use list match the three triggers in Task 1.

### Task 5: Decide PR Guidelines depth (choose default, document it)

**Files:** `skills/goose/pr-review/SKILL.md`, `skills/goose/pr-review/references/review-axes.md`

**Decision to encode (recommended):**

| PR situation | Guidelines behavior |
|--------------|---------------------|
| Normal review | Spot-check against pack README + touched-skill checklists in the reviewing agent (no verify fan-out) |
| Engineer says “strict guidelines” / “run verify” / full audit language | Call `verify` gate on the PR diff |
| Tiny LGTM PR | Smell baseline + obvious pack Don’ts only |

**Acceptance:** `pr-review` no longer states that Guidelines “runs verify rather than eyeballing” as the only path.

**Verify:** Related link still points to verify for the deep pass.

### Task 6: Align router and tickets docs

**Files:** `skills/goose/ask/SKILL.md`, `skills/goose/README.md`, `skills/goose/create-tickets/SKILL.md`

**Changes:**

- Main flow: `implement` → (optional verify) → … or `implement` → git-practices, with verify as a side door.
- create-tickets: keep “Input: a verify report” for full-audit backlog; clarify that everyday implement does not produce that report.

**Acceptance:** No lifecycle diagram still shows verify as an automatic box after every implement.

### Task 7: Close `resilience` checklist gap

**Files:** create `skills/goose/implement/dotnet/resilience/references/checklist.md` from that skill’s hard rules / Don’ts (Enforcement column included).

**Acceptance:** `find skills/goose/implement/dotnet -name SKILL.md` paired with checklist: zero MISS.

**Verify:** `find …` one-liner from earlier exploration returns only HAS.

### Task 8: Manual dry-run (prove the loop is gone)

**Files:** none in skills repo required; run against any small .NET slice or a dry mental walkthrough recorded in the PR body.

**Script:**

1. Pretend implement on a one-handler change.
2. Confirm agent opens 3–6 touched checklists, not 26 subagents.
3. Confirm done bar text asks for pack-conformance self-check, not verify gate.
4. Confirm `/verify` still dispatches subagents for an explicit audit.

**Acceptance:** PR Notes describe that walkthrough; no skill text contradicts it.

## Risks

| Risk | Mitigation |
|------|------------|
| Self-check rubber-stamps its own code | Keep `/verify` and optional strict PR Guidelines; do not delete verify |
| Agent “forgets” checklists mid-build | pack-conformance.md requires re-open at done bar; done-checklist checkbox |
| Touched-skill filter under-selects | “If unsure, include”; always-on core set for code/test changes |
| Engineers still invoke `/verify` every time by habit | ask/README say when not to; short Briefing in the reshape PR |
| Pack load at start stays expensive | Out of scope here; separate plan if needed (progressive disclosure / load-by-touch) |

## Out of scope

- Thinning “load every `SKILL.md` before coding” (separate cost; different lever).
- Rewriting verify’s subagent prompt or Enforced health checks (keep for real audits).
- Auto-generating checklists with an LLM at runtime.
- Changing CI mutation / Stryker policy (already pipeline-or-request).
- Merging this with unrelated open PRs (`docs/mutation-pipeline-or-request`, etc.).

## Open questions

1. **PR Guidelines default:** recommended = spot-check; verify only on request. Confirm before Task 5 lands.
2. **Always-on core skill set for `dotnet`:** proposed list in Task 2. Confirm or edit before coding Task 2.
3. **Should Gate mode stay as a named verify mode** for “user asked to gate this diff,” or rename to “Diff audit” to avoid sounding like the old implement done bar? Recommendation: rename to **Diff audit** in verify’s Modes table.

## Success metrics (after merge, qualitative)

- Normal implement pause: **zero** verify subagent dispatches unless the engineer asked.
- Pack misses that used to appear as Drift rows after the build show up as **in-turn edits** or an explicit Gap/ticket note at pause.
- `/verify` and full audit still produce one-row-per-rule reports with subagent isolation.

## Next

After you confirm Open questions (especially #1 and #2): **implement** this plan as one docs/skills PR (single slice; no create-tickets split needed unless you want resilience checklist on its own).
