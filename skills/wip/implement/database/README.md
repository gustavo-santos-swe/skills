# database

Language-agnostic **data & engine** rules. Lives under **`implement`**.

Path: `skills/wip/implement/database/`.

| Pack | Owns |
|------|------|
| [`database`](./SKILL.md) | Schema, integrity, indexes, transactions, evolution, SQL-level performance |
| [`../dotnet/db-integration/`](../dotnet/db-integration/) | How EF/Dapper/C# talks to that model |

Load **database** when modeling or evolving schema; load **db-integration** when writing persistence code. Often both on the same change.
