# Review axes (matters only)

Every `pr-review` run covers these axes. Skip empty axes in the report (omit the section); do not fill with “N/A” theater.

## Correctness

**Report:** wrong results, broken user-visible paths, swallowed errors, races that corrupt state, null/empty handling that fails in prod.

**Skip:** alternate implementations that are equivalent; taste refactors.

## Spec / source of truth drift

**Sources (in order):** engineer-provided link/paste → PR body references → ticket/plan/OpenAPI/ADR cited in commits → ask once if still unclear.

**Report:** missing/partial AC; behaviour not in spec; field/route/rule mismatch vs cited SoT.

**Skip:** inventing product requirements. If no spec: one line “No spec provided” and continue other axes.

## Security (in diff)

**Report:** high-confidence issues after tracing (authz gaps, secrets, injection, IDOR, SSRF from user input).

**Skip:** theoretical hardening; framework false positives. For a wider pass, suggest **security-check**.

## Integration coverage

**Report:** new/changed main success path or critical failure path with no integration (or agreed seam) test.

**Skip:** demanding unit tests on every private method; coverage % theater.

## Guidelines

**Sources:** repo `CONTRIBUTING` / coding standards, Goose pack skills relevant to the stack, ADRs in the touched area.

**Report:** violations that cause real pain (wrong layer, captive DI, API convention breaks, etc.).

**Skip:** anything CI/analyzers already enforce; pure naming bikesheds.

## Ship risk + CI

**Report:** failing checks; missing required checks when the PR claims ready; breaking API/schema without expand-contract or notes; dangerous migration order.

**Skip:** “add more labels”; process nits with no ship impact.

## Severity

| Level | Use when |
|-------|----------|
| **Block** | Must fix before merge |
| **Should-fix** | Real issue; engineer judges ship |
| **Nit** | Tiny; max **2** per review; omit if nothing useful |
