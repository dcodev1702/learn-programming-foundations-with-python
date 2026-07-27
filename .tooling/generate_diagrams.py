"""Regenerate every SVG diagram used by the chapters.

Usage (from the repository root):

    python .tooling/generate_diagrams.py

Every diagram is written to ``diagrams/``. The visual theme lives in
``.tooling/diagram_kit.py`` — change a colour there and rerun this script to
restyle the whole course at once.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import diagrams_month1
import diagrams_month2
import diagrams_month3

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "diagrams"

BUILDERS = diagrams_month1.DIAGRAMS + diagrams_month2.DIAGRAMS + diagrams_month3.DIAGRAMS


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    for builder in BUILDERS:
        filename, svg = builder()
        target = OUTPUT_DIR / filename
        target.write_text(svg, encoding="utf-8")
        written.append((filename, len(svg)))

    width = max(len(name) for name, _ in written)
    for name, size in written:
        print(f"  {name.ljust(width)}  {size / 1024:6.1f} KB")
    print(f"\n{len(written)} diagrams written to {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
