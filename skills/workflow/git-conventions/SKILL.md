---
name: git-conventions
description: >-
  Apply conventional branch names and commit messages on every git action. Use
  whenever creating a branch, writing a commit message, or naming a PR branch —
  even outside the full ship-feature flow. Covers feat/, fix/, chore/, docs/,
  refactor/, hotfix/ branch prefixes and the <type>(<scope>): <description>
  commit format.
metadata:
  area: workflow
---

# Git Conventions

Apply consistent branch names and commit messages on every git action. These
conventions are always active — not only during a full ship flow.

## Branch naming

```
<type>/<short-kebab-description>
```

| Prefix | When to use |
|--------|-------------|
| `feat/` | New feature or capability |
| `fix/` | Bug fix |
| `refactor/` | Code restructure without behavior change |
| `chore/` | Maintenance — deps, config, CI, scripts |
| `docs/` | Documentation only |
| `test/` | Adding or fixing tests |
| `hotfix/` | Urgent fix that must go straight to production |
| `perf/` | Performance improvement |

**Rules:**

- Lowercase, kebab-case: `feat/add-payment-flow` not `feat/AddPaymentFlow`
- Short and specific: 3–5 words that describe what the branch does
- No issue numbers unless the project convention requires them
- No `my-branch`, `wip`, `test123`, or other throwaway names

**Examples:**

```
feat/stripe-webhook-handler
fix/session-token-expiry
refactor/extract-auth-middleware
chore/bump-vitest-3
docs/mcp-setup-instructions
hotfix/null-user-crash
```

## Commit messages

One-liner in [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <imperative description>
```

| Type | When to use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code change without altering behavior |
| `test` | Add or fix tests |
| `docs` | Documentation only |
| `chore` | Maintenance (deps, config, CI) |
| `style` | Formatting, no logic change |
| `perf` | Performance improvement |

**Rules:**

- Scope is optional but recommended: area a reviewer recognizes in the diff
- Imperative, present tense: "add", "fix", "remove" — not "added", "fixes"
- Lowercase, no trailing period, max ~72 characters
- One line — no body unless the user explicitly asks for one
- Do not use `--no-verify` unless the user asks

**Examples:**

```
feat(checkout): add pix payment option
fix(session): expire token on logout
refactor(users): extract validation to service
chore(deps): bump vitest to 3.2
docs(readme): add MCP setup instructions
```

**Anti-patterns:**

```
fix bug                    # no type, vague
feat: stuff                # useless description
Fixed the login issue.     # past tense, trailing period
WIP                        # not a commit message
feat(auth): add reset flow and also update readme and fix typo
                           # too many concerns — split or trim
```

## When the branch is wrong

If asked to commit or push on `main`/`master` with uncommitted work, stop and
create a feature branch first:

```bash
git checkout -b feat/short-description
```

Never commit directly to the base branch unless the user explicitly asks.

## Alignment with ship-feature

This skill governs naming at every step. The `ship-feature` skill calls this
implicitly — every commit it writes must follow this format. When both apply,
this skill is the source of truth for the format; `ship-feature` is the source
of truth for the full push + PR flow.
