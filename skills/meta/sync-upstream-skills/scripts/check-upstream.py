#!/usr/bin/env python3
"""Check upstream freshness for skills with metadata.upstream in SKILL.md."""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SKILLS_ROOT = Path(__file__).resolve().parents[3]
AREAS = frozenset(
    {
        "meta",
        "workflow",
        "engineering",
        "product",
        "design",
        "mobile",
        "communication",
        "marketing",
        "operations",
        "wip",
    }
)
GITHUB_API = "https://api.github.com"
_COMMIT_CACHE: dict[tuple[str, str], str | None] = {}


@dataclass
class UpstreamMeta:
    repo: str | None
    path: str | None
    commit: str | None
    synced_at: str | None
    note: str | None
    inspired_by: str | None


@dataclass
class SkillStatus:
    name: str
    category: str
    local_commit: str | None
    upstream_commit: str | None
    synced_at: str | None
    repo: str | None
    path: str | None
    note: str | None
    detail: str | None = None


def parse_frontmatter(text: str) -> dict[str, Any]:
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}

    upstream: dict[str, str] = {}
    in_upstream = False

    for line in match.group(1).splitlines():
        stripped = line.strip()
        if stripped == "upstream:":
            in_upstream = True
            continue
        if in_upstream:
            # Campos de upstream: indentação >= 4 espaços sob metadata.upstream
            field = re.match(r"^\s{4,}(\w+):\s*(.*)$", line)
            if field:
                key, value = field.group(1), field.group(2).strip()
                upstream[key] = value.strip('"').strip("'")
            elif stripped and not line.startswith(" "):
                in_upstream = False
            elif re.match(r"^\s{0,3}\S", line) and not re.match(r"^\s{4,}\w+:", line):
                in_upstream = False

    return {"upstream": upstream}


def load_upstream(skill_dir: Path) -> UpstreamMeta:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return UpstreamMeta(None, None, None, None, None, None)

    data = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    upstream = data.get("upstream", {})
    return UpstreamMeta(
        repo=upstream.get("repo"),
        path=upstream.get("path"),
        commit=upstream.get("commit"),
        synced_at=upstream.get("synced_at"),
        note=upstream.get("note"),
        inspired_by=upstream.get("inspired_by"),
    )


def github_get(url: str, *, retries: int = 3) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "sync-upstream-skills",
    }
    token = __import__("os").environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    last_error: urllib.error.HTTPError | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code in (403, 429) and attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
    if last_error:
        raise last_error
    raise RuntimeError("github_get failed without HTTPError")


def latest_commit_for_path(repo: str, path: str) -> str | None:
    cache_key = (repo, path)
    if cache_key in _COMMIT_CACHE:
        return _COMMIT_CACHE[cache_key]

    encoded_path = urllib.parse.quote(path, safe="/")
    result: str | None = None
    for branch in ("main", "master"):
        url = f"{GITHUB_API}/repos/{repo}/commits?path={encoded_path}&sha={branch}&per_page=1"
        try:
            commits = github_get(url)
        except urllib.error.HTTPError:
            time.sleep(0.3)
            continue
        if commits:
            result = commits[0]["sha"]
            break
        time.sleep(0.3)

    _COMMIT_CACHE[cache_key] = result
    return result


def categorize(meta: UpstreamMeta) -> str:
    if meta.repo and meta.path and meta.commit:
        return "adapted" if meta.note else "syncable"
    if meta.inspired_by or meta.note:
        return "custom"
    return "local"


def check_skill(skill_dir: Path) -> SkillStatus:
    name = skill_dir.name
    meta = load_upstream(skill_dir)
    category = categorize(meta)

    if category == "local":
        return SkillStatus(
            name=name,
            category="local",
            local_commit=meta.commit,
            upstream_commit=None,
            synced_at=meta.synced_at,
            repo=meta.repo,
            path=meta.path,
            note=meta.note,
            detail="Sem metadata.upstream.repo - nao sincronizavel automaticamente.",
        )

    if category == "custom":
        return SkillStatus(
            name=name,
            category="custom",
            local_commit=meta.commit,
            upstream_commit=None,
            synced_at=meta.synced_at,
            repo=meta.repo or meta.inspired_by,
            path=meta.path,
            note=meta.note,
            detail="Skill customizada - sync manual se necessario.",
        )

    assert meta.repo and meta.path and meta.commit
    try:
        upstream_commit = latest_commit_for_path(meta.repo, meta.path)
    except urllib.error.HTTPError as exc:
        return SkillStatus(
            name=name,
            category=category,
            local_commit=meta.commit,
            upstream_commit=None,
            synced_at=meta.synced_at,
            repo=meta.repo,
            path=meta.path,
            note=meta.note,
            detail=f"Erro ao consultar GitHub: HTTP {exc.code}",
        )

    if not upstream_commit:
        return SkillStatus(
            name=name,
            category=category,
            local_commit=meta.commit,
            upstream_commit=None,
            synced_at=meta.synced_at,
            repo=meta.repo,
            path=meta.path,
            note=meta.note,
            detail="Nao foi possivel resolver commit upstream (path, branch ou rate limit).",
        )

    if meta.commit == upstream_commit:
        status_detail = "Atualizado."
    else:
        status_detail = (
            f"Desatualizado: local {meta.commit[:12]} -> upstream {upstream_commit[:12]}"
        )

    return SkillStatus(
        name=name,
        category=category,
        local_commit=meta.commit,
        upstream_commit=upstream_commit,
        synced_at=meta.synced_at,
        repo=meta.repo,
        path=meta.path,
        note=meta.note,
        detail=status_detail,
    )


def main() -> int:
    skills = sorted(
        p.parent
        for p in SKILLS_ROOT.rglob("SKILL.md")
        if p.parent.parent.name in AREAS
    )
    if not skills:
        print(f"Nenhuma skill em {SKILLS_ROOT}", file=sys.stderr)
        return 1

    rows: list[SkillStatus] = []
    for skill_dir in skills:
        rows.append(check_skill(skill_dir))
        time.sleep(0.2)

    outdated = [r for r in rows if r.detail and "Desatualizado" in r.detail]
    errors = [r for r in rows if r.detail and "Nao foi possivel" in r.detail]
    up_to_date = [
        r
        for r in rows
        if r.detail == "Atualizado." or (r.category in ("custom", "local") and r.detail)
    ]
    adapted = [r for r in rows if r.category == "adapted"]
    custom = [r for r in rows if r.category == "custom"]
    local = [r for r in rows if r.category == "local"]

    print(f"Skills verificadas: {len(rows)}")
    print(f"  Atualizadas: {len(up_to_date)}")
    print(f"  Desatualizadas: {len(outdated)}")
    print(f"  Erros de consulta: {len(errors)}")
    print(f"  Adaptadas (merge manual): {len(adapted)}")
    print(f"  Custom/local: {len(custom) + len(local)}")
    if errors and not __import__("os").environ.get("GITHUB_TOKEN"):
        print("  Dica: export GITHUB_TOKEN para evitar rate limit da API (60 req/h sem token).")
    print()

    for row in rows:
        flag = "!" if row.detail and "Desatualizado" in row.detail else " "
        print(f"{flag} {row.name}")
        print(f"    categoria: {row.category}")
        if row.repo:
            print(f"    upstream:  {row.repo} @ {row.path}")
        if row.local_commit:
            print(f"    local:     {row.local_commit[:12]}")
        if row.upstream_commit:
            print(f"    remoto:    {row.upstream_commit[:12]}")
        if row.synced_at:
            print(f"    synced_at: {row.synced_at}")
        if row.note:
            print(f"    note:      {row.note[:80]}{'…' if len(row.note) > 80 else ''}")
        if row.detail:
            print(f"    -> {row.detail}")
        print()

    return 1 if outdated or errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
