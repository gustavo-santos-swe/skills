# Conventional Commits (one-liner)

Required format for commits in this flow:

```
<type>(<scope>): <description>
```

## Types

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

## Scope

Optional but recommended. Area of the code: `auth`, `api`, `ui`, `skills`, etc.

Use the scope a reviewer would recognize in the diff.

## Description

- Imperative, present tense: "add", "fix", "remove" — not "added", "fixes"
- Lowercase (except proper nouns)
- No trailing period
- Max ~72 characters
- One line — no commit body unless the user asks

## Good examples

```
feat(checkout): add pix payment option
fix(session): expire token on logout
refactor(users): extract validation to service
chore(deps): bump vitest to 3.2
docs(readme): add MCP setup instructions
```

## Bad examples

```
fix bug                    # no type/scope, vague
feat: stuff                # useless description
Fixed the login issue.     # past tense, with period
WIP                        # not a conventional commit
feat(auth): add password reset flow and also update the readme and fix a typo in comments
                           # too long — split into commits or trim
```

## Multiple commits

Prefer **one commit** per cohesive feature. If the diff mixes unrelated concerns, split:

```
feat(billing): add stripe webhook handler
test(billing): cover webhook signature validation
```

Do not mix unrelated `feat` + `fix` in the same commit.
