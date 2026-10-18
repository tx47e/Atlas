"""Reproduce Alina's charts exclusively through the approved skill generators."""
from pathlib import Path
import importlib.util
import sys
import json
from dataclasses import asdict
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/lucrari/1994-07-25-DANGULEA-ALINA-MONICA'
NAME, DATE = 'Dangulea Alina Monica', '25.07.1994'

def module(skill, script):
    spec = importlib.util.spec_from_file_location(script, ROOT / 'skills' / skill / 'scripts' / (script + '.py'))
    result = importlib.util.module_from_spec(spec)
    sys.modules[script] = result
    spec.loader.exec_module(result)
    return result

def all_dicts(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from all_dicts(item)
    elif isinstance(value, list):
        for item in value:
            yield from all_dicts(item)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    calc = json.loads(next(OUT.glob('*calculator.json')).read_text(encoding='utf-8-sig'))
    nodes = list(all_dicts(calc))
    matrices = [n['casute'] for n in nodes if 'casute' in n and isinstance(n['casute'], dict)]
    report = {}
    for key, skill, script, label in [
        ('date', 'numerologie-SVG-matrita-datei-de-nastere', 'generate_matrita_datei_de_nastere', 'matrita-datei'),
        ('name', 'numerologie-SVG-matrita-numelui', 'generate_matrita_numelui', 'matrita-numelui'),
    ]:
        generator = module(skill, script)
        svg, meta = generator.build_svg(NAME, DATE)
        component, _ = generator.build_html_component(NAME, DATE)
        ET.fromstring(svg)
        assert 'Atlas Numerologie' in svg
        assert component.count('class="matrix-cell ') == 9
        counts = {str(d): meta['counts'].get(d, 0) for d in range(1, 10)}
        assert any(all(m[str(d)]['cantitate'] == counts[str(d)] for d in range(1, 10)) for m in matrices)
        (OUT / (label + '-dangulea-alina-monica.svg')).write_text(svg, encoding='utf-8')
        (OUT / (label + '-dangulea-alina-monica-component.html')).write_text(component, encoding='utf-8')
        report[key] = meta
    fate = module('numerologie-SVG-soarta-si-destin', 'generate_soarta_si_destin')
    data = fate.calculate(NAME, DATE)
    svg = fate.svg_text(data)
    ET.fromstring(svg)
    assert 'Atlas Numerologie' in svg
    (OUT / 'soarta-si-destin-dangulea-alina-monica.svg').write_text(svg, encoding='utf-8')
    report['soarta_si_destin'] = asdict(data)
    # Read positions from the generator's piecewise-linear chart, not a new numerology formula.
    age = 32
    index = next(i for i in range(6) if data.ages[i] <= age <= data.ages[i + 1])
    fraction = (age - data.ages[index]) / data.interval
    chart_values = lambda code: int(code[index]) + fraction * (int(code[index + 1]) - int(code[index]))
    crossings = set()
    for i in range(6):
        left = int(data.fate[i]) - int(data.destiny[i])
        right = int(data.fate[i + 1]) - int(data.destiny[i + 1])
        if left == 0:
            crossings.add(float(data.ages[i]))
        if right == 0:
            crossings.add(float(data.ages[i + 1]))
        if left * right < 0:
            crossings.add(data.ages[i] + data.interval * (-left) / (right - left))
    report['chart_reading'] = {
        'method': 'Linear interpolation of the points returned by the approved chart generator',
        'age': age, 'fate': chart_values(data.fate), 'destiny': chart_values(data.destiny),
        'intersection_ages': sorted(crossings),
    }
    scale = module('numerologie-SVG-scara-bunastarii', 'generate_scara_bunastarii')
    born = scale.parse_birth_date(DATE)
    ladder = scale.calculate(born)
    svg = scale.render_svg(NAME, born, ladder)
    ET.fromstring(svg)
    assert 'Atlas Numerologie' in svg
    assert len(ladder['rows']) == 17
    assert [r['value'] for r in ladder['rows']] == sorted([r['value'] for r in ladder['rows']], reverse=True)
    assert any(n.get('scara_bunastarii') and sorted(r['valoare'] for r in n['scara_bunastarii']) == sorted(r['value'] for r in ladder['rows']) for n in nodes)
    (OUT / 'scara-bunastarii-dangulea-alina-monica.svg').write_text(svg, encoding='utf-8')
    report['scara_bunastarii'] = ladder
    (OUT / 'graphics-numeric-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print('GRAPHICS_XML_COUNTS_LADDER_OK')

if __name__ == '__main__':
    main()
