#!/usr/bin/env python3
"""Sync one skill directory from upstream GitHub path at latest commit."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

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


def find_skill_dir(name: str) -> Path | None:
    for skill_md in SKILLS_ROOT.rglob("SKILL.md"):
        if skill_md.parent.name == name and skill_md.parent.parent.name in AREAS:
            return skill_md.parent
    return None
GITHUB_API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"


def parse_upstream(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}

    upstream: dict[str, str] = {}
    in_upstream = False
    for line in match.group(1).splitlines():
        if line.strip() == "upstream:":
            in_upstream = True
            continue
        if in_upstream:
            field = re.match(r"^\s{4,}(\w+):\s*(.*)$", line)
            if field:
                key, value = field.group(1), field.group(2).strip()
                upstream[key] = value.strip('"').strip("'")
            elif line.strip() and not line.startswith(" "):
                in_upstream = False
            elif re.match(r"^\s{0,3}\S", line) and not re.match(r"^\s{4,}\w+:", line):
                in_upstream = False
    return upstream


def github_get(url: str) -> object:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "sync-upstream-skills",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def latest_commit(repo: str, path: str) -> str:
    encoded = urllib.parse.quote(path, safe="/")
    for branch in ("main", "master"):
        url = f"{GITHUB_API}/repos/{repo}/commits?path={encoded}&sha={branch}&per_page=1"
        try:
            commits = github_get(url)
        except urllib.error.HTTPError:
            continue
        if commits:
            return commits[0]["sha"]
    raise RuntimeError(f"Não encontrei commits para {repo}:{path}")


def list_tree_files(repo: str, path: str, ref: str) -> list[tuple[str, str]]:
    """Return list of (relative_path, download_url_or_api_path) for all files under path."""
    encoded = urllib.parse.quote(path, safe="/")
    url = f"{GITHUB_API}/repos/{repo}/git/trees/{ref}?recursive=1"
    tree = github_get(url)
    prefix = path.rstrip("/") + "/"
    files: list[tuple[str, str]] = []
    for item in tree.get("tree", []):
        if item.get("type") != "blob":
            continue
        full = item["path"]
        if full == path.rstrip("/"):
            files.append((Path(full).name, full))
        elif full.startswith(prefix):
            files.append((full[len(prefix) :], full))
    if not files:
        raise RuntimeError(f"Nenhum arquivo em {repo}@{ref}:{path}")
    return files


def download_file(repo: str, ref: str, repo_path: str) -> bytes:
    url = f"{RAW}/{repo}/{ref}/{repo_path}"
    req = urllib.request.Request(url, headers={"User-Agent": "sync-upstream-skills"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def update_skill_frontmatter(skill_md: Path, commit: str, synced_at: str) -> None:
    text = skill_md.read_text(encoding="utf-8")
    text = re.sub(
        r"(?m)^(\s{4}commit:\s*).*$",
        rf"\1{commit}",
        text,
        count=1,
    )
    if re.search(r"(?m)^\s{4}synced_at:\s*", text):
        text = re.sub(
            r'(?m)^(\s{4}synced_at:\s*).*$',
            rf'\1"{synced_at}"',
            text,
            count=1,
        )
    else:
        text = re.sub(
            r"(?m)^(\s{4}commit:\s*.+)$",
            rf'\1\n    synced_at: "{synced_at}"',
            text,
            count=1,
        )
    skill_md.write_text(text, encoding="utf-8")


def sync_skill(name: str, *, force: bool, dry_run: bool) -> int:
    skill_dir = find_skill_dir(name)
    if skill_dir is None:
        print(f"Skill nao encontrada: {name}", file=sys.stderr)
        return 1
    skill_md = skill_dir / "SKILL.md"

    upstream = parse_upstream(skill_md)
    repo = upstream.get("repo")
    path = upstream.get("path")
    note = upstream.get("note")

    if not repo or not path:
        print(f"{name}: sem metadata.upstream.repo/path — não sincronizável.", file=sys.stderr)
        return 1

    if note and not force:
        print(
            f"{name}: skill adaptada (note presente). "
            "Rode com --force após revisar o diff manualmente.",
            file=sys.stderr,
        )
        return 1

    ref = latest_commit(repo, path)
    files = list_tree_files(repo, path, ref)
    synced_at = date.today().isoformat()

    print(f"Sincronizando {name} de {repo}@{ref[:12]} ({len(files)} arquivos)")
    if dry_run:
        for rel, _ in sorted(files):
            print(f"  would write: {skill_dir / rel}")
        return 0

    for rel, repo_path in files:
        dest = skill_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(download_file(repo, ref, repo_path))
        print(f"  wrote: {rel}")

    update_skill_frontmatter(skill_dir / "SKILL.md", ref, synced_at)
    print(f"Atualizado metadata: commit={ref[:12]}, synced_at={synced_at}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync one skill from upstream.")
    parser.add_argument("skill", help="Nome da pasta em skills/")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Permite sync de skills adaptadas (com metadata.upstream.note).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Lista arquivos que seriam baixados, sem escrever.",
    )
    args = parser.parse_args()
    return sync_skill(args.skill, force=args.force, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
