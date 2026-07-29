---
name: pr-raise
description: Open or update a PR (title, body, push) - never merge. Use when shipping a branch to review.
metadata:
  area: goose
---

# PR Raise

Part of the `pr-*` family: **pr-raise** → **pr-review** → **pr-iterate**.

Owns **PR title, body, template merge, push, and create/update**.  
Branch names + commit messages → **`git-practices`**. Voice → **`write-like-goose`**.

| Concern | Skill |
|---------|--------|
| Branch / commits | **`git-practices`** |
| PR title / body / open | **this skill** |
| Voice | **`write-like-goose`** |

## Title

Same shape as a [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) subject - primary outcome of the branch:

```
feat(checkout): add pix payment option
fix(web): correct session cookie path
```

Not a laundry list. Align with the branch type when practical (`feat/…` → `feat(…):`).

## Body

Keep short - **code speaks; prose orients**. Details: [`references/pr-body.md`](references/pr-body.md).

### Goose sections (default)

| Section | Job |
|---------|-----|
| **Briefing** | 1-3 sentences: what + why. Descriptive STE shape, ≤25 words/sentence ([`ste100.md`](../write-like-goose/references/ste100.md)) |
| **References** | Ticket / issue / ADR links |
| **Changes** | Short human bullets; screenshots for UI if needed |
| **Notes** | Env, flags, migrations, rollout - omit if empty |

Optional **Test plan** only when the repo or change needs it - no theater checklists.

### Repo PR template

Before drafting:

1. Look in the **target repo**:
   - `.github/pull_request_template.md` / `.github/PULL_REQUEST_TEMPLATE.md`
   - `.github/PULL_REQUEST_TEMPLATE/*`
   - `docs/pull_request_template.md`
2. **Found** → keep that skeleton; map Goose intent into its headings ([`references/pr-body.md`](references/pr-body.md)). Keep required checkboxes; add `## Notes` at the end if ops details don't fit.
3. **Missing** → Goose default sections above.

Substance (conventional title, short Changes, real Notes) follows Goose. Shape follows the repo template when present.

## Steps

### 1. Preflight

1. Self-review the branch diff if that wasn't done at the end of **implement**.
2. Load **`git-practices`** - branch + commits must comply (ask before rewriting published history).
3. Discover PR template (above); draft **title** + **body**.
4. Voice pass: **`write-like-goose`**.

### 2. Push

```bash
git push -u origin HEAD
```

If the remote diverged, stop and ask - don't force-push unless the user asks.

### 3. Discover GitHub tooling

Do **not** hardcode `gh`. First that works ([`references/tooling.md`](references/tooling.md)):

1. **GitHub MCP** (e.g. `create_pull_request`, `update_pull_request`, list/read) → prefer; read schema before calling.
2. Else **`gh`** installed and authenticated → CLI.
3. Else draft title/body for the human and stop.

Check for an **existing PR** on this head branch before creating a duplicate.

### 4. Create or update

- **Create:** never merge. Draft if the user wants WIP.
- **Exists:** report URL; update title/body only if asked or clearly stale.

#### Example - MCP (shape only; use real schema)

```text
create_pull_request
  owner, repo, head, base
  title: "feat(checkout): add pix payment option"
  body: "<template-merged or Goose default markdown>"
```

#### Example - `gh` CLI

```bash
gh pr create --title "feat(checkout): add pix payment option" --body "$(cat <<'EOF'
## Briefing

<what and why>

## References

- <ticket>

## Changes

- <bullet>

## Notes

- <ops notes, or omit section>
EOF
)"
```

If the repo template uses different headings, `body` follows **that** shape with Goose content mapped in.

### 5. Report

Branch, PR URL, MCP vs `gh`, leftover ops notes for the human.

## Guardrails

1. Discover GitHub tooling (MCP then `gh`) before acting; draft for the human if neither works.
2. Prefer the repo PR template when present; short Changes (no full diff paste).
3. **Never merge** to `main`/`master`. One PR per head branch (update if it already exists).

## Next

Reviewer → **pr-review**. Author after comments → **pr-iterate**.
