---
name: sync-upstream-skills
description: Verifica e sincroniza skills importadas com os repos upstream via metadata.upstream. Use quando o usuário pede "sync skills", "atualizar skills", "checar upstream", "skills desatualizadas", ou após importar/adaptar uma skill de outro repo.
metadata:
  area: meta
---

# Sync Upstream Skills

Manter skills importadas alinhadas com os repos fonte, usando `metadata.upstream` em cada `SKILL.md`.

**Anunciar no início:** "Estou usando a skill sync-upstream-skills."

## Quando usar

- Checar se skills importadas estão desatualizadas
- Sincronizar uma skill **syncable** (sem `note`) após confirmar com o usuário
- Validar `metadata.upstream` após importar skill nova
- Antes de adaptar skill upstream — saber o que mudou desde o último sync

**Quando NÃO usar:** skills custom (`ship-feature`) ou template sem `repo` — são `custom`/`local`.

## Passo 1: Verificar todas as skills

Na raiz do repo `skills/`:

```bash
python skills/meta/sync-upstream-skills/scripts/check-upstream.py
```

Sem autenticação a API do GitHub limita a **60 req/h**. Com muitas skills, exporte um token:

```bash
export GITHUB_TOKEN=ghp_...
python skills/meta/sync-upstream-skills/scripts/check-upstream.py
```

O script lista cada skill com:

| Categoria | Significado |
|-----------|-------------|
| `syncable` | Tem `repo` + `path` + `commit`, sem `note` — sync automático permitido |
| `adapted` | Tem `note` — conteúdo local difere do upstream; merge manual |
| `custom` | `inspired_by` ou sem `repo` — não sincronizar |
| `local` | Sem upstream — skill nativa/template |

Exit code `1` = há skills desatualizadas (útil em CI opcional).

## Passo 2: Apresentar relatório

Resumir para o usuário:

1. Quantas desatualizadas
2. Lista por skill: local SHA → upstream SHA
3. Separar **syncable** vs **adapted** — adapted nunca sync automático sem `--force`

Para skill adaptada desatualizada, sugerir:

```bash
# Ver diff upstream vs local (exemplo brainstorming)
curl -sL "https://api.github.com/repos/obra/superpowers/compare/LOCAL_SHA...UPSTREAM_SHA" | head
```

Ou clonar/sparse-checkout temporário e `diff -r`.

## Passo 3: Sincronizar (uma skill por vez)

**Regra:** uma skill por execução. Confirmar com o usuário antes de escrever arquivos.

### Skill syncable (sem `note`)

```bash
# Preview
python skills/meta/sync-upstream-skills/scripts/sync-skill.py NOME --dry-run

# Aplicar
python skills/meta/sync-upstream-skills/scripts/sync-skill.py NOME
```

O script:

1. Resolve o commit mais recente que tocou `metadata.upstream.path`
2. Baixa todos os arquivos sob esse path
3. Escreve em `skills/NOME/`
4. Atualiza `commit` e `synced_at` no frontmatter

### Skill adaptada (com `note`)

1. Mostrar o que mudou no upstream desde `commit` local
2. Aplicar mudanças **manualmente** preservando adaptações (ex.: remover subagents, worktrees)
3. Atualizar `commit` e `synced_at` no frontmatter
4. Só usar `--force` se o usuário aceitar sobrescrever e re-aplicar adaptações depois:

```bash
python skills/meta/sync-upstream-skills/scripts/sync-skill.py NOME --force
```

## Passo 4: Validar após sync

```bash
python skills/meta/sync-upstream-skills/scripts/check-upstream.py
```

Para skills com scripts (`mcp-builder`), confirmar que `scripts/` e `reference/` vieram junto.

Se o usuário pedir ship: usar `ship-feature` com commit tipo:

```
chore(skills): sync NOME from upstream @ abc1234
```

## Importar skill nova (checklist)

1. Copiar arquivos do upstream para `skills/<area>/<nome>/`
2. Preencher `metadata.upstream` — ver [references/upstream-schema.md](references/upstream-schema.md)
3. Se adaptar conteúdo: adicionar `note` explicando o que mudou
4. Rodar `check-upstream.py` — deve mostrar "Atualizado"
5. Atualizar `README.md` na seção/área correta

## Erros comuns

| Problema | Correção |
|----------|----------|
| `path` errado no frontmatter | Apontar para pasta real no upstream, não nome local |
| Sync sobrescreveu adaptação | Restaurar do git; usar merge manual ou `--force` só com re-aplicação |
| `stop-slop` com `path: .` | Correto — skill na raiz do repo upstream |
| Rate limit GitHub API | Esperar ou usar `GITHUB_TOKEN` (futuro) |
| Branch não é `main` | Script tenta `main` depois `master`; outros branches = sync manual |

## Referências

- Schema completo: [references/upstream-schema.md](references/upstream-schema.md)
- Authoring de skills: `writing-skills`
- Ship após mudanças: `ship-feature`
