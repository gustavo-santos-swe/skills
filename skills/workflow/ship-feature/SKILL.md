---
name: ship-feature
description: Commitar com conventional commits (one-liner), fazer push e abrir PR — nunca mergear na main. Use quando o usuário diz "ship", "abre o PR", "commita e abre PR", "finaliza a feature", "manda pro GitHub", ou quando a implementação está pronta e falta integrar via PR.
metadata:
  area: workflow
  upstream:
    inspired_by: obra/superpowers
    path: skills/finishing-a-development-branch
    url: https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch
    note: Versão customizada — sem merge local, sem worktrees, foco em commit + PR.
---

# Ship Feature

Finalizar uma feature: verificar, commitar, push, abrir PR. **Nunca mergear na main.**

**Anunciar no início:** "Estou usando a skill ship-feature para finalizar o trabalho."

## Regras absolutas

**Nunca fazer** (a menos que o usuário peça explicitamente):

- `git merge` na `main` ou `master`
- `git push origin main` (ou qualquer push direto na branch base)
- `gh pr merge`
- `git checkout main && git merge <feature-branch>`

**Fluxo único:** verificar → commitar → push → abrir PR → reportar URL.

Não apresentar menu de opções. Não oferecer merge local.

## Passo 1: Verificar estado

```bash
git status
git branch --show-current
```

- Se estiver em `main` ou `master` com mudanças não commitadas, **pare** e avise: trabalho deve estar em uma branch de feature.
- Se a branch atual for `main`/`master` sem mudanças pendentes, **pare** — não há o que shippar.

Identificar a branch base (geralmente `main`):

```bash
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

## Passo 2: Verificar qualidade

Rodar o que o projeto usa (adaptar ao stack):

```bash
# exemplos — usar o que existir no repo
npm test
# npm run lint
# npm run typecheck
```

Se falhar: reportar erros e **parar**. Não commitar nem abrir PR com testes quebrados.

## Passo 3: Commitar

Se houver mudanças não commitadas:

1. Revisar o diff: `git diff` e `git diff --staged`
2. Agrupar em commit(s) lógico(s) — preferir **um commit** se a feature for coesa
3. Mensagem **one-liner** no formato [Conventional Commits](references/conventional-commits.md):

```
<type>(<scope>): <descrição imperativa em minúsculas>
```

Exemplos:

```
feat(auth): add password reset flow
fix(api): handle null user on session lookup
refactor(skills): extract upstream metadata helper
```

4. Commitar:

```bash
git add <arquivos relevantes>
git commit -m "$(cat <<'EOF'
feat(scope): descrição curta e clara

EOF
)"
```

**Não** usar `--no-verify` a menos que o usuário peça.

Se o usuário já commitou tudo, pular para o passo 4.

## Passo 4: Push

```bash
git push -u origin HEAD
```

Se o push falhar (branch remota divergiu), reportar e pedir orientação — não force push.

## Passo 5: Abrir PR

Verificar se já existe PR para a branch:

```bash
gh pr view --json url,state 2>/dev/null
```

- Se **já existe**: reportar a URL e atualizar descrição se o usuário pediu.
- Se **não existe**: criar com `gh pr create`.

**Título do PR:** mesma linha do commit principal, ou resumo ligeiramente mais legível.

**Corpo:** seguir `references/pr-template.md`.

```bash
gh pr create --title "feat(scope): descrição" --body "$(cat <<'EOF'
## Summary
- <bullet 1: o que mudou>
- <bullet 2: por quê>

## Test plan
- [ ] <como verificar>

EOF
)"
```

## Passo 6: Reportar

Entregar ao usuário:

1. Branch name
2. Commit SHA (`git rev-parse HEAD`)
3. URL do PR
4. O que foi verificado (testes rodados)

Exemplo:

```
Shipped on branch feat/auth-reset (abc1234).
PR: https://github.com/org/repo/pull/42
Tests: npm test — passed.
```

## Erros comuns

| Problema | Correção |
|----------|----------|
| Commitar na main | Criar branch de feature primeiro |
| Merge local "mais rápido" | Proibido — sempre PR |
| PR sem test plan | Preencher checklist no template |
| Mensagem vaga (`fix stuff`) | Usar type + scope + descrição específica |
| Múltiplos commits WIP | Squash ou reorganizar antes do PR, se o usuário preferir um commit limpo |

## Referências

- Formato de commit: `references/conventional-commits.md`
- Template de PR: `references/pr-template.md`
