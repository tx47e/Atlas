# Dashboard V3 — Design QA

## Referințe

- Colț ornamental: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-f7fb4c42-f345-45ee-8559-0da54602c65a.png`
- Carduri Vault: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-8a5cb93d-07c5-4e3d-a8e4-d551f83a500a.png`
- Calculator înainte de integrare: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-d3eb391d-e3cb-4602-822c-28afe2ac49fe.png`
- Împletitură simetrică de colț: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-a0528b32-c1af-4c20-974f-d699f6ef41fe.png`
- Poziția valorilor numelui în matrice: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-5d2e834e-1724-4acb-ae7c-c579aa23771f.png`
- Poziția selectorului de persoane: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-6cf0e5c8-b43b-4578-b726-36c872c3f047.png`
- Extinderea calculatorului până la marginea de jos: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-7e320a8d-37e5-41f4-aa6e-b90b299c37df.png`
- Ruptura vizibilă dintre ornamentul de colț și cel median: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-ff462191-6d58-4d94-a78e-2af3c915768f.png`
- Schița fade-out pentru colț și ornamentul median: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-413a406e-a2e7-4999-8117-104deb4c374f.png` (1600 × 251 px).
- Curățarea Hărții suprapuse și delimitarea secțiunilor Calculatorului: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-06121598-7b85-48d6-87ce-e5075222b58b.png`.
- Ilustrația Tarot detaliată: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-2e876f44-88a1-4293-ad41-73d3ad9fb767.png`.
- Poziția barei persoanei sub ornamentul superior: `C:\Users\Mihai\AppData\Local\Temp\codex-clipboard-1f61f670-8adf-4807-bb48-be074e59e25c.png`.

Referința pentru carduri este tratată drept direcție artistică pentru ilustrațiile vectoriale, nu drept captură a întregii pagini.

## Mediu verificat

| Suprafață | Viewport | Stare |
| --- | ---: | --- |
| Vault / Bibliotecă | 1265 × 720 | cardurile Numerologie, Tarot și Matricea Destinului vizibile |
| Calculator | 1265 × 720 | persoana implicită, secțiunea Calcule deschisă |
| Harta suprapusă | 1265 × 720 | data 01.01.2000, vârsta curentă 26 |
| Calculator mobil | 390 × 844 | selectorul persoanei și Calcule vizibile |
| Meniu mobil deschis | 390 × 844 | lățimi egale pentru conținut și scroll, fără overflow X |
| Matrice integrată | 1265 × 720 | Birsan Daniel Robert, 19.02.1998, șirurile datei și numelui validate vizual |
| Ornament fade desktop | 1280 × 720 | colțurile și nodurile mediane vizibile simultan; capetele ornamentelor dispar gradual |
| Ornament fade mobil | 390 × 844 | colțurile, nodul superior și nodurile laterale rămân lizibile fără suprapuneri |
| Vault / Tarot final | 1265 × 720 | The Moon XVIII, The Fool 0 și The Star XVII vizibile în card |
| Formular Persoană nouă final | 1265 × 720 | checkbox-ul activează ora; X și Renunță închid fără validare |
| Harta suprapusă final | 1265 × 720 | fără titlu/nume/datǎ; o singură etichetă de vârstă deasupra graficului |

## Dovezi de implementare

- `dashboard-v3-vault-svg-refinement.png` — vedere completă pentru cele trei SVG-uri și colțurile vegetale.
- `dashboard-v3-calculator-single-parchment.png` — calculator integrat într-o singură pagină de pergament.
- `dashboard-v3-harta-varsta-curenta.png` — vedere focalizată pe linia și etichetele vârstei curente.
- `dashboard-v3-calculator-mobile-single-parchment.png` — verificarea structurii responsive.
- `dashboard-v3-calculator-scroll-restored.png` — bara verticală și suprafața calculatorului.
- `dashboard-v3-matrice-integrata-birsan.png` — o singură matrice mărită, cu valorile numelui în stânga-jos.
- `dashboard-v3-tarot-detaliat.png` — verificarea focalizată a ilustrației Tarot.
- `dashboard-v3-colt-impletit-simetric.png` — verificarea focalizată a simetriei ornamentului.
- `dashboard-v3-meniu-mobil-fara-overflow.png` — meniul mobil fără overflow orizontal.
- `dashboard-v3-rama-fade-central.png` — ramă continuă cu fade și noduri centrale orizontale și verticale.
- `dashboard-v3-scroll-ciclicitati-functional.png` — secțiunea Ciclicități accesată prin scrollul nativ al calculatorului.
- `dashboard-v3-scroll-ciclicitati-mobile.png` — scrollul calculatorului verificat la 390 × 844.
- `dashboard-v3-calculator-toolbar-frame.png` — selectorul de persoane mutat în antetul din dreapta și calculatorul extins până la marginea inferioară.
- `dashboard-v3-calculator-scroll-ciclicitati.png` — Ciclicități vizibile prin scrollul intern al suprafeței extinse.
- `dashboard-v3-calculator-mobile-toolbar.png` — controlul persoanei rearanjat responsive, fără overflow orizontal.
- `dashboard-v3-carduri-integrate-desktop.png` — Calcule fără card exterior, bara persoanei transparentă și butoane turcoaz.
- `dashboard-v3-ciclicitati-integrate.png` — harta Ciclicități integrată în aceeași suprafață, fără outline exterior.
- `dashboard-v3-carduri-integrate-mobile.png` — aceeași integrare la 390 × 844, cu marginea ornamentală inferioară vizibilă.
- `dashboard-v3-rama-continua-carduri-transparente.png` — rama fără întreruperi și cardurile interne fără fundal sau umbră.
- `dashboard-v3-rama-continua-mobile.png` — continuitatea ramei și transparența cardurilor verificate pe mobil.

- `dashboard-v3-harta-transparenta.png` — harta suprapusă randată direct peste textura pergamentului calculatorului pe desktop.
- `dashboard-v3-harta-transparenta-mobile.png` — transparența fundalului hărții verificată la 390 × 844.

- `dashboard-v3-calculator-profil-implicit.png` — profilul Szabo Mihai Gabriel selectat și încărcat implicit în calculator.
- `dashboard-v3-persoana-noua-desktop.png` — dialogul complet pentru identitate, data separată zi/lună/an, relații și întrebări.
- `dashboard-v3-persoana-noua-dialog.png` — relație și întrebări multiple adăugate funcțional în formular.
- `dashboard-v3-persoana-noua-mobile.png` — începutul formularului verificat la 390 × 844, fără suprapunerea acțiunilor.
- `dashboard-v3-persoana-noua-mobile-final.png` — finalul formularului și toate acțiunile de salvare accesibile pe mobil.
- `dashboard-v3-ornamente-fade-desktop.png` — intensitate maximă în colțuri și nodurile mediane, cu fade continuu între ele.

- `dashboard-v3-registry-mihai.png` — registrul YAML real, fără dummy-uri, cu Mihai încărcat și rezultatele numerice aferente.
- `dashboard-v3-registry-sabina.png` — selecția Sabina produce altă matrice și altă Scară a bunăstării.
- `dashboard-v3-registry-sabina-harta.png` — Harta suprapusă recalculată pentru Sabina, cu numele, data și traseele sale.
- `dashboard-v3-registry-mobile.png` — dropdown-ul registrului și rezultatele calculatorului verificate la 390 × 844.
- `dashboard-v3-dropdown-fara-timestamp.png` — dropdown-ul afișează exclusiv numele complet și data nașterii, fără data introducerii sau a lucrării.
- `dashboard-v3-ornament-fade-desktop-final.png` — implementarea finală desktop, 1280 × 720 px, comparată vizual cu schița de 1600 × 251 px pe regiunea ornamentală superioară.
- `dashboard-v3-ornament-fade-mobile-final.png` — verificarea responsive la 390 × 844 px; fade-ul rămâne continuu și nu acoperă controalele.
- `qa/dashboard-v3-vault-tarot-detailed-final.jpg` — integrarea PNG-ului Tarot detaliat în cardul Vault.
- `qa/dashboard-v3-vault-tarot-transparent-final.jpg` — verificarea canalului alfa direct peste textura de pergament, fără dreptunghi alb.
- `qa/dashboard-v3-calculator-svg-final.jpg` — Harta suprapusă fără antet redundant și cu linia vârstei conectată la eticheta superioară.
- `qa/dashboard-v3-person-form-birthtime-final.jpg` — ora nașterii activată explicit prin checkbox și preferințele simplificate.
- `qa/dashboard-v3-relation-date-ddmmyyyy-final.jpg` — data persoanei asociate afișată în câmpuri Zi / Lună / An, cu selector-calendar sincronizat.
- `qa/dashboard-v3-calculator-toolbar-lowered-final.jpg` — selectorul și butoanele persoanei coborâte sub ornamentul superior.
- `qa/dashboard-v3-import-yaml-dialog-final.jpg` — dialogul funcțional pentru alegerea și adăugarea unei fișe YAML în registru.

## Istoric constatări

| Severitate | Constatare | Rezolvare |
| --- | --- | --- |
| P1 | Calculatorul era încadrat în mai multe carduri și repeta titlul. | Eliminat antetul/cardul intern și păstrat un singur control principal pe pergamentul paginii. |
| P2 | Colțurile erau prea geometrice și rare față de referință. | Înlocuite cu un SVG de dantelă vegetală cu frunze, vrejuri, rozete și trasee împletite. |
| P2 | Eticheta vârstei de pe axa X era prea mică. | Mărită caseta la 84 × 25 și fontul la 13 px, păstrat mai mic decât gradajul principal. |
| P2 | Grafica Matricea Destinului era prea simplă. | Reconstruită ca diagramă vectorială de tip Floarea Vieții, cu inele, noduri și canale ornamentale. |
| P1 | Scrollul paginii nu răspundea când cursorul era peste calculatorul integrat. | Evenimentele wheel și touch sunt transferate către scrollul paginii principale; testul a produs exact delta cerută de 420 px. |
| P1 | Matricea datei și matricea numelui ocupau două blocuri separate. | Înlocuite cu o singură matrice de 520 px; data rămâne în centru, numele apare marcat `N` în stânga-jos. |
| P2 | Meniul lateral putea afișa o bară orizontală. | Lățime responsive cu `clamp`, overflow X ascuns și indicator activ inclus în lățimea elementului. |
| P2 | Colțul nu reprezenta două împletituri simetrice. | Ambele brațe folosesc aceeași geometrie SVG, al doilea fiind oglindit exact pe diagonală. |
| P2 | Personajele Tarot păreau figuri din linii. | Adăugate siluete anatomice închise, mâini, mâneci, veșminte, curea, încălțăminte și gravură interioară. |
| P1 | Scrollul transferat către pagina părinte nu funcționa consecvent în utilizarea reală. | Eliminată redimensionarea automată a iframe-ului; calculatorul are acum viewport propriu, `scrolling="yes"` și scroll vertical nativ. |
| P2 | Ornamentul se oprea imediat după colț. | Adăugate SVG-uri pentru marginile orizontale și verticale, cu fade subtil, împletituri oglindite și noduri centrale pe toate cele patru laturi. |
| P2 | Citatul din subsol nu mai era dorit. | Eliminat complet footer-ul cu textul „Numerele sunt limbajul universului.” și ornamentele sale. |
| P1 | Selectorul de persoane era repetat în corpul calculatorului. | Mutat în colțul dreapta-sus al pergamentului și conectat funcțional la comenzile calculatorului din iframe. |
| P2 | Rama se estompa în colț și nu ajungea clar la ornamentul central. | Intensitatea maximă pornește acum din colț, brațele se suprapun cu dantela de colț și traseele centrale leagă nodul median. |
| P2 | Suprafața calculatorului lăsa un gol mare sub conținut. | Pergamentul calculatorului folosește înălțimea viewportului, iar iframe-ul ocupă tot spațiul rămas cu o margine inferioară de 20 px pe desktop. |
| P2 | Panourile Calcule și Ciclicități păreau două carduri introduse într-un alt card. | Eliminate borderul, raza, fundalul și umbra panourilor exterioare; conținutul rămâne direct pe pergamentul principal. |
| P2 | Bara persoanei avea încă un container opac și eticheta redundantă. | Păstrate numai dropdown-ul și cele două acțiuni; containerul este transparent, iar butoanele folosesc turcoazul paletei V3. |
| P2 | Legătura dintre brațele ornamentale și nodul median rămânea întreruptă vizual. | Adăugat în SVG un traseu central continuu, cu două frunze și bucle simetrice care se suprapun peste brațele laterale. |
| P2 | Calculatorul acoperea prea mult ornamentul inferior. | Marginea inferioară este acum 50 px pe desktop și 42 px pe mobil, astfel încât dantela rămâne vizibilă. |
| P1 | Măștile de opacitate întrerupeau brațele ornamentale înaintea nodului median. | Eliminate măștile; brațele oglindite și conectorul central se suprapun, formând un traseu continuu pe toate cele patru laturi. |
| P2 | Cardurile interne păstrau o suprafață colorată și umbră proprie. | Fundalul, imaginea de fundal și umbra cardurilor interne sunt eliminate; textura provine exclusiv din pergamentul calculatorului. |

| P2 | Harta suprapusă desena un al doilea strat de pergament peste textura calculatorului. | Eliminate din generator gradientul `overlayPaper`, textura `paperFibers` și cele două dreptunghiuri de fundal; SVG-ul este transparent și lasă vizibil pergamentul principal. |

| P1 | Butonul exterior „Persoană nouă” activa formularul ascuns din iframe și părea nefuncțional. | Înlocuit cu un dialog V3 real, conectat la registrul persoanelor și la calculator. |
| P1 | Registrul persoanelor nu păstra toate datele cerute și nu oferea o ieșire YAML reutilizabilă. | Adăugate identitatea completă, data în trei câmpuri, genul, relații multiple, întrebări multiple, persistență locală și export YAML conform schemei canonice. |
| P2 | Calculatorul pornea cu date demonstrative în locul profilului principal. | Profilul `Szabo Mihai Gabriel — 06.11.1984` este inclus, selectat și încărcat implicit, inclusiv după migrarea stării locale existente. |
| P2 | Acțiunea globală „Lucrare nouă” apărea și pe Dashboard. | Eliminată din antetul global; acțiunea rămâne numai în registrul Lucrări. |
| P2 | Ornamentele păreau tăiate între colț și mijlocul laturii pe desktop. | Adăugate măști SVG graduale cu maxime în colțuri și centru, minime intermediare și suprapuneri extinse sub ornamentele de colț. |
| P1 | Bara sticky a dialogului acoperea secțiunea Relații pe mobil. | Acțiunile revin în fluxul formularului sub 520 px și rămân accesibile la final prin scroll. |

| P1 | Dropdown-ul folosea persoane hardcodate și nu reprezenta registrul de fișiere. | Eliminat seed-ul demonstrativ; noul serviciu local scanează `Dashboard/v3/persoane/*.yaml` și expune numai înregistrările reale. |
| P1 | Selectarea unei persoane schimba valoarea dropdown-ului, dar nu recalcula automat calculatorul. | Evenimentul `change` încarcă toate câmpurile persoanei în iframe și apelează recalcularea matricei, Scării bunăstării și Hărții suprapuse. |
| P1 | Salvarea unei persoane producea numai un download și nu actualiza registrul. | `POST /api/persons` validează datele, scrie YAML direct în registrul V3, rescanează directorul și selectează noua înregistrare. |
| P2 | Fișierul YAML nu diferenția versiuni multiple ale aceleiași persoane. | Numele fișierului conține data nașterii, numele complet și timestamp-ul introducerii până la secundă. |
| P2 | Formularul nu includea toate câmpurile deja existente în schema YAML. | Adăugate ora nașterii, numele anterioare și toate preferințele lucrării, păstrând întrebările și relațiile multiple. |
| P1 | Dropdown-ul afișa timestamp-ul tehnic al fișierului YAML, deși acesta trebuie să rămână doar metadată de stocare. | Eticheta opțiunii conține acum numai `Nume complet — ZZ.LL.AAAA`; numele a fost normalizat la `Szabo Mihai Gabriel`. |
| P2 | Ornamentația de colț și cea mediană foloseau trasee lungi cu minime de opacitate interne, iar capetele păreau tăiate. | Colțul folosește acum un SVG dedicat cu brațe vegetale lungi și fade până la transparență; ornamentul median este separat, simetric, accentuat în centru și estompat la ambele extremități, orizontal și vertical. |
| P2 | Ilustrația Tarot era prea schematică și personajele nu aveau gravură suficientă. | Înlocuită cu un PNG de înaltă rezoluție, cu trei cărți în proporție clasică, scene gravate și numerotarea XVIII / 0 / XVII. |
| P2 | PNG-ul Tarot păstra un fundal alb dreptunghiular în cardul Vault. | Creată o versiune RGBA cu fundal exterior complet transparent, margini contractate și fără halou cromatic; suprafața interioară a cărților rămâne opacă. |
| P1 | Harta suprapusă repeta titlul, numele, data și vârsta la bază. | Eliminate textele redundante și eticheta inferioară; linia neagră ajunge acum până la eticheta unică `VÂRSTA 41` de deasupra graficului. |
| P1 | Renunță putea fi acoperit de conținutul formularului și nu primea click. | Bara sticky a primit strat superior, iar Renunță și X închid dialogul fără validarea câmpurilor obligatorii. |
| P2 | Ora nașterii era permanent vizibilă, iar preferințele conțineau controale redundante. | Ora este activată prin checkbox; au rămas numai template-urile Examen și Scurt plus intervalul lucrării. |
| P2 | Data persoanei asociate depindea de formatul regional implicit al browserului. | Înlocuită afișarea cu trei câmpuri explicite Zi / Lună / An și un buton-calendar nativ; selecția și editarea manuală se sincronizează bidirecțional, iar persistența rămâne ISO în YAML. |
| P2 | Bara selectorului de persoane se suprapunea peste dantela ornamentală din colțul dreapta-sus. | Bara a fost coborâtă cu 33 px pe desktop, rămânând în afara ornamentului și fără a acoperi conținutul Calculatorului. |
| P1 | Butonul „Încarcă” doar reaplica persoana selectată și nu putea adăuga fișe externe în registru. | Butonul deschide acum un dialog de import `.yaml` / `.yml`; serviciul parsează cu `safe_load`, validează schema, scrie o versiune în `Dashboard/v3/persoane/`, actualizează dropdown-ul și încarcă persoana importată. |
| P1 | Harta suprapusă stabilea ritmul Soartă–Destin după gen, apoi numai după paritatea zilei reduse, și desena seriile în pași fixați la 10 ani. | Ziua se reduce la o cifră, apoi se analizează predominanța în șirul `zi redusă + LL + AAAA`; par/feminin = 12 ani, impar/masculin = 10 ani. Aceeași valoare controlează punctele, seriile, grila, axa și legenda SVG. Rebeca: `6032020`, 6 pare / 1 impară, 12 ani; Mihai: `6111984`, 3 pare / 4 impare, 10 ani. |

## Rezultat final

Nu au rămas constatări P0, P1 sau P2. Verificarea finală a trecut pe desktop și mobil. Ornamentele și graficele calculatorului rămân SVG; ilustrația Tarot folosește intenționat PNG de înaltă rezoluție pentru nivelul de detaliu cerut.

Browserul de test raportează la fiecare reîncărcare o eroare internă de instrumentare `MutationObserver`, fără URL de sursă; textul nu există în sursele Dashboard V3, iar fluxurile și randarea aplicației nu sunt afectate.

**final result: passed**
