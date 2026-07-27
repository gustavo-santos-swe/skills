# Optional polish (simplify)

Clarity pass on **this batch’s** code after green. Goal: a new teammate understands it faster — not fewer lines.

## When

- Feature works and tests for the batch pass, but the change feels heavier than it should
- Nested logic, muddy names, or duplication landed while shipping under pressure

## When not

- Already clear — don’t polish for sport
- You don’t understand why something exists yet (Chesterton’s fence)
- Perf-critical path and “simpler” would be slower
- About to rewrite the module anyway

## Rules

1. **Preserve behaviour.** Same inputs/outputs, errors, side effects, ordering. Existing tests stay green without rewriting them for the polish itself.
2. **Match the repo.** Neighbour style wins over external taste (imports, naming, error patterns).
3. **Clarity over cleverness.** Prefer explicit over dense when dense costs a mental pause.
4. **Don’t overshoot.** Don’t inline a named helper that carried meaning; don’t merge unrelated logic; don’t strip seams that exist for testability (**codebase-design**).
5. **Scope = this batch.** No drive-by refactors outside the dirty-tree change unless the engineer widens scope.

## Tiny loop

Understand why it looks that way → make one clarity change → re-run the batch’s verifies → next spot. Stop when further edits are taste, not comprehension.
