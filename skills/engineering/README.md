# engineering

Qualidade de código: TDD, debug, review, verificação, exploração, simplificação, MCP, tech debt.

| Skill | Uso |
|-------|-----|
| `test-driven-development` | Red-green-refactor |
| `systematic-debugging` | Root cause antes de fix |
| `verification-before-completion` | Evidência antes de "pronto" |
| `requesting-code-review` | Self-review rápido pré-PR |
| `code-review-and-quality` | Review 5 eixos (diff grande, security, APIs) |
| `receiving-code-review` | Processar feedback |
| `code-simplification` | Reduzir complexidade sem mudar behavior |
| `zoom-out` | Mapa de módulos |
| `finding-duplicate-functions` | Duplicação semântica |
| `mcp-builder` | MCP servers |

**Review:** `requesting-code-review` para todo ship; `code-review-and-quality` quando o diff toca auth, APIs, performance ou passa de ~100 linhas.

**Simplificação:** `code-simplification` após feature funcionar; `finding-duplicate-functions` para audit de codebase.
