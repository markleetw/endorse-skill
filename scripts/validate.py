#!/usr/bin/env python3
"""Dependency-free structural checks; NOT a language-model quality evaluation."""
from pathlib import Path
import re
import sys
import zipfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def fail(msg):
    raise ValueError(msg)

def check():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "\n---\n" not in skill[4:]:
        fail("SKILL.md: missing YAML frontmatter")
    front = skill.split("---", 2)[1]
    if not re.search(r"(?m)^name: endorse$", front):
        fail("SKILL.md: invalid name")
    if not re.search(r"(?m)^description: .{30,}$", front):
        fail("SKILL.md: missing meaningful description")
    for p in ["README.md", "README.zh-TW.md", "RELEASE_NOTES.md",
              "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md",
              "evals/README.md", "evals/rubric.md"]:
        if not (ROOT / p).is_file() or not (ROOT / p).read_text(encoding="utf-8").strip():
            fail(f"Missing or empty: {p}")
    for p in ["README.md", "README.zh-TW.md"]:
        txt = (ROOT / p).read_text(encoding="utf-8")
        for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", txt):
            if link.startswith(("https://", "http://", "#", "mailto:")):
                continue
            if not (ROOT / link.split("#", 1)[0]).exists():
                fail(f"{p}: broken local link: {link}")
    cases = list((ROOT / "evals/cases").glob("*.md"))
    if len(cases) < 5:
        fail("Expected at least five regression cases")
    for case in cases:
        content = case.read_text(encoding="utf-8")
        for heading in ["## Input", "## Facts available on follow-up", "## Evaluator expectations"]:
            if heading not in content:
                fail(f"{case.name}: missing section {heading}")
    with tempfile.TemporaryDirectory() as directory:
        archive = Path(directory) / "endorse.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
            for file in ["SKILL.md", "README.md", "README.zh-TW.md", "RELEASE_NOTES.md"]:
                z.write(ROOT / file, f"endorse/{file}")
        with zipfile.ZipFile(archive) as z:
            if z.testzip() is not None:
                fail("Corrupt release ZIP")
            assert "endorse/SKILL.md" in z.namelist()
    print("PASS: frontmatter, docs, links, cases and ZIP layout (structural only)")

if __name__ == "__main__":
    try:
        check()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
