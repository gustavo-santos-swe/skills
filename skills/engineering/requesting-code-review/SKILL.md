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
    note: Adaptada — self-review na mesma sessão, sem subagents.
---

# Requesting Code Review

Self-review your work before it ships. Catch issues while context is fresh.

**Core principle:** Review early, review often.

**Announce at start:** "Estou usando a skill requesting-code-review."

## When to Request Review

**Mandatory:**
- After completing a major feature or plan task
- Before opening a PR (`ship-feature`)

**Optional but valuable:**
- When stuck (fresh perspective on your own diff)
- Before refactoring (baseline check)
- After fixing a complex bug

**Escalar para `code-review-and-quality`** quando o diff for grande (~100+ linhas), tocar auth/security, APIs públicas ou performance — review nos 5 eixos completos.

## How to Review

### 1. Get git range

```bash
# desde a branch base
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master
BASE_SHA=<resultado acima>
HEAD_SHA=$(git rev-parse HEAD)

git diff --stat $BASE_SHA..$HEAD_SHA
git diff $BASE_SHA..$HEAD_SHA
```

### 2. Gather context

- **What was implemented:** resumo em 2-3 frases
- **Requirements / plan:** caminho do plano, spec, ou requisitos do usuário

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
