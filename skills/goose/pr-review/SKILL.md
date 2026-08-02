---
name: pr-review
description: Review an open PR (correctness, SoT drift, security-in-diff, main-path tests, CI). Draft first; optional GitHub post. Not for local self-check or addressing comments (pr-iterate).
metadata:
  area: goose
---

# PR Review

Goose handbook for **reviewing an open pull request**. Part of `pr-*`: **pr-raise** → **pr-review** → **pr-iterate**.

Voice: **`write-like-goose`**.

Local pre-PR self-check stays in **implement** / **pr-raise**. Guidelines axis runs **verify** rather than eyeballing pack conformance. Deep AppSec → offer **security-check**. Author loop on feedback → **pr-iterate**.

## When to use

- User pastes a PR URL or says “review this PR”
- Current branch already has an open PR and they want a review
- Re-review after **pr-iterate**

## When not to

- No PR yet → **implement** self-check or **pr-raise**
- Author applying comments → **pr-iterate**
- Full-repo security audit → **security-check** (full audit mode)

## What we check (matters only)

Use [`references/review-axes.md`](references/review-axes.md). Short list:

| Axis | Signal |
|------|--------|
| **Correctness** | Logic bugs, bad error paths, data loss / wrong results |
| **Spec / SoT drift** | Missing/partial AC; behaviour not asked; mismatch vs cited ticket/plan/OpenAPI/brief |
| **Security (in diff)** | High-confidence trust-boundary issues after a quick trace |
| **Integration coverage** | Main success + critical failure paths tested at an agreed seam |
| **Guidelines** | Repo + Goose pack rules that prevent real pain (not linter theater) |
| **Ship risk + CI** | Migrations/breaking API/rollout; failing or missing checks |

**Approval bar:** approve when the change clearly improves overall code health and matches the repo — not when it’s “how I would have written it.” Perfect code doesn’t exist; don’t block on taste.

**Nitpick bar:** prefer fewer stronger findings. Severity: **Block** / **Should-fix** / **Nit** (≤2 Nits). Skip style tooling already enforces. Don’t invent requirements when no spec was provided - say “no spec provided” and still run the other axes.

**Fat PRs:** you may split mental work into **Spec** vs **Standards/Guidelines** passes (same axes, separate notes) so one doesn’t mask the other — still one draft report.

## Hard rules

1. **Draft first.** Nothing posted to GitHub until the engineer approves posting.
2. **Ask surface** (chat / markdown doc / canvas) unless the default applies (below).
3. **Always** include a **human review guide** with a **dynamic file walk order** inferred from *this* repo’s layout and the diff - not a canned Clean Architecture speech. Template: [`references/human-walk-guide.md`](references/human-walk-guide.md).
4. **Same shapes every time** - report, walk guide, and canvas sections follow the templates under `references/`. Do not invent new section names.
5. Never merge the PR from this skill.

## Deliverable surfaces

Ask: **chat**, **markdown doc**, or **canvas**?

**Defaults if they shrug:**

| Situation | Surface |
|-----------|---------|
| Multi-axis findings and/or non-trivial walk order | **Canvas** (Cursor canvas beside chat) |
| Tiny PR, few findings, “LGTM + one note” | **Chat** |
| They asked for a file / durable note | **Markdown** `docs/reviews/YYYY-MM-DD-pr-<n>.md` (or repo convention) |

**Canvas:** copy [`references/pr-review-canvas.template.tsx`](references/pr-review-canvas.template.tsx) → workspace `canvases/pr-<n>-review.canvas.tsx`, replace the `review` object. Layout rules: [`references/canvas-layout.md`](references/canvas-layout.md) + Cursor **canvas** skill. Link the file in chat when created.

**Markdown / chat:** same section order as [`references/report-template.md`](references/report-template.md).

## Steps

1. **Identify PR** - URL, number, or `gh pr view` / GitHub MCP for the current branch.
2. **Fetch** - title, body, base/head, commits, diff, checks/CI, existing review threads. Tooling: same discovery as **pr-raise** (MCP then `gh`).
3. **Spec / SoT** - from PR body, linked tickets, paths the engineer gives, or plan/OpenAPI cited in the change. If none: note it; don’t invent AC.
4. **Understand layout** - from the diff + repo tree, infer modules/layers for the walk guide (see human-walk template).
5. **Review** against the axes (incl. smell baseline under Guidelines). Trace before security flags. Check main-path integration coverage.
6. **Draft** using the report template + human walk guide (required sections).
7. **Render** on the chosen/default surface (templates must match).
8. **Ask** - post to GitHub? If yes: **request changes** if any Block; else **comment**; **approve** only if they explicitly ask.
9. **Next** - blockers/should-fixes → author runs **pr-iterate**. Clean approve path → human merges (not this skill). Offer **security-check** if trust boundary needs a deeper pass.

## Posting (optional)

Only after explicit go-ahead. One review submission with summary + inline comments where useful. Don’t duplicate existing threads - reply in-thread. Don’t approve with open Blocks.

## Guardrails

1. **Draft first** - post to GitHub only after the engineer approves.
2. Always include the **human review guide** using the fixed templates (same section titles every time).
3. Human merges; deep AppSec → offer **security-check**. Stay matters-only (skip linter theater).

**Done when:** review rendered on the chosen surface; posting asked (or skipped); next step clear.

## References

- [`references/review-axes.md`](references/review-axes.md) - what matters / what to skip
- [`references/smell-baseline.md`](references/smell-baseline.md) - Fowler smells for Guidelines
- [`references/report-template.md`](references/report-template.md) - fixed report shape
- [`references/human-walk-guide.md`](references/human-walk-guide.md) - dynamic layer/file order
- [`references/canvas-layout.md`](references/canvas-layout.md) - canvas section + aesthetic
- [`references/pr-review-canvas.template.tsx`](references/pr-review-canvas.template.tsx) - copy-paste canvas (consistent UI)

## Related

- Open PR → **pr-raise**
- Address feedback → **pr-iterate**
- Guidelines axis, rule by rule → **verify**
- Trust-boundary deep pass → **security-check**
- Module shape / seams → **codebase-design**
