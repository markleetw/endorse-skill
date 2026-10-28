#!/usr/bin/env python3
"""Create the actual Endorse release ZIP. No external dependencies."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse
import hashlib

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_FILES = ("SKILL.md", "README.md", "README.zh-TW.md", "LICENSE")

def build(destination: Path, release_notes: Path) -> str:
    if not release_notes.is_file() or not release_notes.read_text(encoding="utf-8").strip():
        raise ValueError(f"Missing release notes: {release_notes}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        for name in PACKAGE_FILES:
            source = ROOT / name
            if not source.is_file():
                raise ValueError(f"Missing package file: {name}")
            archive.write(source, f"endorse/{name}")
        archive.write(release_notes, "endorse/RELEASE_NOTES.md")
    with ZipFile(destination) as archive:
        expected = {f"endorse/{name}" for name in PACKAGE_FILES} | {"endorse/RELEASE_NOTES.md"}
        if set(archive.namelist()) != expected or archive.testzip() is not None:
            raise ValueError("ZIP structure/integrity validation failed")
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    return digest

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="e.g. v1.1.0")
    parser.add_argument("--output", type=Path, default=Path("endorse.zip"))
    args = parser.parse_args()
    if not __import__("re").fullmatch(r"v\d+\.\d+\.\d+", args.version):
        parser.error("version must be vMAJOR.MINOR.PATCH")
    notes = ROOT / "releases" / f"{args.version}.md"
    checksum = build(args.output, notes)
    print(f"{checksum}  {args.output.name}")
