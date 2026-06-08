# PR Template

Usar este corpo ao criar PRs com `gh pr create --body`.

```markdown
## Summary
- <1–3 bullets: o que mudou e por quê>
- <foco no resultado para o usuário/reviewer, não na implementação>

## Test plan
- [ ] <passo concreto para verificar>
- [ ] <outro passo, se aplicável>
```

## Regras

- **Summary:** 1–3 bullets. Cada bullet = uma mudança ou motivo claro.
- **Test plan:** checklist com ações que o reviewer pode repetir.
- Se for mudança de UI, adicionar seção opcional:

```markdown
## Screenshots
<descrever o que mudou visualmente, ou colar imagem se o usuário forneceu>
```

## Exemplo

**Título:** `feat(auth): add password reset flow`

**Corpo:**

```markdown
## Summary
- Add forgot-password endpoint and email template
- Reset link expires after 1 hour

## Test plan
- [ ] Request reset for existing user — email arrives
- [ ] Click link within 1h — password updates
- [ ] Click expired link — shows error page
- [ ] `npm test` passes
```

## O que evitar

- Parágrafos longos no Summary
- "Test plan: tested locally" sem detalhes
- Copiar o diff inteiro na descrição
- Deixar Test plan vazio
