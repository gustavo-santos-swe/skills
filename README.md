# skills

Central repository for my [Agent Skills](https://agentskills.io/) — playbooks that teach the agent how to execute specific tasks in my workflow.

Served via [Skills Over MCP](https://skillsovermcp.com/). Push to `main` and any connected MCP client picks up the change immediately.

## MCP URL

```
https://mcp.skillsovermcp.com/mcp/gustavo-santos-swe/skills
```

**Cursor:** Settings → MCP → Add server → paste the URL above (transport: `streamable-http`).

## Area structure

Skills organized under `skills/<area>/<name>/`. [Skills Over MCP](https://skillsovermcp.com/) supports nested folders.

```
skills/
├── meta/           # discover, maintain, and sync skills
├── workflow/       # spec → plan → execution → PR
├── engineering/    # code, tests, review, MCP, tech debt
├── product/        # domain, discovery, positioning
├── design/         # UI/UX
├── mobile/         # React Native / Expo — native feel, performance
├── communication/  # prose and copy
├── marketing/      # pricing, launch, acquisition (reserved)
└── operations/     # support, metrics, deploy ops
```

Each `SKILL.md` includes `metadata.area` with the corresponding area.

## Inventory

### meta

| Skill | Purpose |
|-------|---------|
| [`using-superpowers`](skills/meta/using-superpowers/) | Check available skills before acting |
| [`writing-skills`](skills/meta/writing-skills/) | Create and maintain skills |
| [`writing-great-skills`](skills/meta/writing-great-skills/) | Vocabulary/principles for predictable skills |
| [`handoff`](skills/meta/handoff/) | Compact session for the next agent |
| [`teach`](skills/meta/teach/) | Multi-session teaching workspace |
| [`sync-upstream-skills`](skills/meta/sync-upstream-skills/) | Check and sync skills with upstream repos |
| [`suggesting-skills`](skills/meta/suggesting-skills/) | Suggest new skills |

### workflow

| Skill | Purpose |
|-------|---------|
| [`brainstorming`](skills/workflow/brainstorming/) | Design and spec before implementing |
| [`grilling`](skills/workflow/grilling/) | Relentless interview until the decision tree is resolved |
| [`grill-me`](skills/workflow/grill-me/) | User-invoked grilling entrypoint |
| [`batch-grill-me`](skills/workflow/batch-grill-me/) | Grilling in rounds (whole frontier at once) |
| [`writing-plans`](skills/workflow/writing-plans/) | Detailed implementation plan |
| [`executing-plans`](skills/workflow/executing-plans/) | Execute plan task by task |
| [`doc-coauthoring`](skills/workflow/doc-coauthoring/) | Co-author specs, RFCs, PRDs |
| [`ship-feature`](skills/workflow/ship-feature/) | Commit, push, and open PR — never merge to main |
| [`git-conventions`](skills/workflow/git-conventions/) | Branch naming (feat/, fix/, chore/…) and conventional commit messages on every git action |
| [`quick-recap`](skills/workflow/quick-recap/) | Red/yellow/green status block convention at the end of every response |

Source: [obra/superpowers](https://github.com/obra/superpowers), [mattpocock/skills](https://github.com/mattpocock/skills), [anthropics/skills](https://github.com/anthropics/skills), [BuilderIO/skills](https://github.com/BuilderIO/skills) — custom `ship-feature`. `batch-grill-me` from upstream `in-progress`.

### engineering

| Skill | Purpose |
|-------|---------|
| [`ask-matt`](skills/engineering/ask-matt/) | Router — which Matt skill/flow fits |
| [`grill-with-docs`](skills/engineering/grill-with-docs/) | Grilling + domain model (`CONTEXT.md`, ADRs) |
| [`domain-modeling`](skills/engineering/domain-modeling/) | Sharpen domain language and ADRs |
| [`codebase-design`](skills/engineering/codebase-design/) | Deep modules, seams, small interfaces |
| [`improve-codebase-architecture`](skills/engineering/improve-codebase-architecture/) | Find deepening opportunities, grill one |
| [`prototype`](skills/engineering/prototype/) | Throwaway prototype to answer a design question |
| [`to-spec`](skills/engineering/to-spec/) | Conversation → spec on the issue tracker |
| [`to-tickets`](skills/engineering/to-tickets/) | Plan/spec → tracer-bullet tickets with blockers |
| [`implement`](skills/engineering/implement/) | Build from spec/tickets with TDD + review |
| [`wayfinder`](skills/engineering/wayfinder/) | Multi-session map of decision tickets |
| [`triage`](skills/engineering/triage/) | Issue triage state machine |
| [`tdd`](skills/engineering/tdd/) | Red-green-refactor vertical slices |
| [`diagnosing-bugs`](skills/engineering/diagnosing-bugs/) | Reproduce → minimise → instrument → fix |
| [`code-review`](skills/engineering/code-review/) | Standards + spec review (parallel sub-agents) |
| [`research`](skills/engineering/research/) | Cited research from primary sources |
| [`resolving-merge-conflicts`](skills/engineering/resolving-merge-conflicts/) | Resolve merge/rebase by intent |
| [`setup-matt-pocock-skills`](skills/engineering/setup-matt-pocock-skills/) | One-time repo setup for the Matt flow |
| [`test-driven-development`](skills/engineering/test-driven-development/) | TDD — tests first (obra) |
| [`systematic-debugging`](skills/engineering/systematic-debugging/) | Systematic debugging before fixing (obra) |
| [`verification-before-completion`](skills/engineering/verification-before-completion/) | Evidence before claiming "done" |
| [`requesting-code-review`](skills/engineering/requesting-code-review/) | Quick self-review of the diff before a PR |
| [`code-review-and-quality`](skills/engineering/code-review-and-quality/) | 5-axis review (correctness, architecture, security, perf) |
| [`receiving-code-review`](skills/engineering/receiving-code-review/) | Process review feedback |
| [`code-simplification`](skills/engineering/code-simplification/) | Simplify code without changing behavior |
| [`finding-duplicate-functions`](skills/engineering/finding-duplicate-functions/) | Audit semantic duplication |
| [`mcp-builder`](skills/engineering/mcp-builder/) | Create MCP servers (Python/TypeScript) |

Source: [mattpocock/skills](https://github.com/mattpocock/skills), [obra/superpowers](https://github.com/obra/superpowers), [anthropics/skills](https://github.com/anthropics/skills), [obra/superpowers-lab](https://github.com/obra/superpowers-lab), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).

### product

| Skill | Purpose |
|-------|---------|
| [`to-questionnaire`](skills/product/to-questionnaire/) | Turn a knowledge gap into an async questionnaire |

Source: [mattpocock/skills](https://github.com/mattpocock/skills) `in-progress`.

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
| [`stop-slop`](skills/communication/stop-slop/) | Remove AI writing patterns |
| [`write-like-a-human`](skills/communication/write-like-a-human/) | Humanize text (template) |
| [`writing-fragments`](skills/communication/writing-fragments/) | Explore — mine raw fragments for an article |
| [`writing-beats`](skills/communication/writing-beats/) | Exploit — assemble fragments into a beat journey |
| [`writing-shape`](skills/communication/writing-shape/) | Exploit — shape pile into article paragraph by paragraph |

Source: [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop), [mattpocock/skills](https://github.com/mattpocock/skills) `in-progress` (writing-*).

### marketing

_Reserved for future imports (`pricing-strategy`, `launch-strategy`, etc.)._

### operations

| Skill | Purpose |
|-------|---------|
| [`triage-bug`](skills/operations/triage-bug/) | Bug report → structured ticket |

## Typical workflow

```
ask-matt / grilling / grill-with-docs  (or brainstorming / doc-coauthoring)
  → to-spec / to-tickets / writing-plans
  → implement / executing-plans
  → tdd or test-driven-development / frontend-design / diagnosing-bugs
  → verification-before-completion
  → code-review or code-review-and-quality
  → ship-feature
```

Writing pipeline: `writing-fragments` → `writing-beats` or `writing-shape`.

Helpers: `finding-duplicate-functions`, `mcp-builder`, `handoff`, `stop-slop`, `sync-upstream-skills`, `to-questionnaire`, `batch-grill-me`.

## Adding a new skill

1. Choose an area (`meta`, `workflow`, `engineering`, …)
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

Schema: [`skills/meta/sync-upstream-skills/references/upstream-schema.md`](skills/meta/sync-upstream-skills/references/upstream-schema.md).

Check upstream:

```bash
python skills/meta/sync-upstream-skills/scripts/check-upstream.py
```

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
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- [BuilderIO/skills](https://github.com/BuilderIO/skills)
- [software-mansion-labs/skills](https://github.com/software-mansion-labs/skills)
- [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills)
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [wshobson/agents](https://github.com/wshobson/agents)
