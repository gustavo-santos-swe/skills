# Extracting checkable rules from a pack SKILL.md

A pack skill mixes prose, headings, and bullets. Turn it into rows **before** touching code, so the check follows the skill, not what the agent happens to remember.

## Checklist-first

Before extracting anything from prose, check whether the skill already ships `references/checklist.md` (sibling to this file, inside the skill being checked, not inside `verify`). If it exists, **it is the rule list** - read it and skip everything below. It is pre-atomized, version-controlled, and does not depend on any agent's judgment call about what counts as a rule. Only fall back to prose extraction (the rest of this file) when `checklist.md` is missing, and say so explicitly in the subagent's output (a `Fallback: prose-extracted, no checklist.md` line) so the gap in that skill's coverage is visible and fixable, not silently absorbed.

## Where rules hide

- **Hard rules / numbered lists** - each numbered item is one rule.
- **"Don't" sections** - each bullet is a negative rule that forbids a pattern.
- **Tables** ("Layer owns", "Mode / Scope") - each row is often a rule about *where* something belongs, not only what it is.
- **Declarative sentences outside lists** - "Run validation first in the handler" is a rule even without a bullet marker.
- **Cross-references** ("aligns with `error-handling`") - don't duplicate the other skill's rule here. Note the link and check it once, under whichever skill owns it.

## What is not a rule

- Rationale / "why" prose with no imperative. Context, not a checkable line.
- "When to use" / "When not to". Routing, not a code-conformance rule.
- Examples in `references/`. They illustrate a rule already stated in the body; don't mint a second row for the example.

## Target repo wins

Every pack states defaults for **greenfield**. Before marking Drift, check the repo for a **documented** local convention (ADR, README, CONTRIBUTING, or a pattern applied everywhere, not just missed once). Documented override: Style at most, not Drift. Undocumented, one-off variance: still Drift, and a candidate for either a fix or a written ADR.

## Output shape

One row per rule, before checking code:

| Skill | Rule (one line, imperative) | Source |
|-------|-------------------------------|--------|
| `validation` | Run FluentValidation first in the handler; failure maps to 422 | Timing and placement |
| `validation` | Enforce uniqueness with a DB unique constraint, not only a handler check | Uniqueness and I/O |
| `validation` | Don't rely on FluentValidation alone for domain invariants | Don't |

Walk this table against the code (diff or full tree) next, and fill Status and Evidence per row using [`report-template.md`](report-template.md).

Prose-extracted rules have no `Enforcement` tag - that metadata only exists once a skill has a `checklist.md` (see below). Treat every prose-extracted row as `verify`; this is one more reason a missing `checklist.md` is a visible coverage gap, not a free pass.

## `checklist.md` format (for backfilling a skill)

Same two columns, committed once, read forever after, plus an optional third column:

| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Run FluentValidation first in the handler; failure maps to 422 | verify | Timing and placement |
| Enforce uniqueness with a DB unique constraint, not only a handler check | verify | Uniqueness and I/O |
| Don't rely on FluentValidation alone for domain invariants | verify | Don't |

Backfilling a pack's `checklist.md` files is a content task, owned by whoever maintains that pack - not something `verify` generates for itself at check time. A skill without one still gets checked (prose fallback), just without the determinism guarantee.

### `Enforcement` column (optional)

Marks whether a rule is already caught by a deterministic tool the target repo can run on every build/test, or genuinely needs an LLM's judgment every time. **Optional and backward-compatible**: any `checklist.md` written before this column existed has no `Enforcement` column at all, and every row in it is treated as `verify` - the absent-column default, not a special case to code around.

Controlled vocabulary, one value per row:

| Value | Meaning | Example |
|-------|---------|---------|
| `editorconfig` | A `.editorconfig` severity, `dotnet_naming_rule`, or project-level compiler switch (`Nullable`, `TreatWarningsAsErrors`, `EnforceCodeStyleInBuild`) fails the build when the rule is violated - not just an IDE suggestion. | "File-scoped namespaces for new files" → `csharp_style_namespace_declarations = file_scoped:warning` plus `EnforceCodeStyleInBuild=true`. "Nullable enabled; warnings fail CI" → `<Nullable>enable</Nullable>` + `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`. |
| `analyzer` | A specific Roslyn analyzer diagnostic ID - built into the SDK or shipped by a referenced NuGet analyzer package - catches the exact pattern, and its severity fails the build (not `none`/`suggestion`). | "No `async void`" → `VSTHRD100` (needs `Microsoft.VisualStudio.Threading.Analyzers` referenced). "Always flow `CancellationToken`" → `CA2016` (ships with the SDK, no extra package). |
| `architecture-test` | A structural/layering rule checked by a reflection-based test (NetArchTest.Rules or similar) that runs as part of the normal test suite. | "Domain must not depend on EF Core" → `Types.InAssembly(...).ShouldNot().HaveDependencyOnAny("Microsoft.EntityFrameworkCore")`. "Every Domain repository interface has exactly one implementation" → a reflection test asserting implementor count. |
| `regression-test` | A concrete unit/integration test asserts one specific behavioral outcome (input → expected result), not a static structural property. | "A tampered/forged JWT must be rejected" → a test that signs a token with the wrong key and asserts 401. "A missing FK target is rejected by the database" → a Testcontainers test inserting a dangling FK and asserting the DB throws. |
| `verify` (default) | No static tool covers this today - it needs an LLM (or human) reading the code and using judgment. This is also the value for any row in a checklist written before this column existed. | "Invariants are enforced in constructors/factories, not public setters" - requires judging whether a given setter is really unsafe to expose. |

A row's `Enforcement` value is a claim about the *mechanism that would prove it*, not a promise that the mechanism exists in every repo `verify` ever checks. A `dotnet` pack skill is shared across repos; one repo may have wired the analyzer/test and another may not have gotten there yet. That gap is exactly why `verify`'s dispatch never *skips* an `editorconfig`/`analyzer`/`architecture-test`/`regression-test` row outright - it does a cheap presence/health check first and only short-circuits to a lightweight `Enforced` status when the mechanism is confirmed present and green in *this* target repo. Mechanics: [`subagent-dispatch.md`](subagent-dispatch.md) and [`subagent-prompt.md`](subagent-prompt.md).
