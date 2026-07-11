#!/usr/bin/env python3
"""Generate a Semnatura Astrala SVG from a name and a birth date."""
from __future__ import annotations
import argparse, html, re
from collections import Counter
from pathlib import Path

POINTS = {1:(60,60),4:(180,60),7:(300,60),2:(60,180),5:(180,180),8:(300,180),3:(60,300),6:(180,300),9:(300,300)}
GRID = '''<rect x="0" y="0" width="360" height="360" fill="#fffdf8" stroke="#7a6558" stroke-width="3"/><path d="M120 0V360M240 0V360M0 120H360M0 240H360" stroke="#c6b7aa" stroke-width="2" fill="none"/>'''
GRID += ''.join(f'<text x="{x}" y="{y+12}" text-anchor="middle" font-family="Georgia,serif" font-size="38" fill="#7a6558">{n}</text>' for n,(x,y) in POINTS.items())
def reduce(n:int)->int:
    while n>9:n=sum(map(int,str(n)))
    return n
def main()->int:
    p=argparse.ArgumentParser();p.add_argument('--name',required=True);p.add_argument('--birth-date',required=True);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    m=re.fullmatch(r'(\d{1,2})[./-](\d{1,2})[./-](\d{4})',a.birth_date.strip())
    if not m: raise ValueError('Data trebuie sa fie dd.mm.yyyy.')
    d,mo,y=m.groups(); d=d.zfill(2);mo=mo.zfill(2); raw=d+mo+y; n1=sum(map(int,raw));n2=reduce(n1);n3=n1-2*next(int(x) for x in d if x!='0');n4=reduce(n3)
    cnp=f'{d}.{mo}.{y}.{n1}.{n2}.{n3}.{n4}'; route=[int(x) for x in (raw+str(n1)+str(n2)+str(n3)+str(n4)) if x!='0']; start=POINTS[route[0]]
    seg=Counter(tuple(sorted(pair)) for pair in zip(route,route[1:]) if pair[0]!=pair[1]); path=[]
    for (left,right),count in seg.items():
        x1,y1=POINTS[left];x2,y2=POINTS[right];path.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-width="{7+5*(count-1)}"/>')
    for value in route:
        if route.count(value)>1:path.append(f'<circle cx="{POINTS[value][0]}" cy="{POINTS[value][1]}" r="24" stroke-width="5"/>')
    path=''.join(path); colors=['#b11f2a','#d08a24','#0f7f85','#5a4aa0','#7b3f00','#3b5b92','#7f1d1d','#3f6212','#6b21a8']
    rotations=''.join(f'<g transform="rotate({i*360/n2:.6g} {start[0]} {start[1]})" stroke="{colors[i]}" opacity=".52">{path}</g>' for i in range(n2))
    route_text=' -> '.join(map(str,route));name=html.escape(a.name);sx,sy=start
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760"><rect width="1200" height="760" fill="#fbf7ef"/><text x="600" y="54" text-anchor="middle" font-family="Georgia,serif" font-size="28" fill="#3d2c22">Semnatura astrala - {name}</text><text x="600" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#6d5b50">CNP astral: {cnp} | Destin: {n2} | Centru de rotire: cifra {route[0]}</text><g transform="translate(120 160)"><text x="180" y="-24" text-anchor="middle" font-family="Arial,sans-serif" font-size="18">Forma de baza</text>{GRID}<g fill="none" stroke="#b11f2a" stroke-linecap="round" stroke-linejoin="round">{path}</g><circle cx="{sx}" cy="{sy}" r="14" fill="#0f7f85" stroke="#fffdf8" stroke-width="4"/></g><g transform="translate(700 160)"><text x="180" y="-24" text-anchor="middle" font-family="Arial,sans-serif" font-size="18">Multiplicare dupa destin: {n2} rotiri</text>{GRID}{rotations}<circle cx="{sx}" cy="{sy}" r="14" fill="#0f7f85" stroke="#fffdf8" stroke-width="4"/></g><text x="118" y="610" font-family="Arial,sans-serif" font-size="16">Traseu folosit:</text><text x="118" y="640" font-family="Arial,sans-serif" font-size="18" fill="#6d5b50">{route_text}</text><text x="1180" y="745" text-anchor="end" font-family="Arial,Helvetica,sans-serif" font-size="14" fill="#aaa" font-weight="800">Atlas Numerologie</text></svg>'''
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(svg,encoding='utf-8',newline='\n');print(f'Generated: {a.output} | CNP: {cnp}');return 0
if __name__=='__main__':raise SystemExit(main())
