---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
metadata:
  area: workflow
  upstream:
    repo: obra/superpowers
    path: skills/executing-plans
    url: https://github.com/obra/superpowers/tree/main/skills/executing-plans
    synced_at: "2026-06-07"
    commit: 6fd4507659784c351abbd2bc264c7162cfd386dc
    note: Adaptada — sem subagents/worktrees; usa ship-feature ao finalizar.
---

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

## The Process

### Step 1: Load and Review Plan
1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. If concerns: Raise them with your human partner before starting
4. If no concerns: Create TodoWrite and proceed

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow each step exactly (plan has bite-sized steps)
3. Run verifications as specified
4. Mark as completed

### Step 3: Complete Development

After all tasks complete and verified:
- Run `requesting-code-review` on the full diff
- Announce: "Estou usando a skill ship-feature para finalizar."
- **REQUIRED SUB-SKILL:** Use `ship-feature` — commit, push, open PR (never merge to main)

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Hit a blocker (missing dependency, test fails, instruction unclear)
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly

**Ask for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## Remember
- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Reference skills when plan says to
- Stop when blocked, don't guess
- Never start implementation on main/master branch without explicit user consent

## Integration

**Related skills:**
- **writing-plans** — creates the plan this skill executes
- **requesting-code-review** — review before shipping
- **ship-feature** — commit, push, open PR after all tasks
