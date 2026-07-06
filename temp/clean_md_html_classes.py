import pathlib
import re

MD_PATH = pathlib.Path(
    r"output\lucrari\1998-02-19-BIRSAN-DANIEL-ROBERT\1998-02-19-BIRSAN-DANIEL-ROBERT-v1r.md"
)


def inline_cleanup(value: str) -> str:
    value = value.replace("<br>", "; ")
    value = re.sub(r"<strong>(.*?)</strong>", r"**\1**", value)
    return value.strip()


text = MD_PATH.read_text(encoding="utf-8")

text = re.sub(
    r'<div class="calc-box">(.*?)</div>',
    lambda m: f"**Calcul:** {inline_cleanup(m.group(1))}",
    text,
    flags=re.S,
)

text = re.sub(
    r'<div class="matrix-grid">.*?</div>\s*\n',
    """```text
1: 111 | 4: - | 7: 7
2: 2   | 5: - | 8: 8
3: 333 | 6: - | 9: 9999
```

""",
    text,
    count=1,
    flags=re.S,
)

text = re.sub(
    r'<figure class="svg-figure">\s*<img src="([^"]+)" alt="([^"]+)">\s*<figcaption>(.*?)</figcaption>\s*</figure>',
    lambda m: f"![{m.group(2)}]({m.group(1)})\n\n_{m.group(3).strip()}_",
    text,
    flags=re.S,
)

text = text.replace('<div class="table-wrap">\n', "")
text = text.replace("\n</div>", "")

MD_PATH.write_text(text, encoding="utf-8")
print("cleaned md")

