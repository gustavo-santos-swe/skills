# Schema `metadata.upstream`

Todo skill importado de outro repo deve ter este bloco no frontmatter de `SKILL.md`:

```yaml
metadata:
  area: engineering          # opcional — meta, workflow, engineering, product, design, communication, marketing, operations
  upstream:
    repo: owner/repo         # obrigatório para sync automático
    path: skills/nome        # caminho no repo upstream (`.` se a skill é a raiz do repo)
    url: https://github.com/owner/repo/tree/main/skills/nome
    commit: "<sha completo do commit sincronizado>"
    synced_at: "YYYY-MM-DD"
    note: "..."              # opcional — marca skill adaptada; sync exige merge manual
```

## Categorias de sync

| Situação | `repo` | `note` | Comportamento |
|----------|--------|--------|---------------|
| **Syncable** | presente | ausente | `sync-skill.py` pode sobrescrever arquivos |
| **Adapted** | presente | presente | Check reporta desatualização; sync só com `--force` + revisão de diff |
| **Custom** | ausente | `inspired_by` ou `note` | Não sincronizável — ex.: `ship-feature` |
| **Local** | ausente | ausente | Template ou skill nativa — ex.: `suggesting-skills` |

## Campos

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `repo` | para sync | `owner/repo` no GitHub |
| `path` | para sync | Pasta da skill no upstream (não o nome local se renomeada) |
| `url` | recomendado | Link humano para o path no upstream |
| `commit` | para sync | SHA do commit de onde os arquivos foram copiados |
| `synced_at` | recomendado | Data da última sincronização (ISO) |
| `note` | opcional | Explica adaptações locais; bloqueia sync automático |

## Renomeação local

Se a pasta local difere do upstream (ex.: `brainstorm-with-docs` ← `grill-with-docs`), `path` aponta para o **upstream**, não para o nome local.

## Skills com subpastas

Skills como `mcp-builder` incluem `scripts/`, `reference/`, etc. O sync baixa **toda a árvore** em `path` — não só `SKILL.md`.

## Layout do repo

```
skills/
├── meta/<skill>/
├── workflow/<skill>/
├── engineering/<skill>/
├── product/<skill>/
├── design/<skill>/
├── communication/<skill>/
├── marketing/<skill>/
└── operations/<skill>/
```

`metadata.area` deve corresponder à pasta pai da skill.

## Após importar ou adaptar

1. Preencher `metadata.upstream` com commit exato (`git rev-parse` no clone upstream ou SHA da URL raw).
2. Definir `metadata.area` com a área escolhida.
3. Rodar `python skills/meta/sync-upstream-skills/scripts/check-upstream.py` para validar.
