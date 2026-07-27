# GitHub tooling — pick what's available

Owned by **`pr-raise`**. Do **not** assume `gh` CLI. Discover, then act.

## Discovery order

1. **GitHub MCP** — if a server exposes PR tools (e.g. `create_pull_request`, `update_pull_request`, `list_pull_requests`), prefer it when already authenticated / listed in the session.
2. **`gh` CLI** — if `gh` exists and `gh auth status` succeeds, use it.
3. **Neither** — draft title + body for the user (or open the compare URL) and stop; don't pretend the PR was created.

Inspect schemas before calling MCP (`GetMcpTools` / equivalent). Don't invent flags.

## Rough equivalents

| Intent | MCP (typical) | `gh` CLI |
|--------|----------------|----------|
| Create PR | `create_pull_request` | `gh pr create` |
| Update PR | `update_pull_request` | `gh pr edit` |
| View / list | `pull_request_read` / `list_pull_requests` | `gh pr view` / `gh pr list` |
| Push branch | still `git push` (local) | `git push -u` |

Push is always git. Only the **GitHub API surface** switches MCP ↔ CLI.
