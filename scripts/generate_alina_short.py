from __future__ import annotations

import html
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
PID = '1994-07-25-DANGULEA-ALINA-MONICA'
PREFIX = 'DAM-19940725-v1.00r'
OUT = ROOT / 'output/lucrari' / PID
STEM = PID + '-scurt-v1.00r'
MODEL = ROOT / 'skills/numerologie-lucrare-redactare/references/modele-html/lucrare-scurta-daniel-v1.00r'

def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

H = module('generate_rebeca_short')
R = module('render_rebeca_short_html')
blocks = []
used = set()

def put(idx, text):
    assert idx not in used, idx
    used.add(idx)
    blocks.append(f'Index: {PREFIX}-{idx}\n\n{text.strip()}\n')

def para(idx, text):
    put('P-' + idx, text)

def calc(idx, *lines):
    put('C-' + idx, '> [!example] Calcul\n> ' + '  \n> '.join(lines))

def sub(idx, title):
    put('SUB-' + idx, '### ' + title)

def chapter(idx, title):
    put('CAP-' + idx, '## ' + title)

def table(headers, rows, cls=''):
    return '<table' + (f' class="{cls}"' if cls else '') + '><thead><tr>' + ''.join('<th>'+str(v)+'</th>' for v in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>'+str(v)+'</td>' for v in row) + '</tr>' for row in rows) + '</tbody></table>'

def read_fragment(pattern):
    files = list(OUT.glob(pattern))
    assert len(files) == 1, (pattern, files)
    return files[0].read_text(encoding='utf-8')

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    result = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'skills/numerologie-lucrare-redactare/scripts/calculator_numerologic_examen.py'), '--data-nasterii', '25.07.1994', '--nume-complet', 'Dangulea Alina Monica', '--nume-familie', 'Dangulea', '--prenume', 'Alina Monica', '--prenume-activ', 'Alina', '--gen', 'feminin', '--an-start', '1994', '--an-final', '2102', '--pretty'], capture_output=True, text=True, encoding='utf-8', check=True)
    report = json.loads(result.stdout)
    (OUT / (STEM + '-calculator.json')).write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    c = report['capitolul_2_formule_calcule_tabele_grafice']
    base = c['2.1_codul_numerologic_personal_data_nasterii']
    m = c['2.2_structura_matriciala']
    n = c['2.3_codul_numerologic_personal_al_numelui']
    cycles = c['2.4_ciclicitati']
    assert [base[k]['calcul']['rezultat'] for k in ['vibratia_interioara','vibratia_exterioara','destinul_vibratia_destinului']] == [7,7,10]
    for source, dest in [('03-The Empress.jpg','tarot-03-imparateasa.jpg'), ('07-The Chariot.jpg','tarot-07-carul.jpg'), ('15-The Devil.jpg','tarot-15-diavolul.jpg')]:
        shutil.copyfile(ROOT/'vault/Tarot/imagini'/source, OUT/dest)
    put('CAP-001', '# Dangulea Alina Monica — 25.07.1994')
    chapter('002', 'Date generale')
    put('L-001', '- Persoana analizată: Dangulea Alina Monica\n- Prenume activ: Alina\n- Data nașterii: 25.07.1994\n- Gen: feminin\n- Nume anterior: necomunicat\n- Template selectat: scurt\n- Stil de redactare: conversațional\n- Interval analizat: 0–108 ani, 1994–2102\n- Data lucrării: 10.09.2026\n- Versiune: V1.00R')
    chapter('003', 'Cuprins')
    put('L-002', '1. Vibrația interioară — Cine ești tu?\n2. Vibrația exterioară — Rolul social\n3. Destinul — Muntele de urcat\n4. Matrița numerologică — Pătratul lui Pitagora\n5. Numele — Eu și neamul\n6. Spirit și karmă — Lecții și direcții de maturizare\n7. Pinacluri: Oportunități și provocări\n8. Ciclicități\n9. Concluzii')

    chapter('005', 'Capitolul 1. Vibrația interioară — Cine ești tu?')
    sub('001', '1.1. Definiție')
    para('006', 'Alina, vibrația interioară descrie natura ta lăuntrică: felul în care primești experiențele, ceea ce îți dorești cu adevărat și motivațiile care rămân active chiar când nu trebuie să răspunzi așteptărilor nimănui. O citești din ziua nașterii, reducând cifrele până la o singură cifră. În această lectură simbolică, ea îți oferă un punct de plecare pentru a observa ce te susține și ce ai de maturizat, fără să îți fixeze caracterul într-o etichetă.')
    calc('001', 'Ziua din data de naștere = **25** → 2 + 5 = **7**')
    sub('002', '1.2. Caracterul')
    para('007', 'Alina, cu vibrația interioară **7**, cauți sens, profunzime și explicații care rezistă unei priviri atente. Arhetipal, te apropii de Observator și Cercetător: îți place să înțelegi cum funcționează un lucru înainte să îl accepți sau să îl transmiți mai departe. Poți avea răbdare cu o întrebare dificilă și poți observa detalii pe care o privire grăbită le pierde. Pentru tine, liniștea poate deveni un spațiu de lucru interior în care informația se așază și se transformă în înțelegere.')
    para('007a', 'Ziua **25** aduce în acest rezultat două nuanțe: **2** caută apropiere, ascultă și simte relația, iar **5** vrea libertate, mișcare și experiență directă. Împreună ajung la **7**, care cercetează ceea ce a trăit. Poți învăța mult din oameni și experiențe noi, apoi ai nevoie de timp să le deslușești. Acest traseu te ajută să unești sensibilitatea cu discernământul: să asculți ce simți, dar și să verifici ce presupui.')
    para('007b', 'În viața concretă, calitatea acestei energii se vede când pui o întrebare bună, compari explicații și găsești o soluție simplă pentru o problemă complicată. Umbra apare când analiza devine neîncredere, când te retragi fără să explici sau când aștepți să știi totul înainte de a încerca. Maturizarea înseamnă să alegi un moment în care închei cercetarea și treci la un experiment mic. Poți rămâne atentă și profundă, lăsând totodată oamenii să afle ce gândești și ce ai nevoie.')
    sub('003', '1.3. Dorințele')
    para('008', 'Îți dorești să ai spațiu pentru gândire, relații în care poți fi sinceră și libertatea de a nu accepta o explicație doar pentru că este repetată de mulți. Te poate împlini sentimentul că stăpânești temeinic un domeniu și că ceea ce înveți are sens. Ai grijă să îți exprimi nevoia de liniște în cuvinte simple: o pauză anunțată poate proteja apropierea, în timp ce tăcerea fără explicație îi poate lăsa pe ceilalți să ghicească.')
    sub('004', '1.4. Motivația')
    para('009', 'Te motivează întrebările deschise, descoperirea unei legături și munca în care calitatea contează mai mult decât agitația. Poți susține un efort atent dacă înțelegi de ce îl faci. Începe un proiect cu o întrebare precisă, alege câteva surse bune și stabilește ce rezultat vei produce: o explicație, o analiză, o soluție verificată. Așa, curiozitatea ta primește o direcție și nu se pierde în acumulare fără aplicare.')
    sub('005', '1.5. Teama')
    para('010', 'Teama asociată simbolic lui **7** este să te expui înainte să fii pregătită, să fii înțeleasă greșit sau să ai încredere într-un lucru care se dovedește fragil. Ea poate apărea ca perfecționism ori distanță critică. Când o observi, separă ceea ce știi de ceea ce presupui și spune ce informație îți lipsește. Nu ai nevoie de certitudine totală pentru fiecare pas; ai nevoie să poți verifica și corecta direcția.')
    sub('006', '1.6. Polarități și maturizare')
    rows = [('Polarități pozitive',['discernământ și observație atentă','răbdare pentru studiu','independență în gândire','profunzime și respect pentru adevăr','capacitate de a lega experiența de înțelegere']),('Polarități negative',['retragere greu de înțeles de ceilalți','critică excesivă','neîncredere și verificare fără sfârșit','amânarea acțiunii prin analiză','dificultatea de a cere ajutor']),('Direcții de dezvoltare',['explică nevoia de liniște','testează concluziile în practică','cere feedback de la oameni competenți','păstrează relații în care poți vorbi deschis','transformă o descoperire într-un rezultat util'])]
    put('T-009', '<table class="polarities-table"><tbody>'+''.join('<tr><th scope="row">'+label+'</th><td><ul>'+''.join('<li>'+x+'</li>' for x in items)+'</ul></td></tr>' for label,items in rows)+'</tbody></table>')

    chapter('006', 'Capitolul 2. Vibrația exterioară — Rolul social')
    sub('008', '2.1. Definiție')
    para('011', 'Vibrația exterioară descrie felul în care te manifești în lume: prezența, comportamentul vizibil și prima impresie pe care o poți lăsa. O citești din luna nașterii. Ea arată o poartă de contact cu oamenii, iar felul în care o folosești depinde de context, experiență și alegerile tale. Observând-o, poți face mai clară legătura dintre intenția ta și ceea ce ajunge efectiv la celălalt.')
    calc('002', 'Luna din data de naștere = **7**')
    sub('009', '2.2. Rolul social')
    para('012', 'Fiind născută în iulie, ai vibrația exterioară **7**, asociată rolului social al Observatorului și Specialistului. Oamenii te pot percepe atentă, selectivă și interesată de fondul unei probleme. Îți poți câștiga locul prin competență, întrebări precise și capacitatea de a explica ce ai verificat. Într-un grup, nu trebuie să vorbești cel mai mult ca să ai influență: o intervenție bine pregătită poate clarifica direcția tuturor. Ai grijă ca rezerva să nu fie citită ca dezinteres sau superioritate; arată ce apreciezi și fă loc întrebărilor celorlalți.')
    sub('010', '2.3. Interior și exterior')
    para('013', 'Alina, în interior ești **7**, iar la exterior oamenii te pot percepe tot prin **7**. Nevoia ta de profunzime poate fi vizibilă în felul în care asculți, alegi și răspunzi. Această potrivire îți poate susține coerența, dar poate întări și retragerea: dacă analizezi mult înăuntru și arăți foarte puțin în afară, ceilalți pot avea acces numai la tăcerea ta. Lasă-i să vadă și drumul gândirii, nu doar concluzia.')
    para('013a', 'Puntea dintre interior și exterior arată ajustarea dintre ceea ce trăiești și imaginea pe care o exprimi. O obții din diferența absolută a celor două vibrații. Pentru tine, ea te ajută să observi cât de bine se potrivesc intenția, cuvintele și faptele, mai ales atunci când ai nevoie de timp ca să răspunzi.')
    calc('002a', '|**7** − **7**| = **0**')
    para('013b', 'Puntea **0** arată că cele două vibrații au aceeași valoare; nu introduce o direcție numerică diferită între ele. Coerența poate veni firesc atunci când îți exprimi limpede intenția. Totuși, aceeași umbră se poate vedea pe ambele planuri: îndoiala interioară poate deveni distanță vizibilă. Autenticitatea ta crește când poți spune „am nevoie să verific” sau „încă nu sunt pregătită să răspund”, păstrând legătura cu oamenii și făcându-ți rolul ușor de înțeles și acceptat.')

    chapter('007', 'Capitolul 3. Destinul — Muntele de urcat')
    sub('011', '3.1. Definiție și calcul')
    para('014', 'Destinul îți arată o direcție de maturizare pe care o poți construi de-a lungul vieții. Aduni toate cifrele datei pentru Calea Destinului, apoi însumezi cifrele acestei sume o singură dată pentru Destin. Păstrezi rezultatul compus și distingi de el cifra de interpretare, obținută prin reducerea completă. Citește această direcție ca pe un munte pe care înveți să îl urci în felul tău, fără să presupui că un anumit eveniment este obligatoriu.')
    calc('003', 'Toate cifrele adunate din data de naștere = 2 + 5 + 0 + 7 + 1 + 9 + 9 + 4 = **37**', 'Destinul = 3 + 7 = **10**', 'Cifra de interpretare = 1 + 0 = **1**')
    sub('012', '3.2. Interpretare')
    para('015', 'Alina, Destinul tău este **10**, cu cifra de interpretare **1**. Direcția de maturizare pune accent pe autonomie, inițiativă și asumarea alegerii. Poți învăța să deschizi un drum propriu fără să aștepți ca toate condițiile să fie perfecte. Nu este o obligație de a conduce oameni, ci o invitație să îți asumi autoritatea asupra muncii și deciziilor tale. O idee pe care o semnezi, o limită pe care o exprimi sau un proiect pe care îl începi conștient pot fi forme concrete ale acestei direcții.')
    para('015d', 'Vibrația interioară **7** vrea să înțeleagă, iar direcția **1** cere să alegi și să pui în mișcare ceea ce ai înțeles. Între ele poți construi un dialog fertil: studiezi suficient ca să ai o bază și acționezi suficient ca să înveți din realitate. Umbra apare când cercetarea devine amânare sau când, după prea multă așteptare, vrei să impui brusc o concluzie. O etapă de probă, cu un rezultat clar și un termen realist, poate uni profunzimea cu inițiativa.')
    para('015e', 'Maturizarea lui **10 / 1** se vede în responsabilitatea pentru ceea ce pornești. Îți poți păstra independența fără să refuzi sprijinul, iar un feedback bine argumentat nu îți anulează vocea. În loc să îți măsori valoarea prin comparație sau prin controlul fiecărui detaliu, urmărește ce ai construit și ce ai învățat din încercare. Așa, direcția personală capătă continuitate.')
    sub('012c', '3.3. Puntea interior–destin și aspectele de îndreptat')
    para('015f', 'Puntea interior–destin îți arată ajustarea dintre natura lăuntrică și direcția de maturizare. Folosești cifra de interpretare a Destinului în această diferență. Aspectele de îndreptat și soluția lor completează lectura: pornești din Calea Destinului, scazi dublul primei cifre din zi și însumezi cifrele rezultatului o singură dată pentru soluție.')
    calc('003e', 'Puntea interior–destin: |7 − 1| = **6**', 'Aspecte de îndreptat: 37 − 2 × 2 = **33**', 'Soluția: 3 + 3 = **6**')
    para('015g', 'Puntea **6** te invită să legi cunoașterea de grijă și de o responsabilitate concretă. O analiză devine mai vie când ajută pe cineva sau îmbunătățește o situație reală. Aspectele **33** îți aduc în atenție felul în care comunici și folosești informația: poți avea multe explicații, dar ele au nevoie de ordine și de un destinatar. Soluția **6** este să alegi ce îți asumi, să duci până la capăt și să păstrezi măsura. A fi utilă nu înseamnă să rezolvi toate problemele din jur.')

    chapter('008', 'Capitolul 4. Matrița numerologică — Pătratul lui Pitagora')
    sub('013', '4.1. Matricea datei de naștere')
    para('016', 'Matricea pornește din cifrele datei și cele patru numere de lucru. Prin ea poți observa resursele simbolic active și energiile conservate, care au nevoie de contexte, oameni și exercițiu pentru a deveni accesibile mai constant. Cele nouă căsuțe îți propun nouă sfere de inteligență:\n\n- **1** — psihică;\n- **2** — emoțională;\n- **3** — prelucrarea informațiilor;\n- **4** — corporală;\n- **5** — intuitivă;\n- **6** — pragmatism;\n- **7** — spirituală;\n- **8** — putere și socială;\n- **9** — mentală.\n\nLe citești împreună, prin felul în care îți poți folosi resursele și construi obiceiuri potrivite.')
    calc('004', 'Data compactă = **25071994**', 'N1 = 2 + 5 + 0 + 7 + 1 + 9 + 9 + 4 = **37**', 'N2 = 3 + 7 = **10**', 'N3 = 37 − 2 × 2 = **33**', 'N4 = 3 + 3 = **6**', 'Șir complet = 25071994 + 37 + 10 + 33 + 6 = **250719943710336**')
    put('G-002', read_fragment('matrita-datei-*-component.html'))
    matrix_texts = [
        'Ai **2** apariții. Inițiativa și forța psihică se pot exprima prin fermitate însoțită de dialog: poți formula o direcție și poți primi o altă perspectivă fără să renunți imediat la tine. Într-o discuție, te ajută să spui ce dorești înainte de a explica toate argumentele. Umbra poate fi oscilația între insistență și retragere, mai ales când nu te simți înțeleasă. Alege criteriul după care iei o decizie și revino la el când apar prea multe păreri. Astfel, îți păstrezi centrul și poți colabora fără să transformi fiecare diferență într-o luptă.',
        'Ai **1** apariție. Sensibilitatea, comunicarea emoțională și colaborarea au un punct de sprijin, dar au nevoie de atenție și de un mediu în care poți vorbi deschis. Poți sesiza atmosfera fără să găsești imediat cuvintele pentru ceea ce simți. Dacă te retragi pentru a înțelege, spune când poți reveni la discuție. Umbra apare când aștepți ca celălalt să ghicească sau când răspunzi numai după ce tensiunea a crescut. Un mesaj simplu despre emoție, nevoie și cerere concretă poate face mai mult decât o explicație lungă despre cine are dreptate.',
        'Ai **3** apariții. Prelucrarea informației și relaționarea sunt resurse bine reprezentate: poți observa legături, aduna exemple și transforma o idee într-o explicație accesibilă. Împreună cu accentul tău pe **7**, această căsuță poate susține studiul, analiza și transmiterea cunoașterii. Umbra este să menții prea multe fire deschise sau să continui explicația după ce mesajul esențial a fost înțeles. Selectează ce este relevant pentru interlocutor și verifică ce a reținut. Cunoașterea devine folositoare atunci când îl ajută să facă un pas, nu doar să primească mai multă informație.',
        'Ai **1** apariție. Organizarea, contactul cu concretul și ritmul de lucru au o bază pe care o poți consolida. Te ajută să vezi ce ai de făcut, în ce ordine și cu ce resurse, mai ales când mintea deschide mai multe posibilități. Umbra poate fi alternanța dintre planuri detaliate și oboseala de a le urma. Alege un program realist, cu pauze și câteva repere stabile, în locul unui sistem dificil de întreținut. Referirea simbolică a acestei căsuțe la corp nu măsoară starea ta de sănătate; folosește-o ca îndemn la atenție față de propriul ritm.',
        'Ai **1** apariție. Libertatea, adaptarea, stima de sine și curajul de a încerca au un punct de pornire. Poți folosi experiența directă ca să verifici concluziile minții, în loc să rămâi numai în analiză. Umbra apare când schimbi direcția la primul disconfort sau când îți condiționezi încrederea de aprobarea altora. Alege provocări suficient de mici ca să le poți duce până la capăt și observă ce ai învățat. Libertatea ta crește prin alegeri asumate și prin posibilitatea de a corecta, fără să ai nevoie să abandonezi de fiecare dată tot cadrul.',
        'Ai **1** apariție. Grija, simțul practic și nevoia de armonie pot deveni gesturi concrete: să pregătești, să repari, să organizezi sau să creezi un spațiu plăcut. Te poate ajuta să legi o idee bună de folosul ei imediat pentru cineva. Umbra apare când îți asumi mai mult decât poți susține sau când aștepți ca ceilalți să aibă exact standardele tale. Clarifică ce oferi și ce contribuție ceri. Ocrotirea matură păstrează loc și pentru nevoile tale, iar responsabilitatea devine mai stabilă atunci când este împărțită limpede.',
        'Ai **2** apariții. Observația, analiza și căutarea sensului pot circula între experiență și reflecție: înveți din ceea ce vezi și poți verifica în practică ceea ce ai înțeles. Această resursă întărește vibrațiile interioară și exterioară **7**, fără să însemne că fiecare impresie este corectă. Umbra este îndoiala repetată sau distanța față de oameni când simți că nu ai încă toate răspunsurile. Păstrează un jurnal de întrebări, ipoteze și rezultate. Diferența dintre o intuiție și o concluzie verificată îți protejează discernământul și face cunoașterea mai ușor de transmis.',
        'Nu ai nicio apariție. Energia puterii, a asumării autorității și a administrării performanței este **conservată**: nu o accesezi neapărat la fel de constant în orice situație. Poți oscila între a prelua multă responsabilitate și a lăsa decizia altcuiva, mai ales când nu există un cadru clar. O poți sprijini prin oameni competenți, roluri bine definite, criterii de rezultat și exerciții graduale de negociere. Stabilește ce poți decide singură, ce verifici cu altcineva și cum urmărești progresul. Căsuța conservată nu îți interzice conducerea sau reușita; arată unde construiești conștient suportul.',
        'Ai **2** apariții. Capacitatea de sinteză, compasiunea și perspectiva largă se pot susține reciproc. Poți privi o situație din mai multe unghiuri și poți extrage din experiență o lecție care rămâne utilă. Umbra este să înțelegi atât de multe perspective încât să amâni concluzia sau să te simți responsabilă pentru ceea ce nu depinde de tine. Alege ce merită continuat, ce poate fi încheiat și ce lași în responsabilitatea altcuiva. Când pui un capăt clar unei etape, mintea ta primește spațiu pentru o contribuție nouă.'
    ]
    for digit, text in enumerate(matrix_texts, 1):
        para(str(34+digit).zfill(3), f'**Căsuța {digit}.** ' + text)
    sub('015', '4.2. Elemente și temperament')
    # Sums of occurrences, not digit-weighted values; expose this display aggregation.
    groups = [('Foc','foc',[1,5,9]),('Pământ','pamant',[4,8]),('Aer','aer',[3,7]),('Apă','apa',[2,6])]
    elements = [(label,cls,sum(m['casute'][str(d)]['cantitate'] for d in ds)) for label,cls,ds in groups]
    assert [v for _,_,v in elements] == [5,1,5,2]
    para('044', 'Elementele grupează aparițiile din matrice: Focul reunește **1, 5, 9**, Pământul **4, 8**, Aerul **3, 7**, iar Apa **2, 6**. Prin această distribuție poți observa dialogul dintre inițiativă, concret, gândire și emoție. Numărăm aparițiile din fiecare grup, fără să folosim valoarea ponderată a cifrelor.')
    put('T-012', '<div class="element-analysis framed-panel"><div class="element-bars">'+''.join(f'<div class="element-bar"><div class="element-bar-label"><span>{label}</span><strong>{value}</strong></div><div class="element-bar-track"><span class="element-bar-fill element-{cls}" style="width:{value/5*100}%"></span></div></div>' for label,cls,value in elements)+'</div></div>')
    para('045', 'La tine, **Focul și Aerul sunt la egalitate, cu câte 5 apariții**, urmate de **Apă, cu 2**, și **Pământ, cu 1**. În limbajul temperamentelor, lectura este mixtă, coleric–sangvinică: inițiativa poate întâlni curiozitatea, ideile și nevoia de schimb. Nu alegem artificial un singur temperament dominant. Poți porni repede în minte, dar ai nevoie să cobori ideea într-un pas concret și să lași spațiu pentru trăirea celuilalt. Un program simplu și o discuție clară te ajută să legi energia de rezultate.')
    sub('016', '4.3. Masculin și feminin')
    put('G-007', '<div class="parity-chart framed-panel" style="width:100%;max-width:none" role="img" aria-label="13 cifre: 10 impare și 3 pare"><div class="parity-chart-total">Total: <strong>13</strong> cifre</div><div class="parity-chart-bar"><span class="parity-odd" style="width:76.92%"><strong>Impare · 10</strong></span><span class="parity-even" style="width:23.08%"><strong>Pare · 3</strong></span></div></div>')
    para('017', 'Matricea ta are **10 apariții impare și 3 pare**. În limbajul simbolic al metodei, polaritatea masculină este asociată inițierii și proiectării, iar cea feminină receptivității și schimbului. Aceste etichete nu stabilesc identitatea sau rolurile tale ca femeie. Accentul pe impare te invită să observi cum pornești și susții o intenție; energia pară îți amintește să primești, să asculți și să verifici efectul asupra celuilalt. Poți echilibra decizia cu o întrebare sinceră și cu răbdarea de a auzi răspunsul.')
    sub('017', '4.4. Daruri și nevoi')
    para('018', 'Darurile și nevoile se citesc din căsuțele cu cel puțin două apariții: la tine, **1, 3, 7 și 9**. Prin **1** poți iniția și ai nevoie de autonomie; prin **3** poți prelucra și transmite informație și ai nevoie de dialog viu; prin **7** poți cerceta și ai nevoie de liniște și profunzime; prin **9** poți sintetiza și ai nevoie de sens. O resursă se poate încorda când nevoia ei este ignorată. Dacă ai multe idei, dar niciun spațiu de reflecție, sau multă liniște, dar nicio ocazie de a împărtăși, echilibrul se pierde. Alternează studiul, exprimarea și aplicarea.')
    sub('017a', '4.5. Scara bunăstării')
    para('019', 'Scara bunăstării ordonează valorile celor nouă căsuțe și ale celor opt vectori, pentru a vedea prin ce activități poți simți împlinire. La tine, vectorul **369 — Bunăstare materială, 33** ocupă prima treaptă, urmat de **789 — Creativitate, 32**, **357 — Scopuri, 28** și **159 — Carieră, 25**. Poți găsi satisfacție când o idee devine utilă și produce o formă concretă de stabilitate. Creativitatea îți oferă soluții, scopul le selectează, iar direcția profesională le pune în lucru. Valorile descriu ordinea internă a acestei hărți, nu venituri sau rezultate garantate.')
    put('G-004', H.wellbeing(m['scara_bunastarii']))
    para('019a', 'Vectorul **369** este complet: informația și relaționarea lui **3**, pragmatismul lui **6** și sinteza lui **9** îți pot susține drumul de la idee la folos. Vectorul **789** are o valoare mare, dar căsuța **8** este conservată; de aceea, o soluție bună are nevoie și de un cadru de decizie, resurse și responsabilități. Nu confunda intensitatea creativității cu administrarea automată a rezultatului. Definește cui îi folosește munca ta, ce livrezi și cum verifici dacă a fost utilă.')

    chapter('009', 'Capitolul 5. Numele — Eu și neamul')
    sub('018', '5.1. Numărul activ')
    para('020a', 'Numărul activ pornește din prenumele pe care îl folosești zi de zi. Îl obții însumând valorile literelor și reducând rezultatul. Prin el poți observa nuanța adusă de nume în reacțiile obișnuite, în felul în care răspunzi când ești chemată și în energia cu care intri într-un context.')
    calc('009', 'Alina = A1 + L3 + I9 + N5 + A1 = **19** → 1 + 9 = **10** → 1 + 0 = **1**')
    para('021', 'Alina, Numărul activ **1** îți susține inițiativa și nevoia de a face lucrurile într-un fel care îți aparține. El poate scoate în exterior ceea ce vibrația interioară **7** pregătește în liniște: o alegere, o idee originală, un prim pas. Umbra apare când simți că trebuie să te descurci singură sau când respingi contribuția altcuiva înainte să o asculți. Poți spune clar ce vrei și poți cere un ajutor precis. Autonomia matură îți lasă libertatea de a coopera.')
    sub('019', '5.2. Numărul intim')
    para('021b', 'Numărul intim se calculează din vocalele numelui complet și îți propune o lectură a dorințelor profunde și a motivației afective. Spre deosebire de comportamentul vizibil, el te îndeamnă să observi ce te hrănește chiar și atunci când nu ceri recunoaștere în exterior.')
    calc('009a', 'Vocalele = 1 + 3 + 5 + 1 + 1 + 9 + 1 + 6 + 9 + 1 = **37** → 3 + 7 = **10** → 1 + 0 = **1**')
    para('021c', 'Numărul intim **1** poate aduce nevoia de a alege din convingere, de a avea o voce proprie și de a fi respectată ca persoană distinctă. Apropierea devine mai confortabilă când poți rămâne tu însăți în ea. Umbra este să citești orice sugestie ca pe o încercare de control sau să îți ascunzi nevoile ca să nu pari dependentă. Spune ce contează pentru tine și de ce, apoi caută o formă în care autonomia și colaborarea pot coexista. Coincidența dintre Numărul activ și cel intim poate face această nevoie mai ușor de recunoscut în viața de zi cu zi.')
    sub('020', '5.3. Numărul ereditar')
    para('020b', 'Numărul ereditar se obține din numele de familie. Prin el privești simbolic felul în care apartenența, regulile și relațiile de familie pot fi puse în dialog cu alegerile tale. El nu reconstruiește fapte despre strămoși și nu te obligă să repeți un model familial.')
    calc('008', 'Dangulea = 4 + 1 + 5 + 7 + 3 + 3 + 5 + 1 = **29** → 2 + 9 = **11** → 1 + 1 = **2**')
    para('020', 'Numărul ereditar **2** aduce în lectură cooperarea, sensibilitatea și atenția la legături. Poți păstra din această direcție răbdarea de a asculta și capacitatea de a construi împreună. În raport cu Numărul activ și Numărul intim **1**, apare o întrebare folositoare: cum îți urmezi alegerea fără să pierzi dialogul? Umbra lui **2** poate fi adaptarea excesivă sau evitarea unei discuții necesare. Maturizarea înseamnă să rămâi atentă la ceilalți, spunând totodată ce poți oferi și unde este limita ta.')
    sub('021', '5.4. Numărul ereditar karmic')
    para('022b', 'Numărul ereditar karmic păstrează suma numelui de familie în intervalul **1–22**, prin scăderi de 22 când sunt necesare. Îți oferă o imagine simbolică a resursei de neam. Textul tradițional de mai jos este păstrat în forma sa canonică; afirmațiile despre strămoși se citesc în cadrul acestei tradiții, nu ca istorie genealogică verificată.')
    calc('005', 'Dangulea = **29** → 29 − 22 = **7**')
    nek_source = ROOT/'vault/Numerologie/Nume/Numarul Ereditar Karmic/NEK - Interpretari/NEKI-NN-7.md'
    nek = nek_source.read_text(encoding='utf-8').split('# Numarul Ereditar Karmic 7 - Interpretare',1)[1].split('## Asociere')[0].strip()
    put('T-013', '<table class="tarot-profile-table"><tbody><tr><td><div class="idx">Index: '+PREFIX+'-G-003</div><img src="tarot-07-carul.jpg" alt="Arcana Majoră 7 — Carul"><div class="tarot-image-caption">Arcana Majoră 7 — Carul</div></td><td><div class="idx">Index: '+PREFIX+'-P-022e</div><p>'+html.escape(nek)+'</p></td></tr></tbody></table>')
    para('022c', 'Alina, poți continua simbolic această resursă prin seriozitatea cu care cercetezi o întrebare, prin îmbunătățirea unui proces sau printr-o explicație care îi ajută pe ceilalți să înțeleagă. Nu trebuie să alegi o profesie anume ca să pui în valoare cunoașterea. În munca ta, caută ce poate fi verificat, simplificat și făcut mai util. Asocierea cu **Carul** adaugă imaginea direcției asumate: descoperirea are nevoie de un drum pe care să fie pusă în practică.')
    para('022d', 'Umbra acestei lecturi poate fi acumularea de cunoaștere fără aplicare, izolarea în propriile explicații sau presiunea de a demonstra mereu că știi mai mult. Maturizarea înseamnă să păstrezi curiozitatea și să accepți revizuirea unei concluzii. Împărtășește ce ai învățat, ascultă întrebările și lasă rezultatul să fie verificabil. Astfel, respectul pentru cunoaștere poate deveni o contribuție concretă, fără să se transforme într-o obligație de a confirma o poveste despre familie.')
    sub('022', '5.5. Numărul de realizare')
    para('021a', 'Numărul de realizare se calculează din consoanele numelui complet. El completează vibrația exterioară prin felul în care poți transforma resursele în manifestare vizibilă: comportamente, colaborări și rezultate pe care ceilalți le pot observa.')
    calc('010', 'Consoanele = 4 + 5 + 7 + 3 + 3 + 5 + 4 + 5 + 3 = **39** → 3 + 9 = **12** → 1 + 2 = **3**')
    para('022', 'Numărul de realizare **3** susține exprimarea, creativitatea și capacitatea de a face legătura între oameni și idei. Poți valorifica ceea ce știi prin scris, prezentare, explicații, proiecte educative sau soluții care simplifică un lucru dificil. Umbra apare când energia rămâne în idei și promisiuni sau când cauți o formă perfectă înainte să arăți ceva. Alege un mesaj central, un public clar și un rezultat terminat. O contribuție mică, dar completă, îți poate susține încrederea mai mult decât multe proiecte începute.')
    para('022a', 'Vibrația exterioară **7** te poate face rezervată și atentă la detalii, în timp ce Numărul de realizare **3** îți oferă o cale de a te face înțeleasă. Împreună pot susține comunicarea bazată pe competență: cercetezi în profunzime și explici limpede. Nu este nevoie să devii permanent expansivă. Poți alege un format potrivit ritmului tău, precum un text bine organizat, o demonstrație pregătită sau o discuție în care întrebările au loc.')
    sub('023', '5.6. Numărul de exprimare')
    para('023a', 'Numărul de exprimare reunește componentele numelui complet. Însumezi rezultatele reduse ale fiecărei componente și reduci suma obținută. Prin el poți urmări cum se așază resursele numelui într-o expresie mai coerentă a personalității și a muncii tale.')
    calc('012', 'Dangulea = **29** → 11 → **2**', 'Alina = **19** → 10 → **1**', 'Monica = **28** → 10 → **1**', 'Numărul de exprimare = 2 + 1 + 1 = **4**')
    para('024', 'Numărul de exprimare **4** îți propune temeinicie, ordine și rezultate care rezistă în timp. Poți face vizibilă valoarea ta printr-un proces clar, prin atenția la calitate și prin respectarea unei înțelegeri. Această direcție poate oferi un cadru ideilor și explicațiilor susținute de Numărul de realizare **3**. Umbra lui **4** este rigiditatea: să păstrezi o regulă după ce nu mai ajută sau să amâni începutul până ai organizat fiecare detaliu. Construiește un cadru suficient de stabil ca să lucrezi și suficient de flexibil ca să înveți.')
    para('024a', 'În dialog cu Destinul **10 / 1**, exprimarea **4** poate transforma inițiativa într-un lucru durabil. Direcția **1** spune „aleg și încep”, iar **4** întreabă „cum continui și cum verific?”. Pentru tine, un plan bun pornește dintr-o alegere proprie și se traduce în etape scurte, cu rezultate observabile. Nu lăsa organizarea să stingă inițiativa și nici entuziasmul să sară peste detaliile esențiale. Ritmul repetabil poate fi puntea dintre o idee personală și încrederea pe care o construiești în jurul ei.')
    sub('023a', '5.7. Codul numerologic al numelui')
    name_lines = []
    for comp in n['numarul_de_exprimare']['componente']:
        digits = ''.join(str(v['valoare']) for v in comp['valori'])
        letters = ' + '.join(v['litera']+str(v['valoare']) for v in comp['valori'])
        name_lines.append(comp['componenta']+' = '+letters+' → **'+digits+'**')
    personal = n['matricea_numelui']['meta']['codul_numelui']['sir']
    assert personal == '41573351139514659314'
    name_lines += ['Codul literelor numelui = **'+personal[:-1]+'**', 'Codul numerologic personal al numelui = '+personal[:-1]+' + 4 = **'+personal+'**']
    calc('011', *name_lines)
    put('G-002a', read_fragment('matrita-numelui-*-component.html'))
    para('023', 'Alina, comparând numele cu data nașterii, poți vedea unde exprimarea prin nume întâlnește o resursă nativă. Sunt susținute pe ambele planuri cifrele **1, 3, 4, 5, 6, 7 și 9**. Căsuța **2** există în data ta, dar nu are apariții în codul numelui; rămâne o resursă nativă pe care o poți cultiva prin ascultare și exprimarea emoțiilor. Căsuța **8** nu are apariții în niciuna dintre matrici și nu primește o interpretare suplimentară din nume.')
    para('023b', 'Numele aduce **5 apariții ale lui 1**, **4 ale lui 3**, **3 ale lui 4** și **4 ale lui 5**. Acestea întâlnesc energii deja prezente în matricea nativă și pot accentua inițiativa, comunicarea, nevoia de structură și libertatea de alegere. Privește tensiunea dintre ordine și mișcare ca pe o sarcină practică: păstrează cadrul, dar schimbă metoda când nu mai este utilă. Poți susține o direcție proprie fără să respingi contribuția altcuiva și poți explica o idee fără să ocupi tot spațiul conversației.')
    para('023c', 'Prin **6**, cu o apariție în fiecare matrice, poți lega exprimarea de grijă și de folosul concret. Prin **7**, cu două apariții native și una în nume, poți menține dialogul dintre cercetare și aplicare. Prin **9**, cu câte două apariții, poți sprijini sinteza și încheierea unei etape. Acordă atenție și energiei native **2**: numele nu îi adaugă apariții, dar tu poți păstra colaborarea vie prin întrebări directe și prin curajul de a spune ce simți. Matricile se citesc împreună, fără să transformi un număr de apariții într-o promisiune despre rezultate.')

    write_remaining(c)
    source = '---\ntitlu: Lucrare numerologică scurtă — Dangulea Alina Monica\ntemplate: scurt\nstatus: revizie\nversiune: V1.00R\npersoana: Dangulea Alina Monica\ndata_nasterii: 1994-07-25\nagent: The Scribe\n---\n\n' + '\n'.join(blocks)
    md_path = OUT / (STEM + '.md')
    md_path.write_text(source, encoding='utf-8', newline='\n')
    render(source)
    print(md_path)

def render(source):
    R.DIR = OUT
    R.PREFIX = PREFIX
    source = re.sub(r'\A---\n.*?\n---\n', '', source, count=1, flags=re.S)
    source = R.embed_markdown_images(source)
    body = R.add_heading_ids(R.render_markdown(source))
    body = re.sub(r'<p>Index: ([^<]+)</p>', r'<div class="idx">Index: \1</div>', body)
    body = R.convert_callouts(body)
    body = R.build_toc(body)
    body = re.sub(r'(?<!<div class="table-wrap">)(<table\b.*?</table>)', r'<div class="table-wrap">\1</div>', body, flags=re.S)
    body = R.apply_component_classes(body)
    body = R.wrap_tarot_figures(body)
    body = R.embed_sources(body)
    css = re.search(r'<style>(.*?)</style>', Path(str(MODEL)+'.html').read_text(encoding='utf-8'), re.S).group(1)
    css += '\nmain{overflow-wrap:anywhere}.matrix-main{overflow-wrap:normal}.active-cycle td{color:#b42318!important;font-weight:700!important}.active-cycle-cell{color:#b42318;font-weight:700}.tarot-profile-table p{margin:0}.element-analysis{display:block}.element-bars{width:100%}.table-wrap{max-width:100%;overflow-x:auto}figure{margin:18px 0}figcaption{text-align:center;color:var(--muted);font-style:italic}\n'
    out = '<!doctype html>\n<html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dangulea Alina Monica — 25.07.1994</title><style>'+css+'</style></head><body><header><div class="title">Dangulea Alina Monica · lucrare numerologică scurtă</div><div class="meta">Revizie V1.00R · 10.09.2026 · The Scribe</div></header><main>'+body+'</main></body></html>'
    (OUT/(STEM+'.html')).write_text(out,encoding='utf-8',newline='\n')

def write_remaining(c):
    cycles = c['2.4_ciclicitati']
    audit = json.loads((OUT/'audit-supliment-lore-2026-09-10.json').read_text(encoding='utf-8'))
    s = audit['spirit']
    assert (s['code'],s['substage'],s['birth_age'],s['current_age']) == (16,3,2835,2867)
    graphics = json.loads((OUT/'graphics-numeric-report.json').read_text(encoding='utf-8'))
    chapter('007b', 'Capitolul 6. Spirit și karmă — Lecții și direcții de maturizare')
    sub('038', '6.1. Codul Spiritului și vârsta Spiritului')
    para('182', 'Codul Spiritului se citește la intersecția zilei cu luna nașterii, în tabelul de mai jos. Prin el poți urmări zona simbolică de învățare și subetapa care oferă un fir de reflecție asupra experiențelor tale. Zona și subetapa se citesc pe două niveluri distincte: prima arată domeniul, iar a doua felul în care lucrezi lecția.')
    para('185', 'Alina, poziția ta este la ziua **25** și luna **VII**, unde se află **Codul Spiritului 16**. Celula turcoaz marchează exact această intersecție.')
    put('T-017', H.spirit_code_table(25,7))
    para('186', 'Codul **16** se află în zona **Rațiune, 14–26**. Poți citi această zonă ca pe o invitație să transformi experiențele în discernământ: să înțelegi motivele unei alegeri, să verifici ce este adevărat și să nu confunzi o explicație convingătoare cu o concluzie verificată. În dialog cu cele două vibrații **7**, accentul poate deveni foarte mental. Păstrează legătura cu emoția și cu efectul concret al deciziei, astfel încât gândirea să te ajute să trăiești mai clar.')
    put('T-018', '| Zonă | Coduri | Direcție de lucru |\n| --- | --- | --- |\n| <span class="zone-badge zone-love">Iubire</span> | 0–13 | Apropiere, înțelegere și echilibru afectiv. |\n| <span class="zone-badge zone-reason">Rațiune</span> | 14–26 | Discernământ, învățare și folosirea conștientă a gândirii. |\n| <span class="zone-badge zone-material">Material</span> | 27–39 | Aplicare, responsabilitate și relația cu resursele. |\n| <span class="zone-badge zone-gifts">Haruri</span> | 40–52 | Integrarea și transmiterea responsabilă a darurilor. |')
    put('T-019', H.spirit_stage_table(s['substage']))
    para('192', 'Subetapa ta este **3 — Căutarea echilibrului**, în **Etapa 1 — Înțelegere și stabilizare**. Lecția te invită să găsești măsura dintre centrul tău și lumea din jur: apropiere fără pierdere de sine, libertate fără ruperea legăturilor, reflecție fără retragere permanentă. Pentru tine, poate fi util să observi când protejezi o nevoie reală de liniște și când eviți o discuție care te-ar ajuta. Echilibrul se construiește prin ajustări repetate, nu printr-o poziție perfectă pe care trebuie să o menții mereu.')
    para('193', 'Vârsta Spiritului este un reper simbolic al acestei metode, distinct de vârsta biologică. O citești pornind de la codul tabelului și de la unitatea convențională de **189**, apoi adaugi anii împliniți pentru reperul actual. Nu este o măsurătoare a existenței tale și nu dovedește experiențe din alte vieți.')
    calc('003d', 'Codul Spiritului = **16**; subetapa = **3**', 'Vârsta Spiritului la naștere = (16 − 1) × 189 = **2.835 ani**', 'Vârsta Spiritului la 10.09.2026 = 2.835 + 32 = **2.867 ani**')
    para('197', 'O practică potrivită acestei lecturi este să îți oferi timp pentru înțelegere și apoi să revii în relație cu o propoziție clară: ce ai înțeles, ce simți și ce propui. Poți păstra gândirea atentă și poți rămâne accesibilă oamenilor. Când apar două nevoi care par opuse, caută o formă concretă în care fiecare primește un loc, de exemplu o pauză de reflecție urmată de o conversație stabilită.')
    sub('007a', '6.2. Karma din ziua de naștere')
    para('009a', 'Karma din ziua nașterii păstrează ziua calendaristică și îi asociază o Arcană Majoră în intervalul metodei. Pentru ziua **25**, lectura folosește **Arcana 3 — Împărăteasa** și intervalul convențional **spre 60%**, specific zilelor 20–29. Acest procent aparține limbajului simbolic al tradiției; nu măsoară vinovăția, probabilitatea unor evenimente sau valoarea unei persoane.')
    calc('001a', 'Ziua nașterii = **25**', 'Arcana zilei = 25 − 22 = **3 — Împărăteasa**', 'Intervalul 20–29 = **spre 60%**')
    put('G-001a', '![Arcana 3 — Împărăteasa](tarot-03-imparateasa.jpg)\n\n_Arcana 3 — Împărăteasa. Karma din ziua de naștere._')
    para('009b', 'Împărăteasa aduce în această lectură capacitatea de a crea, de a hrăni și de a transforma o intenție într-o formă vie. Alina, poți lucra această direcție printr-un proiect care crește cu atenție, printr-un spațiu făcut mai primitor sau printr-o relație în care grija este exprimată concret. Creativitatea poate însemna și o soluție practică, un text, un obiect sau un mod mai bun de a organiza munca; nu este limitată la artă ori maternitate.')
    para('009b1', 'Umbra poate apărea când grija devine control, când amâni o decizie pentru a păstra confortul sau când îți măsori valoarea numai prin ceea ce oferi. În dialog cu natura ta **7**, o idee poate rămâne mult timp protejată în minte. Las-o să primească o formă suficient de bună pentru a fi încercată și acceptă că dezvoltarea cere feedback, ajustări și uneori renunțarea la o variantă.')
    para('009b2', 'Maturizarea înseamnă să îngrijești fără să sufoci și să creezi fără să aștepți condiții perfecte. Alege ce vrei să crești, stabilește ce îi oferi constant și observă dacă acel efort aduce viață și pentru tine. Un gest repetat, o etapă terminată și un spațiu în care ceilalți pot contribui dau substanță acestei direcții.')
    sub('010a', '6.3. Karma din luna de naștere')
    para('013c', 'Karma lunii se citește din luna calendaristică, păstrată între **1 și 12**. Prin ea poți reflecta la relația cu originea, familia, locurile și felul în care te adaptezi. Pentru tine, interpretarea lunii **7** este numită **karma mobilității**. O folosești ca pe o direcție de învățare, fără să presupui că o mutare sau o profesie anume este obligatorie.')
    calc('002b', 'Luna nașterii = **7**', 'Karma lunii = **karma mobilității**')
    para('013d', 'Alina, această direcție te invită la mobilitate mentală și fizică: să poți ieși dintr-un cadru cunoscut, să întâlnești alte moduri de a gândi și să păstrezi deschiderea când contextul se schimbă. Poți lucra tema prin deplasări, proiecte cu oameni din alte medii, învățarea unei perspective noi sau schimbarea conștientă a unei rutine. Sursa tradițională leagă tema de locul de naștere și de o imagine a vieții anterioare; citește această imagine simbolic, fără să o transformi într-o poveste factuală despre tine.')
    para('013d1', 'Umbra mobilității are două capete: să rămâi într-un loc numai din teamă sau să schimbi mereu locul ca să eviți o problemă care te urmează. Înainte de o schimbare, clarifică ce cauți, ce condiții îți sunt necesare și ce poți încerca la scară mică. Reflecția lui **7** poate pregăti pasul, iar libertatea sugerată de ziua **25** îți poate aminti că o perspectivă nouă se câștigă și trăind experiența.')
    sub('012a', '6.4. Karma din Calea Destinului')
    para('015a', 'Karma din Calea Destinului păstrează suma tuturor cifrelor datei tale, **37**, pentru nuanța ei proprie. Nu o înlocuiești cu Destinul **10** sau cu cifra de interpretare **1**. Prin această lectură poți urmări imaginile simbolice ale sprijinului, obstacolelor și ale felului în care îți folosești alegerile. Asocierea Tarot a valorii **37** este **Arcana 15 — Diavolul**.')
    calc('003a', '2 + 5 + 0 + 7 + 1 + 9 + 9 + 4 = **37**', 'Karma din Calea Destinului = **37**', 'Asociere Tarot: 37 − 22 = **15 — Diavolul**')
    para('015b', 'Alina, sursa pentru **Calea Karmică 37** descrie simbolic un drum cu multe ajutoare și puține obstacole „prescrise”, folosind imaginea multor „bile albe” și a puținelor „bile negre”. Poți primi această imagine ca pe o invitație să observi sprijinul, să întreții relațiile bune și să folosești oportunitățile cu recunoștință, fără să presupui că viața îți garantează un parcurs ușor. Documentația leagă această cale de apropiere, prietenie și de posibilitatea ca o viață interioară îngrijită să deschidă și relația cu lumea socială. Imaginea tradițională a unui slujitor religios, propovăduitor sau pustnic într-o viață anterioară rămâne o metaforă a căutării sensului și a dedicării, nu un fapt despre trecutul tău. Referirea la tradițiile vedice poate fi citită ca interes pentru un limbaj spiritual și pentru studiu; nu stabilește superioritatea unei tradiții și nu înlocuiește cunoașterea verificată. Asocierea cu **Diavolul** aduce o întrebare complementară: de ce te atașezi atât de mult încât îți restrângi libertatea? Poate fi confortul unei explicații, validarea, controlul sau o promisiune făcută din impuls. Umbra nu este o condamnare, ci riscul de a lăsa un atașament să decidă în locul tău. Maturizarea se vede când primești ajutor fără să devii dependentă de el, păstrezi plăcerea fără să pierzi măsura și îți alegi angajamentele conștient. În dialog cu cele două vibrații **7**, cheia este să îți asculți lumea interioară și să îi verifici concluziile în relații reale, prin fapte, reciprocitate și libertatea de a spune atât „da”, cât și „nu”.')
    put('G-001b', '![Arcana 15 — Diavolul. Karma din Calea Destinului 37](tarot-15-diavolul.jpg)\n\n_Arcana 15 — Diavolul. Karma din Calea Destinului 37._')
    sub('012b', '6.5. Concluzie: direcția de lucru')
    para('015c', 'Firul care leagă aceste lecturi este libertatea folosită cu discernământ. Zona **Rațiune** te invită să înțelegi, subetapa **3** să cauți echilibrul, ziua **25** să dai o formă vie ideilor, iar luna **7** să rămâi mobilă în gândire și experiență. Calea **37** îți amintește să recunoști sprijinul și să nu îl transformi în dependență. Alina, poți pune toate acestea în lucru printr-o alegere clară, un pas practic și o conversație sinceră despre ceea ce ai nevoie.')

    chapter('010', 'Capitolul 7. Pinacluri: Oportunități și provocări')
    para('024b', 'Pinaclurile îți oferă patru intervale mari de viață, fiecare cu o Oportunitate și o Provocare. Oportunitatea arată o direcție de exprimare, iar Provocarea o capacitate de exersat. Pentru limita primului Pinaclu folosești **Destinul compus 10**, fără să îl reduci la cifra de interpretare; următoarele două intervale au câte zece ani inclusivi. Limitele se citesc la aniversare.')
    calc('013', 'Calea Destinului = **37** → Destinul = **10**', 'Limita Pinaclului 1 = 36 − 10 = **26 ani**', 'Intervale = **0–26 / 27–36 / 37–46 / 47+ ani**')
    pin = cycles['pinacluri']['randuri']
    put('T-003', table(['Pinaclu','Vârste','Oportunitate','Provocare'], [[f"Pinaclul {x['pinaclu']}",x['interval_varsta'],x['oportunitate'],x['provocare']] for x in pin]))
    para('024c', '**Pinaclul 1: 0–26 ani. Oportunitatea 5, Provocarea 0.** Poți privi prima parte a drumului prin tema explorării: experiențe, schimbări de perspectivă și învățarea libertății. Provocarea **0** nu înseamnă că nu există dificultăți; în această metodă, nu fixează o singură cifră de lucru. Privind în urmă, poți observa ce alegeri ți-au lărgit lumea și în ce situații mișcarea a avut nevoie de un reper stabil. Nu deducem evenimente biografice din acest interval.')
    para('024d', '**Pinaclul 2: 27–36 ani. Oportunitatea 3, Provocarea 2.** Intervalul dintre **25.07.2021 și 24.07.2031** te invită să exprimi, să creezi și să pui cunoașterea în contact cu oamenii. Provocarea **2** cere răbdare, colaborare și clarificarea emoțiilor. Poți fi pregătită să spui ceva valoros, dar să eziți din teama de reacția celuilalt. Exersează exprimarea într-un cadru potrivit, cere feedback concret și evită să transformi acordul tuturor într-o condiție a începutului.')
    para('024e', '**Pinaclul 3: 37–46 ani. Oportunitatea 8, Provocarea 2.** În lectura intervalului **25.07.2031–24.07.2041**, tema exprimării se poate lega mai mult de administrare, responsabilitate și rezultate. Căsuța nativă **8** este conservată, astfel că rolurile cu autoritate au nevoie de suport concret: reguli, competențe și colaboratori potriviți. Provocarea **2** păstrează importanța tactului și a acordurilor clare. Poți construi influență fără să confunzi fermitatea cu presiunea și fără să negociezi împotriva propriilor limite.')
    para('024f', '**Pinaclul 4: 47+ ani. Oportunitatea 3, Provocarea 2.** Din **25.07.2041**, lectura revine la exprimare și transmiterea experienței, cu aceeași invitație la cooperare matură. Poți folosi ceea ce ai învățat într-o formă mai selectivă: să explici, să creezi și să susții proiecte care merită timpul tău. Umbra poate fi repetarea unor promisiuni sau adaptarea la așteptări care nu te mai reprezintă. Alege ce vrei să dai mai departe și cu cine poți construi un schimb echilibrat.')
    para('024g', 'La **32 de ani**, ești în **Pinaclul 2**, cu **Oportunitatea 3** și **Provocarea 2**. Un pas potrivit acestei combinații este să faci vizibilă o parte din ceea ce știi, într-o formă care poate primi răspuns: o explicație, o propunere sau un proiect mic. Colaborarea devine mai ușoară când precizezi ce oferi, ce aștepți și până când. Astfel, exprimarea ta capătă un cadru, iar sensibilitatea îți poate susține mesajul.')

    chapter('011', 'Capitolul 8. Ciclicități')
    sub('024', '8.1. Soarta și Destinul')
    para('025', 'Graficul Soartă–Destin îți propune două linii de lectură a timpului. Numărul Sorții se obține înmulțind ziua și luna concatenate cu anul; pentru numărul Destinului grafic, zerourile din factorii inițiali sunt înlocuite cu 1 înainte de înmulțire. Aceste numere grafice sunt distincte de Destinul **10** din capitolul 3. Fiecare linie are propriul reper de confort, calculat ca media celor șapte cifre ale numărului grafic.')
    calc('006', 'Soarta = **2507 × 1994 = 4998958**', 'Destinul grafic = **2517 × 1994 = 5018898**', 'Confort Soartă = 52 ÷ 7 ≈ **7,43**', 'Confort Destin = 39 ÷ 7 ≈ **5,57**')
    put('G-005', '![Grafic Soarta și Destin pentru Dangulea Alina Monica](soarta-si-destin-dangulea-alina-monica.svg)')
    para('025a', 'Alina, cifrele Sorții sunt **4–9–9–8–9–5–8**, iar cele ale Destinului grafic **5–0–1–8–8–9–8**. Pe prima linie poți urmări simbolic alternanța dintre organizare, încheiere, responsabilitate și adaptare; pe a doua, mobilitatea întâlnește un prag de deschidere, inițiativa și apoi un accent pe asumarea rezultatelor. Cifra **0** nu adaugă o direcție separată; în această lectură poate reprezenta un spațiu de oprire, acumulare sau reorientare. Nu deducem din aceste valori evenimente obligatorii.')
    para('025b', 'Punctele graficului sunt așezate din **10 în 10 ani**, de la **0 la 60 de ani**. Între puncte, liniile sunt drepte; pentru vârsta actuală de **32 de ani**, lectura prin interpolare este **Soarta 8,2** și **Destinul grafic 8**. Ambele se află deasupra propriului reper de confort. Poți folosi această poziție ca pe o invitație la dozarea responsabilităților și la clarificarea rezultatelor urmărite, fără să o citești ca pe o măsură a norocului, veniturilor sau intensității reale a vieții tale.')
    para('025c', 'Curbele se întâlnesc la aproximativ **1 an**, **30**, **42** și **60 de ani**, în reprezentarea generatorului. Intersecția arată egalitatea valorilor desenate, nu dovada unui eveniment. La **30 de ani**, ambele linii au valoarea **8**; între **30 și 40**, linia Sorții urcă de la **8 la 9**, iar linia Destinului grafic rămâne la **8**. Dacă folosești această imagine pentru reflecție, întreabă-te ce responsabilitate merită păstrată și ce condiții te ajută să o susții.')
    para('025d', 'Pentru perioada prezentă, citește acest accent pe **8** împreună cu **Oportunitatea 3** și **Provocarea 2** din Pinaclul actual: explică limpede ce propui, negociază contribuțiile și urmărește un rezultat concret. Cum **8** este conservat în matricea nativă, un cadru exterior bine ales poate fi de folos. Un acord scris, un calendar realist și un moment de verificare a progresului pot susține asumarea fără să te împingă în control permanent. Graficul se încheie la 60 de ani; tabelele următoare continuă intervalul general al lucrării.')
    sub('025', '8.2. Anii importanți')
    para('026a', '**Anii importanți interiori** sunt repere prin care poți urmări schimbări pornite din tine: decizii, conștientizări, nevoi și moduri noi de a înțelege o experiență. Îi citești ca invitații la observație și reflecție, fără să presupui că fiecare an listat trebuie să aducă o ruptură.')
    years = cycles['ani_importanti_interiori_exteriori']
    para('026b', '**Șirul anilor importanți interiori:** ' + ' → '.join(map(str,years['interiori'])) + '.')
    para('026c', '**Anii importanți exteriori** îți propun repere pentru observarea contextelor, oamenilor și situațiilor la care răspunzi. O schimbare din afară poate solicita adaptare, dar felul în care alegi să o întâmpini rămâne important. Șirurile provin din implementarea iterativă a calculatorului și au statut de repere orientative, nu de calendar verificat al evenimentelor.')
    para('026d', '**Șirul anilor importanți exteriori:** ' + ' → '.join(map(str,years['exteriori'])) + '.')
    common = sorted(set(years['interiori']) & set(years['exteriori']))
    para('026e', 'În cele două șiruri se suprapun **' + ', '.join(map(str, common)) + '**. Anul **2026** apare în șirul interior, iar **2027** apare în ambele. Poți folosi acest lucru pentru a-ți formula întrebările: ce se schimbă în felul în care alegi și ce răspuns concret cere contextul? Nu este necesar să provoci o schimbare pentru a confirma lista; lasă experiența reală să decidă ce este relevant pentru tine.')
    sub('025a', '8.3. Lecțiile de viață')
    lessons = cycles['lectii_de_viata']['sir_lectii']
    para('028', 'Lecțiile de viață pornesc din produsul **zi × lună × an**. Păstrezi fiecare cifră, inclusiv **0**, în ordinea rezultatului și repeți șirul pe anii de viață. Fiecare coloană reprezintă o poziție din acest șir; fiecare an indică intervalul de la aniversarea din acel an până în ajunul aniversării următoare. În felul acesta poți urmări revenirea unei teme, fără să o transformi într-o predicție.')
    calc('014', '25 × 7 × 1994 = **348950**', 'Șirul lecțiilor = **3–4–8–9–5–0**')
    lesson_md = H.lesson_table(lessons,1994,108)
    lesson_md += '\n| 108 ani | 2102 |  |  |  |  |  |'
    lesson_md = lesson_md.replace('| Vârstă |', '| An de viață |').replace('| 108 ani |','| 109 (108 ani împliniți) |')
    put('T-008', lesson_md)
    para('028a', 'Între **25.07.2026 și 24.07.2027**, lecția ta este **8**. Ea îți propune să observi relația cu puterea personală, resursele și consecințele alegerilor: ce îți asumi, ce poți administra și ce rezultat urmărești. În șirul tău, **3** deschide exprimarea, **4** cere structură, **8** aduce asumarea, **9** încheierea, **5** adaptarea, iar **0** un spațiu de acumulare și reorientare, fără o direcție numerică separată. Tema actuală are nevoie de limite și criterii clare, mai ales când în jur apar multe cereri.')
    sub('027', '8.4. Ciclul de 9 ani')
    para('028d', 'Ciclul de 9 ani urmărește succesiunea anilor personali **1–9**, în convenția aniversară folosită de model. Fiecare an personal începe la **25 iulie** și se încheie la următoarea aniversare. Anul din tabel este anul de început al intervalului. Poți citi fiecare rând ca pe un ciclu, de la inițiere la încheiere, iar coloana îți arată tema anului din acel ciclu.')
    para('028e', 'Acest ritm îți poate oferi un mod de a pune întrebări despre proiecte și relații: când inițiezi, când construiești, când clarifici și când închei? Tabelul nu îți impune acțiunea și nu înlocuiește condițiile reale în care iei o decizie. Folosește tema ca punct de reflecție și verifică ce se potrivește experienței tale.')
    para('028g', '- **Anul 1:** inițiezi și îți asumi o direcție.\n- **Anul 2:** asculți, cooperezi și construiești acorduri.\n- **Anul 3:** exprimi, cercetezi și pui ideile în circulație.\n- **Anul 4:** organizezi și consolidezi.\n- **Anul 5:** explorezi și te adaptezi.\n- **Anul 6:** îngrijești relațiile și alegi responsabilități.\n- **Anul 7:** aprofundezi și clarifici.\n- **Anul 8:** administrezi resursele și urmărești consecințele.\n- **Anul 9:** închei, reorganizezi și eliberezi ce nu mai servește.')
    cycle9 = cycles['ciclul_de_9_ani']
    rows = []
    for start in range(0,len(cycle9),9):
        items = cycle9[start:start+9]
        cells = [f'C{start//9+1} ({start}–{min(start+8,108)} ani)']
        cells += [f'<span class="active-cycle-cell">{x["an"]}</span>' if x['an']==2026 else str(x['an']) for x in items]
        cells += ['']*(10-len(cells))
        rows.append(cells)
    put('T-007', table(['Ciclu (vârstă)']+[f'Anul {i}' for i in range(1,10)],rows,'nine-year-table'))
    current = next(x for x in cycle9 if x['an']==2026)
    assert current['an_personal'] == 6 and current['lectie'] == 8
    para('027', 'Alina, la data lucrării ești în **ciclul 4**, în **anul personal 6**, pentru intervalul **25.07.2026–24.07.2027**. Tema lui **6** pune accent pe grijă, relații apropiate și responsabilități pe care le poți susține. Împreună cu lecția **8**, ea te invită să observi cât oferi, în ce condiții și cu ce resurse. Poți avea grijă fără să preiei tot, iar un angajament clar este mai folositor decât o promisiune făcută din vinovăție.')
    sub('027a', '8.5. Ciclul de 12 ani')
    para('027b', 'Ciclul de 12 ani îți oferă o perspectivă mai largă asupra felului în care îți extinzi lumea și reorganizezi experiența. Citești intervalele ca etape de reflecție adaptate vârstei. Reperele calendaristice pornesc de la aniversare; rândul roșu este cel în care te afli la **10.09.2026**. Ultimul rând arată începutul ciclului următor, la limita de 108 ani a lucrării, fără să sugereze o durată de viață.')
    readings = ['Îți formezi primele repere prin explorare, relații apropiate și un cadru care îți permite să întrebi.', 'Îți testezi autonomia, valorile și apartenența; înveți să separi alegerea ta de așteptările grupului.', 'Îți poți extinde experiența prin proiecte, relații și alegeri asumate; verifici ce direcții merită consolidate.', 'Poți reorganiza munca și responsabilitățile pe baza experienței, alegând mai clar unde investești energie.', 'Poți rafina ce ai construit și poți face loc transmiterii competenței, cu limite mai atente față de solicitări.', 'Poți reechilibra ritmul, contribuția și timpul personal, păstrând activitățile cu sens pentru tine.', 'Poți pune accent pe sinteză, legături apropiate și transmiterea experienței într-o formă accesibilă.', 'Poți simplifica angajamentele și păstra continuitatea relațiilor și a practicilor care îți sunt potrivite.', 'Poți privi experiența ca pe un patrimoniu personal, cu atenție la sprijinul și ritmul concret de care ai nevoie.', 'La limita analizei începe un nou interval convențional; reperul continuă metoda, fără predicții despre longevitate.']
    lines = ['| Ciclu | Interval calendaristic | Vârste | Citire |','| --- | --- | --- | --- |']
    for i,x in enumerate(cycles['ciclul_de_12_ani']):
        a,b=map(int,x['interval_varsta'].split('-'))
        vals=[f'C{i+1}',f'{1994+a}–{1994+b}',f'{a}–{b}',readings[i]]
        if a<=32<=b:
            vals=[f'<span class="active-cycle-cell">{v}</span>' for v in vals]
        lines.append('| '+' | '.join(vals)+' |')
    put('T-015','\n'.join(lines))
    para('027a', 'Ești în **ciclul 3 de 12 ani**, la vârstele **24–35**, între **25.07.2018 și 24.07.2030**. Poți folosi această etapă pentru a transforma explorarea în alegeri pe care le susții: ce înveți mai profund, ce relații întreții și ce proiecte capătă o formă stabilă? În prezent, exprimarea din Pinaclul **2**, anul personal **6** și lecția **8** se pot reuni într-un pas simplu: să clarifici un angajament și să îi dai un cadru realist.')

    chapter('015', 'Capitolul 9. Concluzii')
    sub('030', '9.1. Carieră și bani')
    career = [
        'Alina, firul profesional al lucrării pornește din **7–7**: poți avea nevoie să înțelegi temeinic și să lucrezi cu sens. Cele **3 apariții ale lui 3**, cele **2 ale lui 7** și cele **2 ale lui 9** adaugă prelucrarea informației, analiza și sinteza. În această hartă, valoarea ta poate deveni vizibilă când transformi o problemă complexă într-o explicație clară și într-un rezultat folositor.',
        'Această combinație poate fi pusă la lucru în activități de analiză, cercetare, documentare, scris, instruire, proiectare sau îmbunătățire a unor procese. Sunt direcții simbolice de explorat în raport cu pregătirea și interesele tale reale, nu o selecție a profesiei potrivite făcută numai din numere. Observă în ce activitate poți uni curiozitatea cu un folos concret și în ce mediu ai timp să verifici calitatea.',
        'Destinul **10 / 1**, Numărul activ **1** și Numărul intim **1** susțin nevoia unei contribuții care îți aparține. Te poate ajuta să ai un domeniu clar de decizie, chiar într-o echipă: o întrebare pe care o duci până la capăt, un proces de care răspunzi sau un proiect pe care îl coordonezi. Autonomia este mai ușor de susținut când știi ce poți decide și unde ai nevoie de acordul altcuiva.',
        'Numărul de realizare **3** te invită să faci munca ușor de înțeles. O analiză valoroasă care rămâne numai în mintea ta poate trece neobservată. Pregătește o prezentare scurtă a problemei, a soluției și a efectului urmărit. Oamenii au nevoie să poată vedea ce aduci și cum pot folosi rezultatul, fără să fie obligați să refacă întregul tău traseu de cercetare.',
        'Numărul de exprimare **4** oferă o cheie de continuitate: proceduri simple, etape și criterii de finalizare. Matricea are câte o apariție în **4, 5 și 6**, deci vectorul **456** este complet, însă intensitatea lui nu este aceeași cu a vectorului Energie. Ai resurse pentru concret, dar merită să le protejezi printr-un ritm realist. Nu transforma organizarea într-un proiect mai mare decât munca pe care ar trebui să o susțină.',
        'Imaginea cailor, trăsurii și vizitiului poate clarifica această relație: vectorul **123** are **6 apariții**, vectorul **456** are **3**, iar vectorul **789** are **4**. Poți avea multe idei și o capacitate bună de a porni, în timp ce cadrul practic cere mai multă grijă. Alege un singur rezultat principal, împarte-l în etape și verifică dacă ritmul poate fi menținut. Energia devine folositoare când trăsura o poate duce.',
        'În Scara bunăstării, **369 = 33** este prima treaptă. Relaționarea și informația, pragmatismul și sinteza pot susține împreună satisfacția de a produce ceva util. Pentru relația cu banii, această lectură te invită să poți numi valoarea concretă a muncii tale: ce problemă rezolvi, pentru cine și prin ce rezultat. Cifrele nu stabilesc venitul; îți oferă o întrebare despre felul în care îți transformi competența în contribuție.',
        'Treapta **789 = 32** aduce creativitatea aproape de bunăstarea materială, iar **357 = 28** pune accent pe scop. Poți găsi mai multe soluții, dar nu toate merită urmărite simultan. Alege după utilitate, resurse și interes real. Când îți stabilești scopul, păstrează un criteriu de oprire: cum vei ști că ai lucrat suficient și că este momentul să livrezi?',
        'Căsuța **8** este conservată. În roluri care cer negociere, autoritate sau administrarea resurselor, sprijinul exterior poate fi important: un mentor competent, responsabilități scrise și instrumente simple de urmărire. Poți exersa gradual o conversație despre valoarea muncii sau o decizie pentru care răspunzi. Această construcție nu îți micșorează potențialul; îi oferă condiții în care să devină mai constant.',
        'Numărul ereditar karmic **7**, cu imaginea cunoașterii și a descoperirii, se întâlnește cu natura ta analitică. Îl poți folosi ca motivație pentru a îmbunătăți ceva ce există deja, pentru a documenta bine sau pentru a face învățarea mai accesibilă. Asocierea cu **Carul** îți amintește că o direcție clară este necesară: studiul capătă sens când alegi unde îl aplici.',
        'Riscul principal al acestei combinații poate fi distanța dintre competență și exprimare: să știi mult, dar să amâni să arăți; să îți dorești autonomie, dar să eviți o negociere; să cauți o explicație perfectă, dar să pierzi momentul unei încercări. Alege un experiment cu miză potrivită, arată ce ai făcut și cere un feedback precis. Poți păstra exigența fără să îi ceri primei versiuni să fie definitivă.',
        'O direcție profesională coerentă pentru această hartă unește **studiul, explicația și construcția practică**. Te poate susține un mediu care respectă calitatea, oferă autonomie și are acorduri clare. Ceea ce ai de construit conștient este trecerea de la înțelegere la vizibilitate și asumare: să formulezi oferta, să finalizezi și să rămâi în dialog cu oamenii care folosesc munca ta.'
    ]
    for i,text in enumerate(career):
        para('032'+('' if i==0 else chr(96+i)),text)
    sub('032', '9.2. Momentul prezent')
    present = [
        'La **10.09.2026**, ai **32 de ani**. Între **25.07.2026 și 24.07.2027**, lecția activă este **8**: asumarea puterii personale, administrarea resurselor și atenția la consecințe. Începe prin a observa ce responsabilități sunt ale tale și care au ajuns la tine fără un acord clar. O limită exprimată la timp poate proteja atât munca, cât și relațiile.',
        'În același interval aniversar, te afli în **anul personal 6**, în **ciclul 4 de 9 ani**. Tema grijii și a responsabilității poate fi pusă în dialog cu lecția **8**: cum poți oferi fără să preiei tot și cum poți administra fără să transformi totul în control? Un angajament bine definit îți lasă loc să fii prezentă și să îți păstrezi energia.',
        'Pinaclul actual este **2**, cu **Oportunitatea 3** și **Provocarea 2**, la vârstele **27–36**. Exprimarea și colaborarea au nevoie una de cealaltă. Dacă ai o propunere importantă, formuleaz-o într-o formă ușor de discutat și precizează ce feedback te-ar ajuta. Nu aștepta să dispară orice emoție înainte să vorbești și nu lua o diferență de opinie drept refuz al persoanei tale.',
        'Pe grafic, la **32 de ani**, **Soarta 8,2** și **Destinul grafic 8** sunt deasupra mediilor lor de confort, **7,43** și **5,57**. Aceste poziții provin din desenul liniar al metodei și pot fi folosite ca metaforă pentru dozarea asumării. Cum energia nativă **8** este conservată, ajută să alegi un cadru care te sprijină: reguli simple, verificarea resurselor și oameni cu care poți clarifica responsabilitatea.',
        'Ciclul de **12 ani** activ este **C3**, la vârstele **24–35**, până în ajunul aniversării din **2030**. El oferă un cadru mai larg pentru extinderea experienței și alegerea direcțiilor care merită consolidate. Mobilitatea lunii **7** nu cere schimbare de dragul schimbării; poți lărgi perspectiva și printr-un proiect nou, o colaborare sau un mod diferit de a învăța.',
        'Anul **2026** apare între reperele interioare, iar **2027** în ambele șiruri de ani importanți. Privește aceste repere cu măsură și lasă realitatea să îți arate ce este relevant. Poți nota ce alegere se clarifică în tine, ce condiții exterioare o susțin și ce informație îți mai lipsește. Lista anilor nu te obligă să iei o decizie înainte să fie pregătită.',
        'Pentru următoarea perioadă, alege un rezultat pe care îl poți termina, clarifică un angajament care te solicită și rezervă timp pentru studiu urmat de aplicare. Aceste trei gesturi leagă analiza lui **7**, inițiativa lui **1**, exprimarea lui **3** și structura lui **4**. Nu trebuie să faci totul simultan; urmărește dacă pașii aleși aduc mai multă claritate și continuitate.',
        'Alina, firul prezentului poate fi exprimat simplu: **fă vizibil ceea ce înțelegi și asumă numai ceea ce poți susține**. Când îți explici intenția, ceri contribuția potrivită și verifici rezultatul, profunzimea ta poate deveni un sprijin concret pentru tine și pentru ceilalți. Harta îți oferă teme de observat; sensul lor se construiește prin experiența și alegerile tale.'
    ]
    for i,text in enumerate(present):
        para('033'+chr(97+i),text)
    chapter('016', 'Documentația și trasabilitatea lucrării')
    put('T-014', table(['Componentă','Sursă și verificare'],[
        ['Identitate','Dangulea Alina Monica; 25.07.1994; feminin; prenume activ Alina — date furnizate de utilizator. Numele anterior și date relaționale nu au fost comunicate.'],
        ['Structură și stil','Modelul scurt Daniel Robert V1.00R; structură individuală cu 9 capitole, fără capitolele condiționale pentru relație.'],
        ['Calcule personale',STEM+'-calculator.json; generat pentru intervalul 1994–2102. Destinul compus, numerele de lucru, numele, Pinaclurile și lecțiile sunt preluate din acest raport.'],
        ['Spirit și elemente','audit-supliment-lore-2026-09-10.json, The Lore Keeper: codul 16 și subetapa 3 confirmate punctual din tabel și helper. Agregatorul păstrează codul 5 într-o rubrică parțială, neconformă cu metoda tabelului; nu a fost modificat.'],
        ['Grafice','The Cartographer: graphics-numeric-report.json și scriptul generate_alina_graphics.py; concordanță numerică și validare XML. Soartă–Destin folosește generatorul dedicat, deoarece agregatorul are rubrica incompletă.'],
        ['Interpretări canonice','NEKI-NN-7 păstrată integral în paragraful din tabel; KLNI-LL-7 și KCDI-NN-37 adaptate conversațional, cu încadrarea simbolică a afirmațiilor tradiționale.'],
        ['Limite','Anii importanți au statut de implementare inițială în calculator. Rubricile neimplementate care nu aparțin structurii scurte nu primesc valori inventate. Ciclul C10 de 12 ani este afișat pentru contextul limitei de 108 ani.'],
        ['Redare','Markdown și HTML provin din aceeași sursă. HTML autonom cu imagini încorporate; indici de revizie păstrați pentru corecturi.']
    ]))

if __name__ == '__main__':
    main()
