"""Audit the delivered Alina artifacts, source parity and calculator-backed figures."""
import base64
import collections
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import generate_alina_short as G

class Content(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text=[]
    def handle_data(self,data):
        self.text.append(data)

def visible(s):
    p=Content();p.feed(s)
    return re.sub(r'\s+',' ',' '.join(p.text)).strip()

def main():
    md=(G.OUT/(G.STEM+'.md')).read_text(encoding='utf-8')
    doc=(G.OUT/(G.STEM+'.html')).read_text(encoding='utf-8')
    body=re.search(r'<main>(.*?)</main>',doc,re.S).group(1)
    source=re.sub(r'\A---\n.*?\n---\n','',md,count=1,flags=re.S)
    expected=G.R.add_heading_ids(G.R.render_markdown(G.R.embed_markdown_images(source)))
    expected=G.R.build_toc(expected)
    # Renderer adds a bold callout label and removes the Obsidian callout token.
    assert visible(expected).replace('[!example] ','') == visible(body), 'MD_HTML_TEXT_PARITY'
    indices=re.findall(r'<div class="idx">Index: (DAM-19940725-v1\.00r-[A-Z]+-\d+[a-z0-9]*)</div>',body)
    assert len(indices)==len(set(indices)), 'DUPLICATE_INDEX'
    ids=re.findall(r'\bid="([^"]+)"',body)
    assert len(ids)==len(set(ids)), 'DUPLICATE_ID'
    assert set(re.findall(r'href="#([^"]+)"',body))<=set(ids), 'BROKEN_ANCHOR'
    assert len(re.findall(r'<h2[^>]*>Capitolul ',body))==9
    assert len(re.findall(r'matrix-grid matrix-grid-outlined',body))==2
    assert body.count('class="spirit-cell-highlight"')==1
    for src in re.findall(r'<img[^>]*src="([^"]+)"',body):
        assert src.startswith('data:image/'),src
        payload=base64.b64decode(src.split(',',1)[1],validate=True)
        assert len(payload)>100
    for src,name in re.findall(r'<img[^>]*src="([^"]+)"[^>]*data-source="([^"]+)"',body):
        assert base64.b64decode(src.split(',',1)[1])==(G.OUT/html.unescape(name)).read_bytes()
    for unwanted in ['Vulcu','Rebeca','Roman Andreea','Bîrsan','BDR-19980219','19021998','{{','[!info]']:
        assert unwanted not in body,unwanted
    calc=json.loads((G.OUT/(G.STEM+'-calculator.json')).read_text(encoding='utf-8'))['capitolul_2_formule_calcule_tabele_grafice']
    graph=json.loads((G.OUT/'graphics-numeric-report.json').read_text(encoding='utf-8'))
    for key,mat in [('date',calc['2.2_structura_matriciala']),('name',calc['2.3_codul_numerologic_personal_al_numelui']['matricea_numelui'])]:
        assert all(graph[key]['counts'].get(str(d),0)==mat['casute'][str(d)]['cantitate'] for d in range(1,10))
    assert calc['2.2_structura_matriciala']['meta']['sir_complet'] in body
    assert calc['2.3_codul_numerologic_personal_al_numelui']['matricea_numelui']['meta']['codul_numelui']['sir'] in body
    nek=(G.ROOT/'vault/Numerologie/Nume/Numarul Ereditar Karmic/NEK - Interpretari/NEKI-NN-7.md').read_text(encoding='utf-8').split('# Numarul Ereditar Karmic 7 - Interpretare',1)[1].split('## Asociere')[0].strip()
    assert nek in html.unescape(body),'CANONICAL_NEK_CHANGED'
    assert '2102' in re.search(r'Index: '+G.PREFIX+r'-T-008</div>(.*?)(?=Index:)',body,re.S).group(1)
    summary={'result':'OK','chapters':9,'unique_indices':len(indices),'unique_ids':len(ids),'embedded_images':len(re.findall(r'<img',body)),'words':len(visible(body).split()),'md_html_text_parity':True,'canonical_nek_exact':True,'matrix_calculator_parity':True,'browser_visual_review':'Blocked by file URL policy; no browser workaround attempted.'}
    (G.OUT/'validation-report.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':
    main()
