# Lesson card

Fill one card per lesson (max 5 per retro). Keep each field short.

```text
Lesson:     <one line: the house rule in positive form>
Evidence:   <where it showed up: review note, failed approach, repeated ask>
Bad default:<what the agent did or would do without the rule>
Good move:  <what to do instead>
Scope:      <goose-wide | product>
Owner guess:<Goose skill path, or .claude/skills/<name>, or "unknown">
Disposition:<absorb | local | evolve | defer | drop>  (set after step 3)
```

## Examples

```text
Lesson:     Extend kit Button variants before adding page-local buttons
Evidence:   Review: "do not hardcode a second primary CTA"
Bad default:New styled <button> in the page
Good move:  Add or use a Button variant in components/ui
Scope:      goose-wide
Owner guess:skills/goose/implement/frontend/styling
Disposition:absorb
```

```text
Lesson:     New outbound HTTP clients use typed clients; leave legacy factory call sites
Evidence:   Review: "use typed clients for new classes like this"
Bad default:Inject IHttpClientFactory in every new handler
Good move:  AddHttpClient<TClient> for new vendors; do not rewrite old call sites in this pass
Scope:      product
Owner guess:.claude/skills/http-clients
Disposition:local
```
