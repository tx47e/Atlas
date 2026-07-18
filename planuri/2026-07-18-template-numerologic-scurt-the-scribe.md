# Template numerologic „scurt” pentru The Scribe

## Rezumat

Se creează o pereche reutilizabilă Markdown–HTML cu cheia `scurt`, bazată pe cele 9 capitole din lucrarea `Micu (Ivan) Ana Maria 05.09.1983.md`, extinsă condițional cu un capitol pentru Omulețul relațiilor între Lecțiile de viață și Concluzii. Template-ul existent `examen` și lucrarea-sursă rămân nemodificate.

Noul template păstrează structura scurtă a lucrării-model, dar preia carcasa editorială și vizuală a template-ului de examen: frontmatter, Date generale, Cuprins, Cuvânt înainte, chenare de calcul, indexarea revizie/final, stilurile HTML, navigarea, tipărirea și validările.

## Modificări

- Se creează `Template_Lucrare_Numerologica_Scurt.md` și `.html` în `templates/`, apoi copii identice în resursele `numerologie-lucrare-redactare`.
- Structura conține:
  1. Vibrația interioară, inclusiv Tarot;
  2. Vibrația exterioară;
  3. Destinul;
  4. Matrița numerologică;
  5. Numele și neamul;
  6. Oportunități și provocări;
  7. Soarta și Destinul;
  8. Lecțiile de viață;
  9. Relații — Omulețul relațiilor, dacă sunt furnizate datele celei de-a doua persoane;
  10. Concluzii.
- Markdown-ul este optimizat pentru Obsidian: frontmatter, titluri cu diacritice, Cuprins cu wikilinkuri către heading-uri exacte, embeduri Obsidian pentru arcane, callout-uri/chenare și fără fragmente HTML de prezentare.
- Capitolul „Matrița numerologică” include obligatoriu pătratul matriceal 3×3 după modelul vizual `BDR-19980219-v1.07r-G-001`, imediat după chenarul cu data compactă, `N1`, `N2`, `N3`, `N4` și șirul complet. Ordinea căsuțelor este `1–4–7 / 2–5–8 / 3–6–9`; fiecare căsuță afișează cifra, repetițiile calculate, reperul optim, culoarea elementului și simbolul geometric sau starea absentă. În Markdown se folosește un tabel 3×3 compatibil Obsidian, iar în HTML se păstrează structura și stilurile `matrix-grid`/`matrix-cell` din lucrarea de examen.
- Cele șapte capturi de tabele sunt înlocuite cu tabele editabile:
  - două tabele pentru codul numelui;
  - ani interiori;
  - ani exteriori;
  - ciclul de 7 ani;
  - ciclul de 9 ani;
  - lecțiile de viață.
- Tabelele folosesc câmpuri generice și păstrează marcajele semantice necesare: totaluri, anul evidențiat, începuturile și finalurile ciclurilor și lecția activă.
- Tarotul este dinamic: fiecare secțiune care numește o arcană conține și câmpul imaginii corespunzătoare din `vault/tarot/imagini`. Markdown-ul folosește embed Obsidian, iar lucrarea HTML generată încorporează imaginea ca data URI, cu legendă și text alternativ.
- Capitolul relațional se construiește după metoda din lucrarea lui Daniel. Imediat după titlu afișează blocul factual cu numele complet, data nașterii și tipul relației, apoi subcapitolul „Omulețul relațiilor”, introducerea care definește lectura drept hartă de orientare și nu verdict, SVG-ul validat, calculul „realizare împreună” și „de rezolvat împreună”, urmat de interpretarea personalizată.
- SVG-ul Omulețului relațiilor este generat de The Cartographer exclusiv cu `numerologie-SVG-omuletul-relatiilor`, din numele și datele de naștere ale ambelor persoane. Se păstrează geometria Vitruviană validată, distribuția cifrelor brute `0–9`, culorile distincte ale persoanelor, sinteza elementelor și watermark-ul exact `Atlas Numerologie`; SVG-ul nu se editează manual după generare.
- Interpretarea relațională acoperă contribuția fiecărei persoane, cifrele și elementele comune, dominantele, complementaritățile, rezultatul comun și tema de rezolvat. Zonele absente sunt grupate în recomandări concrete, fiecare urmată de cifra corespunzătoare în paranteză; se explică atât construirea intenționată în cuplu, cât și aportul extern posibil prin contexte, oameni, activități sau instrumente potrivite.
- În Markdown, Omulețul relațiilor este inclus ca imagine SVG normală, cu legendă. În HTML autonom se folosește `figure > img.embedded-svg + figcaption`, cu SVG-ul încorporat ca `data:image/svg+xml;base64,...`; nu se adaugă o imagine PNG duplicată.
- HTML-ul folosește carcasa canonică a examenului: copertă/topbar, Cuprins cu ancore HTML, aceeași paletă și tipografie, chenare de calcul, tabele responsive, stiluri pentru ecran și imprimare și paritate semantică cu Markdown-ul.
- Se elimină din template toate datele și interpretările personale ale Anei; rămân instrucțiuni editoriale și câmpuri de completat.
- Harta template-urilor și skill-ul primesc ruta explicită `scurt` către noua pereche.
- Configurația YAML, documentația și promptul The Scribe sunt sincronizate pentru a recunoaște `scurt` ca tip disponibil, fără a duplica integral conținutul template-ului în fișierul agentului.

## Interfețe

- Cheie de selecție: `Template: scurt`.
- Livrabile obligatorii: `.md` și `.html`.
- Câmpurile pentru Tarot includ numărul arcanei, denumirea, fișierul imaginii, interpretarea și data URI pentru HTML.
- Tabelele dependente de perioadă sunt populate din rezultatul calculatorului pentru intervalul cerut; nu păstrează anii persoanei-model.
- Pătratul matriceal este populat exclusiv din șirul complet returnat de calculator și folosește reperele optime și codificarea vizuală stabilite de template-ul de examen; nu reutilizează valorile lui Daniel.
- Dacă nu există nume anterior, al doilea tabel al numelui și comparația aferentă sunt omise integral.
- Relația este condițională. Dacă există date relaționale, Omulețul relațiilor devine Capitolul 9, iar Concluziile devin Capitolul 10. Dacă datele lipsesc, capitolul relațional și intrarea sa din Cuprins sunt eliminate integral, iar Concluziile rămân Capitolul 9.

## Verificare și criterii de acceptare

- Template-ul `examen` și lucrarea Micu nu prezintă modificări.
- Copiile din `templates/` și din skill sunt identice.
- Nu rămân referințe la `Pasted image`, Micu, Ivan, Ana Maria, `05.09.1983` sau valori personale.
- Toate cele șapte imagini-tabel au echivalent HTML și Markdown editabil; nicio imagine nu este folosită pentru a reda un tabel.
- Matrița numerologică apare în ambele livrabile ca pătrat 3×3, în ordinea exactă `1–4–7 / 2–5–8 / 3–6–9`, cu toate cele nouă căsuțe, valorile calculate, reperele optime, culorile și simbolurile conforme modelului `BDR-19980219-v1.07r-G-001`.
- Fiecare arcană menționată are imagine în același subcapitol.
- Când relația este prezentă, SVG-ul Omulețului relațiilor există în ambele livrabile, este XML valid, conține watermark-ul `Atlas Numerologie`, folosește datele corecte ale ambelor persoane și are legendă și text alternativ coerente; în HTML autonom sursa imaginii este data URI.
- Interpretarea Omulețului relațiilor verifică distribuția cifrelor, sinteza elementelor, realizarea împreună, tema de rezolvat și fiecare zonă absentă, fără verdicte de compatibilitate sau resturi din modelul Daniel–Andreea.
- Toate wikilinkurile Cuprinsului Markdown indică exact un heading; HTML-ul nu conține wikilinkuri și nu are ancore lipsă sau duplicate.
- Markdown-ul și HTML-ul au aceleași capitole, tabele, calcule, figuri și instrucțiuni condiționale.
- Se verifică randarea HTML pe desktop, mobil și print, inclusiv tabelele late și imaginile Tarot.
- Se rulează controlul de igienă al diferențelor și se confirmă că modificările sunt limitate la noul template și registrele The Scribe.

## Presupuneri adoptate

- Se folosește structura recomandată „9 capitole de bază + capitol relațional condițional + carcasa examen”.
- Arcanele sunt selectate dinamic din Vault, nu sunt limitate la Marele Preot și Soarele.
- Template-ul este publicat atât în `templates/`, cât și în resursele skill-ului The Scribe.
- Skill-ul global din `.codex/skills` nu este modificat, deoarece nu a fost cerută publicarea globală.
