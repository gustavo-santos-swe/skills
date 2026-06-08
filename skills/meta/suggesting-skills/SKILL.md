---
name: suggesting-skills
description: Look at what the user keeps re-explaining to the agent and propose new SKILL.md files that would replace those repeated explanations. Use when the user says "what skills should I have", "suggest skills", "audit my skills", or when you notice you're being asked the same kind of task three times in a row.
metadata:
  area: meta
license: MIT
---

# Suggesting Skills

Find the gaps in the user's skill library. Skills are most valuable when they capture the things the user *would otherwise have to explain to the agent every time*.

## When to use

- The user explicitly asks "what skills am I missing", "what should I add", "audit my skills".
- You notice the same kind of request happening repeatedly in a session — that's a skill waiting to be written.
- After a long session, before the user closes the chat, offer to extract any reusable playbook from the work just done.

## Steps

1. **Inventory what's already there.** Read every `SKILL.md` in the repo. Note for each: name, the trigger phrase in the description, and the one-line goal. If two existing skills overlap, flag the duplication.

2. **Look for the pattern of "I keep telling you to…".** Strong candidates for new skills are:
   - **Repeated workflow** — the user has asked for the same multi-step task at least twice.
   - **Repeated correction** — the user has had to fix the same kind of mistake the agent makes (formatting, voice, missing a step).
   - **Tribal knowledge** — facts about *this* user's stack, team, or product that aren't in the codebase but the user keeps having to restate.
   - **External tool wiring** — the user has an MCP, CLI, or API the agent could be using but isn't.

3. **Propose 3–5 candidate skills**, each as a one-paragraph pitch:
   ```
   Name:        kebab-case-name
   Trigger:     when the user says "..." or asks to "..."
   What it does: one sentence
   Why it's worth a skill: the repeated thing it replaces
   ```

4. **Rank them.** Sort by frequency × annoyance: how often does the situation come up, and how painful is it when it's not automated?

5. **Ask the user which 1–2 to actually write.** Don't auto-generate all of them. Skills that aren't trusted get ignored, which is worse than not having them.

6. **For each chosen skill, scaffold a `SKILL.md`** in `skills/<name>/` with:
   - Frontmatter (`name`, `description` with trigger phrases, `license`).
   - "When to use" — the trigger conditions, in plain English.
   - "Steps" — numbered, imperative.
   - "Don't" — the failure modes you've seen.

## Output format

```markdown
## Existing skills (N)
- skill-name — what it does, when it fires.

## Suggested additions
1. **<name>** — <pitch> _(seen X times this session)_
2. ...

## Candidate skill files
<scaffolded SKILL.md(s) for the chosen ones>
```

## Don't

- Don't suggest a skill for something the agent already does well by default. Skills are for the cases where the *un-prompted* behavior is wrong.
- Don't propose 20 skills. The repo gets noisy and the agent's skill-selection routing degrades. 5–15 well-trusted skills > 50 mediocre ones.
- Don't write the SKILL.md without the user's go-ahead. Half the value of a skill is that the user trusts it; that requires their hand on the design.
