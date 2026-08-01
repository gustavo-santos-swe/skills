import {
  Callout,
  Card,
  CardBody,
  CardHeader,
  Code,
  Divider,
  Grid,
  H1,
  H2,
  H3,
  Pill,
  Stack,
  Stat,
  Table,
  Text,
} from "cursor/canvas";

/**
 * verify canvas TEMPLATE (sample data).
 * Agents: copy to `<repo-or-slug>-verify.canvas.tsx`, replace the `report` object.
 * Keep section order and label strings identical every time.
 */

type Classification = "Drift" | "Gap" | "Style";

type Finding = {
  skill: string;
  rule: string;
  evidence: string;
};

type Aligned = {
  skill: string;
  text: string;
};

/** Replace this object per audit. Do not rename keys. */
const report = {
  slug: "acme-api",
  date: "2026-07-29",
  packsChecked: "dotnet, database",
  scope: "whole repo",
  summary:
    "Backbone (layers, errors, ids/time, tests) already matches the pack. Five Drift findings need a hardening pass before wider rollout: unsigned external tokens, entities leaking onto the wire, missing FKs, no structured validation, and a committed secret.",
  drift: [
    {
      skill: "security (defer to security-check)",
      rule: "External auth must verify token signature",
      evidence: "Infrastructure/Auth/ExternalIdentityVerifier.cs",
    },
    {
      skill: "application-layer",
      rule: "Return response DTOs, not domain entities, from handlers",
      evidence: "AddItemHandler.cs, Api/Http/ResultExtensions.cs",
    },
    {
      skill: "db-integration",
      rule: "Model real foreign keys, not index-only relations",
      evidence: "Infrastructure.Persistence/Mappings/*.cs",
    },
  ] satisfies Finding[],
  gap: [
    {
      skill: "validation",
      rule: "FluentValidation on request DTOs",
      evidence: "No IValidator in the repo yet; manual checks only",
    },
    {
      skill: "rate-limiting",
      rule: "Throttle auth endpoints",
      evidence: "/auth/register, /auth/login have no policy",
    },
  ] satisfies Finding[],
  style: [
    {
      skill: "testing",
      rule: "Name tests Should_..._When_...",
      evidence: "Tests use Method_Scenario_Result instead",
    },
  ] satisfies Finding[],
  aligned: [
    {
      skill: "solution-structure",
      text: "Ports-only layering held by NetArchTest; Domain/Application never reference Infrastructure/Api.",
    },
    {
      skill: "error-handling",
      text: "Result<T> union (Ok/NotFound/ValidationFailed/Forbidden/Conflict) maps to Problem Details in one place.",
    },
    {
      skill: "time-and-ids",
      text: "UUIDv7 ids and NodaTime Instant/LocalDate used end to end in the domain.",
    },
  ] satisfies Aligned[],
  methodology:
    "Read every SKILL.md under the dotnet and database packs fresh, atomized into checkable rules, then walked the repo tree (DI, entities, handlers, endpoints, mappings, tests, CI). UI/mobile packs stayed out of scope.",
};

function classificationTone(c: Classification): "danger" | "warning" | "info" {
  if (c === "Drift") return "danger";
  if (c === "Gap") return "warning";
  return "info";
}

function FindingsTable({
  title,
  classification,
  rows,
}: {
  title: string;
  classification: Classification;
  rows: Finding[];
}) {
  if (rows.length === 0) return null;
  const tone = classificationTone(classification);
  return (
    <Card>
      <CardHeader trailing={<Pill tone={tone}>{classification}</Pill>}>
        {title}
      </CardHeader>
      <CardBody style={{ padding: 0 }}>
        <Table
          headers={["Skill", "Rule", "Evidence"]}
          columnAlign={["left", "left", "left"]}
          rows={rows.map((r) => [r.skill, r.rule, r.evidence])}
          rowTone={rows.map(() => tone)}
        />
      </CardBody>
    </Card>
  );
}

export default function VerifyTemplate() {
  const d = report;

  return (
    <Stack gap={20} style={{ padding: 20, maxWidth: 960 }}>
      <Stack gap={8}>
        <Text
          size="small"
          tone="tertiary"
          style={{ letterSpacing: 0.08, textTransform: "uppercase" }}
        >
          Pack conformance audit
        </Text>
        <H1>{d.slug}</H1>
        <Text size="small" tone="secondary">
          {d.date} - packs checked: <Code>{d.packsChecked}</Code> - scope: {d.scope}
        </Text>
      </Stack>

      <Grid columns={4} gap={12}>
        <Stat
          value={String(d.drift.length)}
          label="Drift"
          tone={d.drift.length ? "danger" : "success"}
        />
        <Stat
          value={String(d.gap.length)}
          label="Gap"
          tone={d.gap.length ? "warning" : undefined}
        />
        <Stat value={String(d.style.length)} label="Style" />
        <Stat value={String(d.aligned.length)} label="Aligned" tone="success" />
      </Grid>

      <Divider />

      <Stack gap={6}>
        <H2>Summary</H2>
        <Text>{d.summary}</Text>
      </Stack>

      {d.drift.length ? (
        <Callout tone="warning" title="Where to focus first">
          Drift findings broke a locked pack rule, not a missing feature. Clear
          these before widening rollout.
        </Callout>
      ) : null}

      <Stack gap={10}>
        <H2>Findings</H2>
        <FindingsTable title="Drift" classification="Drift" rows={d.drift} />
        <FindingsTable title="Gap" classification="Gap" rows={d.gap} />
        <FindingsTable title="Style" classification="Style" rows={d.style} />
      </Stack>

      <Divider />

      <Stack gap={10}>
        <H2>Aligned with the pack</H2>
        <Table
          headers={["Skill", "What already matches"]}
          rows={d.aligned.map((a) => [
            <Text weight="medium">{a.skill}</Text>,
            <Text>{a.text}</Text>,
          ])}
          rowTone={d.aligned.map(() => "success" as const)}
        />
      </Stack>

      <Divider />

      <Stack gap={8}>
        <H3>Methodology</H3>
        <Text tone="tertiary" size="small">
          {d.methodology}
        </Text>
      </Stack>

      <Text size="small" tone="quaternary">
        Template sample with fictional data. Copy, rename to
        &lt;repo-or-slug&gt;-verify.canvas.tsx, replace the report object. Not a
        real audit.
      </Text>
    </Stack>
  );
}
