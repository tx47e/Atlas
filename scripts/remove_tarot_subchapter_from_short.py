from __future__ import annotations

import argparse
import re
from pathlib import Path


MARKDOWN_PATTERN = re.compile(
    r"(?ms)^Index: [^\n]+-SUB-007\r?\n(?:\r?\n)?### 1\.7\. Tarot\r?\n.*?"
    r"(?=^Index: [^\n]+-CAP-006\r?$)"
)
HTML_PATTERN = re.compile(
    r'(?s)(?:<div class="(?:idx|index)">Index: [^<]+-SUB-007</div>\s*)?'
    r'<h3 id="1-7-tarot">1\.7\. Tarot</h3>.*?'
    r'(?=<div class="(?:idx|index)(?: index-heading)?">Index: [^<]+-CAP-006</div>)'
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Elimină vechiul subcapitol 1.7. Tarot din sursele template-ului scurt."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    for path in args.paths:
        text = path.read_text(encoding="utf-8")
        pattern = HTML_PATTERN if path.suffix.lower() == ".html" else MARKDOWN_PATTERN
        updated, count = pattern.subn("", text, count=1)
        if count != 1:
            raise RuntimeError(f"Blocul 1.7. Tarot nu a fost identificat o singură dată în {path}")
        path.write_text(updated, encoding="utf-8", newline="\n")
        print(f"Actualizat: {path}")


if __name__ == "__main__":
    main()
