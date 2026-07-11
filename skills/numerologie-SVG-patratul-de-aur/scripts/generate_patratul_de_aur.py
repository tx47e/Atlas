#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path

ORDER=(4,9,2,3,5,7,8,1,6); POS={1:(0,0),4:(1,0),7:(2,0),2:(0,1),5:(1,1),8:(2,1),3:(0,2),6:(1,2),9:(2,2)}
COL={1:'#ff3f46',5:'#ff3f46',9:'#ff3f46',2:'#6fa0e8',6:'#6fa0e8',3:'#e8ecef',7:'#e8ecef',4:'#d19b61',8:'#d19b61'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--name',required=True);p.add_argument('--birth-date',required=True);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
 day=int(a.birth_date.strip().replace('/','.').replace('-','.').split('.')[0]); vals={cell:day+i for i,cell in enumerate(ORDER)}; c=vals[5]; total=c*3
 cells=[]
 for n,(x,y) in POS.items():
  fg='#fffdf8' if n in (1,2,5,6,9) else '#3d2c22'
  cells.append(f'<rect x="{250+x*200}" y="{145+y*200}" width="200" height="200" fill="{COL[n]}"/><text x="{350+x*200}" y="{193+y*200}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="22" fill="{fg}">casuta {n}</text><text x="{350+x*200}" y="{271+y*200}" text-anchor="middle" font-family="Georgia, serif" font-size="72" font-weight="700" fill="{fg}">{vals[n]}</text>')
 grid=[[vals[1],vals[4],vals[7]],[vals[2],vals[5],vals[8]],[vals[3],vals[6],vals[9]]]; sums=[' + '.join(map(str,row))+f' = {total}' for row in grid]+[' + '.join(map(str,col))+f' = {total}' for col in zip(*grid)]+[f'{vals[1]} + {vals[5]} + {vals[9]} = {total}',f'{vals[7]} + {vals[5]} + {vals[3]} = {total}']
 side='<text x="875" y="190" font-family="Arial, Helvetica, sans-serif" font-size="18">Linii:</text>'+''.join(f'<text x="875" y="{224+i*30}" font-family="Arial, Helvetica, sans-serif" font-size="18">{s}</text>' for i,s in enumerate(sums[:3]))+'<text x="875" y="342" font-family="Arial, Helvetica, sans-serif" font-size="18">Coloane:</text>'+''.join(f'<text x="875" y="{376+i*30}" font-family="Arial, Helvetica, sans-serif" font-size="18">{s}</text>' for i,s in enumerate(sums[3:6]))+'<text x="875" y="494" font-family="Arial, Helvetica, sans-serif" font-size="18">Diagonale:</text>'+''.join(f'<text x="875" y="{528+i*30}" font-family="Arial, Helvetica, sans-serif" font-size="18">{s}</text>' for i,s in enumerate(sums[6:]))
 grid='<rect x="250" y="145" width="600" height="600" rx="10" fill="none" stroke="#7a6558" stroke-width="4"/><g stroke="#fffdf8" stroke-width="4"><line x1="450" y1="145" x2="450" y2="745"/><line x1="650" y1="145" x2="650" y2="745"/><line x1="250" y1="345" x2="850" y2="345"/><line x1="250" y1="545" x2="850" y2="545"/></g>'
 legend='<g transform="translate(330 805)" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#3d2c22"><circle cx="0" cy="-5" r="10" fill="#ff3f46"/><text x="18" y="0">Foc</text><circle cx="120" cy="-5" r="10" fill="#6fa0e8"/><text x="138" y="0">Apa</text><circle cx="240" cy="-5" r="10" fill="#e8ecef" stroke="#9aa3aa"/><text x="258" y="0">Aer</text><circle cx="360" cy="-5" r="10" fill="#d19b61"/><text x="378" y="0">Pamant</text></g>'
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="860" viewBox="0 0 1100 860"><rect width="1100" height="860" fill="#fbf7ef"/><text x="550" y="56" text-anchor="middle" font-family="Georgia, serif" font-size="30" fill="#3d2c22">Patratul de Aur - {a.name}</text><text x="550" y="88" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#6d5b50">Ordine: 4 -> 9 -> 2 -> 3 -> 5 -> 7 -> 8 -> 1 -> 6 | Centru: {c} | Suma: {total}</text>{"".join(cells)}{grid}{side}{legend}<text x="1080" y="845" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#aaa" font-weight="800">Atlas Numerologie</text></svg>'
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(svg,encoding='utf-8');print(a.output)
if __name__=='__main__':main()
