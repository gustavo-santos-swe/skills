---
name: ship-feature
description: Commit with conventional commits (one-liner), push, and open a PR — never merge to main. Use when the user says "ship", "open the PR", "commit and open PR", "finish the feature", "push to GitHub", or when the implementation is ready and needs to be integrated via PR.
metadata:
  area: workflow
  upstream:
    inspired_by: obra/superpowers
    path: skills/finishing-a-development-branch
    url: https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch
    note: Custom version — no local merge, no worktrees, focused on commit + PR.
---

# Ship Feature

Finish a feature: verify, commit, push, open PR. **Never merge to main.**

**Announce at start:** "Using the ship-feature skill to finish the work."

## Absolute rules

**Never do** (unless the user explicitly asks):

- `git merge` into `main` or `master`
- `git push origin main` (or any direct push to the base branch)
- `gh pr merge`
- `git checkout main && git merge <feature-branch>`

**Single flow:** verify → commit → push → open PR → report URL.

Do not present option menus. Do not offer local merge.

## Step 1: Check state

```bash
git status
git branch --show-current
```

- If on `main` or `master` with uncommitted changes, **stop** and warn: work should be on a feature branch.
- If the current branch is `main`/`master` with no pending changes, **stop** — nothing to ship.

Identify the base branch (usually `main`):

```bash
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

## Step 2: Check quality

Run whatever the project uses (adapt to the stack):

```bash
# examples — use whatever exists in the repo
npm test
# npm run lint
# npm run typecheck
```

If it fails: report errors and **stop**. Do not commit or open a PR with broken tests.

## Step 3: Commit

If there are uncommitted changes:

1. Review the diff: `git diff` and `git diff --staged`
2. Group into logical commit(s) — prefer **one commit** if the feature is cohesive
3. **One-liner** message in [Conventional Commits](references/conventional-commits.md) format:

```
<type>(<scope>): <imperative description in lowercase>
```

Examples:

```
feat(auth): add password reset flow
fix(api): handle null user on session lookup
refactor(skills): extract upstream metadata helper
```

4. Commit:

```bash
git add <relevant files>
git commit -m "$(cat <<'EOF'
feat(scope): short and clear description

EOF
)"
```

**Do not** use `--no-verify` unless the user asks.

If the user has already committed everything, skip to step 4.

## Step 4: Push

```bash
git push -u origin HEAD
```

If push fails (remote branch diverged), report and ask for guidance — do not force push.

## Step 5: Open PR

Check whether a PR already exists for the branch:

```bash
gh pr view --json url,state 2>/dev/null
```

- If it **already exists**: report the URL and update the description if the user asked.
- If it **does not exist**: create with `gh pr create`.

**PR title:** same line as the main commit, or a slightly more readable summary.

**Body:** follow `references/pr-template.md`.

```bash
gh pr create --title "feat(scope): description" --body "$(cat <<'EOF'
## Summary
- <bullet 1: what changed>
- <bullet 2: why>

## Test plan
- [ ] <how to verify>

EOF
)"
```

## Step 6: Report

Deliver to the user:

1. Branch name
2. Commit SHA (`git rev-parse HEAD`)
3. PR URL
4. What was verified (tests run)

Example:

```
Shipped on branch feat/auth-reset (abc1234).
PR: https://github.com/org/repo/pull/42
Tests: npm test — passed.
```

## Common errors

| Problem | Fix |
|---------|-----|
| Committing to main | Create a feature branch first |
| Local merge "faster" | Forbidden — always use a PR |
| PR without test plan | Fill in the checklist in the template |
| Vague message (`fix stuff`) | Use type + scope + specific description |
| Multiple WIP commits | Squash or reorganize before the PR, if the user prefers a clean commit |

## References

- Commit format: `references/conventional-commits.md`
- PR template: `references/pr-template.md`
