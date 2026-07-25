# Migrations sketches

## Apply in CD (not first pod)

```text
build → test →
  migrate job: dotnet ef database update --project …Infrastructure --startup-project …Api
  → roll out new app instances
```

Optional later: `dotnet ef migrations bundle -o efbundle` and run `./efbundle` in the migrate job.

## Expand / contract (rename column)

```text
1) Migration: add NewName (nullable) — expand
2) App: write both OldName and NewName; read NewName ?? OldName
3) Backfill: UPDATE … SET NewName = OldName WHERE NewName IS NULL
4) App: read/write NewName only
5) Migration: drop OldName — contract
```

## Never

```text
Edit 20240101120000_Initial.cs after it ran in prod
Database.Migrate() in Program.cs as the only prod apply path under multiple replicas
```
