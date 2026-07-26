# wip

Scratch space for skills I'm authoring myself — drafts, experiments, and half-baked playbooks.

**Rules of the sandbox:**

- Rough edges are fine. Don't sync from upstream (`metadata.upstream.repo` stays empty / omit it).
- Use `metadata.area: wip` in every `SKILL.md`.
- Prefer `disable-model-invocation: true` on lifecycle skills — invoke via `/ask` (router) or by name.
- When a skill is ready, **graduate** it: move to the right stable area (`workflow`, `engineering`, …), update `metadata.area`, and list it in the root `README.md` inventory.
- PR-related skills use the **`pr-`** prefix for discoverability (`pr-raise`, `pr-review`, `pr-iterate`).

## Lifecycle map

Main flow — idea → ship:

```
research → brainstorm → [documentation:adr?] → planning → create-tickets → implement
  → [documentation:ship-docs?] → [security-check?] → git-practices
  → pr-raise → pr-review ⇄ pr-iterate
```

Self-check of the branch diff lives inside **implement** or **pr-raise** (not a separate skill).  
**documentation** — branch `adr` (pre-build) or `ship-docs` (post-build).  
**security-check** is an optional gate when the change hits a trust boundary.

On-ramps:

```
diagnose ──→ fix + lock ──→ git-practices → pr-raise
```

Router (always start here when unsure):

```
ask  →  picks the skill / flow above
     →  write-like-goose is always-on for durable prose (rule + AGENTS.md)
```

| # | Folder | Role |
|---|--------|------|
| — | [`ask`](./ask/) | Router — which skill/flow fits |
| 0 | [`research`](./research/) | Explore options, libraries, approaches (cited) |
| 1 | [`brainstorm`](./brainstorm/) | Sharpen the idea before a plan exists |
| — | [`documentation`](./documentation/) | ADR (pre-build) + ship-docs (post-build) — two branches |
| 2 | [`planning`](./planning/) | Frozen what → ordered how (tasks, files, risks) |
| 3 | [`create-tickets`](./create-tickets/) | Plan/spec → tracer-bullet issues (e.g. Linear) + blockers |
| — | [`diagnose`](./diagnose/) | Failure on-ramp — repro → root cause → fix → lock |
| 4 | [`implement`](./implement/) | Build the work; packs: [`database/`](./implement/database/), [`dotnet/`](./implement/dotnet/), [`react-native/`](./implement/react-native/), [`frontend/`](./implement/frontend/) |
| — | [`security-check`](./security-check/) | Optional gate — auth/secrets/boundaries before ship |
| 5 | [`git-practices`](./git-practices/) | Branch names + commit messages |
| 6 | [`pr-raise`](./pr-raise/) | PR title/body + open (never merge) |
| 7 | [`pr-review`](./pr-review/) | Review an existing PR |
| 8 | [`pr-iterate`](./pr-iterate/) | Author loop — handle feedback, push, re-request |
| — | [`write-like-goose`](./write-like-goose/) | **Always-on voice** — prose + code comments (see root `AGENTS.md` + `.cursor/rules/write-like-goose.mdc`) |

Later (not stubbed yet): verify/done.

