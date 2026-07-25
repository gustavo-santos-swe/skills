# Messaging sketches

## Intent check (ask before coding)

```text
Is this "something happened" (other services/workers may react) → integration event + bus ports.
Is this "do work later in this app" (email, sync, cleanup) → Hangfire / background-work.
Unclear → ask the engineer; don't default to a queue.
```

## Application port (bus-agnostic)

```csharp
public interface IEventPublisher
{
    Task PublishAsync<T>(T integrationEvent, CancellationToken cancellationToken)
        where T : class;
}
```

Infrastructure implements this with whatever bus the repo chose. Handlers depend on `IEventPublisher`, not `IAmazonSQS` / `ServiceBusClient`.

## Listener hosting

```csharp
// API or Worker Program.cs — consumption is hosted, not request-scoped
builder.Services.AddHostedService<IntegrationEventConsumerHost>(); // or bus AddMassTransit / Wolverine host integration
```

Don’t start long-running receive loops inside Minimal API handlers.

## Outbox (conceptual)

```text
Same DB transaction: write business rows + outbox row.
Dispatcher (hosted) publishes outbox → bus, then marks dispatched.
Never: SaveChanges(); await bus.Publish(...); // dual-write
```
