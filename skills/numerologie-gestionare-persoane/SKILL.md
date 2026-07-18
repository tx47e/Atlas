---
name: numerologie-gestionare-persoane
description: Colectează conversațional, validează, salvează, actualizează, listează și încarcă fișe YAML pentru persoanele analizate numerologic, inclusiv ora opțională a nașterii. Folosește când utilizatorul cere adăugarea unei persoane, completarea datelor personale pe rând, corectarea unei fișe existente, selectarea unei persoane pentru The Scribe sau gestionarea întrebărilor, preferințelor de lucrare și relațiilor sale.
---

# Gestionarea persoanelor

## Reguli obligatorii

1. Folosește `Atlas/persoane` ca registru canonic. Nu folosi `Dashboard/persoane.txt` și nu salva fișele în `output/lucrari`.
2. Citește [[skills/numerologie-gestionare-persoane/references/schema-persoana|Schema fișei unei persoane]] înainte de creare sau actualizare.
3. Pune o singură întrebare pe mesaj și validează răspunsul înainte de întrebarea următoare.
4. Nu deduce genul, prenumele activ, numele anterior, ora nașterii sau tipul relației din nume ori din alte date.
5. Nu scrie nimic înainte de a afișa rezumatul complet și de a primi o confirmare explicită.
6. Rulează `scripts/gestioneaza_persoane.py` pentru identificatori, validare, salvare, listare și încărcare. Nu construi manual identificatorul.
7. Nu crea directorul din `output/lucrari` decât atunci când începe efectiv o lucrare.

## Adăugarea unei persoane

Întreabă, câte un câmp pe rând, în această ordine:

1. numele complet;
2. numele de familie;
3. prenumele sau prenumele complete;
4. prenumele activ;
5. data nașterii în format `ZZ.LL.AAAA`;
6. ora nașterii în format `HH:MM`, dacă este cunoscută; dacă nu este cunoscută, salvează `null` fără să o deduci;
7. genul: `masculin` sau `feminin`;
8. numele anterioare, dacă există;
9. template-ul implicit disponibil;
10. exprimarea: `conversational` sau `formal`;
11. nivelul de detaliere: `scurt`, `mediu` sau `amplu`;
12. intervalul implicit: complet `0-108` sau specific;
13. întrebările clientului, repetând categoria și textul până la răspunsul `gata`;
14. relațiile, repetând datele fiecărei relații până la răspunsul `gata`.

Pentru o relație cu o persoană absentă din registru, salvează numele, data cunoscută și tipul cu `status: provizorie` și `persoana_id: null`. Nu începe automat colectarea celeilalte persoane.

Construiește documentul complet în memorie, afișează-l ca rezumat ușor de citit și întreabă exact dacă poate fi salvat. După confirmare, scrie un fișier temporar YAML sau JSON și rulează:

```powershell
python scripts/gestioneaza_persoane.py save --input <fisier-temporar> --confirmat
```

Șterge fișierul temporar după salvarea reușită. Scriptul creează `persoane/AAAA-LL-ZZ-NUME-COMPLET/persoana.yaml`.

## Actualizarea unei persoane

1. Încarcă fișa cu `show <id>`.
2. Întreabă numai câmpurile care trebuie schimbate, unul pe rând.
3. Păstrează toate câmpurile nemodificate, inclusiv ora nașterii, întrebările și relațiile.
4. Afișează diferențele și cere confirmare explicită.
5. Salvează documentul complet cu `save --actualizare --confirmat`.

Nu adăuga sufixe pentru o coliziune exactă de nume și dată. Tratează identificatorul existent ca actualizare și cere clarificare dacă utilizatorul susține că este altă persoană.

## Selectarea pentru The Scribe

Folosește `list` pentru a găsi persoana și `show <id>` pentru a încărca fișa. Transmite identitatea și preferințele către `numerologie-lucrare-redactare`. Opțiunile cerute pentru lucrarea curentă pot suprascrie temporar preferințele, dar nu actualiza fișa decât la cererea explicită a utilizatorului.

## Comenzi

Rulează comenzile din rădăcina Atlas:

```powershell
python skills/numerologie-gestionare-persoane/scripts/gestioneaza_persoane.py build-id --data-nasterii 1998-01-12 --nume-complet "Roman Andreea Maria"
python skills/numerologie-gestionare-persoane/scripts/gestioneaza_persoane.py list
python skills/numerologie-gestionare-persoane/scripts/gestioneaza_persoane.py show 1998-01-12-ROMAN-ANDREEA-MARIA
python skills/numerologie-gestionare-persoane/scripts/gestioneaza_persoane.py validate persoane/1998-01-12-ROMAN-ANDREEA-MARIA/persoana.yaml
```

Dacă importul YAML eșuează, instalează dependența din `requirements.txt` înainte de a continua.
