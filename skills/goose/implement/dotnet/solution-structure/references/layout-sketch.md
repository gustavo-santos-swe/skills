# Layout sketch

Illustrative only. Names follow `{Product}.{Vertical}.{Layer}`.

## Single vertical (flat)

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
