# Conventional Commits (one-liner)

Formato obrigatório para commits neste fluxo:

```
<type>(<scope>): <descrição>
```

## Types

| Type | Quando usar |
|------|-------------|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `refactor` | Mudança de código sem alterar comportamento |
| `test` | Adicionar ou corrigir testes |
| `docs` | Só documentação |
| `chore` | Manutenção (deps, config, CI) |
| `style` | Formatação, sem mudança lógica |
| `perf` | Melhoria de performance |

## Scope

Opcional mas recomendado. Área do código: `auth`, `api`, `ui`, `skills`, etc.

Use o scope que um reviewer reconheceria no diff.

## Descrição

- Imperativo, presente: "add", "fix", "remove" — não "added", "fixes"
- Minúsculas (exceto nomes próprios)
- Sem ponto final
- Máximo ~72 caracteres
- Uma linha — sem corpo de commit, salvo se o usuário pedir

## Bons exemplos

```
feat(checkout): add pix payment option
fix(session): expire token on logout
refactor(users): extract validation to service
chore(deps): bump vitest to 3.2
docs(readme): add MCP setup instructions
```

## Maus exemplos

```
fix bug                    # sem type/scope, vago
feat: stuff                # descrição inútil
Fixed the login issue.     # passado, com ponto
WIP                        # não é conventional commit
feat(auth): add password reset flow and also update the readme and fix a typo in comments
                           # muito longo — dividir em commits ou enxugar
```

## Múltiplos commits

Preferir **um commit** por feature coesa. Se o diff mistura concerns não relacionados, separar:

```
feat(billing): add stripe webhook handler
test(billing): cover webhook signature validation
```

Não misturar `feat` + `fix` não relacionados no mesmo commit.
