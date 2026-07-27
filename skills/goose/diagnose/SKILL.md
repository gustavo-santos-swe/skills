---
name: diagnose
description: Evidence-first debug to root cause, then fix and lock. Use when something is broken, flaky, or failing tests - before guessing a fix.
disable-model-invocation: true
metadata:
  area: goose
  inspired_by:
    - mattpocock/skills - diagnosing-bugs
    - obra/superpowers - systematic-debugging
---

# Diagnose

On-ramp for failures. Find the **root cause**, fix it, and leave a **lock** so it stays fixed.

Voice for commits/comments on the fix: **`write-like-goose`**.

**Iron law:** no fix without evidence. Symptom patches are failure.

## When to use

- Bug, unexpected behavior, test red, build break, perf regression.
- Flake / intermittent failure.
- "Just one quick fix" feels tempting under pressure.

## When not to

- Feature work with no failure signal → **`implement`** (or brainstorm/planning first).
- Pure "how should we design X" with nothing broken → **`brainstorm`**.

## Paths

| Path | When | Extra rules |
|------|------|-------------|
| **Simple** | Default | Reliable repro (steps and/or a command). One falsifiable hypothesis at a time. |
| **Hard** | Flake / intermittent, regression between two known-good states, user already tried and missed, **or** simple path failed to close in one hypothesis cycle | One **agent-runnable** command that goes red on *this* symptom. Ranked list of 3-5 hypotheses with predictions before testing. |

Promote simple → hard as soon as a hard trigger hits. Don't thrash in simple mode.

## Flow

```
orient → repro → [promote hard?] → hypothesize → prove → fix+lock → cleanup+note
```

### 1. Orient

- Restate the **user's symptom** in one sentence (not your theory).
- Skim recent changes and the obvious call path. Don't invent a root cause yet.
- Pick **simple** or **hard** from the table above.

### 2. Repro

Always required.

- **Simple:** numbered steps and/or a command that shows the failure. Run it (or walk the user through HITL) until the symptom appears.
- **Hard:** build a **tight loop** - one command you have already run, that:
  - hits the bug path and asserts the **exact symptom** (not "didn't crash")
  - is deterministic enough to debug (flake: raise repro rate until usable)
  - is fast enough to iterate (seconds when possible)
  - you can run unattended (HITL script only if a human must click)

No red-capable signal → stop. List what you tried. Ask for env access, artifact (log/HAR/dump), or permission for temporary instrumentation. **Do not** proceed to hypothesize without a loop on the hard path.

**Minimise** once red: cut inputs/steps one at a time; keep only what is load-bearing for the failure.

Completion: symptom reproduced; on hard, the command is named and shown red at least once.

### 3. Hypothesize

- **Simple:** one falsifiable hypothesis. Format: "If X is the cause, then changing Y will make the symptom go away / changing Z will make it worse."
- **Hard:** write **3-5 ranked** hypotheses with predictions. Show the list to the user (don't block if AFK). Then test from the top.

If you can't state a prediction, it's a vibe - sharpen or drop it.

### 4. Prove

Test **one** variable at a time against the current hypothesis.

Prefer: debugger/REPL → targeted logs at distinguishing boundaries → never "log everything".

Tag temporary logs with a unique prefix (e.g. `[DEBUG-a4f2]`) so cleanup is a single grep.

**Perf:** measure first (timing, profiler, query plan), then bisect. Don't "optimize by feel".

Hypothesis wrong → next hypothesis (hard) or form a new one (simple). Don't stack unrelated fixes.

### 5. Fix + lock

Only after evidence points to a cause.

1. Prefer a **lock before or with the fix**: failing test / assertion at a seam that exercises the **real** bug pattern.
2. If no correct seam exists, say so - that is a finding. Still fix if you can verify via the Phase 2 loop; note the missing seam in the prevention note.
3. Apply the minimal fix for that cause.
4. Watch the lock go green (or the hard loop go green on the original symptom).
5. Re-run the original (un-minimised) repro once.

### 6. Cleanup + prevention note

Before calling done:

- [ ] Original symptom gone (re-run the repro / hard command)
- [ ] Lock in place, or missing seam documented
- [ ] All `[DEBUG-…]` / throwaway harnesses removed or clearly marked
- [ ] **Prevention note** (1-3 concrete lines): what would have caught or prevented this - skip if nothing honest to say

Then ship the fix via **`git-practices`** → **`pr-raise`** when the change leaves the tree.

## Guardrails

1. Repro (simple) or red loop (hard) **before** proposing a fix; one hypothesis at a time.
2. Done = original repro green **and** lock in place (or missing seam documented).
3. Fix (or prove you can’t yet) here - filing/prioritizing tracker tickets is out of scope for this skill.

## For other Goose skills

> Failure / flake / regression → use `diagnose` before guessing a patch.
