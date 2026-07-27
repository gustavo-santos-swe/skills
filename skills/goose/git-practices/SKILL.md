---
name: git-practices
description: Conventional branch names and commit messages. Use when branching or committing; PR open stays in pr-raise.
metadata:
  area: goose
---

# Git Practices

Source of truth for **branch names** and **commit messages** only.  
PR title, body, templates, push/open → **`pr-raise`**.  
Voice for commit subjects/bodies → **`write-like-goose`** (always; not optional).


Specs:

- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [Conventional Branch 1.1.0](https://conventionalbranch.org/)

## When to use

- Naming a branch or writing/amending a commit (including before **`pr-raise`**).

## Branches - Conventional Branch

```
<type>/<description>
```

### Goose defaults (purpose prefixes)

| Prefix | Use |
|--------|-----|
| `feat/` | New capability (`feature/` ok - prefer `feat/`) |
| `fix/` | Bug fix (`bugfix/` ok - prefer `fix/`) |
| `hotfix/` | Urgent production fix |
| `release/` | Release prep (`release/v1.2.0`) |
| `chore/` | Deps, CI, config, non-product chores |

Team extensions (document in target repo if CI enforces): `docs/`, `refactor/`, `test/`, `perf/`.

### Rules ([spec](https://conventionalbranch.org/))

- Lowercase, digits, hyphens; dots only in release versions
- No underscores, spaces, consecutive/leading/trailing hyphens
- Short kebab description; ticket when we have one: `feat/abc-123-short-name`
- Never commit on trunk (`main` / `master` / `develop`) unless the user explicitly asks - create a prefixed branch first

### AI agent prefixes (v1.1.0)

Spec allows `cursor/`, `claude/`, `codex/`, `copilot/`, `ai/`. **Goose intentional work uses purpose prefixes** so intent is obvious. Don't rename a good `feat/…` to `cursor/…` for ceremony.

### Examples

```
feat/pix-checkout
fix/session-token-expiry
feat/abc-42-webhook-retries
hotfix/null-user-crash
chore/bump-vitest
release/v1.4.0
```

## Commits - Conventional Commits

```
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | Meaning |
|------|---------|
| `feat` | New feature (SemVer MINOR) |
| `fix` | Bug fix (SemVer PATCH) |
| `docs` | Docs only |
| `style` | Formatting; no logic |
| `refactor` | Restructure; no behavior change |
| `perf` | Performance |
| `test` | Tests only |
| `build` | Build system / deps bundling |
| `ci` | CI config |
| `chore` | Other maintenance |
| `revert` | Revert; footer `Refs: <sha>` |

Breaking: `!` after type/scope and/or footer `BREAKING CHANGE: …`.

### Rules

- Imperative present tense: `add`, `fix`, `remove` - not “added” / “fixes”
- Description: lowercase start preferred, no trailing period, ~72 chars
- **Default: one-liner.** Body only when why isn't obvious from the diff
- Scope = recognizable area (`auth`, `checkout`, `web`, …)
- One concern per commit when practical
- Footers: `Closes #123`, `Refs: #123`, `BREAKING CHANGE: …` as needed
- Never skip hooks unless the user asks; no secrets in commits

### Examples

```
feat(checkout): add pix payment option
fix(session): expire token on logout
feat(api)!: drop legacy v1 list endpoint

BREAKING CHANGE: clients must use /v2/items
```

### Anti-patterns

```
fix bug
WIP
Fixed the login issue.
feat(auth): add reset, update readme, fix typo   # split
```

### Hygiene patterns

| Pattern | Practice |
|---------|----------|
| Atomic commits | One logical change when it helps review/revert |
| Why over what | Body carries *why* when needed; diff shows *what* |
| Align with branch | `feat/…` branch → mostly `feat:` commits |

## Guardrails

1. This skill owns **branch names + commit messages** only - PR open → **pr-raise**.
2. Stick to the Conventional Branch / Commits tables (document any extra types in the target repo first).
3. Prefer purpose prefixes (`feat/…`, `fix/…`) over vendor ceremony prefixes.

## Next

Commit on a good branch → **`pr-raise`** (title, body, open PR).
