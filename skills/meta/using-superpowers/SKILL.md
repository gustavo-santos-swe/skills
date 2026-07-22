---
name: using-superpowers
description: Use when starting any conversation or task — check available skills before responding or acting. Use when deciding which skill applies, or when beginning new work.
metadata:
  area: meta
  upstream:
    repo: obra/superpowers
    path: skills/using-superpowers
    url: https://github.com/obra/superpowers/tree/main/skills/using-superpowers
    synced_at: "2026-06-07"
    commit: 6fd4507659784c351abbd2bc264c7162cfd386dc
    note: Adaptada para Cursor + Skills Over MCP.
---

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST read and follow that skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## Instruction Priority

Skills override default behavior, but **user instructions always take precedence**:

1. **User's explicit instructions** (rules, AGENTS.md, direct requests) — highest priority
2. **Skills from this repo** — override default behavior where they conflict
3. **Default system prompt** — lowest priority

## How to Access Skills

**In Cursor (this repo via MCP):** Skills are exposed as MCP tools at `gustavo-santos-swe/skills`. When a skill can apply, **read the full content** (MCP tool or `Read` on the local file) and follow it directly.

**Never** assume you remember a skill's content — skills evolve. Always read the current version.

## The Rule

**Check and invoke relevant skills BEFORE any response or action.** Even a 1% chance a skill might apply means you should read it. If it doesn't fit, you can stop — but you must check first.

1. User message received → alguma skill pode aplicar?
2. Se sim (mesmo 1%) → ler a skill → anunciar: "Estou usando a skill X para Y"
3. Se a skill tem checklist → criar todos e seguir na ordem
4. Seguir a skill exatamente → responder

## Red Flags

These thoughts mean STOP — you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | Skill check comes BEFORE clarifying questions. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "I remember this skill" | Skills evolve. Read current version. |
| "The skill is overkill" | Simple things become complex. Use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |

## Skill Priority

When multiple skills could apply:

1. **Process skills first** (brainstorming, grilling / grill-with-docs, systematic-debugging / diagnosing-bugs) — HOW to approach
2. **Implementation skills second** (test-driven-development / tdd, frontend-design, writing-plans, implement, mcp-builder) — execution
3. **Completion skills last** (verification-before-completion, ship-feature)

Examples:
- "Let's build X" → brainstorming or grilling (grill-with-docs if domain language matters) → writing-plans / to-tickets → executing-plans / implement
- "Fix this bug" → systematic-debugging or diagnosing-bugs → test-driven-development / tdd
- "It's done" → verification-before-completion → ship-feature

## Skill Types

**Rigid** (TDD, debugging, verification): Follow exactly. Don't adapt away discipline.

**Flexible** (brainstorming, writing-plans): Adapt principles to context.

The skill itself tells you which.

## User Instructions

Instructions say WHAT, not HOW. "Add X" or "Fix Y" doesn't mean skip workflows.
