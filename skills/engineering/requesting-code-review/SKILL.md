---
name: requesting-code-review
description: Use when completing tasks, implementing major features, or before opening a PR — self-review the diff against requirements and quality standards.
metadata:
  area: engineering
  upstream:
    repo: obra/superpowers
    path: skills/requesting-code-review
    url: https://github.com/obra/superpowers/tree/main/skills/requesting-code-review
    synced_at: "2026-06-07"
    commit: 6fd4507659784c351abbd2bc264c7162cfd386dc
    note: Adapted — self-review in the same session, no subagents.
---

# Requesting Code Review

Self-review your work before it ships. Catch issues while context is fresh.

**Core principle:** Review early, review often.

**Announce at start:** "Using the requesting-code-review skill."

## When to Request Review

**Mandatory:**
- After completing a major feature or plan task
- Before opening a PR (`ship-feature`)

**Optional but valuable:**
- When stuck (fresh perspective on your own diff)
- Before refactoring (baseline check)
- After fixing a complex bug

**Escalate to `code-review-and-quality`** when the diff is large (~100+ lines), touches auth/security, public APIs, or performance — full 5-axis review.

## How to Review

### 1. Get git range

```bash
# from the base branch
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master
BASE_SHA=<output above>
HEAD_SHA=$(git rev-parse HEAD)

git diff --stat $BASE_SHA..$HEAD_SHA
git diff $BASE_SHA..$HEAD_SHA
```

### 2. Gather context

- **What was implemented:** 2-3 sentence summary
- **Requirements / plan:** path to plan, spec, or user requirements

### 3. Run self-review

Follow the checklist in `references/self-review-checklist.md`. Produce output in the format defined there (Strengths, Issues by severity, Assessment).

### 4. Act on feedback

- Fix **Critical** issues immediately
- Fix **Important** issues before `ship-feature`
- Note **Minor** issues for later (or fix if quick)
- Push back on feedback only with technical reasoning and evidence

## Integration with Workflows

**Executing plans:**
- Review after each task or at natural checkpoints in the plan
- Fix before moving to next task

**Ad-hoc development:**
- Review before `ship-feature`
- Review when stuck

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore Critical issues
- Proceed to PR with unfixed Important issues
- Say "looks good" without reading the diff

**If a finding seems wrong:**
- Verify with tests or code reading
- Document why it's a false positive
- Fix only what holds up under scrutiny
