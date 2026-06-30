#!/usr/bin/env python3
"""Verify SHA-256 hashes listed in receipts/SHA256SUMS.txt."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "receipts" / "SHA256SUMS.txt"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not MANIFEST.exists():
        print(f"Missing manifest: {MANIFEST}")
        return 1
    failures = []
    checked = 0
    for lineno, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            expected, rel = line.split(None, 1)
        except ValueError:
            failures.append(f"Line {lineno}: malformed manifest line")
            continue
        rel = rel.strip()
        path = ROOT / rel
        if not path.exists():
            failures.append(f"Line {lineno}: missing file {rel}")
            continue
        actual = sha256(path)
        checked += 1
        if actual != expected:
            failures.append(f"Line {lineno}: hash mismatch for {rel}: expected {expected}, got {actual}")
    if failures:
        print("MANIFEST CHECK FAILED")
        for f in failures:
            print("-", f)
        return 1
    print(f"MANIFEST CHECK PASSED: {checked} files verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
