from pathlib import Path


OUT = Path("output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/harta-suprapusa-soarta-destin-birsan-daniel-robert.svg")

WIDTH = 2400
HEIGHT = 1500
LEFT = 170
RIGHT = 80
TOP = 130
TIMELINE_W = WIDTH - LEFT - RIGHT
START_AGE = 0
END_AGE = 98


def x(age: float) -> float:
    return LEFT + (age - START_AGE) / (END_AGE - START_AGE) * TIMELINE_W


def esc(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def text(xp, yp, value, cls="label", anchor="start"):
    return f'<text class="{cls}" x="{xp:.1f}" y="{yp:.1f}" text-anchor="{anchor}">{esc(value)}</text>'


def line(x1, y1, x2, y2, cls="grid"):
    return f'<line class="{cls}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'


def rect(xp, yp, w, h, cls, rx=10):
    return f'<rect class="{cls}" x="{xp:.1f}" y="{yp:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}"/>'


def band(y, start, end, cls, title, detail, min_label=90):
    x1 = x(start)
    x2 = x(end)
    w = x2 - x1
    parts = [rect(x1, y, w, 54, cls, 12)]
    if w >= min_label:
        parts.append(text(x1 + 10, y + 22, title, "band-title"))
        parts.append(text(x1 + 10, y + 42, detail, "band-detail"))
    else:
        parts.append(text(x1 + w / 2, y + 33, title, "band-title", "middle"))
    return "\n".join(parts)


def marker(age, y1, y2, cls, label, detail=None, anchor="middle"):
    xp = x(age)
    parts = [line(xp, y1, xp, y2, cls), f'<circle class="{cls}-dot" cx="{xp:.1f}" cy="{y1:.1f}" r="8"/>']
    parts.append(text(xp, y1 - 12, label, f"{cls}-label", anchor))
    if detail:
        parts.append(text(xp, y2 + 18, detail, f"{cls}-small", anchor))
    return "\n".join(parts)


def fate_destiny_chart():
    fate = [3, 8, 0, 0, 1, 9, 6]
    destiny = [3, 8, 2, 0, 1, 7, 6]
    ages = [0, 10, 20, 30, 40, 50, 60]
    y_top = TOP
    h = 300
    y_base = y_top + h

    def yv(v):
        return y_base - (v / 9) * h

    parts = []
    for v in range(10):
        yy = yv(v)
        parts.append(line(LEFT, yy, LEFT + 7 / 9.8 * TIMELINE_W, yy, "chart-grid"))
        parts.append(text(LEFT - 32, yy + 5, v, "axis-label", "end"))
    for age in ages:
        parts.append(line(x(age), y_top, x(age), y_base, "chart-grid"))
        parts.append(text(x(age), y_base + 28, age, "axis-label", "middle"))

    fate_points = " ".join(f"{x(a):.1f},{yv(v):.1f}" for a, v in zip(ages, fate))
    destiny_points = " ".join(f"{x(a):.1f},{yv(v):.1f}" for a, v in zip(ages, destiny))
    parts.append(f'<polyline class="fate-line" points="{fate_points}"/>')
    parts.append(f'<polyline class="destiny-line" points="{destiny_points}"/>')

    for a, f, d in zip(ages, fate, destiny):
        if f == d:
            parts.append(f'<circle class="meet-dot" cx="{x(a):.1f}" cy="{yv(f):.1f}" r="10"/>')
            parts.append(text(x(a), yv(f) - 16, f, "point-label", "middle"))
        else:
            parts.append(f'<circle class="fate-dot" cx="{x(a):.1f}" cy="{yv(f):.1f}" r="8"/>')
            parts.append(text(x(a), yv(f) - 12, f, "point-label", "middle"))
            parts.append(f'<circle class="destiny-dot" cx="{x(a):.1f}" cy="{yv(d):.1f}" r="8"/>')
            parts.append(text(x(a), yv(d) - 12, d, "point-label", "middle"))
    return "\n".join(parts)


def main():
    c7 = [
        (0, 7, "C1", "criza 3,5 / 2001", "1/8 -> 9"),
        (7, 14, "C2", "criza 10,5 / 2008", "2/6 -> 8"),
        (14, 21, "C3", "criza 17,5 / 2015", "3/10 -> 4"),
        (21, 28, "C4", "criza 24,5 / 2022", "4/11 -> 6"),
        (28, 35, "C5", "criza 31,5 / 2029", "5/9 -> 5"),
        (35, 42, "C6", "criza 38,5 / 2036", "3/7 -> 1"),
        (42, 49, "C7", "criza 45,5 / 2043", "1/5 -> 6"),
        (49, 56, "C8", "criza 52,5 / 2050", "1/8 -> 9"),
        (56, 63, "C9", "criza 59,5 / 2057", "2/6 -> 8"),
        (63, 70, "C10", "criza 66,5 / 2064", "3/10 -> 4"),
        (70, 77, "C11", "criza 73,5 / 2071", "4/11 -> 6"),
        (77, 84, "C12", "criza 80,5 / 2078", "5/9 -> 5"),
        (84, 91, "C13", "criza 87,5 / 2085", "3/7 -> 1"),
        (91, 98, "C14", "criza 94,5 / 2092", "1/5 -> 6"),
    ]
    c12 = [
        (0, 12, "C1", "1998-2009", "Formare primara"),
        (12, 24, "C2", "2010-2021", "Explorare si autonomie"),
        (24, 36, "C3", "2022-2033", "Constructie identitara"),
        (36, 48, "C4", "2034-2045", "Expansiune si impact"),
        (48, 60, "C5", "2046-2057", "Autoritate si transmitere"),
        (60, 72, "C6", "2058-2069", "Intelepciune aplicata"),
        (72, 84, "C7", "2070-2081", "Sinteza si eliberare"),
    ]
    pinacles = [
        (0, 33, "P1", "Oportunitate 3 / Provocare 1"),
        (34, 42, "P2", "Oportunitate 1 / Provocare 8"),
        (43, 51, "P3", "Oportunitate 4 / Provocare 7"),
        (52, 98, "P4", "Oportunitate 2 / Provocare 7"),
    ]
    c9 = [
        (28, 2026, 4, 2), (29, 2027, 5, 4), (30, 2028, 6, 7), (31, 2029, 7, 5),
        (32, 2030, 8, 9), (33, 2031, 9, 2), (34, 2032, 1, 4), (35, 2033, 2, 7),
        (36, 2034, 3, 5), (37, 2035, 4, 9), (38, 2036, 5, 2),
    ]
    important = [(18, "2016", "I"), (27, "2025", "I+E"), (36, "2034", "I+E"), (45, "2043", "I+E")]
    jupiter = [(12, "2010"), (24, "2022"), (36, "2034"), (48, "2046"), (60, "2058")]

    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <title>Harta suprapusa Soarta, Destin si cicluri - Birsan Daniel Robert</title>
  <desc>Grafic sintetic amplu care suprapune Soarta si Destin cu ciclurile de 9, 7 si 12 ani, anii importanti si pinaclurile.</desc>
  <defs>
    <style>
      .bg {{ fill: #f7efe3; }}
      .panel {{ fill: #fffaf2; stroke: #d8c5aa; stroke-width: 2; }}
      .title {{ font-family: Arial, Helvetica, sans-serif; font-size: 38px; font-weight: 800; fill: #27231f; }}
      .subtitle {{ font-family: Arial, Helvetica, sans-serif; font-size: 18px; font-weight: 700; fill: #66594b; }}
      .section-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 18px; font-weight: 800; fill: #3b332b; }}
      .axis-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 14px; fill: #5d5145; }}
      .label {{ font-family: Arial, Helvetica, sans-serif; font-size: 15px; fill: #3f372f; }}
      .band-title {{ font-family: Arial, Helvetica, sans-serif; font-size: 15px; font-weight: 800; fill: #1f1f1f; }}
      .band-detail {{ font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-weight: 700; fill: #4a4138; }}
      .grid {{ stroke: #dccbb5; stroke-width: 1; }}
      .major-grid {{ stroke: #bca78d; stroke-width: 2; }}
      .chart-grid {{ stroke: #ddcdb8; stroke-width: 1; }}
      .fate-line {{ fill: none; stroke: #c56f2d; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; }}
      .destiny-line {{ fill: none; stroke: #0f6a70; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; }}
      .fate-dot {{ fill: #c56f2d; stroke: #fffaf2; stroke-width: 3; }}
      .destiny-dot {{ fill: #0f6a70; stroke: #fffaf2; stroke-width: 3; }}
      .meet-dot {{ fill: #2e2b27; stroke: #fffaf2; stroke-width: 3; }}
      .point-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 16px; font-weight: 900; fill: #1f1f1f; }}
      .pinacle {{ fill: #f2c14e; stroke: #8f6b12; stroke-width: 1.5; opacity: .88; }}
      .cycle12 {{ fill: #9cc9c1; stroke: #356f69; stroke-width: 1.5; opacity: .9; }}
      .cycle7 {{ fill: #d9b6df; stroke: #7c4d86; stroke-width: 1.3; opacity: .86; }}
      .cycle9 {{ fill: #f7a072; stroke: #9f4d29; stroke-width: 1.2; opacity: .9; }}
      .crisis {{ stroke: #7c1f1f; stroke-width: 2.5; stroke-dasharray: 8 5; }}
      .crisis-dot {{ fill: #7c1f1f; stroke: #fffaf2; stroke-width: 2; }}
      .crisis-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-weight: 800; fill: #7c1f1f; }}
      .crisis-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 11px; font-weight: 700; fill: #7c1f1f; }}
      .important {{ stroke: #263b8f; stroke-width: 3; }}
      .important-dot {{ fill: #263b8f; stroke: #fffaf2; stroke-width: 2; }}
      .important-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 13px; font-weight: 900; fill: #263b8f; }}
      .important-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-weight: 800; fill: #263b8f; }}
      .jupiter {{ stroke: #2f7d32; stroke-width: 2.5; stroke-dasharray: 4 5; }}
      .jupiter-dot {{ fill: #2f7d32; stroke: #fffaf2; stroke-width: 2; }}
      .jupiter-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-weight: 900; fill: #2f7d32; }}
      .jupiter-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 11px; font-weight: 800; fill: #2f7d32; }}
      .legend-title {{ font-family: Arial, Helvetica, sans-serif; font-size: 17px; font-weight: 900; fill: #27231f; }}
      .legend-text {{ font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: 700; fill: #4f453b; }}
    </style>
  </defs>
''']
    parts.append('<rect class="bg" width="2400" height="1500"/>')
    parts.append('<rect class="panel" x="40" y="35" width="2320" height="1415" rx="18"/>')
    parts.append(text(70, 82, "Harta suprapusa: Soarta, Destin si cicluri", "title"))
    parts.append(text(70, 112, "Birsan Daniel Robert | 19.02.1998 | baza: Soarta 3800196 si Destin grafic 3820176", "subtitle"))

    for age in range(0, 99, 7):
        parts.append(line(x(age), 128, x(age), 1375, "grid"))
    for age in range(0, 99, 14):
        parts.append(line(x(age), 128, x(age), 1375, "major-grid"))
    for age in range(0, 99, 7):
        parts.append(text(x(age), 1405, str(age), "axis-label", "middle"))
    parts.append(text(LEFT, 1430, "varsta", "axis-label", "middle"))

    parts.append(text(70, 175, "Soarta / Destin", "section-label"))
    parts.append(fate_destiny_chart())
    parts.append(text(LEFT + 800, 165, "Soarta: 3-8-0-0-1-9-6", "label"))
    parts.append(text(LEFT + 800, 190, "Destin: 3-8-2-0-1-7-6", "label"))
    parts.append(text(LEFT + 800, 215, "Puncte comune: 0, 10, 30, 40, 60 ani", "label"))
    parts.append(text(LEFT + 800, 240, "Rascruce vizibila: 20 si 50 ani", "label"))

    parts.append(text(70, 525, "Pinacluri", "section-label"))
    for start, end, title, detail in pinacles:
        parts.append(band(500, start, min(end, END_AGE), "pinacle", title, detail))

    parts.append(text(70, 625, "Ciclul 12 ani", "section-label"))
    for start, end, title, years, theme in c12:
        parts.append(band(600, start, end, "cycle12", f"{title} {years}", theme))
    for age, year in jupiter:
        parts.append(marker(age, 588, 670, "jupiter", f"{age}", year))

    parts.append(text(70, 725, "Ciclul 7 ani", "section-label"))
    for start, end, title, crisis, pair in c7:
        parts.append(band(700, start, end, "cycle7", f"{title} {start}-{end}", pair, min_label=70))
        crisis_age = start + 3.5
        parts.append(marker(crisis_age, 690, 770, "crisis", f"{crisis_age:g}", crisis.split(" / ")[-1]))

    parts.append(text(70, 855, "Ciclul 9 ani", "section-label"))
    for age, year, personal, lesson in c9:
        parts.append(band(830, age, age + 1, "cycle9", str(year), f"AP {personal} / L {lesson}", min_label=10))
    parts.append(text(x(28), 910, "interval calculat explicit in lucrare: 2026-2036", "label"))

    parts.append(text(70, 995, "Ani importanti", "section-label"))
    for age, year, kind in important:
        parts.append(marker(age, 960, 1080, "important", f"{year}", f"{age} ani / {kind}"))

    parts.append(text(70, 1160, "Citire sintetica", "section-label"))
    notes = [
        "28-35 ani: suprapunere activa intre pinaclul 1 spre 2, ciclul 7 C5, ciclul 12 C3 si anii personali 2026-2033.",
        "2029 / 31,5 ani: criza ciclului de 7 ani cade in intervalul de schimbare din ciclul de 9 ani.",
        "2034 / 36 ani: prag comun important; se intalnesc ciclul de 9 ani, ciclul de 12 ani si anul interior/exterior.",
        "Linia destinului nu inlocuieste ciclurile; ea este baza peste care se citesc ritmurile de maturizare si oportunitate.",
    ]
    for i, note in enumerate(notes):
        parts.append(text(LEFT, 1160 + i * 30, note, "label"))

    legend_x = 1660
    legend_y = 1145
    parts.append(rect(legend_x, legend_y, 620, 210, "panel", 14))
    parts.append(text(legend_x + 25, legend_y + 35, "Legenda", "legend-title"))
    legend = [
        ("#c56f2d", "Linia Soartei"),
        ("#0f6a70", "Linia Destinului"),
        ("#f2c14e", "Pinacluri: oportunitate / provocare"),
        ("#9cc9c1", "Cicluri de 12 ani"),
        ("#d9b6df", "Cicluri de 7 ani si crize"),
        ("#f7a072", "Ani personali in ciclul de 9 ani"),
        ("#263b8f", "Ani importanti interiori / exteriori"),
    ]
    for i, (color, label) in enumerate(legend):
        yy = legend_y + 65 + i * 20
        parts.append(f'<rect x="{legend_x + 25}" y="{yy - 11}" width="16" height="16" rx="3" fill="{color}"/>')
        parts.append(text(legend_x + 52, yy + 2, label, "legend-text"))

    parts.append(text(2290, 1428, "Atlas Numerologie", "axis-label", "end"))
    parts.append("</svg>\n")

    OUT.write_text("\n".join(parts), encoding="utf-8")


if __name__ == "__main__":
    main()
