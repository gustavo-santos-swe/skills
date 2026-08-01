# Subagent dispatch (verify)

The orchestrating agent never grades a rule itself, and it never decides **which skills exist** by memory or inference either - both are single points of failure the same way. It resolves paths, dispatches subagents, collects tables, and applies the gate. Grading always happens in a subagent with no memory of writing the code under test - that isolation is the point, not a cost-saving trick. The agent that just decided its own implementation was fine is a biased judge of it; a subagent that starts fresh is not.

## Discovering skills: glob, not judgment

"Which skills exist in the dotnet pack" is not a question an LLM answers from memory or by skimming a README - it is a filesystem fact. Enumerate with a real glob/`find` before dispatching anything, every run, even if you dispatched five minutes ago:

```
find <pack-root>/dotnet -name SKILL.md
```

Whatever that command returns is the exhaustive, ordered dispatch list. No skill is skipped because it seemed less relevant to the diff, and none is added from a stale mental list of "the dotnet skills." If the diff's touched paths only plausibly implicate a subset (gate mode), the *filtering* can be a judgment call against the pack README's path map - but the *universe* of skills to filter from always comes from the glob, never from recall. Full audit mode skips the filtering step entirely: every skill the glob returns gets dispatched.

## Granularity

| Mode | Unit of dispatch | Default | When to change |
|------|--------------------|---------|------------------|
| **Gate** | One subagent per skill touched by the diff | Per-skill | Rarely - gate scope is already small (usually 2-6 skills) |
| **Full audit** | One subagent per skill | Per-skill, when the pack has up to ~12 skills | Pack bigger than that (dotnet has 26): ask - per-skill (max rigor, more calls) or per-cluster using the pack's own README groupings (cheaper, still isolated) |

Never let one subagent grade more than one skill's rules in a single pass unless clustering was a deliberate choice for cost. One skill per call is the default: it is the unit that keeps a subagent's job small enough to stay honest.

## Resolving paths before dispatch

The subagent starts with nothing from this conversation. Resolve every path to an **absolute path** before writing its prompt:

- The `SKILL.md` (or clustered set) it must check, as loaded in *this* session (plugin cache or synced skills dir), not the skills source repo, unless that is what is actually loaded here.
- `rule-extraction.md` from this same **`verify`** install.
- The target repo root, and any touched-path hints for gate mode.

Wrong paths produce a subagent that reads nothing and returns nothing useful - check the paths resolve before dispatching, not after.

## Dispatch

Use the Task tool, `subagent_type: generalPurpose`, one call per unit. Send every call for one `verify` run **in the same message** so they run concurrently. Copy [`subagent-prompt.md`](subagent-prompt.md) verbatim, filling only its placeholders.

## Collecting

1. Wait for every dispatched subagent.
2. Concatenate the returned tables into one, grouped by Status per [`report-template.md`](report-template.md): Drift / Gap / Style / Enforced get their own sections; Followed / N/A roll into a count only.
3. Sanity-check each subagent's `Counts:` line against its own row count (now `Enforced` + `Followed` + `Drift` + `Gap` + `Style` + `N/A`). Disagreement means a dropped or invented row - re-dispatch that one subagent rather than trust the mismatch.
4. Read every `Rules-from:` line. Skills marked `prose-fallback` were checked without a `checklist.md` - list them once in the report as a coverage note (not a Drift, not a blocker). This is the visible signal that backfilling that skill's `checklist.md` would make the next run more deterministic.
5. Spot-check the `Enforced` rows, don't just trust the count. Pick at least one `Enforced` row per subagent and confirm its Evidence cell actually names a real file/line or test - a subagent that marks a row `Enforced` without a concrete citation skipped the health check instead of running it. Treat that as a malformed response (see Failure handling) and re-dispatch, not a shortcut to accept.
6. Apply the gate: any Drift row blocks the `implement` review pause until the engineer decides. `Enforced` rows never block and never need an engineer decision - they are the cheap-verification path, not a skipped check, so nothing further to gate on that row.

## The `Enforced` lane is a cheap check, not a skip

A checklist row tagged `editorconfig`, `analyzer`, `architecture-test`, or `regression-test` still gets dispatched and still gets a row in the output table every single run - the tag changes *how cheaply* the subagent can clear it, not *whether* it gets checked. The subagent verifies the mechanism is present and green in the target repo, right now, before it can write `Enforced`; a stale or absent mechanism falls back to the full Followed/Drift/Gap/Style/N/A judgment, same as an untagged rule. See [`subagent-prompt.md`](subagent-prompt.md) step 3a for the exact per-`Enforcement`-value check, and [`rule-extraction.md`](rule-extraction.md) for what each value means.

## Failure handling

- Subagent returns prose instead of the table, or skips the `Counts:` line: re-dispatch once with the same prompt.
- Two failures on the same unit: do that skill's check inline instead, and say so in the report as a known-degraded row group, not a silent gap.
- Subagent times out or errors: re-dispatch once; second failure lists that skill under "Out of scope / not covered" rather than guessing its rows.
