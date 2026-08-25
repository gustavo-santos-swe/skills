# Local skills (product repo)

Use when disposition is **local**. Rules live in the **product** repository, not in the Goose skills repo.

## Default path (Claude-first teams)

```text
.claude/skills/
  <skill-name>/
    SKILL.md
    references/          # optional
```

Cursor also loads `.claude/skills/`, so one tree covers Claude Code and Cursor.

Do not use the name “goose” in paths or skill prose in a shared product repo.

## Shape

Same as any Agent Skill: folder + `SKILL.md` (+ optional `references/`). Keep the body thin: product delta, not a full stack handbook.

Typical brownfield pattern:

- **Legacy:** leave existing call sites alone
- **New work:** follow the stated rule (and point at an installed pack skill when the how-to already exists upstream)
- **Paths / names:** product-specific only

## Example (typed HTTP clients)

Product still has `IHttpClientFactory` sprinkled in old code. New outbound clients must be typed.

```text
.claude/skills/
  http-clients/
    SKILL.md
```

`SKILL.md` states the legacy vs new rule and where to register clients. It does not rename or fork the whole upstream HTTP handbook.

## Other roots

| Path | When |
|------|------|
| `.claude/skills/` | Default for Claude-heavy teams |
| `.agents/skills/` | Prefer when the team standardizes on the cross-client folder and Claude can load it (or you bridge it) |
| `.cursor/skills/` | Cursor-only teams; Claude will not see it |

If the product `AGENTS.md` or `CLAUDE.md` already names a skills root, follow that root.

## Pointers

Add a short line in product `CLAUDE.md` or `AGENTS.md` only when discovery is weak (for example: “Project skills live under `.claude/skills/`”). Do not dump the lesson into `AGENTS.md` when a skill folder is the better home.
