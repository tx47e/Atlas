from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts/render_rebeca_short_html.py"
spec = importlib.util.spec_from_file_location("atlas_short_renderer", SOURCE)
if not spec or not spec.loader:
    raise RuntimeError("Nu pot încărca rendererul template-ului scurt.")
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)

renderer.DIR = ROOT / "output/lucrari/2025-07-14-VULCU-MARC-IOAN"
renderer.MD_PATH = renderer.DIR / "2025-07-14-VULCU-MARC-IOAN-scurt-v1.00r.md"
renderer.HTML_PATH = renderer.DIR / "2025-07-14-VULCU-MARC-IOAN-scurt-v1.00r.html"
renderer.PREFIX = "VMI-20250714-v1.00r"


def main() -> None:
    renderer.main()
    path = renderer.HTML_PATH
    text = path.read_text(encoding="utf-8")
    text = text.replace("Vulcu Rebeca Andreea — 15.03.2020", "Vulcu Marc Ioan — 14.07.2025")
    text = text.replace("Vulcu Rebeca Andreea · lucrare numerologică scurtă", "Vulcu Marc Ioan · lucrare numerologică scurtă")
    path.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
