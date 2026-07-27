# Deepening

How to deepen a cluster of shallow modules. Vocabulary: **module**, **interface**, **seam**, **adapter** (parent skill).

## Dependency categories

| Category | What | How to deepen / test |
|----------|------|----------------------|
| **In-process** | Pure compute, in-memory, no I/O | Merge; test through the new interface; no adapter |
| **Local-substitutable** | Has a local stand-in (e.g. PGLite, in-memory FS) | Deepen; tests use the stand-in; seam can stay internal |
| **Remote but owned** | Your services over the network | Port at the seam; prod adapter + in-memory adapter for tests |
| **True external** | Third party you don’t control (Stripe, …) | Injected port; tests use a mock adapter |

## Seam discipline

- One adapter → hypothetical; two → real. Don’t add a port for one adapter.
- Internal seams (private) vs external seam (the module’s interface) — don’t leak internals just for tests.

## Testing: replace, don’t layer

- Once tests exist at the deepened interface, delete old unit tests on the shallow pieces they replace.
- Assert observable outcomes through the interface, not internal state.
- Tests should survive internal refactors; if they break when guts change, they’re testing past the seam.
