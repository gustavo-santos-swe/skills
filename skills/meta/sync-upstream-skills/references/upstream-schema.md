# `metadata.upstream` schema

Every skill imported from another repo must have this block in the `SKILL.md` frontmatter:

```yaml
metadata:
  area: engineering          # optional — meta, workflow, engineering, product, design, mobile, communication, marketing, operations, wip
  upstream:
    repo: owner/repo         # required for automatic sync
    path: skills/name        # path in the upstream repo (`.` if the skill is the repo root)
    url: https://github.com/owner/repo/tree/main/skills/name
    commit: "<full SHA of the synced commit>"
    synced_at: "YYYY-MM-DD"
    note: "..."              # optional — marks adapted skill; sync requires manual merge
```

## Sync categories

| Situation | `repo` | `note` | Behavior |
|-----------|--------|--------|----------|
| **Syncable** | present | absent | `sync-skill.py` can overwrite files |
| **Adapted** | present | present | Check reports outdated; sync only with `--force` + diff review |
| **Custom** | absent | `inspired_by` or `note` | Not syncable — e.g. Goose `wip/` skills |
| **Local** | absent | absent | Template or native skill — e.g.: `suggesting-skills` |

## Fields

| Field | Required | Description |
|-------|----------|-------------|
| `repo` | for sync | `owner/repo` on GitHub |
| `path` | for sync | Skill folder in upstream (not the local name if renamed) |
| `url` | recommended | Human-readable link to the path in upstream |
| `commit` | for sync | SHA of the commit from which the files were copied |
| `synced_at` | recommended | Date of last sync (ISO) |
| `note` | optional | Explains local adaptations; blocks automatic sync |

## Local renaming

If the local folder differs from upstream (e.g.: `brainstorm-with-docs` ← `grill-with-docs`), `path` points to the **upstream** name, not the local one.

## Skills with subfolders

Skills like `mcp-builder` include `scripts/`, `reference/`, etc. The sync downloads **the entire tree** at `path` — not just `SKILL.md`.

## Repo layout

```
skills/
├── meta/<skill>/
├── workflow/<skill>/
├── engineering/<skill>/
├── product/<skill>/
├── design/<skill>/
├── mobile/<skill>/
├── communication/<skill>/
├── marketing/<skill>/
├── operations/<skill>/
└── wip/<skill>/            # personal drafts — no upstream sync
    # e.g. implement/dotnet/<skill>/ for stack packs under a parent skill
```

`metadata.area` must match the skill's parent folder.

## After importing or adapting

1. Fill in `metadata.upstream` with the exact commit (`git rev-parse` in the upstream clone or SHA from the raw URL).
2. Set `metadata.area` to the chosen area.
3. Run `python skills/meta/sync-upstream-skills/scripts/check-upstream.py` to validate.
