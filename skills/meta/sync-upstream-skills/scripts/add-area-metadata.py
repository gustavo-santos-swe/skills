#!/usr/bin/env python3
"""One-off helper: set metadata.area from parent folder name in SKILL.md files."""

from __future__ import annotations

import re
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[3]
AREAS = {
    "meta",
    "workflow",
    "engineering",
    "product",
    "design",
    "mobile",
    "communication",
    "marketing",
    "operations",
}


def set_area(skill_md: Path, area: str) -> bool:
    text = skill_md.read_text(encoding="utf-8")
    if re.search(r"(?m)^\s{2}area:\s", text):
        return False
    if re.search(r"(?m)^metadata:\s*$", text):
        text = re.sub(r"(?m)^(metadata:\s*)$", rf"\1\n  area: {area}", text, count=1)
    else:
        text = re.sub(
            r"(?m)^(description:.*?)$",
            rf"\1\nmetadata:\n  area: {area}",
            text,
            count=1,
        )
    skill_md.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    updated = 0
    for skill_md in SKILLS_ROOT.rglob("SKILL.md"):
        area = skill_md.parent.parent.name
        if area not in AREAS:
            continue
        if set_area(skill_md, area):
            updated += 1
            print(f"area:{area} -> {skill_md.parent.name}")
    print(f"Updated {updated} files")


if __name__ == "__main__":
    main()
