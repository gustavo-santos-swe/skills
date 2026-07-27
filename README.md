# skills

Central repository for my [Agent Skills](https://agentskills.io/) — playbooks that teach the agent how to execute specific tasks in my workflow.

Served via [Skills Over MCP](https://skillsovermcp.com/). Push to `main` and any connected MCP client picks up the change immediately.

## MCP URL

```
https://mcp.skillsovermcp.com/mcp/gustavo-santos-swe/skills
```

**Cursor:** Settings → MCP → Add server → paste the URL above (transport: `streamable-http`).

## Cursor plugin marketplace

This repo is a Cursor marketplace (single plugin). Manifest: [`.cursor-plugin/marketplace.json`](.cursor-plugin/marketplace.json).

**Team / Enterprise:** Dashboard → Plugins → Team Marketplaces → Add Marketplace → Import from Repo → `https://github.com/gustavo-santos-swe/skills`. Then install **gustavo-santos-skills** from Customize in any workspace.

**Local (no Team plan):** symlink or copy the repo to `~/.cursor/plugins/local/gustavo-santos-skills`, then Reload Window.

## Area structure

Skills organized under `skills/<area>/<name>/`. [Skills Over MCP](https://skillsovermcp.com/) supports nested folders.

```
skills/
├── meta/           # skill authoring / discovery helpers
├── workflow/       # remaining workflow helpers (doc co-authoring)
├── engineering/    # architecture, review, simplification helpers
├── product/        # domain, discovery, positioning
├── design/         # UI/UX
├── mobile/         # React Native / Expo — native feel, performance
├── communication/  # prose and copy
├── marketing/      # pricing, launch, acquisition (reserved)
├── operations/     # support, metrics, deploy ops
└── wip/            # Goose lifecycle + stack packs
                    # (implement/{database,dotnet,react-native,frontend}/)
```

Each `SKILL.md` includes `metadata.area` with the corresponding area.

## Inventory

### meta

| Skill | Purpose |
|-------|---------|
| [`writing-great-skills`](skills/meta/writing-great-skills/) | Vocabulary/principles for predictable skills |
| [`teach`](skills/meta/teach/) | Multi-session teaching workspace |
| [`suggesting-skills`](skills/meta/suggesting-skills/) | Suggest new skills |

### workflow

| Skill | Purpose |
|-------|---------|
| [`doc-coauthoring`](skills/workflow/doc-coauthoring/) | Co-author specs, RFCs, PRDs |

Lifecycle lives under [`wip/`](skills/wip/). Source: [anthropics/skills](https://github.com/anthropics/skills).

### engineering

| Skill | Purpose |
|-------|---------|
| [`codebase-design`](skills/engineering/codebase-design/) | Deep modules, seams, small interfaces |
| [`improve-codebase-architecture`](skills/engineering/improve-codebase-architecture/) | Find deepening opportunities, grill one |
| [`code-review`](skills/engineering/code-review/) | Standards + spec review (parallel sub-agents) |
| [`resolving-merge-conflicts`](skills/engineering/resolving-merge-conflicts/) | Resolve merge/rebase by intent |
| [`code-review-and-quality`](skills/engineering/code-review-and-quality/) | 5-axis review (correctness, architecture, security, perf) |
| [`code-simplification`](skills/engineering/code-simplification/) | Simplify code without changing behavior |
| [`finding-duplicate-functions`](skills/engineering/finding-duplicate-functions/) | Audit semantic duplication |

Goose lifecycle is under [`wip/`](skills/wip/). Source for remaining engineering skills: [mattpocock/skills](https://github.com/mattpocock/skills), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).

### product

_Reserved — no skills yet._

### design

| Skill | Purpose |
|-------|---------|
| [`frontend-design`](skills/design/frontend-design/) | Distinctive, production-grade UI, anti-"AI slop" |

Source: [anthropics/skills](https://github.com/anthropics/skills).

### mobile

| Skill | Purpose |
|-------|---------|
| [`react-native-design`](skills/mobile/react-native-design/) | Native look-and-feel for React Native/Expo — anti-"web port", grounded in the Monetis mobile stack |
| [`react-native-best-practices`](skills/mobile/react-native-best-practices/) | Animations (Reanimated 4/Skia/GPU), gestures, audio, on-device AI, JSI, multithreading |
| [`react-native-performance`](skills/mobile/react-native-performance/) | FPS, TTI, bundle size, memory leaks, re-renders |
| [`ui-ux-pro-max`](skills/mobile/ui-ux-pro-max/) | Searchable style/color/typography/UX-guideline database (incl. React Native stack) |
| [`react-native-styling-and-navigation`](skills/mobile/react-native-styling-and-navigation/) | Basic StyleSheet/Navigation/Reanimated quick reference |

Source: custom (`react-native-design`), [software-mansion-labs/skills](https://github.com/software-mansion-labs/skills), [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills), [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), [wshobson/agents](https://github.com/wshobson/agents).

### communication

| Skill | Purpose |
|-------|---------|
| [`writing-fragments`](skills/communication/writing-fragments/) | Explore - mine raw fragments for an article |
| [`writing-beats`](skills/communication/writing-beats/) | Exploit - assemble fragments into a beat journey |
| [`writing-shape`](skills/communication/writing-shape/) | Exploit - shape pile into article paragraph by paragraph |

House voice for Goose prose: [`wip/write-like-goose`](skills/wip/write-like-goose/). Source for writing-*: [mattpocock/skills](https://github.com/mattpocock/skills) `in-progress`.

### marketing

_Reserved for future imports (`pricing-strategy`, `launch-strategy`, etc.)._

### operations

_Reserved — no skills yet._

### wip

Goose lifecycle under [`skills/wip/`](skills/wip/). No upstream sync. Prefer these over deleted Matt/obra duplicates. See the [wip map](skills/wip/README.md).

| Skill | Role |
|-------|------|
| [`ask`](skills/wip/ask/) | Router |
| [`research`](skills/wip/research/) | Explore options (cited) |
| [`brainstorm`](skills/wip/brainstorm/) | Sharpen idea before plan |
| [`documentation`](skills/wip/documentation/) | ADR + ship-docs (two branches) |
| [`planning`](skills/wip/planning/) | Implementation plan |
| [`create-tickets`](skills/wip/create-tickets/) | Plan → issues + blockers |
| [`diagnose`](skills/wip/diagnose/) | Failure → root cause → fix → lock |
| [`implement`](skills/wip/implement/) | Build the work (+ [`database/`](skills/wip/implement/database/), [`dotnet/`](skills/wip/implement/dotnet/), [`react-native/`](skills/wip/implement/react-native/), [`frontend/`](skills/wip/implement/frontend/)) |
| [`security-check`](skills/wip/security-check/) | Optional security gate before ship |
| [`git-practices`](skills/wip/git-practices/) | Branch / commits |
| [`pr-raise`](skills/wip/pr-raise/) | Open PR (never merge) |
| [`pr-review`](skills/wip/pr-review/) | Review existing PR |
| [`pr-iterate`](skills/wip/pr-iterate/) | Handle PR feedback / re-request |
| [`write-like-goose`](skills/wip/write-like-goose/) | House voice (prose + comments) |

## Typical workflow

Goose lifecycle (`wip/`):

```
ask → research? → brainstorm → documentation:adr? → planning → create-tickets
  → implement (+ stack packs) → documentation:ship-docs? → security-check?
  → git-practices → pr-raise → pr-review ⇄ pr-iterate
```

Optional complements: `code-review-and-quality` / `codebase-design` / `frontend-design`.

Writing pipeline: `writing-fragments` → `writing-beats` or `writing-shape`.

Helpers: `finding-duplicate-functions`, `to-questionnaire`.

## Adding a new skill

1. Choose an area (`meta`, `workflow`, `engineering`, `wip`, …)
2. Create `skills/<area>/<name>/SKILL.md`
3. Minimum frontmatter:

```markdown
---
name: <name>
description: What it does and when to use it — keywords I typically say.
metadata:
  area: engineering
  upstream:
    repo: owner/repo
    path: skills/<name>
    url: https://github.com/owner/repo/tree/main/skills/<name>
    synced_at: "YYYY-MM-DD"
    commit: "<sha>"
---
```

For imported skills, keep `metadata.upstream` (repo, path, url, commit, synced_at). Goose `wip/` skills usually use `inspired_by` instead — no sync tooling in this repo anymore.

4. Keep the body concise (< 500 lines). Details go in `references/`.
5. Update the area `README.md` and this inventory.

## Notes

- Repo is **public** — anyone with the MCP URL can read the skills.
- Do not store secrets, credentials, or sensitive data.
- The `description` field in frontmatter is what the agent uses to decide *when* to activate the skill.

## Installing as a plugin

This repo works as an installable plugin in Claude Code and Cursor — no SKILL.md files are moved or duplicated. The manifest points to the [Skills Over MCP](https://skillsovermcp.com/) endpoint as the remote server.

### Claude Code

```bash
# Single session (does not persist):
claude --plugin-dir .

# Permanent installation (user-scoped):
claude plugins install --local "$(pwd)"
```

### Cursor (Windows / bash)

Cursor has no CLI installer for local plugins — it loads anything placed (or symlinked) under `~/.cursor/plugins/local/<name>`, matching the `name` in `plugin.json`.

```bash
mkdir -p ~/.cursor/plugins/local

# Option 1 — symlink (requires Developer Mode enabled on Windows, or run as Administrator):
cmd /c mklink /D "%USERPROFILE%\.cursor\plugins\local\gustavo-santos-skills" "%cd%"

# Option 2 — copy (no permission restrictions, but won't auto-update on pull):
cp -r . ~/.cursor/plugins/local/gustavo-santos-skills
```

Then run **Developer: Reload Window** from the Command Palette and confirm it loaded under **Customize** in the sidebar.

## Plugin stack

Full list of plugins installed alongside these skills — a reference for reproducing the environment on a new machine.

### cursor-public (Cursor Marketplace + Claude Code)

| Plugin | What it does |
|--------|--------------|
| [`compound-engineering`](https://github.com/EveryInc/compound-engineering-plugin) | AI-powered dev tools: code review, research, design, workflow automation |
| [`superpowers`](https://github.com/obra/superpowers) | Core skills library: TDD, debugging, collaboration patterns |
| [`cursor-team-kit`](https://github.com/cursor/plugins) | CI, code review, shipping, control-cli/ui, verify-this |
| [`continual-learning`](https://github.com/cursor/plugins) | Learns preferences and keeps `AGENTS.md` updated from transcripts |
| [`thermos`](https://github.com/cursor/plugins) | Thermo-nuclear code review and security audit |
| [`docs-canvas`](https://github.com/cursor/plugins) | Renders architecture docs as a navigable Cursor Canvas |
| [`pr-review-canvas`](https://github.com/cursor/plugins) | Renders PR diffs as a reviewer-organized Cursor Canvas |
| [`notion-workspace`](https://www.notion.so/) | Notion skills + MCP server |
| [`stripe`](https://github.com/stripe/ai) | Stripe best practices + MCP server |
| [`context7-plugin`](https://context7.com/) | Context7 MCP — version-specific docs from source repos |

### claude-plugins-official (Claude Code only)

| Plugin | What it does |
|--------|--------------|
| `compound-engineering` | Same plugin, registered in the Claude Code marketplace |
| `code-review` | Automated code review with specialized agents and confidence scoring |
| `code-simplifier` | Code simplification without changing behavior |
| `feature-dev` | Feature development workflow |
| `frontend-design` | Production-grade UI generation |
| `pr-review-toolkit` | PR review toolkit |
| `linear` | Linear issue tracking MCP |
| `github` | Official GitHub MCP server |
| `context7` | Context7 MCP (Claude Code variant) |

## References

- [Agent Skills spec](https://agentskills.io/specification)
- [Skills Over MCP](https://skillsovermcp.com/)
- [obra/superpowers](https://github.com/obra/superpowers)
- [mattpocock/skills](https://github.com/mattpocock/skills)
- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers-lab](https://github.com/obra/superpowers-lab)
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- [BuilderIO/skills](https://github.com/BuilderIO/skills)
- [software-mansion-labs/skills](https://github.com/software-mansion-labs/skills)
- [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills)
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [wshobson/agents](https://github.com/wshobson/agents)
