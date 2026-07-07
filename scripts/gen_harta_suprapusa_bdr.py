from pathlib import Path


OUT = Path("output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/harta-suprapusa-soarta-destin-birsan-daniel-robert.svg")

WIDTH = 1900
HEIGHT = 1080
LEFT = 270
RIGHT = 410
TOP = 245
CHART_H = 430
CHART_W = WIDTH - LEFT - RIGHT
CHART_BOTTOM = TOP + CHART_H
START_AGE = 0
END_AGE = 108

GREEN = "#22b14c"
RED = "#ff1616"
ORANGE = "#ff9800"
BLUE = "#1f8fbf"
OPPORTUNITY = "#8e44ad"
PINACLE = "#b9a44a"
PAPER = "#f7efe3"
GRID = "#c9d0d2"


def esc(value):
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def x(age):
    return LEFT + (age - START_AGE) / (END_AGE - START_AGE) * CHART_W


def y(value):
    return CHART_BOTTOM - (value / 9) * CHART_H


def digit_sum(value):
    return sum(int(char) for char in str(value))


def numerological_reduce(value):
    while value > 9:
        value = digit_sum(value)
    return value


def important_years(birth_year, end_year, mode):
    years = []
    current = birth_year
    while True:
        step = numerological_reduce(current) if mode == "interior" else digit_sum(current)
        current += step
        if current > end_year:
            break
        years.append((current - birth_year, str(current)))
    return years


def point_label_position(xp, yp, value, side):
    if xp <= LEFT + 18:
        side = "right"
    elif xp >= LEFT + CHART_W - 18:
        side = "left"

    dx = -18 if side == "left" else 18
    anchor = "end" if side == "left" else "start"

    if value >= 8:
        dy = 26
    elif value <= 1:
        dy = -16
    else:
        dy = 26 if side == "right" else -18

    label_x = xp + dx
    label_y = yp + dy
    label_y = max(TOP + 18, min(CHART_BOTTOM - 8, label_y))
    return label_x, label_y, anchor


def meet_label_positions(xp, yp, value):
    if xp <= LEFT + 18:
        return (
            (xp + 18, max(TOP + 18, yp - 18), "start"),
            (xp + 18, min(CHART_BOTTOM - 8, yp + 28), "start"),
        )
    if xp >= LEFT + CHART_W - 18:
        return (
            (xp - 18, max(TOP + 18, yp - 18), "end"),
            (xp - 18, min(CHART_BOTTOM - 8, yp + 28), "end"),
        )
    if value >= 8:
        return ((xp - 18, yp + 26, "end"), (xp + 18, yp + 26, "start"))
    if value <= 1:
        return ((xp - 18, yp - 16, "end"), (xp + 18, yp - 16, "start"))
    return ((xp - 18, yp - 18, "end"), (xp + 18, yp + 28, "start"))


def text(xp, yp, value, cls="label", anchor="start", extra=""):
    return f'<text class="{cls}" x="{xp:.1f}" y="{yp:.1f}" text-anchor="{anchor}"{extra}>{esc(value)}</text>'


def line(x1, y1, x2, y2, cls="grid", extra=""):
    return f'<line class="{cls}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{extra}/>'


def rect(xp, yp, w, h, cls, rx=6, extra=""):
    return f'<rect class="{cls}" x="{xp:.1f}" y="{yp:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}"{extra}/>'


def circle(xp, yp, r, cls, extra=""):
    return f'<circle class="{cls}" cx="{xp:.1f}" cy="{yp:.1f}" r="{r}"{extra}/>'


def down_triangle(xp, yp, size, cls):
    half = size / 2
    points = f"{xp - half:.1f},{yp - half:.1f} {xp + half:.1f},{yp - half:.1f} {xp:.1f},{yp + half:.1f}"
    return f'<polygon class="{cls}" points="{points}"/>'


def down_triangle_points(xp, yp, size):
    half = size / 2
    return f"{xp - half:.1f},{yp - half:.1f} {xp + half:.1f},{yp - half:.1f} {xp:.1f},{yp + half:.1f}"


def up_triangle(xp, yp, size, cls):
    half = size / 2
    points = f"{xp - half:.1f},{yp + half:.1f} {xp + half:.1f},{yp + half:.1f} {xp:.1f},{yp - half:.1f}"
    return f'<polygon class="{cls}" points="{points}"/>'


def up_triangle_points(xp, yp, size):
    half = size / 2
    return f"{xp - half:.1f},{yp + half:.1f} {xp + half:.1f},{yp + half:.1f} {xp:.1f},{yp - half:.1f}"


def pill(age, y_pos, width_age, label, detail, cls):
    x1 = x(age)
    x2 = x(min(age + width_age, END_AGE))
    w = max(30, x2 - x1 - 3)
    parts = [rect(x1 + 1.5, y_pos, w, 30, cls, 7)]
    if w > 82:
        parts.append(text(x1 + w / 2, y_pos + 13, label, "pill-title", "middle"))
        parts.append(text(x1 + w / 2, y_pos + 25, detail, "pill-detail", "middle"))
    else:
        parts.append(text(x1 + w / 2, y_pos + 20, label, "pill-title", "middle"))
    return "\n".join(parts)


def interval_pill(start_age, end_age, y_pos, label, detail, cls):
    x1 = x(start_age)
    x2 = x(min(end_age, END_AGE))
    w = max(30, x2 - x1 - 3)
    parts = [rect(x1 + 1.5, y_pos, w, 30, cls, 7)]
    if w > 82:
        parts.append(text(x1 + w / 2, y_pos + 13, label, "pill-title", "middle"))
        parts.append(text(x1 + w / 2, y_pos + 25, detail, "pill-detail", "middle"))
    else:
        parts.append(text(x1 + w / 2, y_pos + 20, label, "pill-title", "middle"))
    return "\n".join(parts)


def vertical_marker(age, color_cls, y_start, label, below=None, top_to_axis=True):
    xp = x(age)
    parts = []
    if top_to_axis:
        parts.append(line(xp, TOP, xp, y_start, color_cls))
    else:
        parts.append(line(xp, y_start, xp, CHART_BOTTOM + 25, color_cls))
    parts.append(circle(xp, y_start, 4, f"{color_cls}-dot"))
    parts.append(text(xp, y_start - 8, label, f"{color_cls}-label", "middle"))
    if below:
        parts.append(text(xp, y_start + 16, below, f"{color_cls}-small", "middle"))
    return "\n".join(parts)


def cycle7_top_marker(age, label):
    xp = x(age)
    marker_y = TOP - 72
    triangle_center_y = marker_y
    triangle_size = 22
    triangle_tip_y = triangle_center_y + triangle_size / 2
    year = 1998 + age
    year_y = (triangle_tip_y + TOP) / 2
    parts = [
        line(xp, triangle_tip_y, xp, CHART_BOTTOM, "orange cycle7-line", ' stroke-dasharray="7 7"'),
        down_triangle(xp, triangle_center_y, triangle_size, "cycle7-triangle"),
        text(xp, triangle_center_y - 16, age, "crisis-top-label", "middle"),
        text(xp, triangle_center_y - 5, label, "triangle-number", "middle"),
        text(xp - 5, year_y, year, "cycle7-year", "middle", f' transform="rotate(-90 {xp - 5:.1f} {year_y:.1f})"'),
    ]
    return "\n".join(parts)


def crisis_top_marker(age, label):
    xp = x(age)
    marker_y = TOP - 72
    triangle_center_y = marker_y
    triangle_size = 22
    triangle_tip_y = triangle_center_y + triangle_size / 2
    parts = [
        line(xp, triangle_tip_y, xp, CHART_BOTTOM, "crisis", ' stroke-dasharray="6 6"'),
        up_triangle(xp, triangle_center_y, triangle_size, "crisis-triangle"),
        text(xp, triangle_center_y - 16, label, "crisis-top-label", "middle"),
    ]
    return "\n".join(parts)


def chart():
    fate = [3, 8, 0, 0, 1, 9, 6]
    destiny = [3, 8, 2, 0, 1, 7, 6]
    ages = list(range(0, 101, 10)) + [END_AGE]
    fate_values = [fate[i % len(fate)] for i in range(len(ages))]
    destiny_values = [destiny[i % len(destiny)] for i in range(len(ages))]
    parts = []

    for value in range(10):
        yy = y(value)
        cls = "grid major-y" if value in (0, 9) else "grid"
        parts.append(line(LEFT, yy, LEFT + CHART_W, yy, cls))
        parts.append(text(LEFT - 20, yy + 5, value, "axis-y", "end"))

    for age in list(range(0, 101, 10)) + [END_AGE]:
        xp = x(age)
        parts.append(line(xp, TOP, xp, CHART_BOTTOM, "grid major-x" if age % 20 == 0 else "grid"))
        parts.append(text(xp, CHART_BOTTOM + 24, age, "axis-x", "middle"))

    parts.append(line(LEFT, TOP, LEFT, CHART_BOTTOM, "axis"))
    parts.append(line(LEFT, CHART_BOTTOM, LEFT + CHART_W, CHART_BOTTOM, "axis"))
    parts.append(line(LEFT + CHART_W, TOP, LEFT + CHART_W, CHART_BOTTOM, "axis-light"))

    comfort = 27 / 7
    cy = y(comfort)
    parts.append(line(LEFT, cy - 3, LEFT + CHART_W, cy - 3, "comfort comfort-green"))
    parts.append(line(LEFT, cy + 3, LEFT + CHART_W, cy + 3, "comfort comfort-red"))

    fate_points = " ".join(f"{x(age):.1f},{y(value):.1f}" for age, value in zip(ages, fate_values))
    destiny_points = " ".join(f"{x(age):.1f},{y(value):.1f}" for age, value in zip(ages, destiny_values))
    parts.append(f'<polyline class="fate-line" points="{fate_points}"/>')
    parts.append(f'<polyline class="destiny-line" points="{destiny_points}"/>')

    for age, fv, dv in zip(ages, fate_values, destiny_values):
        xp = x(age)
        fy = y(fv)
        dy = y(dv)
        if fv == dv:
            parts.append(circle(xp, fy, 8, "meet-dot"))
            fate_label, destiny_label = meet_label_positions(xp, fy, fv)
            parts.append(text(fate_label[0], fate_label[1], fv, "point-value green-text", fate_label[2]))
            parts.append(text(destiny_label[0], destiny_label[1], dv, "point-value red-text", destiny_label[2]))
        else:
            parts.append(circle(xp, fy, 7, "fate-dot"))
            label_x, label_y, label_anchor = point_label_position(xp, fy, fv, "left")
            parts.append(text(label_x, label_y, fv, "point-value green-text", label_anchor))
            parts.append(circle(xp, dy, 7, "destiny-dot"))
            label_x, label_y, label_anchor = point_label_position(xp, dy, dv, "right")
            parts.append(text(label_x, label_y, dv, "point-value red-text", label_anchor))

    return "\n".join(parts)


def pinacle_lines(pinacles):
    parts = []

    def step_path(value_index):
        commands = []
        for idx, item in enumerate(pinacles):
            start, end, _label, opportunity, challenge = item
            value = (opportunity, challenge)[value_index]
            if idx == 0:
                commands.append(f"M {x(start):.1f} {y(value):.1f}")
            commands.append(f"H {x(end):.1f}")
            if idx < len(pinacles) - 1:
                next_value = (pinacles[idx + 1][3], pinacles[idx + 1][4])[value_index]
                commands.append(f"V {y(next_value):.1f}")
        return " ".join(commands)

    parts.append(f'<path class="opportunity-line" d="{step_path(0)}"/>')
    parts.append(f'<path class="challenge-line" d="{step_path(1)}"/>')

    for item in pinacles:
        start, end, label, opportunity, challenge = item
        mid = (start + end) / 2

        parts.append(circle(x(mid), y(opportunity), 4, "opportunity-dot"))
        parts.append(circle(x(mid), y(challenge), 4, "challenge-dot"))
        parts.append(text(x(mid), y(opportunity) - 9, f"O{opportunity}", "opportunity-label", "middle"))
        parts.append(text(x(mid), y(challenge) + 15, f"P{challenge}", "challenge-label", "middle"))

    return "\n".join(parts)


def main():
    birth_year = 1998
    end_year = birth_year + END_AGE
    c7 = [
        (0, "C1", "0-7"), (7, "C2", "7-14"), (14, "C3", "14-21"), (21, "C4", "21-28"),
        (28, "C5", "28-35"), (35, "C6", "35-42"), (42, "C7", "42-49"), (49, "C8", "49-56"),
        (56, "C9", "56-63"), (63, "C10", "63-70"), (70, "C11", "70-77"), (77, "C12", "77-84"),
        (84, "C13", "84-91"), (91, "C14", "91-98"), (98, "C15", "98-105"), (105, "C16", "105-108"),
    ]
    c9 = []
    for age in range(0, END_AGE, 9):
        start_year = 1998 + age
        c9_end_year = min(1998 + age + 8, 1998 + END_AGE - 1)
        c9.append((age, f"{start_year}-{c9_end_year}", f"{age}-{min(age + 9, END_AGE)}"))
    c12 = [(0, "C1", "1998-2009"), (12, "C2", "2010-2021"), (24, "C3", "2022-2033"),
           (36, "C4", "2034-2045"), (48, "C5", "2046-2057"), (60, "C6", "2058-2069"),
           (72, "C7", "2070-2081"), (84, "C8", "2082-2093"), (96, "C9", "2094-2105")]
    crises = [(3.5, "2001"), (10.5, "2008"), (17.5, "2015"), (24.5, "2022"), (31.5, "2029"),
              (38.5, "2036"), (45.5, "2043"), (52.5, "2050"), (59.5, "2057"), (66.5, "2064"),
              (73.5, "2071"), (80.5, "2078"), (87.5, "2085"), (94.5, "2092"), (101.5, "2099")]
    opportunities = [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]
    pinacles = [(0, 33, "P1", 3, 1), (34, 42, "P2", 1, 8), (43, 51, "P3", 4, 7), (52, 108, "P4", 2, 7)]
    interior = important_years(birth_year, end_year, "interior")
    exterior = important_years(birth_year, end_year, "exterior")

    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <title>Harta suprapusa soarta-destin-ciclicitati - Birsan Daniel Robert</title>
  <desc>Grafic suprapus cu Soarta, Destin, zona de confort, ani interior/exterior si cicluri de 7, 9 si 12 ani.</desc>
  <defs>
    <style>
      .bg {{ fill: {PAPER}; }}
      .title {{ font-family: Arial, Helvetica, sans-serif; font-size: 22px; font-weight: 800; fill: #293238; }}
      .subtitle {{ font-family: Arial, Helvetica, sans-serif; font-size: 15px; font-weight: 800; fill: #35434a; }}
      .label {{ font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-weight: 700; fill: #333; }}
      .axis-y {{ font-family: Arial, Helvetica, sans-serif; font-size: 16px; font-weight: 800; fill: #2b2119; }}
      .axis-x {{ font-family: Arial, Helvetica, sans-serif; font-size: 13px; font-weight: 700; fill: #222; }}
      .axis-name {{ font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: 900; fill: #2b2119; }}
      .grid {{ stroke: {GRID}; stroke-width: 1; stroke-dasharray: 6 4; }}
      .major-y, .major-x {{ stroke: #aeb7bb; stroke-width: 1.4; }}
      .axis {{ stroke: #111; stroke-width: 3; }}
      .axis-light {{ stroke: #111; stroke-width: 2; }}
      .comfort {{ stroke-width: 4; stroke-dasharray: 18 12; opacity: .75; }}
      .comfort-green {{ stroke: {GREEN}; }}
      .comfort-red {{ stroke: {RED}; }}
      .fate-line {{ fill: none; stroke: {GREEN}; stroke-width: 4; stroke-linecap: round; stroke-linejoin: round; }}
      .destiny-line {{ fill: none; stroke: {RED}; stroke-width: 4; stroke-linecap: round; stroke-linejoin: round; }}
      .fate-dot {{ fill: {GREEN}; stroke: #fff; stroke-width: 2; }}
      .destiny-dot {{ fill: {RED}; stroke: #fff; stroke-width: 2; }}
      .meet-dot {{ fill: #fff; stroke: #333; stroke-width: 2.5; }}
      .point-value {{ font-family: Arial, Helvetica, sans-serif; font-size: 15px; font-weight: 900; paint-order: stroke; stroke: #fff; stroke-width: 3px; }}
      .green-text {{ fill: {GREEN}; }}
      .red-text {{ fill: {RED}; }}
      .orange {{ stroke: {ORANGE}; stroke-width: 2; opacity: .72; }}
      .orange-dot {{ fill: {ORANGE}; }}
      .orange-label, .orange-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 800; fill: {ORANGE}; }}
      .cycle7-line {{ stroke-width: 1.4; opacity: .42; }}
      .cycle7-triangle {{ fill: {ORANGE}; stroke: {ORANGE}; stroke-width: 2; vector-effect: non-scaling-stroke; }}
      .cycle7-top-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: {ORANGE}; paint-order: stroke; stroke: #fff3de; stroke-width: 2px; }}
      .cycle7-year {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: {ORANGE}; paint-order: stroke; stroke: #fff3de; stroke-width: 2px; }}
      .triangle-number {{ font-family: Arial, Helvetica, sans-serif; font-size: 8.5px; font-weight: 900; fill: #fff; dominant-baseline: middle; alignment-baseline: middle; pointer-events: none; }}
      .interior {{ stroke: {RED}; stroke-width: 2.2; opacity: .78; }}
      .interior-dot {{ fill: {RED}; }}
      .interior-label, .interior-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 11px; font-weight: 900; fill: {RED}; }}
      .exterior {{ stroke: {GREEN}; stroke-width: 2.2; opacity: .78; }}
      .exterior-dot {{ fill: {GREEN}; }}
      .exterior-label, .exterior-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 11px; font-weight: 900; fill: {GREEN}; }}
      .year-link {{ stroke: #7a858c; stroke-width: 1.5; opacity: .62; stroke-dasharray: 4 4; }}
      .crisis {{ stroke: {ORANGE}; stroke-width: 1.8; opacity: .64; }}
      .crisis-dot {{ fill: {ORANGE}; }}
      .crisis-label, .crisis-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 800; fill: {ORANGE}; }}
      .crisis-triangle {{ fill: none; stroke: {ORANGE}; stroke-width: 2; vector-effect: non-scaling-stroke; }}
      .crisis-top-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: {ORANGE}; paint-order: stroke; stroke: #fff3de; stroke-width: 2px; }}
      .crisis-number {{ fill: {ORANGE}; stroke: #fff3de; stroke-width: 1.5px; paint-order: stroke; }}
      .pill-title {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: #222; }}
      .pill-detail {{ font-family: Arial, Helvetica, sans-serif; font-size: 9px; font-weight: 700; fill: #333; }}
      .pill7 {{ fill: #ff9800; stroke: #e07400; stroke-width: 1; }}
      .pill9 {{ fill: #ead3dc; stroke: #d59bb0; stroke-width: 1; }}
      .pill12 {{ fill: #cfe4f6; stroke: #98c6e8; stroke-width: 1; }}
      .pill-pinacle {{ fill: #efe4a8; stroke: {PINACLE}; stroke-width: 1; }}
      .opportunity-line {{ fill: none; stroke: {OPPORTUNITY}; stroke-width: 2.4; opacity: .82; }}
      .challenge-line {{ fill: none; stroke: {BLUE}; stroke-width: 2.4; opacity: .78; }}
      .opportunity-dot {{ fill: {OPPORTUNITY}; stroke: #fff; stroke-width: 1.5; }}
      .challenge-dot {{ fill: {BLUE}; stroke: #fff; stroke-width: 1.5; }}
      .opportunity-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: {OPPORTUNITY}; paint-order: stroke; stroke: #fff; stroke-width: 2px; }}
      .challenge-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: {BLUE}; paint-order: stroke; stroke: #fff; stroke-width: 2px; }}
      .row-label {{ font-family: Arial, Helvetica, sans-serif; font-size: 16px; font-weight: 800; }}
      .legend {{ font-family: Arial, Helvetica, sans-serif; font-size: 13px; font-weight: 800; fill: #222; }}
      .watermark {{ font-family: Arial, Helvetica, sans-serif; font-size: 14px; fill: #aaa; font-weight: 800; }}
    </style>
  </defs>''']
    parts.append(f'<rect class="bg" width="{WIDTH}" height="{HEIGHT}"/>')
    parts.append(text(95, 28, "Harta suprapusa soarta-destin-ciclicitati", "title"))
    parts.append(text(WIDTH - 160, 28, "BIRSAN DANIEL ROBERT", "title", "end"))
    parts.append(text(WIDTH - 160, 52, "19.02.1998 -> Soarta 3800196 -> Destin 3820176", "subtitle", "end"))

    # Cycle and crisis markers first, behind the chart lines.
    for age, label, _detail in c7:
        parts.append(cycle7_top_marker(age, label.replace("C", "")))
    for age, year in crises:
        parts.append(crisis_top_marker(age, f"{age:g}"))

    parts.append(chart())
    parts.append(pinacle_lines(pinacles))
    parts.append(text(LEFT + CHART_W / 2, CHART_BOTTOM + 45, "Ani", "axis-name", "middle"))
    parts.append(text(LEFT - 68, TOP + CHART_H / 2, "Vibrație", "axis-name", "middle", f' transform="rotate(-90 {LEFT - 68:.1f} {TOP + CHART_H / 2:.1f})"'))

    # Interior/exterior years above the cycle pills.
    row_label_x = LEFT - 36
    parts.append(text(row_label_x, CHART_BOTTOM + 103, "Ani interior", "row-label red-text", "end"))
    parts.append(text(row_label_x, CHART_BOTTOM + 132, "Ani exterior", "row-label green-text", "end"))
    interior_map = dict(interior)
    exterior_map = dict(exterior)
    for age in sorted(set(interior_map) | set(exterior_map)):
        xp = x(age)
        parts.append(line(xp, TOP, xp, CHART_BOTTOM + 130, "year-link"))
        if age in interior_map:
            label_x = xp - 5
            label_y = CHART_BOTTOM + 100
            parts.append(text(label_x, label_y, interior_map[age], "interior-label", "middle", f' transform="rotate(-90 {label_x:.1f} {label_y:.1f})"'))
        if age in exterior_map:
            label_x = xp + 5
            label_y = CHART_BOTTOM + 130
            parts.append(text(label_x, label_y, exterior_map[age], "exterior-label", "middle", f' transform="rotate(-90 {label_x:.1f} {label_y:.1f})"'))

    y9 = CHART_BOTTOM + 165
    y12 = CHART_BOTTOM + 208
    parts.append(text(row_label_x, y9 + 20, "Ciclu 9", "row-label", "end"))
    for age, years, detail in c9:
        parts.append(pill(age, y9, 9, years, detail, "pill9"))
    parts.append(text(row_label_x, y12 + 20, "Ciclu 12", "row-label", "end"))
    for age, label, detail in c12:
        parts.append(pill(age, y12, 12, label, detail, "pill12"))

    ypin = y12 + 37
    parts.append(text(row_label_x, ypin + 20, "Pinaclu", "row-label", "end"))
    previous_end = None
    for age, end, label, opportunity, challenge in pinacles:
        visual_start = age if previous_end is None else previous_end
        parts.append(interval_pill(visual_start, end, ypin, label, f"O{opportunity} / P{challenge}", "pill-pinacle"))
        previous_end = end

    legend_x = LEFT + CHART_W + 120
    legend_y = 390
    parts.append(text(legend_x, legend_y, "Legenda", "legend", "start"))
    legend_items = [
        (GREEN, "Soarta 3800196"),
        (RED, "Destin 3820176"),
        (GREEN, "Zona confort Soarta 3,86"),
        (RED, "Zona confort Destin 3,86"),
        (OPPORTUNITY, "Oportunitate"),
        (BLUE, "Provocare"),
        (RED, "An interior"),
        (GREEN, "An exterior"),
        (ORANGE, "Ciclu 7"),
        (ORANGE, "Criză ciclu 7"),
        ("#ead3dc", "Ciclu 9"),
        ("#cfe4f6", "Ciclu 12"),
        (PINACLE, "Pinaclu"),
    ]
    for i, (color, label) in enumerate(legend_items):
        yy = legend_y + 24 + i * 22
        if "Zona" in label:
            parts.append(f'<line x1="{legend_x}" y1="{yy}" x2="{legend_x + 22}" y2="{yy}" stroke="{color}" stroke-width="4" stroke-dasharray="8 5"/>')
        elif label == "Ciclu 7":
            parts.append(f'<polygon points="{down_triangle_points(legend_x + 9, yy - 1, 22)}" fill="{ORANGE}" stroke="{ORANGE}" stroke-width="2"/>')
        elif label == "Criză ciclu 7":
            parts.append(f'<polygon points="{up_triangle_points(legend_x + 9, yy - 1, 22)}" fill="none" stroke="{ORANGE}" stroke-width="2"/>')
        else:
            parts.append(f'<rect x="{legend_x}" y="{yy - 8}" width="18" height="12" rx="2" fill="{color}"/>')
        parts.append(text(legend_x + 30, yy + 4, label, "legend"))

    parts.append(text(WIDTH - 20, HEIGHT - 15, "Atlas Numerologie", "watermark", "end"))
    parts.append("</svg>\n")

    OUT.write_text("\n".join(parts), encoding="utf-8")


if __name__ == "__main__":
    main()
