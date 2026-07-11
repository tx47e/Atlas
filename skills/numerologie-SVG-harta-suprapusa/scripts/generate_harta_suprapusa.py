import argparse
from pathlib import Path

WIDTH = 1900
HEIGHT = 1080
LEFT = 270
RIGHT = 410
TOP = 135
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
CYCLE12 = "#6f9fbd"
LESSON = "#9fc9de"
CYCLE9 = "#7f2346"
INTERIOR_YEAR = "#5a4fb0"
EXTERIOR_YEAR = "#2f7f5f"
PAPER = "#f7efe3"
GRID = "#c9d0d2"
MARKER_COUNTS = {}
DATA = {}


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


def parse_birth_date(value):
    parts = value.strip().replace("/", ".").replace("-", ".").split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        raise ValueError("Data nasterii trebuie sa fie in forma ZZ.LL.AAAA.")
    day, month, year = (int(part) for part in parts)
    if not 1 <= day <= 31 or not 1 <= month <= 12 or year < 1:
        raise ValueError("Data nasterii nu este valida.")
    return day, month, year


def harta_data(name, birth_date):
    day, month, birth_year = parse_birth_date(birth_date)
    base_text = f"{day:02d}{month:02d}"
    destiny_base_text = base_text.replace("0", "1")
    destiny_year_text = str(birth_year).replace("0", "1")
    fate_number = str(int(base_text) * birth_year).zfill(7)
    destiny_number = str(int(destiny_base_text) * int(destiny_year_text)).zfill(7)
    fate_digits = [int(digit) for digit in fate_number]
    destiny_digits = [int(digit) for digit in destiny_number]
    vi = numerological_reduce(day)
    ve = numerological_reduce(month)
    destin = numerological_reduce(day + month + birth_year)
    year_digit = numerological_reduce(birth_year)
    opportunities = [
        numerological_reduce(ve + vi),
        numerological_reduce(vi + year_digit),
        0,
        numerological_reduce(ve + year_digit),
    ]
    opportunities[2] = numerological_reduce(opportunities[0] + opportunities[1])
    challenges = [abs(vi - ve), abs(vi - year_digit), 0, abs(ve - year_digit)]
    challenges[2] = abs(challenges[0] - challenges[1])
    p1_end = 36 - destin
    p2_end = p1_end + 9
    p3_end = p2_end + 9
    return {
        "name": name,
        "birth_date": f"{day:02d}.{month:02d}.{birth_year:04d}",
        "birth_year": birth_year,
        "fate_number": fate_number,
        "destiny_number": destiny_number,
        "fate_digits": fate_digits,
        "destiny_digits": destiny_digits,
        "comfort_fate": sum(fate_digits) / 7,
        "comfort_destiny": sum(destiny_digits) / 7,
        "life_digits": [int(digit) for digit in str(day * month * birth_year)],
        "life_product": day * month * birth_year,
        "pinacles": [
            (0, p1_end, "P1", opportunities[0], challenges[0]),
            (p1_end + 1, p2_end, "P2", opportunities[1], challenges[1]),
            (p2_end + 1, p3_end, "P3", opportunities[2], challenges[2]),
            (p3_end + 1, END_AGE, "P4", opportunities[3], challenges[3]),
        ],
    }


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


def marker_width(age, base=1.4):
    count = MARKER_COUNTS.get(age, 1)
    return base + max(0, count - 1) * 0.65


def marker_stroke_extra(age, base=1.4, extra=""):
    return f' stroke-width="{marker_width(age, base):.2f}"{extra}'


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


def square(xp, yp, size, cls):
    half = size / 2
    return f'<rect class="{cls}" x="{xp - half:.1f}" y="{yp - half:.1f}" width="{size:.1f}" height="{size:.1f}" rx="2"/>'


def bottom_square_marker(age, label, year, row_y, line_cls, square_cls, number_cls, year_cls):
    xp = x(age)
    size = 24
    square_top = row_y - size / 2
    year_y = square_top - 18
    year_x = xp - 6
    return "\n".join([
        bottom_marker_line(age, row_y, line_cls),
        bottom_square_label(age, label, year, row_y, square_cls, number_cls, year_cls),
    ])


def bottom_marker_line(age, row_y, line_cls, through_chart=False):
    xp = x(age)
    size = 24
    square_top = row_y - size / 2
    y_start = TOP if through_chart else CHART_BOTTOM
    return line(xp, y_start, xp, square_top, line_cls, marker_stroke_extra(age, 1.4))


def bottom_square_label(age, label, year, row_y, square_cls, number_cls, year_cls):
    xp = x(age)
    size = 24
    square_top = row_y - size / 2
    year_y = square_top - 18
    year_x = xp - 6
    return "\n".join([
        square(xp, row_y, size, square_cls),
        text(xp, row_y + 0.5, label, number_cls, "middle"),
        text(year_x, year_y, year, year_cls, "middle", f' transform="rotate(-90 {year_x:.1f} {year_y:.1f})"'),
    ])


def stagger_year_labels(ages, base_y, close_gap=3, step=22):
    lanes = []
    result = {}
    for age in sorted(ages):
        lane_index = None
        for index, last_age in enumerate(lanes):
            if age - last_age > close_gap:
                lane_index = index
                lanes[index] = age
                break
        if lane_index is None:
            lane_index = len(lanes)
            lanes.append(age)
        result[age] = base_y + lane_index * step
    return result, max(0, (len(lanes) - 1) * step)


def pinacle_bridges(pinacles, row_y):
    parts = []
    size = 24
    top_y = row_y - 6
    bottom_y = row_y + 6
    label_gap = 11
    for index, current in enumerate(pinacles):
        start, _end, _label, opportunity, challenge = current
        next_start = pinacles[index + 1][0] if index < len(pinacles) - 1 else END_AGE
        x1 = x(start) + size / 2
        x2 = x(next_start) - (size / 2 if index < len(pinacles) - 1 else 0)
        mid = (x1 + x2) / 2
        if opportunity >= challenge:
            opportunity_y = top_y
            challenge_y = bottom_y
            opportunity_label_y = opportunity_y - label_gap
            challenge_label_y = challenge_y + label_gap + 4
        else:
            challenge_y = top_y
            opportunity_y = bottom_y
            challenge_label_y = challenge_y - label_gap
            opportunity_label_y = opportunity_y + label_gap + 4

        parts.append(f'<line class="pinacle-opportunity-bridge" x1="{x1:.1f}" y1="{opportunity_y:.1f}" x2="{x2:.1f}" y2="{opportunity_y:.1f}"/>')
        parts.append(f'<line class="pinacle-challenge-bridge" x1="{x1:.1f}" y1="{challenge_y:.1f}" x2="{x2:.1f}" y2="{challenge_y:.1f}"/>')
        parts.append(text(mid, opportunity_label_y, f"O{opportunity}", "opportunity-label", "middle"))
        parts.append(text(mid, challenge_label_y, f"P{challenge}", "challenge-label", "middle"))
    return "\n".join(parts)


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
    year = DATA["birth_year"] + age
    year_y = (triangle_tip_y + TOP) / 2
    parts = [
        line(xp, triangle_tip_y, xp, CHART_BOTTOM, "orange cycle7-line", marker_stroke_extra(age, 1.4, ' stroke-dasharray="7 7"')),
        down_triangle(xp, triangle_center_y, triangle_size, "cycle7-triangle"),
        text(xp, triangle_center_y - 5, label, "triangle-number", "middle"),
        text(xp - 5, year_y, year, "cycle7-year", "middle", f' transform="rotate(-90 {xp - 5:.1f} {year_y:.1f})"'),
    ]
    return "\n".join(parts)


def cycle9_top_marker(age, label):
    xp = x(age)
    marker_center_y = TOP - 155
    marker_size = 24
    marker_bottom_y = marker_center_y + marker_size / 2
    year = DATA["birth_year"] + age
    year_y = marker_bottom_y + 30
    parts = [
        line(xp, marker_bottom_y, xp, CHART_BOTTOM, "cycle9-line", marker_stroke_extra(age, 1.4, ' stroke-dasharray="4 7"')),
        square(xp, marker_center_y, marker_size, "cycle9-square"),
        text(xp, marker_center_y, label, "triangle-number cycle9-number", "middle"),
        text(xp - 5, year_y, year, "cycle9-year", "middle", f' transform="rotate(-90 {xp - 5:.1f} {year_y:.1f})"'),
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
    ]
    return "\n".join(parts)


def cycle7_bottom_line(age, row_y):
    xp = x(age)
    triangle_top = row_y - 12
    return line(xp, TOP, xp, triangle_top, "orange cycle7-line", marker_stroke_extra(age, 1.4, ' stroke-dasharray="7 7"'))


def crisis_bottom_line(age, row_y):
    xp = x(age)
    triangle_top = row_y - 12
    return line(xp, TOP, xp, triangle_top, "crisis", marker_stroke_extra(age, 1.4, ' stroke-dasharray="6 6"'))


def cycle7_bottom_marker(age, label, row_y):
    xp = x(age)
    year = DATA["birth_year"] + age
    year_y = row_y - 30
    return "\n".join([
        down_triangle(xp, row_y, 24, "cycle7-triangle"),
        text(xp, row_y - 5, label, "triangle-number", "middle"),
        text(xp - 6, year_y, year, "cycle7-year", "middle", f' transform="rotate(-90 {xp - 6:.1f} {year_y:.1f})"'),
    ])


def crisis_bottom_marker(age, row_y):
    xp = x(age)
    year = int(DATA["birth_year"] + age)
    year_y = row_y - 30
    return "\n".join([
        up_triangle(xp, row_y, 24, "crisis-triangle"),
        text(xp - 6, year_y, year, "crisis-top-label", "middle", f' transform="rotate(-90 {xp - 6:.1f} {year_y:.1f})"'),
    ])


def life_lesson_line():
    series = DATA["life_digits"]
    points = []
    for age in range(START_AGE, END_AGE + 1):
        life_year = age + 1
        value = series[(life_year - 1) % len(series)]
        points.append(f"{x(age):.1f},{y(value):.1f}")
    return '<polyline class="lesson-line" points="' + " ".join(points) + '"/>'


def chart():
    fate = DATA["fate_digits"]
    destiny = DATA["destiny_digits"]
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

    parts.append(line(LEFT, y(DATA["comfort_fate"]), LEFT + CHART_W, y(DATA["comfort_fate"]), "comfort comfort-green"))
    parts.append(line(LEFT, y(DATA["comfort_destiny"]), LEFT + CHART_W, y(DATA["comfort_destiny"]), "comfort comfort-red"))

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
        else:
            parts.append(circle(xp, fy, 7, "fate-dot"))
            parts.append(circle(xp, dy, 7, "destiny-dot"))

    return "\n".join(parts)


def fate_destiny_rows(row_label_x):
    fate = DATA["fate_digits"]
    destiny = DATA["destiny_digits"]
    intervals = list(range(0, 101, 10))
    fate_y = CHART_BOTTOM + 48
    destiny_y = CHART_BOTTOM + 70
    parts = [
        text(row_label_x, fate_y, "Soartă", "row-label green-text", "end"),
        text(row_label_x, destiny_y, "Destin", "row-label red-text", "end"),
    ]
    for index, start_age in enumerate(intervals):
        mid_age = start_age + 5
        parts.append(text(x(mid_age), fate_y, fate[index % len(fate)], "point-value green-text", "middle"))
        parts.append(text(x(mid_age), destiny_y, destiny[index % len(destiny)], "point-value red-text", "middle"))
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
    global DATA, END_AGE, MARKER_COUNTS
    parser = argparse.ArgumentParser(description="Genereaza Harta Suprapusa Soarta-Destin.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--birth-date", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--end-age", type=int, default=108)
    args = parser.parse_args()
    if args.end_age < 1:
        raise ValueError("Intervalul de varsta trebuie sa fie pozitiv.")
    END_AGE = args.end_age
    DATA = harta_data(args.name, args.birth_date)
    birth_year = DATA["birth_year"]
    end_year = birth_year + END_AGE
    c7 = [(age, f"C{index}", f"{age}-{min(age + 7, END_AGE)}") for index, age in enumerate(range(0, END_AGE + 1, 7), start=1)]
    c9 = []
    for age in range(0, END_AGE, 9):
        start_year = birth_year + age
        c9_end_year = min(birth_year + age + 8, birth_year + END_AGE - 1)
        c9.append((age, f"{start_year}-{c9_end_year}", f"{age}-{min(age + 9, END_AGE)}"))
    c12 = [(age, f"C{index}", f"{birth_year + age}-{min(birth_year + age + 11, birth_year + END_AGE - 1)}") for index, age in enumerate(range(0, END_AGE, 12), start=1)]
    crises = [(age, str(int(birth_year + age))) for age in (3.5 + index * 7 for index in range(0, END_AGE // 7 + 1)) if age < END_AGE]
    pinacles = DATA["pinacles"]
    interior = important_years(birth_year, end_year, "interior")
    exterior = important_years(birth_year, end_year, "exterior")
    marker_events = []
    marker_events.extend(age for age, _year in interior)
    marker_events.extend(age for age, _year in exterior)
    marker_events.extend(age for age, _label, _detail in c7)
    marker_events.extend(age for age, _years, _detail in c9)
    marker_events.extend(age for age, _label, _detail in c12)
    marker_events.extend(age for age, _end, _label, _opportunity, _challenge in pinacles)
    MARKER_COUNTS = {age: marker_events.count(age) for age in set(marker_events)}

    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <title>Harta suprapusa soarta-destin-ciclicitati - {esc(DATA["name"])}</title>
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
      .cycle9-line {{ stroke: {CYCLE9}; stroke-width: 1.4; opacity: .42; }}
      .cycle9-square {{ fill: {CYCLE9}; stroke: {CYCLE9}; stroke-width: 2; vector-effect: non-scaling-stroke; }}
      .cycle9-number {{ font-size: 10px; fill: #fff; }}
      .cycle9-year {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: {CYCLE9}; paint-order: stroke; stroke: #fff3de; stroke-width: 2px; }}
      .interior {{ stroke: {INTERIOR_YEAR}; stroke-width: 2.2; opacity: .78; }}
      .interior-dot {{ fill: {INTERIOR_YEAR}; }}
      .interior-label, .interior-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 11px; font-weight: 900; fill: {INTERIOR_YEAR}; }}
      .exterior {{ stroke: {EXTERIOR_YEAR}; stroke-width: 2.2; opacity: .78; }}
      .exterior-dot {{ fill: {EXTERIOR_YEAR}; }}
      .exterior-label, .exterior-small {{ font-family: Arial, Helvetica, sans-serif; font-size: 11px; font-weight: 900; fill: {EXTERIOR_YEAR}; }}
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
      .pinacle-line {{ stroke: {PINACLE}; stroke-width: 1.4; opacity: .62; stroke-dasharray: 4 6; }}
      .pinacle-square {{ fill: {PINACLE}; stroke: {PINACLE}; stroke-width: 2; }}
      .pinacle-number {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: #fffaf0; dominant-baseline: middle; alignment-baseline: middle; }}
      .pinacle-year {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: #6f5f18; paint-order: stroke; stroke: #fff3de; stroke-width: 2px; }}
      .pinacle-opportunity-bridge {{ stroke: {OPPORTUNITY}; stroke-width: 2.3; stroke-linecap: round; }}
      .pinacle-challenge-bridge {{ stroke: {BLUE}; stroke-width: 2.3; stroke-linecap: round; }}
      .cycle12-line {{ stroke: {CYCLE12}; stroke-width: 1.4; opacity: .52; stroke-dasharray: 4 6; }}
      .cycle12-square {{ fill: {CYCLE12}; stroke: {CYCLE12}; stroke-width: 2; }}
      .cycle12-number {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: #f5fbff; dominant-baseline: middle; alignment-baseline: middle; }}
      .cycle12-year {{ font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: 900; fill: #3e708f; paint-order: stroke; stroke: #fff3de; stroke-width: 2px; }}
      .opportunity-line {{ fill: none; stroke: {OPPORTUNITY}; stroke-width: 2.4; opacity: .82; }}
      .challenge-line {{ fill: none; stroke: {BLUE}; stroke-width: 2.4; opacity: .78; }}
      .lesson-line {{ fill: none; stroke: {LESSON}; stroke-width: 2.2; opacity: .82; stroke-linejoin: round; stroke-linecap: round; }}
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
    parts.append(text(WIDTH - 160, 28, DATA["name"].upper(), "title", "end"))
    parts.append(text(WIDTH - 160, 52, DATA["birth_date"], "subtitle", "end"))

    parts.append(chart())
    parts.append(life_lesson_line())
    parts.append(pinacle_lines(pinacles))
    parts.append(text(LEFT + CHART_W + 34, CHART_BOTTOM + 24, "Ani", "axis-name", "start"))
    parts.append(text(LEFT - 68, TOP + CHART_H / 2, "Vibrație", "axis-name", "middle", f' transform="rotate(-90 {LEFT - 68:.1f} {TOP + CHART_H / 2:.1f})"'))

    # Interior/exterior years above the cycle pills.
    row_label_x = LEFT - 36
    parts.append(fate_destiny_rows(row_label_x))
    interior_base_y = CHART_BOTTOM + 100
    exterior_base_y = CHART_BOTTOM + 130
    interior_map = dict(interior)
    exterior_map = dict(exterior)
    interior_lanes, interior_extra = stagger_year_labels(interior_map.keys(), interior_base_y)
    exterior_lanes, exterior_extra = stagger_year_labels(exterior_map.keys(), exterior_base_y)
    year_extra = max(interior_extra, exterior_extra)
    year_link_bottom = CHART_BOTTOM + 118 + year_extra
    parts.append(text(row_label_x, interior_base_y, "Ani interior", "row-label interior-label", "end"))
    parts.append(text(row_label_x, exterior_base_y, "Ani exterior", "row-label exterior-label", "end"))
    for age in sorted(set(interior_map) | set(exterior_map)):
        xp = x(age)
        parts.append(line(xp, TOP, xp, year_link_bottom, "year-link", marker_stroke_extra(age, 1.5)))
        if age in interior_map:
            label_x = xp - 5
            label_y = interior_lanes[age]
            parts.append(text(label_x, label_y, interior_map[age], "interior-label", "middle", f' transform="rotate(-90 {label_x:.1f} {label_y:.1f})"'))
        if age in exterior_map:
            label_x = xp + 12
            label_y = exterior_lanes[age]
            parts.append(text(label_x, label_y, exterior_map[age], "exterior-label", "middle", f' transform="rotate(-90 {label_x:.1f} {label_y:.1f})"'))

    y7 = exterior_base_y + 67 + year_extra
    y9 = y7 + 65
    y12 = y9 + 65
    ypin = y12 + 65
    for age, label, _detail in c7:
        parts.append(cycle7_bottom_line(age, y7))
    for age, year in crises:
        parts.append(crisis_bottom_line(age, y7))
    for index, (age, years, detail) in enumerate(c9, start=1):
        parts.append(bottom_marker_line(age, y9, "cycle9-line"))
    for age, label, detail in c12:
        parts.append(bottom_marker_line(age, y12, "cycle12-line", through_chart=True))
    for age, end, label, opportunity, challenge in pinacles:
        parts.append(bottom_marker_line(age, ypin, "pinacle-line", through_chart=True))
    for age, label, _detail in c7:
        parts.append(cycle7_bottom_marker(age, label.replace("C", ""), y7))
    for age, year in crises:
        parts.append(crisis_bottom_marker(age, y7))
    for index, (age, years, detail) in enumerate(c9, start=1):
        year = str(birth_year + age)
        parts.append(bottom_square_label(age, str(index), year, y9, "cycle9-square", "cycle9-number", "cycle9-year"))
    for age, label, detail in c12:
        year = str(birth_year + age)
        parts.append(bottom_square_label(age, label.replace("C", ""), year, y12, "cycle12-square", "cycle12-number", "cycle12-year"))
    parts.append(pinacle_bridges(pinacles, ypin))
    for age, end, label, opportunity, challenge in pinacles:
        year = str(birth_year + age)
        parts.append(bottom_square_label(age, label.replace("P", ""), year, ypin, "pinacle-square", "pinacle-number", "pinacle-year"))
    parts.append(text(row_label_x, ypin + 5, "Pinaclu", "row-label", "end"))
    parts.append(text(row_label_x, y7 + 5, "Ciclu 7", "row-label", "end"))
    parts.append(text(row_label_x, y9 + 5, "Ciclu 9", "row-label", "end"))
    parts.append(text(row_label_x, y12 + 5, "Ciclu 12", "row-label", "end"))

    legend_x = LEFT + CHART_W + 120
    legend_y = 390
    parts.append(text(legend_x, legend_y, "Legenda", "legend", "start"))
    legend_items = [
        (GREEN, "Soarta 3800196"),
        (RED, "Destin 3820176"),
        (GREEN, "Zona confort Soarta 3,86"),
        (RED, "Zona confort Destin 3,86"),
        (OPPORTUNITY, "Oportunitate " + "".join(str(pinacle[3]) for pinacle in pinacles)),
        (BLUE, "Provocare " + "".join(str(pinacle[4]) for pinacle in pinacles)),
        (LESSON, "Lecții de viață 75924"),
        (INTERIOR_YEAR, "An interior"),
        (EXTERIOR_YEAR, "An exterior"),
        (ORANGE, "Ciclu 7"),
        (ORANGE, "Criză ciclu 7"),
        (CYCLE9, "Ciclu 9"),
        (CYCLE12, "Ciclu 12"),
        (PINACLE, "Pinaclu"),
    ]
    legend_items = [
        (GREEN, f"Soarta {DATA['fate_number']}"),
        (RED, f"Destin {DATA['destiny_number']}"),
        (GREEN, f"Zona confort Soarta {DATA['comfort_fate']:.2f}"),
        (RED, f"Zona confort Destin {DATA['comfort_destiny']:.2f}"),
        (OPPORTUNITY, "Oportunitate " + "".join(str(pinacle[3]) for pinacle in pinacles)),
        (BLUE, "Provocare " + "".join(str(pinacle[4]) for pinacle in pinacles)),
        (LESSON, f"Lectii de viata {DATA['life_product']}"),
        (INTERIOR_YEAR, "An interior"),
        (EXTERIOR_YEAR, "An exterior"),
        (ORANGE, "Ciclu 7"),
        (ORANGE, "Criza ciclu 7"),
        (CYCLE9, "Ciclu 9"),
        (CYCLE12, "Ciclu 12"),
        (PINACLE, "Pinaclu"),
    ]
    for i, (color, label) in enumerate(legend_items):
        yy = legend_y + 24 + i * 22
        if "Zona" in label:
            parts.append(f'<line x1="{legend_x}" y1="{yy}" x2="{legend_x + 22}" y2="{yy}" stroke="{color}" stroke-width="4" stroke-dasharray="8 5"/>')
        elif label.startswith("Lectii") or label.startswith("Soarta") or label.startswith("Destin") or label in ("Oportunitate", "Provocare", "An interior", "An exterior"):
            dash = ' stroke-dasharray="4 4"' if label in ("An interior", "An exterior") else ""
            parts.append(f'<line x1="{legend_x}" y1="{yy}" x2="{legend_x + 24}" y2="{yy}" stroke="{color}" stroke-width="3"{dash}/>')
        elif label == "Criza ciclu 7":
            parts.append(f'<polygon points="{up_triangle_points(legend_x + 12, yy - 1, 24)}" fill="none" stroke="{ORANGE}" stroke-width="2"/>')
        elif label.startswith("Lecții") or label in ("Soarta 3800196", "Destin 3820176", "Oportunitate", "Provocare", "An interior", "An exterior"):
            dash = ' stroke-dasharray="4 4"' if label in ("An interior", "An exterior") else ""
            parts.append(f'<line x1="{legend_x}" y1="{yy}" x2="{legend_x + 24}" y2="{yy}" stroke="{color}" stroke-width="3"{dash}/>')
        elif label == "Ciclu 7":
            parts.append(f'<polygon points="{down_triangle_points(legend_x + 12, yy - 1, 24)}" fill="{ORANGE}" stroke="{ORANGE}" stroke-width="2"/>')
        elif label == "Criză ciclu 7":
            parts.append(f'<polygon points="{up_triangle_points(legend_x + 12, yy - 1, 24)}" fill="none" stroke="{ORANGE}" stroke-width="2"/>')
        elif label == "Ciclu 9":
            parts.append(f'<rect x="{legend_x}" y="{yy - 12}" width="24" height="24" rx="2" fill="{CYCLE9}" stroke="{CYCLE9}" stroke-width="2"/>')
        elif label == "Ciclu 12":
            parts.append(f'<rect x="{legend_x}" y="{yy - 12}" width="24" height="24" rx="2" fill="{CYCLE12}" stroke="{CYCLE12}" stroke-width="2"/>')
        elif label == "Pinaclu":
            parts.append(f'<rect x="{legend_x}" y="{yy - 12}" width="24" height="24" rx="2" fill="{PINACLE}" stroke="{PINACLE}" stroke-width="2"/>')
        else:
            parts.append(f'<rect x="{legend_x}" y="{yy - 8}" width="18" height="12" rx="2" fill="{color}"/>')
        parts.append(text(legend_x + 30, yy + 4, label, "legend"))

    parts.append(text(WIDTH - 20, HEIGHT - 15, "Atlas Numerologie", "watermark", "end"))
    parts.append("</svg>\n")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(parts), encoding="utf-8", newline="\n")
    print(f"Generated: {args.output}")


if __name__ == "__main__":
    main()
