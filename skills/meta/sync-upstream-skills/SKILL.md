---
name: sync-upstream-skills
description: Check and sync imported skills with upstream repos via metadata.upstream. Use when the user says "sync skills", "update skills", "check upstream", "outdated skills", or after importing/adapting a skill from another repo.
metadata:
  area: meta
---

# Sync Upstream Skills

Keep imported skills aligned with their source repos, using `metadata.upstream` in each `SKILL.md`.

**Announce at start:** "Using the sync-upstream-skills skill."

## When to use

- Check whether imported skills are outdated
- Sync a **syncable** skill (no `note`) after confirming with the user
- Validate `metadata.upstream` after importing a new skill
- Before adapting an upstream skill — know what changed since the last sync

**When NOT to use:** custom skills (`ship-feature`) or templates without a `repo` — those are `custom`/`local`.

## Step 1: Check all skills

From the repo root `skills/`:

```bash
python skills/meta/sync-upstream-skills/scripts/check-upstream.py
```

Without authentication the GitHub API is limited to **60 req/h**. With many skills, export a token:

```bash
export GITHUB_TOKEN=ghp_...
python skills/meta/sync-upstream-skills/scripts/check-upstream.py
```

The script lists each skill with:

| Category | Meaning |
|----------|---------|
| `syncable` | Has `repo` + `path` + `commit`, no `note` — automatic sync allowed |
| `adapted` | Has `note` — local content differs from upstream; manual merge required |
| `custom` | `inspired_by` or no `repo` — do not sync |
| `local` | No upstream — native/template skill |

Exit code `1` = outdated skills found (useful in optional CI).

## Step 2: Present report

Summarize for the user:

1. How many are outdated
2. List per skill: local SHA → upstream SHA
3. Separate **syncable** vs **adapted** — adapted skills are never auto-synced without `--force`

For an outdated adapted skill, suggest:

```bash
# View diff upstream vs local (example: brainstorming)
curl -sL "https://api.github.com/repos/obra/superpowers/compare/LOCAL_SHA...UPSTREAM_SHA" | head
```

Or clone/sparse-checkout temporarily and `diff -r`.

## Step 3: Sync (one skill at a time)

**Rule:** one skill per run. Confirm with the user before writing files.

### Syncable skill (no `note`)

```bash
# Preview
python skills/meta/sync-upstream-skills/scripts/sync-skill.py NAME --dry-run

# Apply
python skills/meta/sync-upstream-skills/scripts/sync-skill.py NAME
```

The script:

1. Resolves the most recent commit that touched `metadata.upstream.path`
2. Downloads all files under that path
3. Writes them to `skills/NAME/`
4. Updates `commit` and `synced_at` in the frontmatter

### Adapted skill (with `note`)

1. Show what changed upstream since the local `commit`
2. Apply changes **manually** preserving adaptations (e.g.: removing subagents, worktrees)
3. Update `commit` and `synced_at` in the frontmatter
4. Only use `--force` if the user accepts overwriting and re-applying adaptations afterwards:

```bash
python skills/meta/sync-upstream-skills/scripts/sync-skill.py NAME --force
```

## Step 4: Validate after sync

```bash
python skills/meta/sync-upstream-skills/scripts/check-upstream.py
```

For skills with scripts (`mcp-builder`), confirm that `scripts/` and `reference/` were included.

If the user asks to ship: use `ship-feature` with a commit like:

```
chore(skills): sync NAME from upstream @ abc1234
```

## Importing a new skill (checklist)

1. Copy files from upstream to `skills/<area>/<name>/`
2. Fill in `metadata.upstream` — see [references/upstream-schema.md](references/upstream-schema.md)
3. If adapting content: add a `note` explaining what changed
4. Run `check-upstream.py` — should show "Up to date"
5. Update `README.md` in the correct area section

## Common errors

| Problem | Fix |
|---------|-----|
| Wrong `path` in frontmatter | Point to the actual folder in upstream, not the local name |
| Sync overwrote an adaptation | Restore from git; use manual merge or `--force` only with re-application |
| `stop-slop` with `path: .` | Correct — skill is at the root of the upstream repo |
| GitHub API rate limit | Wait or use `GITHUB_TOKEN` |
| Branch is not `main` | Script tries `main` then `master`; other branches = manual sync |

## References

- Full schema: [references/upstream-schema.md](references/upstream-schema.md)
- Skill authoring: `writing-skills`
- Ship after changes: `ship-feature`
