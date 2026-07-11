# 2026-07-11 16:50 - Feedback SVG si status skill-uri

## Rol memorie Agent 001

Agent 001 se ocupa doar de SVG-uri numerologice. In `memory/` se noteaza feedback-ul acumulat din SVG-urile create sau editate, ca sa fie reutilizat la lucrari viitoare.

Memoria locala trebuie sa includa:

- ce SVG a fost creat sau modificat;
- ce problema vizuala sau de calcul a aparut;
- ce regula s-a stabilit dupa feedback;
- ce fisier generator/template/reference a fost afectat;
- daca skill-ul aferent este actual sau trebuie actualizat.

## Feedback acumulat din SVG-uri

### Harta suprapusa - Birsan Daniel Robert

Fisiere relevante:

- `output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/harta-suprapusa-soarta-destin-birsan-daniel-robert-v2.svg`
- `scripts/gen_harta_suprapusa_bdr_v2.py`

Feedback stabilizat:

- Varianta V2 este varianta principala si completa.
- Graficul se pastreaza pe intervalul `0-108 ani`.
- Valorile Soarta si Destin se afiseaza in randuri sub axa X, nu peste punctele din grafic.
- Ciclul 7 se marcheaza jos cu triunghiuri, ciclul 9 si ciclul 12 cu patrate, pinaclurile cu patrate mustar.
- Oportunitatea si provocarea pinaclurilor se traseaza in trepte, nu diagonal.
- Linia in trepte pentru oportunitate/provocare trebuie sa schimbe valoarea la inceputul pinaclului urmator, adica la aceeasi varsta cu linia punctata si patratul de sub grafic.
- Pentru Daniel, granițele corecte sunt `0`, `34`, `43`, `52`, `108`.
- Liniile punctate pentru pinacluri trebuie sa fie aliniate cu verticalele din traseul O/P de pe grafic.
- SVG-ul trebuie validat ca XML dupa fiecare regenerare.

### Harta suprapusa - Szabo Mihai Gabriel

Fisiere relevante:

- `output/lucrari/1984-11-06-SZABO-MIHAI-GABRIEL/harta-suprapusa-soarta-destin-szabo-mihai-gabriel.svg`
- `scripts/gen_harta_suprapusa_szabo_mihai_gabriel.py`

Feedback stabilizat:

- Calcule confirmate pentru `06.11.1984`:
  - Soarta: `1212224`
  - Destin: `3196224`
  - Lectii de viata: `130944`
  - Pinacluri: `0-33 O8/P4`, `34-42 O1/P2`, `43-51 O9/P2`, `52-108 O6/P2`
- Si aici linia in trepte pentru oportunitate/provocare trebuie sa schimbe valoarea la `34`, `43`, `52`, nu la `33`, `42`, `51`.
- Etichetele de jos pentru pinacluri trebuie sa corespunda inceputului fiecarui pinaclu: `1984`, `2018`, `2027`, `2036`.
- SVG-ul trebuie validat ca XML dupa regenerare.

### Omuletul relatiilor

Fisiere relevante:

- `output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/omulet-relatii-birsan-daniel-robert-roman-andreea-maria.svg`
- `output/lucrari/1998-01-12-ROMAN-ADREEA-MARIA/omulet-relatii-birsan-daniel-robert-roman-andreea-maria.svg`
- `skills/numerologie-SVG-omuletul-relatiilor/assets/reference.svg`

Feedback stabilizat:

- SVG-ul trebuie preluat 1 la 1 dupa referinta skill-ului; nu se improvizeaza structura.
- Se schimba doar datele persoanelor si valorile calculate, pastrand compozitia, pozitiile si stilul din referinta.
- Daca o varianta generata nu respecta referinta, se sterge complet si se regenereaza curat.

Status skill:

- `numerologie-SVG-omuletul-relatiilor` este considerat actual cat timp referinta ramane sursa vizuala principala.

### Patratul de aur

Fisiere relevante:

- `output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/patratul-de-aur-birsan-daniel-robert.svg`
- `output/lucrari/1998-01-12-ROMAN-ADREEA-MARIA/patratul-de-aur-roman-adreea-maria.svg`
- `skills/numerologie-SVG-patratul-de-aur/assets/reference.svg`

Feedback stabilizat:

- Se foloseste formatul din skill/reference, cu datele persoanei inlocuite fara alterarea compozitiei.
- Dupa generare se verifica lizibilitatea textelor si validitatea XML.

Status skill:

- `numerologie-SVG-patratul-de-aur` este considerat actual pana apare feedback nou.

### Semnatura astrala

Fisiere relevante:

- `output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/semnatura-astrala-birsan-daniel-robert.svg`
- `output/lucrari/1998-01-12-ROMAN-ADREEA-MARIA/semnatura-astrala-roman-adreea-maria.svg`
- `skills/numerologie-SVG-semnatura-astrala/assets/reference.svg`

Feedback stabilizat:

- Se pastreaza structura reference-ului si se modifica doar datele numerologice calculate.
- SVG-ul trebuie verificat vizual pentru suprapuneri si validat ca XML.

Status skill:

- `numerologie-SVG-semnatura-astrala` este considerat actual pana apare feedback nou.

### Triunghiul financiar

Fisiere relevante:

- `output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/triunghiul-financiar-birsan-daniel-robert.svg`
- `output/lucrari/1998-01-12-ROMAN-ADREEA-MARIA/triunghiul-financiar-roman-adreea-maria.svg`
- `skills/numerologie-SVG-triunghiul-financiar/assets/reference.svg`

Feedback stabilizat:

- Se genereaza dupa reference-ul skill-ului, cu datele persoanei si calculele inlocuite.
- Nu se schimba geometria de baza fara feedback explicit.

Status skill:

- `numerologie-SVG-triunghiul-financiar` este considerat actual pana apare feedback nou.

### Septagrama

Fisiere relevante:

- `output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/septagrama-birsan-daniel-robert.svg`
- `skills/numerologie-SVG-septagrama/assets/reference.svg`

Feedback stabilizat:

- Se foloseste referinta skill-ului pentru ciclul de 7 ani si momentele de criza.
- Etichetele trebuie sa ramana lizibile si aliniate cu marcajele ciclului.

Status skill:

- `numerologie-SVG-septagrama` este considerat actual pana apare feedback nou.

### Soarta si destin

Fisiere relevante:

- `output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/soarta-si-destin-birsan-daniel-robert.svg`
- `skills/numerologie-SVG-soarta-si-destin/assets/reference.svg`

Feedback stabilizat:

- Se foloseste reference-ul skill-ului pentru graficul Soarta/Destin simplu.
- Valorile si zona de confort trebuie sa fie consistente cu datele folosite in harta suprapusa.

Status skill:

- `numerologie-SVG-soarta-si-destin` este considerat actual pana apare feedback nou.

### Dashboard

Feedback:

- Dashboard-ul nu se mai prelucreaza pana cand SVG-ul static de referinta nu este stabilizat.
- Implementarea dinamica din dashboard trebuie reluata doar dupa validarea finala a SVG-urilor statice.
- Cand va fi reluat dashboard-ul, algoritmul trebuie copiat din skill/template si verificat impotriva SVG-urilor statice validate.

## Status skill-uri

Skill-uri locale disponibile pentru Agent 001:

- `numerologie-SVG-harta-suprapusa`
- `numerologie-SVG-omuletul-relatiilor`
- `numerologie-SVG-patratul-de-aur`
- `numerologie-SVG-semnatura-astrala`
- `numerologie-SVG-septagrama`
- `numerologie-SVG-soarta-si-destin`
- `numerologie-SVG-triunghiul-financiar`

Status curent:

- `numerologie-SVG-harta-suprapusa` este actual ca intentie si structura, dar trebuie actualizat din nou la final daca modificarile recente de aliniere a pinaclurilor raman validate.
- Celelalte skill-uri sunt considerate actuale pana apare feedback nou pe SVG-urile lor.

## Regula de actualizare skill

Nu se actualizeaza skill-ul dupa fiecare micro-ajustare vizuala. Se actualizeaza doar dupa ce utilizatorul confirma ca varianta SVG este buna si regula trebuie pastrata pentru viitor.
