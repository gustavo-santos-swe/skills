# skills

Repositório central das minhas [Agent Skills](https://agentskills.io/) — playbooks que ensinam o agente a executar tarefas específicas do meu fluxo de trabalho.

Servido via [Skills Over MCP](https://skillsovermcp.com/). Push em `main` e qualquer cliente MCP conectado já vê a versão nova.

## URL MCP

```
https://mcp.skillsovermcp.com/mcp/gustavo-santos-swe/skills
```

**Cursor:** Settings → MCP → Add server → colar a URL acima (transport: `streamable-http`).

## Estrutura por área

Skills organizadas em `skills/<area>/<nome>/`. [Skills Over MCP](https://skillsovermcp.com/) suporta pastas aninhadas.

```
skills/
├── meta/           # descobrir, manter e sincronizar skills
├── workflow/       # spec → plano → execução → PR
├── engineering/    # código, testes, review, MCP, tech debt
├── product/        # domínio, discovery, posicionamento
├── design/         # UI/UX
├── communication/  # prosa e copy
├── marketing/      # pricing, launch, aquisição (reservado)
└── operations/     # suporte, métricas, deploy ops
```

Cada `SKILL.md` inclui `metadata.area` com a área correspondente.

## Inventário

### meta

| Skill | Para quê |
|-------|----------|
| [`using-superpowers`](skills/meta/using-superpowers/) | Checar skills disponíveis antes de agir |
| [`writing-skills`](skills/meta/writing-skills/) | Criar e manter skills |
| [`handoff`](skills/meta/handoff/) | Compactar sessão para o próximo agente |
| [`sync-upstream-skills`](skills/meta/sync-upstream-skills/) | Checar e sincronizar skills com repos upstream |
| [`suggesting-skills`](skills/meta/suggesting-skills/) | Propor novas skills |

### workflow

| Skill | Para quê |
|-------|----------|
| [`brainstorming`](skills/workflow/brainstorming/) | Design e spec antes de implementar |
| [`writing-plans`](skills/workflow/writing-plans/) | Plano de implementação detalhado |
| [`executing-plans`](skills/workflow/executing-plans/) | Executar plano task por task |
| [`doc-coauthoring`](skills/workflow/doc-coauthoring/) | Co-escrever specs, RFCs, PRDs |
| [`ship-feature`](skills/workflow/ship-feature/) | Commit, push e abrir PR — nunca merge na main |

Origem workflow: [obra/superpowers](https://github.com/obra/superpowers), [anthropics/skills](https://github.com/anthropics/skills) — custom `ship-feature`.

### engineering

| Skill | Para quê |
|-------|----------|
| [`test-driven-development`](skills/engineering/test-driven-development/) | TDD — teste primeiro |
| [`systematic-debugging`](skills/engineering/systematic-debugging/) | Debug sistemático antes de fix |
| [`verification-before-completion`](skills/engineering/verification-before-completion/) | Evidência antes de dizer "pronto" |
| [`requesting-code-review`](skills/engineering/requesting-code-review/) | Self-review rápido do diff antes do PR |
| [`code-review-and-quality`](skills/engineering/code-review-and-quality/) | Review 5 eixos (correctness, architecture, security, perf) |
| [`receiving-code-review`](skills/engineering/receiving-code-review/) | Processar feedback de review |
| [`code-simplification`](skills/engineering/code-simplification/) | Simplificar código sem mudar comportamento |
| [`zoom-out`](skills/engineering/zoom-out/) | Mapa de módulos em código desconhecido |
| [`finding-duplicate-functions`](skills/engineering/finding-duplicate-functions/) | Auditar duplicação semântica |
| [`mcp-builder`](skills/engineering/mcp-builder/) | Criar MCP servers (Python/TypeScript) |

Origem: [obra/superpowers](https://github.com/obra/superpowers), [mattpocock/skills](https://github.com/mattpocock/skills), [anthropics/skills](https://github.com/anthropics/skills), [obra/superpowers-lab](https://github.com/obra/superpowers-lab), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).

### product

| Skill | Para quê |
|-------|----------|
| [`brainstorm-with-docs`](skills/product/brainstorm-with-docs/) | Brainstorm + linguagem de domínio (`CONTEXT.md`, ADRs) |

Origem: [mattpocock/skills](https://github.com/mattpocock/skills) — renomeada de `grill-with-docs`.

### design

| Skill | Para quê |
|-------|----------|
| [`frontend-design`](skills/design/frontend-design/) | UI distinta, production-grade, anti-"AI slop" |

Origem: [anthropics/skills](https://github.com/anthropics/skills).

### communication

| Skill | Para quê |
|-------|----------|
| [`stop-slop`](skills/communication/stop-slop/) | Tirar padrões de escrita de IA |
| [`write-like-a-human`](skills/communication/write-like-a-human/) | Humanizar texto (template) |

Origem: [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop).

### marketing

_Reservado para imports futuros (`pricing-strategy`, `launch-strategy`, etc.)._

### operations

| Skill | Para quê |
|-------|----------|
| [`triage-bug`](skills/operations/triage-bug/) | Bug report → ticket estruturado |

## Fluxo típico

```
brainstorming  (ou brainstorm-with-docs / doc-coauthoring)
  → writing-plans → executing-plans
  → test-driven-development / frontend-design / systematic-debugging
  → verification-before-completion
  → code-simplification (se o código ficou pesado)
  → requesting-code-review (ou code-review-and-quality se diff grande / auth / API)
  → ship-feature
```

Auxiliares: `zoom-out`, `finding-duplicate-functions`, `mcp-builder`, `handoff`, `stop-slop`, `sync-upstream-skills`.

## Criar uma skill nova

1. Escolher área (`meta`, `workflow`, `engineering`, …)
2. Criar `skills/<area>/<nome>/SKILL.md`
3. Frontmatter mínimo:

```markdown
---
name: <nome>
description: O que faz e quando usar — palavras-chave que eu costumo dizer.
metadata:
  area: engineering
  upstream:
    repo: owner/repo
    path: skills/<nome>
    url: https://github.com/owner/repo/tree/main/skills/<nome>
    synced_at: "YYYY-MM-DD"
    commit: "<sha>"
---
```

Schema: [`skills/meta/sync-upstream-skills/references/upstream-schema.md`](skills/meta/sync-upstream-skills/references/upstream-schema.md).

Checar upstream:

```bash
python skills/meta/sync-upstream-skills/scripts/check-upstream.py
```

4. Manter o corpo enxuto (< 500 linhas). Detalhes em `references/`.
5. Atualizar o `README.md` da área e este inventário.

## Notas

- Repo **público** — qualquer um com a URL MCP consegue ler as skills.
- Não colocar segredos, credenciais ou dados sensíveis.
- A `description` no frontmatter é o que o agente usa para decidir *quando* ativar a skill.

## Referências

- [Agent Skills spec](https://agentskills.io/specification)
- [Skills Over MCP](https://skillsovermcp.com/)
- [obra/superpowers](https://github.com/obra/superpowers)
- [mattpocock/skills](https://github.com/mattpocock/skills)
- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers-lab](https://github.com/obra/superpowers-lab)
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
