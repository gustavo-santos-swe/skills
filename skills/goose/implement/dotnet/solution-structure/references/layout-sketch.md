# Layout sketch

Illustrative only. Names follow `{Product}.{Vertical}.{Layer}`.

## Polyglot monorepo (default)

```
src/
  backend/                         # .NET + tests + CPM props
    Directory.Packages.props
    Directory.Build.props
    Contoso.slnx                   # optional; root .sln may also exist
    Contoso.App.Domain/
    Contoso.App.Application/
    Contoso.App.Infrastructure/
    Contoso.App.Api/
    Contoso.AppHost/
    Contoso.ServiceDefaults/
    Contoso.App.Tests.Unit/
    Contoso.App.Tests.Integration/
    Contoso.Architecture.Tests/
  frontend/                        # Next.js App Router
    package.json
    src/app/…
  mobile/                          # when Mobile is in
    package.json
    app/…
docs/
docker-compose.yml
```

Not this (anti-pattern agents keep inventing):

```
src/                 # backend only
tests/               # ❌ root tests
web/                 # ❌ root web beside src
Directory.Packages.props   # ❌ usually belongs under src/backend
```

## Single vertical (flat backend)

```
src/backend/
  Directory.Packages.props
  Directory.Build.props
  Contoso.App.Domain/
  Contoso.App.Application/
  Contoso.App.Infrastructure/
  Contoso.App.Api/
  Contoso.AppHost/
  Contoso.ServiceDefaults/
  Contoso.App.Tests.Unit/
  Contoso.App.Tests.Integration/
  Contoso.Architecture.Tests/
```

## Multi-vertical (folder per vertical)

```
src/backend/
  Directory.Packages.props
  Directory.Build.props
  App/
    Contoso.App.Domain/
    Contoso.App.Application/
    Contoso.App.Infrastructure/
    Contoso.App.Api/
    Contoso.App.Tests.Unit/
    Contoso.App.Tests.Integration/
  Admin/
    Contoso.Admin.Domain/
    Contoso.Admin.Application/
    Contoso.Admin.Infrastructure/
    Contoso.Admin.Api/
  Contoso.AppHost/
  Contoso.ServiceDefaults/
  Contoso.Architecture.Tests/
```

## After Persistence split

```
…/Contoso.App.Infrastructure/              # integrations
…/Contoso.App.Infrastructure.Persistence/  # EF + migrations
```
