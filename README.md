# skills

Central repository for [Agent Skills](https://agentskills.io/) — playbooks that teach the agent how to run specific tasks.

Install via the Claude Code or Cursor plugin marketplaces below, or clone the repo and point your agent at `skills/`.

## Claude Code plugin marketplace

Manifest: [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json).

```bash
claude plugin marketplace add gustavo-santos-swe/skills
claude plugin install gustavo-santos-skills@gustavo-santos-skills
```

Or in-session: `/plugin marketplace add gustavo-santos-swe/skills`, then `/plugin install gustavo-santos-skills@gustavo-santos-skills`.

## Cursor plugin marketplace

Manifest: [`.cursor-plugin/marketplace.json`](.cursor-plugin/marketplace.json).

**Team / Enterprise:** Dashboard → Plugins → Team Marketplaces → Add Marketplace → Import from Repo → `https://github.com/gustavo-santos-swe/skills`. Then install **gustavo-santos-skills**.

**Local (no Team plan):** symlink/copy to `~/.cursor/plugins/local/gustavo-santos-skills`, then Reload Window.

---

## How to use Goose skills

Lifecycle skills live under [`skills/goose/`](skills/goose/). They are **model-invoked**: the agent fires them autonomously when a description matches, and skills can reach each other — so **`ask`** can route straight into the skill it picks. You can still invoke any of them by name, or start with **`ask`** when unsure.

Full map + when-table: [`skills/goose/README.md`](skills/goose/README.md).

### Start here

| You… | Run |
|------|-----|
| Don’t know which skill | **ask** |
| Have a fuzzy idea | **brainstorm** (research first if you need facts) |
| Have an agreed design | **planning** → **create-tickets** → **implement** |
| Have a clear small change / ticket | **implement** |
| Finished a build, check it against the packs | **verify** |
| Something is broken | **diagnose** |
| Ready to open a PR | **git-practices** → **pr-raise** |
| Reviewing a PR | **pr-review** |
| Addressing review comments | **pr-iterate** |

### Main flow (idea → ship)

```
ask
  → research? → brainstorm → [documentation:adr?] → planning → create-tickets
  → implement (+ stack packs) → verify (gate) → [documentation:ship-docs?] → [security-check?]
  → git-practices → pr-raise → pr-review (verify + other axes) ⇄ pr-iterate
```

- **Always-on voice:** **write-like-goose** (**ASD-STE100** + anti-AI) for tickets, plans, commits, PRs, review comments, code comments, and skill bodies (see [`AGENTS.md`](AGENTS.md)).
- **Stack packs** (under `implement/`): load the whole pack for the stack you are touching: `database`, `dotnet`, `react-native` (stubs), `frontend` (partial: structure + styling filled).
- **Never merge to main** from the agent; humans merge.

### Anytime (beside the flow)

| Skill | When |
|-------|------|
| **write-like-goose** | Any durable prose / comments |
| **codebase-design** | Shaping module seams, depth, adapters |
| **documentation** | ADR before build, or ship-docs after |
| **security-check** | Diff hits auth, secrets, tenancy, uploads, public APIs |

---

## Area structure

```
skills/
├── goose/          # House lifecycle (idea → ship) + implement stack packs
├── meta/           # Skill authoring helpers
├── workflow/       # Doc co-authoring (Anthropic)
├── engineering/    # Optional architecture / conflict / duplicate helpers
├── design/         # UI craft
├── mobile/         # RN/Expo deep technique (complements goose RN pack)
├── communication/  # Long-form article writing pipeline
├── product/        # Reserved
├── marketing/      # Reserved
└── operations/     # Reserved
```

Each `SKILL.md` has `metadata.area` matching its folder.

---

## Inventory

### goose (primary)

| Skill | When |
|-------|------|
| [`ask`](skills/goose/ask/) | Unsure which skill/flow |
| [`research`](skills/goose/research/) | Cited options before locking design |
| [`brainstorm`](skills/goose/brainstorm/) | Freeze the *what* |
| [`documentation`](skills/goose/documentation/) | ADR or ship-docs |
| [`planning`](skills/goose/planning/) | Implementation plan |
| [`create-tickets`](skills/goose/create-tickets/) | Tracer-bullet issues + blockers |
| [`diagnose`](skills/goose/diagnose/) | Failure → root cause → fix → lock |
| [`implement`](skills/goose/implement/) | Build (+ [`database`](skills/goose/implement/database/), [`dotnet`](skills/goose/implement/dotnet/), [`react-native`](skills/goose/implement/react-native/), [`frontend`](skills/goose/implement/frontend/)) |
| [`verify`](skills/goose/verify/) | Gate or full audit: code vs active pack skills, rule by rule |
| [`security-check`](skills/goose/security-check/) | Optional trust-boundary gate |
| [`git-practices`](skills/goose/git-practices/) | Branch names + commits |
| [`pr-raise`](skills/goose/pr-raise/) | Open PR (never merge) |
| [`pr-review`](skills/goose/pr-review/) | Review open PR |
| [`pr-iterate`](skills/goose/pr-iterate/) | Author feedback loop |
| [`write-like-goose`](skills/goose/write-like-goose/) | House voice (ASD-STE100) |
| [`codebase-design`](skills/goose/codebase-design/) | Deep-module vocabulary |

### meta

| Skill | Purpose |
|-------|---------|
| [`evolve-goose-skills`](skills/meta/evolve-goose-skills/) | Evolve this repo - iterate (inspire → grill → distill) or garden |
| [`skill-retro`](skills/meta/skill-retro/) | Session lessons → Goose absorb, product local skill, or evolve |
| [`writing-great-skills`](skills/meta/writing-great-skills/) | Vocabulary for predictable skills |
| [`teach`](skills/meta/teach/) | Multi-session teaching workspace |
| [`suggesting-skills`](skills/meta/suggesting-skills/) | Suggest new skills from repeated prompts |

### workflow

| Skill | Purpose |
|-------|---------|
| [`doc-coauthoring`](skills/workflow/doc-coauthoring/) | Co-author specs, RFCs, PRDs |

### engineering

| Skill | Purpose |
|-------|---------|
| [`improve-codebase-architecture`](skills/engineering/improve-codebase-architecture/) | Survey deepening opportunities (uses `goose/codebase-design`) |
| [`resolving-merge-conflicts`](skills/engineering/resolving-merge-conflicts/) | Resolve merge/rebase by intent |
| [`finding-duplicate-functions`](skills/engineering/finding-duplicate-functions/) | Audit semantic duplication |

### design

| Skill | Purpose |
|-------|---------|
| [`frontend-design`](skills/design/frontend-design/) | Distinctive UI, anti-“AI slop” (vendored) |

Upstream favorites (Taste, Impeccable, Emil, anti-ui-slop): install only — see [Favorite frontend / design skills](#favorite-frontend--design-skills-install-upstream--do-not-vendor).

### mobile

| Skill | Purpose |
|-------|---------|
| [`react-native-design`](skills/mobile/react-native-design/) | Native look-and-feel (Monetis-grounded) |
| [`react-native-best-practices`](skills/mobile/react-native-best-practices/) | Animations, gestures, audio, JSI, … |
| [`react-native-performance`](skills/mobile/react-native-performance/) | FPS, TTI, leaks, re-renders |
| [`ui-ux-pro-max`](skills/mobile/ui-ux-pro-max/) | Style/UX guideline database |
| [`react-native-styling-and-navigation`](skills/mobile/react-native-styling-and-navigation/) | StyleSheet / Navigation quick ref |

### communication

| Skill | Purpose |
|-------|---------|
| [`writing-fragments`](skills/communication/writing-fragments/) | Explore — mine article fragments |
| [`writing-beats`](skills/communication/writing-beats/) | Exploit — beat journey |
| [`writing-shape`](skills/communication/writing-shape/) | Exploit — shape into article |

### product / marketing / operations

_Reserved._

---

## Adding a new skill

1. Choose an area (`goose`, `meta`, `engineering`, …)
2. Create `skills/<area>/<name>/SKILL.md`
3. Frontmatter minimum:

```markdown
---
name: <name>
description: What it does and when to use it.
disable-model-invocation: true
metadata:
  area: goose
  inspired_by:
    - owner/repo - upstream name
---
```

Imported third-party skills may use `metadata.upstream` instead of `inspired_by`.

4. Keep the body concise; details in `references/`.
5. Update the area README and this inventory.

## Notes

- Repo is **public** — anyone can read the skills.
- Do not store secrets or credentials.
- Frontmatter `description` is what model-invoked skills use for auto-routing. Every skill here is model-invoked, so keep descriptions rich in trigger phrasing — they are the whole routing surface, and they sit in the context window every turn.

## Installing as a plugin

### Claude Code

From GitHub:

```bash
claude plugin marketplace add gustavo-santos-swe/skills
claude plugin install gustavo-santos-skills@gustavo-santos-skills
```

From a local clone (point at the absolute path — a bare `.` is rejected):

```bash
claude plugin marketplace add "$(pwd)"
claude plugin install gustavo-santos-skills@gustavo-santos-skills
```

Verify with `claude plugin list` (expect `✔ enabled`) and `claude plugin details gustavo-santos-skills` for the skill inventory and token cost.

### Cursor (Windows / bash)

```bash
mkdir -p ~/.cursor/plugins/local
cmd /c mklink /D "%USERPROFILE%\.cursor\plugins\local\gustavo-santos-skills" "%cd%"
```

## Installed plugins (outside this repo)

Handy plugins used alongside these skills (not vendored here):

| Plugin | What it does |
|--------|--------------|
| [`cursor-team-kit`](https://github.com/cursor/plugins) | CI, code review, shipping helpers |
| [`continual-learning`](https://github.com/cursor/plugins) | Learns preferences into `AGENTS.md` |
| [`thermos`](https://github.com/cursor/plugins) | Thermo-nuclear review / security |
| [`docs-canvas`](https://github.com/cursor/plugins) | Architecture docs as Canvas |
| [`pr-review-canvas`](https://github.com/cursor/plugins) | PR diffs as Canvas |
| [`notion-workspace`](https://www.notion.so/) | Notion skills + MCP |
| [`stripe`](https://github.com/stripe/ai) | Stripe practices + MCP |
| [`context7-plugin`](https://context7.com/) | Version-specific library docs |

### claude-plugins-official (Claude Code)

| Plugin | What it does |
|--------|--------------|
| `compound-engineering` | Compound Engineering workflows |
| `code-review` | Automated review agents |
| `code-simplifier` | Clarity polish without behavior change |
| `feature-dev` | Feature development workflow |
| `frontend-design` | UI generation |
| `pr-review-toolkit` | PR review toolkit |
| `linear` | Linear MCP |
| `github` | GitHub MCP |
| `context7` | Context7 MCP |

---

## Favorite frontend / design skills (install upstream — do not vendor)

Keep anti-slop / taste skills **outside** this repo. Install them with [`npx skills`](https://skills.sh/) so they update from source. This README is the source of truth for the favorites list.

**Already vendored here** (sync via `metadata.upstream`, not re-install):

| Skill | In this repo | Upstream |
|-------|--------------|----------|
| `frontend-design` | [`skills/design/frontend-design/`](skills/design/frontend-design/) | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| `ui-ux-pro-max` | [`skills/mobile/ui-ux-pro-max/`](skills/mobile/ui-ux-pro-max/) | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |

**Install globally (recommended)** — Cursor + shared `~/.agents/skills/`:

```bash
# Taste — landing pages / marketing anti-slop
npx skills add leonxlnx/taste-skill --skill design-taste-frontend -g -y -a cursor

# Impeccable — brand vs product UI, polish/audit/critique (+ DESIGN.md)
npx skills add pbakaus/impeccable --skill impeccable -g -y -a cursor

# Emil Kowalski — motion + design-eng craft (all skills in the pack)
npx skills add emilkowalski/skills -g -y -a cursor --all

# UIZZE anti-ui-slop — product-specific finish gate (domain-backed skill)
npx skills add https://uizze.com --skill anti-ui-slop -g -y -a cursor
```

**One-liner bootstrap** (same set):

```bash
npx skills add leonxlnx/taste-skill --skill design-taste-frontend -g -y -a cursor \
  && npx skills add pbakaus/impeccable --skill impeccable -g -y -a cursor \
  && npx skills add emilkowalski/skills -g -y -a cursor --all \
  && npx skills add https://uizze.com --skill anti-ui-slop -g -y -a cursor
```

**Update later:**

```bash
npx skills update -g -y
```

**Project-scoped alternative** (lockfile in the app repo): drop `-g`, then commit `.skills.json` / `skills-lock.json` if you want teammates on the same pins. Restore with `npx skills experimental_install`.

| Skill | Role | Link |
|-------|------|------|
| `design-taste-frontend` | LP / marketing taste, brief → direction | [tasteskill.dev](https://www.tasteskill.dev/) · [skills.sh](https://skills.sh/leonxlnx/taste-skill/design-taste-frontend) |
| `impeccable` | Brand vs product modes, polish/audit | [impeccable.style](https://impeccable.style) · [skills.sh](https://skills.sh/pbakaus/impeccable/impeccable) |
| `emil-design-eng` (+ motion pack) | Micro-interactions, animation craft | [emilkowalski/skills](https://github.com/emilkowalski/skills) |
| `anti-ui-slop` | Catalogue-backed finish gate | [uizze.com](https://uizze.com) · [skills.sh](https://skills.sh/uizze.com/anti-ui-slop) |

Optional Taste variants (same repo): `high-end-visual-design`, `redesign-existing-projects`, `minimalist-ui`, `industrial-brutalist-ui`, `image-to-code`, `imagegen-frontend-web`.

**DESIGN.md catalog** (not a skill install — pick / author design systems): [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md).

Suggested stack: Taste (LP) or Impeccable init (SaaS) → ship UI → Emil for motion → anti-ui-slop before call done. Vendored `frontend-design` / `ui-ux-pro-max` stay available via this plugin.

## References

- [Agent Skills spec](https://agentskills.io/specification)
- [skills.sh](https://skills.sh/)
- [Agent Plugins](https://agent-plugins.org/)
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
- [obra/superpowers](https://github.com/obra/superpowers)
- [mattpocock/skills](https://github.com/mattpocock/skills)
- [anthropics/skills](https://github.com/anthropics/skills)
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- [BuilderIO/skills](https://github.com/BuilderIO/skills)
- [software-mansion-labs/skills](https://github.com/software-mansion-labs/skills)
- [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills)
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- [emilkowalski/skills](https://github.com/emilkowalski/skills)
- [uizze/uizze](https://github.com/uizze/uizze)
- [wshobson/agents](https://github.com/wshobson/agents)
