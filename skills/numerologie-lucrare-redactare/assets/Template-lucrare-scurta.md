---
titlu: Template lucrare numerologică scurtă
tip: template
cheie_template: scurt
formate_livrabile: [md, html]
status: activ
agent: The Scribe
tags: [template, numerologie, lucrare, scurt, obsidian]
---

# Template lucrare numerologică scurtă

> [!important] Contract de utilizare
> Acesta este un template reutilizabil, nu o lucrare completată. Înlocuiește toate câmpurile `{{...}}` cu date validate din calculator. Păstrează Markdown-ul și HTML-ul sincronizate. În revizii păstrează indexurile; în varianta finală elimină indexurile și capitolul de trasabilitate.

Index: {{cod_lucrare}}-CAP-001
# {{nume_complet}} — {{data_nasterii}}

Index: {{cod_lucrare}}-CAP-002
## Date generale

Index: {{cod_lucrare}}-L-001
- Persoana analizată: {{nume_complet}}
- Prenume activ: {{prenume_activ}}
- Data nașterii: {{data_nasterii}}
- Gen: {{gen}}
- Nume anterior: {{nume_anterior_sau_nu_exista}}
- Template selectat: scurt
- Stil de redactare: {{conversational_sau_formal}}
- Interval analizat: {{interval_ani}}
- Data lucrării: {{data_lucrarii}}
- Versiune: {{versiune}}

> [!info] Relație opțională
> Dacă sunt furnizate date relaționale, adaugă aici numele complet, prenumele activ, data nașterii, genul și tipul relației. Dacă lipsesc, elimină integral acest callout, Capitolul 9 și intrarea lui din Cuprins; Concluziile devin Capitolul 9.

Index: {{cod_lucrare}}-CAP-003
## Cuprins

Index: {{cod_lucrare}}-L-002
1. [[#Capitolul 1. Vibrația interioară — Cine ești tu?|Vibrația interioară — Cine ești tu?]]
2. [[#Capitolul 2. Vibrația exterioară — Rolul social|Vibrația exterioară — Rolul social]]
3. [[#Capitolul 3. Destinul — Muntele de urcat|Destinul — Muntele de urcat]]
4. [[#Capitolul 4. Matrița numerologică — Pătratul lui Pitagora|Matrița numerologică — Pătratul lui Pitagora]]
5. [[#Capitolul 5. Numele — Eu și neamul|Numele — Eu și neamul]]
6. [[#Capitolul 6. Oportunități și provocări|Oportunități și provocări]]
7. [[#Capitolul 7. Soarta și Destinul — Drumul|Soarta și Destinul — Drumul]]
8. [[#Capitolul 8. Lecțiile de viață|Lecțiile de viață]]
9. [[#Capitolul 9. Relații|Relații]] — numai dacă există date relaționale
10. [[#Capitolul 10. Concluzii|Concluzii]]

Index: {{cod_lucrare}}-CAP-005
## Capitolul 1. Vibrația interioară — Cine ești tu?

Index: {{cod_lucrare}}-SUB-001
### 1.1. Definiție și calcul

Index: {{cod_lucrare}}-P-002
{{definitie_vibratie_interioara_si_metoda}}

Index: {{cod_lucrare}}-C-001
> [!example] Calcul
> {{calcul_vibratie_interioara}} → **{{vibratie_interioara}}**

Index: {{cod_lucrare}}-SUB-002
### 1.2. Caracterul

{{interpretare_caracter}}

Index: {{cod_lucrare}}-SUB-003
### 1.3. Dorințele

{{interpretare_dorinte}}

Index: {{cod_lucrare}}-SUB-004
### 1.4. Motivația

{{interpretare_motivatie}}

Index: {{cod_lucrare}}-SUB-005
### 1.5. Teama

{{interpretare_teama}}

Index: {{cod_lucrare}}-SUB-006
### 1.6. Polarități și maturizare

Index: {{cod_lucrare}}-T-009
| Polaritate constructivă | Polaritate de conștientizat | Direcție de maturizare |
| --- | --- | --- |
| {{polaritate_plus}} | {{polaritate_minus}} | {{directie_maturizare}} |

Index: {{cod_lucrare}}-SUB-007
### 1.7. Tarot

Index: {{cod_lucrare}}-T-010
| Arcana | Denumire | Resursă | Manifestare | Umbră | Maturizare |
| ---: | --- | --- | --- | --- | --- |
| {{numar_arcana_vibratie}} | {{nume_arcana_vibratie}} | {{resursa_arcana_vibratie}} | {{manifestare_arcana_vibratie}} | {{umbra_arcana_vibratie}} | {{maturizare_arcana_vibratie}} |

Index: {{cod_lucrare}}-G-001
![[vault/tarot/imagini/{{fisier_arcana_vibratie}}]]

_Arcana {{numar_arcana_vibratie}} — {{nume_arcana_vibratie}}_

Index: {{cod_lucrare}}-CAP-006
## Capitolul 2. Vibrația exterioară — Rolul social

Index: {{cod_lucrare}}-SUB-008
### 2.1. Definiție și calcul

{{definitie_vibratie_exterioara_si_metoda}}

Index: {{cod_lucrare}}-C-002
> [!example] Calcul
> {{calcul_vibratie_exterioara}} → **{{vibratie_exterioara}}**

Index: {{cod_lucrare}}-SUB-009
### 2.2. Caracterul social

{{interpretare_caracter_social}}

Index: {{cod_lucrare}}-SUB-010
### 2.3. Interior și exterior

{{interpretare_dialog_interior_exterior}}

Index: {{cod_lucrare}}-CAP-007
## Capitolul 3. Destinul — Muntele de urcat

Index: {{cod_lucrare}}-SUB-011
### 3.1. Definiție și calcul

{{definitie_destin_si_metoda}}

Index: {{cod_lucrare}}-C-003
> [!example] Calcul
> {{calcul_destin}} → **{{destin}}**

Index: {{cod_lucrare}}-SUB-012
### 3.2. Interpretare

{{interpretare_destin_manifestare_umbra_maturizare}}

Index: {{cod_lucrare}}-CAP-008
## Capitolul 4. Matrița numerologică — Pătratul lui Pitagora

Index: {{cod_lucrare}}-SUB-013
### 4.1. Matricea datei de naștere

{{definitie_matrice_si_metoda}}

Index: {{cod_lucrare}}-C-004
> [!example] Calcul
> Data compactă: **{{data_compacta}}**  
> N1 = **{{N1}}**  
> N2 = **{{N2_o_singura_insumare}}**  
> N3 = **{{N3}}**  
> N4 = **{{N4_o_singura_insumare}}**  
> Șir complet / număr logic = **{{sir_complet}}**

Index: {{cod_lucrare}}-G-002
| **1 — Foc** · {{cifre_1}} · optim `111` · {{simbol_1}} | **4 — Pământ** · {{cifre_4}} · optim `44` · {{simbol_4}} | **7 — Aer** · {{cifre_7}} · optim `7` · {{simbol_7}} |
| --- | --- | --- |
| **2 — Apă** · {{cifre_2}} · optim `222` · {{simbol_2}} | **5 — Foc** · {{cifre_5}} · optim `55` · {{simbol_5}} | **8 — Pământ** · {{cifre_8}} · optim `8` · {{simbol_8}} |
| **3 — Aer** · {{cifre_3}} · optim `333` · {{simbol_3}} | **6 — Apă** · {{cifre_6}} · optim `66` · {{simbol_6}} | **9 — Foc** · {{cifre_9}} · optim `9` · {{simbol_9}} |

> [!important] Model matriceal
> Păstrează ordinea `1–4–7 / 2–5–8 / 3–6–9`, culorile elementelor și reperul optim. Pentru o cifră folosește un cerc; pentru exact două cifre folosește două cercuri unite printr-o linie care se oprește la contur și nu intră în cercuri; pentru exact trei cifre folosește un triunghi. Căsuțele fără cifre afișează `—` și starea `absent`.

Index: {{cod_lucrare}}-SUB-014
### 4.2. Căsuțele matricei

Index: {{cod_lucrare}}-T-011
| Căsuța | Cifre | Cantitate | Valoare | Reper optim | Interpretare |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | {{cifre_1}} | {{cantitate_1}} | {{valoare_1}} | 111 | {{interpretare_1}} |
| 2 | {{cifre_2}} | {{cantitate_2}} | {{valoare_2}} | 222 | {{interpretare_2}} |
| 3 | {{cifre_3}} | {{cantitate_3}} | {{valoare_3}} | 333 | {{interpretare_3}} |
| 4 | {{cifre_4}} | {{cantitate_4}} | {{valoare_4}} | 44 | {{interpretare_4}} |
| 5 | {{cifre_5}} | {{cantitate_5}} | {{valoare_5}} | 55 | {{interpretare_5}} |
| 6 | {{cifre_6}} | {{cantitate_6}} | {{valoare_6}} | 66 | {{interpretare_6}} |
| 7 | {{cifre_7}} | {{cantitate_7}} | {{valoare_7}} | 7 | {{interpretare_7}} |
| 8 | {{cifre_8}} | {{cantitate_8}} | {{valoare_8}} | 8 | {{interpretare_8}} |
| 9 | {{cifre_9}} | {{cantitate_9}} | {{valoare_9}} | 9 | {{interpretare_9}} |

Index: {{cod_lucrare}}-SUB-015
### 4.3. Elemente

Index: {{cod_lucrare}}-T-012
| Element | Cifre | Total | Interpretare |
| --- | --- | ---: | --- |
| Foc | 1 + 5 + 9 | {{total_foc}} | {{interpretare_foc}} |
| Apă | 2 + 6 | {{total_apa}} | {{interpretare_apa}} |
| Aer | 3 + 7 | {{total_aer}} | {{interpretare_aer}} |
| Pământ | 4 + 8 | {{total_pamant}} | {{interpretare_pamant}} |

Index: {{cod_lucrare}}-SUB-016
### 4.4. Masculin și feminin. Daruri și nevoi

{{interpretare_par_impar_masculin_feminin}}

{{interpretare_daruri_nevoi}}

Index: {{cod_lucrare}}-SUB-017
### 4.5. Fixația

{{calcul_si_interpretare_fixatie}}

Index: {{cod_lucrare}}-CAP-009
## Capitolul 5. Numele — Eu și neamul

Index: {{cod_lucrare}}-SUB-018
### 5.1. Numărul ereditar

{{calcul_si_interpretare_numar_ereditar}}

Index: {{cod_lucrare}}-SUB-019
### 5.2. Numărul activ

{{calcul_si_interpretare_numar_activ}}

Index: {{cod_lucrare}}-SUB-020
### 5.3. Numărul de realizare

{{calcul_si_interpretare_numar_realizare}}

Index: {{cod_lucrare}}-SUB-021
### 5.4. Numărul neamului

Index: {{cod_lucrare}}-C-005
> [!example] Calcul în intervalul 1–22
> {{calcul_numar_neam}} → **{{numar_arcana_neam}}**

Index: {{cod_lucrare}}-T-013
| Arcana | Denumire | Resursă moștenită | Manifestare | Umbră | Maturizare |
| ---: | --- | --- | --- | --- | --- |
| {{numar_arcana_neam}} | {{nume_arcana_neam}} | {{resursa_arcana_neam}} | {{manifestare_arcana_neam}} | {{umbra_arcana_neam}} | {{maturizare_arcana_neam}} |

Index: {{cod_lucrare}}-G-003
![[vault/tarot/imagini/{{fisier_arcana_neam}}]]

_Arcana {{numar_arcana_neam}} — {{nume_arcana_neam}}_

Index: {{cod_lucrare}}-SUB-022
### 5.5. Codul numerologic al numelui

#### Numele actual — {{nume_actual}}

Index: {{cod_lucrare}}-T-001
| Nume | Mentale | Fizice | Emoționale | Intuitive | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Inițiatoare | {{actual_initiatoare_mental}} | {{actual_initiatoare_fizic}} | {{actual_initiatoare_emotional}} | {{actual_initiatoare_intuitiv}} | **{{actual_total_initiatoare}}** |
| Continuatoare | {{actual_continuatoare_mental}} | {{actual_continuatoare_fizic}} | {{actual_continuatoare_emotional}} | {{actual_continuatoare_intuitiv}} | **{{actual_total_continuatoare}}** |
| Finalizatoare | {{actual_finalizatoare_mental}} | {{actual_finalizatoare_fizic}} | {{actual_finalizatoare_emotional}} | {{actual_finalizatoare_intuitiv}} | **{{actual_total_finalizatoare}}** |
| **Total** | **{{actual_total_mental}}** | **{{actual_total_fizic}}** | **{{actual_total_emotional}}** | **{{actual_total_intuitiv}}** | **{{actual_total_general}}** |

> [!info] Bloc condițional — nume anterior
> Păstrează următorul tabel și comparația numai dacă persoana are nume anterior.

#### Numele anterior — {{nume_anterior}}

Index: {{cod_lucrare}}-T-002
| Nume | Mentale | Fizice | Emoționale | Intuitive | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Inițiatoare | {{anterior_initiatoare_mental}} | {{anterior_initiatoare_fizic}} | {{anterior_initiatoare_emotional}} | {{anterior_initiatoare_intuitiv}} | **{{anterior_total_initiatoare}}** |
| Continuatoare | {{anterior_continuatoare_mental}} | {{anterior_continuatoare_fizic}} | {{anterior_continuatoare_emotional}} | {{anterior_continuatoare_intuitiv}} | **{{anterior_total_continuatoare}}** |
| Finalizatoare | {{anterior_finalizatoare_mental}} | {{anterior_finalizatoare_fizic}} | {{anterior_finalizatoare_emotional}} | {{anterior_finalizatoare_intuitiv}} | **{{anterior_total_finalizatoare}}** |
| **Total** | **{{anterior_total_mental}}** | **{{anterior_total_fizic}}** | **{{anterior_total_emotional}}** | **{{anterior_total_intuitiv}}** | **{{anterior_total_general}}** |

{{interpretare_cod_nume_si_comparatie_conditionala}}

Index: {{cod_lucrare}}-SUB-023
### 5.6. Numărul de exprimare

{{calcul_si_interpretare_numar_exprimare}}

Index: {{cod_lucrare}}-CAP-010
## Capitolul 6. Oportunități și provocări

Index: {{cod_lucrare}}-T-003
| Etapă | Interval | Oportunitate | Provocare | Interpretare |
| --- | --- | ---: | ---: | --- |
| {{etapa_1}} | {{interval_1}} | {{oportunitate_1}} | {{provocare_1}} | {{interpretare_etapa_1}} |
| {{etapa_2}} | {{interval_2}} | {{oportunitate_2}} | {{provocare_2}} | {{interpretare_etapa_2}} |
| {{etapa_3}} | {{interval_3}} | {{oportunitate_3}} | {{provocare_3}} | {{interpretare_etapa_3}} |
| {{etapa_4}} | {{interval_4}} | {{oportunitate_4}} | {{provocare_4}} | {{interpretare_etapa_4}} |

Index: {{cod_lucrare}}-CAP-011
## Capitolul 7. Soarta și Destinul — Drumul

Index: {{cod_lucrare}}-SUB-024
### 7.1. Soarta și Destinul

{{definitie_metoda_si_interpretare_soarta_destin}}

Index: {{cod_lucrare}}-C-006
> [!example] Sinteză
> Soartă: **{{sir_soarta}}**  
> Destin: **{{sir_destin}}**

Index: {{cod_lucrare}}-SUB-025
### 7.2. Anii importanți

Index: {{cod_lucrare}}-T-004
| Ani interiori | Reper activ | Interpretare |
| ---: | --- | --- |
| {{an_interior_1}} | {{da_nu}} | {{interpretare_an_interior_1}} |
| {{an_interior_2}} | {{da_nu}} | {{interpretare_an_interior_2}} |
| {{adauga_randuri_din_calculator}} |  |  |

Index: {{cod_lucrare}}-T-005
| Ani exteriori | Reper activ | Interpretare |
| ---: | --- | --- |
| {{an_exterior_1}} | {{da_nu}} | {{interpretare_an_exterior_1}} |
| {{an_exterior_2}} | {{da_nu}} | {{interpretare_an_exterior_2}} |
| {{adauga_randuri_din_calculator}} |  |  |

Index: {{cod_lucrare}}-SUB-026
### 7.3. Ciclul de 7 ani

Index: {{cod_lucrare}}-T-006
| Ciclu | Anul 1 | Anul 2 | Anul 3 | Anul 4 | Anul 5 | Anul 6 | Anul 7 | Interpretare |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| {{ciclu_7_1}} | {{an1}} | {{an2}} | {{an3}} | **{{an4_reper}}** | {{an5}} | {{an6}} | {{an7}} | {{interpretare_ciclu_7_1}} |
| {{adauga_randuri_pentru_interval}} |  |  |  |  |  |  |  |  |

Index: {{cod_lucrare}}-SUB-027
### 7.4. Ciclul de 9 ani

Index: {{cod_lucrare}}-T-007
| Ciclu | Anul 1 — început | Anul 2 | Anul 3 | Anul 4 | Anul 5 | Anul 6 | Anul 7 | Anul 8 | Anul 9 — încheiere |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| {{ciclu_9_1}} | **{{an_inceput}}** | {{an2}} | {{an3}} | {{an4}} | {{an5}} | {{an6}} | {{an7}} | {{an8}} | **{{an_final}}** |
| {{adauga_randuri_pentru_interval}} |  |  |  |  |  |  |  |  |  |

{{interpretare_ciclu_9_si_an_personal}}

Index: {{cod_lucrare}}-CAP-012
## Capitolul 8. Lecțiile de viață

Index: {{cod_lucrare}}-T-008
| An / interval | Lecția 1 — {{lectia_1}} | Lecția 2 — {{lectia_2}} | Lecția 3 — {{lectia_3}} | Lecția 4 — {{lectia_4}} | Lecția 5 — {{lectia_5}} |
| --- | ---: | ---: | ---: | ---: | ---: |
| {{rand_lectii_1}} | {{an_l1}} | {{an_l2}} | {{an_l3}} | {{an_l4}} | {{an_l5}} |
| {{adauga_randuri_pentru_interval}} |  |  |  |  |  |

{{interpretare_lectii_de_viata}}

> [!info] Capitol condițional
> Păstrează Capitolul 9 numai dacă există datele celei de-a doua persoane. Altfel elimină-l împreună cu intrarea din Cuprins și renumerotează Concluziile ca Capitolul 9.

Index: {{cod_lucrare}}-CAP-013
## Capitolul 9. Relații

Index: {{cod_lucrare}}-L-003
- Nume: {{nume_persoana_relationala}}
- Data nașterii: {{data_nasterii_persoana_relationala}}
- Tipul relației: {{tip_relatie}}

Index: {{cod_lucrare}}-SUB-028
### 9.1. Omulețul relațiilor

{{introducere_relatie_ca_harta_nu_verdict}}

Index: {{cod_lucrare}}-G-004
![Omulețul relațiilor pentru {{nume_complet}} și {{nume_persoana_relationala}}]({{fisier_omulet_relatii}}.svg)

_Omulețul relațiilor pentru {{nume_complet}} și {{nume_persoana_relationala}}_

Index: {{cod_lucrare}}-C-007
> [!example] Calcul relațional
> Realizare împreună: {{vibratie_interioara_A}} + {{vibratie_interioara_B}} → **{{realizare_impreuna}}**  
> De rezolvat împreună: |{{vibratie_interioara_A}} − {{vibratie_interioara_B}}| = **{{de_rezolvat_impreuna}}**

{{interpretare_contributie_persoana_A}}

{{interpretare_contributie_persoana_B}}

{{interpretare_cifre_si_elemente_comune_dominante_complementare}}

{{interpretare_realizare_si_de_rezolvat_impreuna}}

{{interpretare_zone_absente_cu_cifra_in_paranteza_constructie_intentionata_aport_extern_si_exemple}}

Index: {{cod_lucrare}}-CAP-014
## Capitolul 10. Concluzii

{{sinteza_finala_personalizata_fara_repetitii_sau_predictii_rigide}}

> [!info] Renumerotare fără relație
> Dacă nu există date relaționale, titlul devine `Capitolul 9. Concluzii`, iar ținta din Cuprins se actualizează identic.

Index: {{cod_lucrare}}-CAP-015
## Documentația și trasabilitatea lucrării

> [!warning] Numai pentru revizie
> Elimină integral acest capitol din varianta finală cu sufix `f`.

Index: {{cod_lucrare}}-T-014
| Resursă | Valoare |
| --- | --- |
| Agent coordonator | The Scribe |
| Agenți subcontractați | {{agenti_subcontractati}} |
| Skill-uri | {{skilluri_folosite}} |
| Template | `scurt` — `Template_Lucrare_Numerologica_Scurt.md` + `.html` |
| Raport calculator | {{cale_raport_json}} |
| Registru formule și data validării | {{registru_si_data}} |
| SVG-uri integrate | {{svg_uri_integrate}} |
| Versiune și data redactării | {{versiune}} — {{data_lucrarii}} |

## Control final al template-ului

- [ ] Câmpul `Template` este exact `scurt`.
- [ ] Toate calculele provin din raportul JSON validat.
- [ ] Markdown-ul și HTML-ul au același conținut semantic.
- [ ] Cuprinsul Markdown folosește numai wikilinkuri către heading-uri exacte.
- [ ] Cele șapte tabele provenite din imaginile-model sunt tabele editabile.
- [ ] Matricea 3×3 respectă modelul `BDR-19980219-v1.07r-G-001`.
- [ ] Fiecare arcană numită are imagine în același subcapitol.
- [ ] Capitolul Relații este inclus numai când există date relaționale.
- [ ] SVG-ul Omulețului relațiilor este valid, are watermark `Atlas Numerologie` și nu a fost editat manual.
- [ ] Nu există date, ani, interpretări sau resurse rămase de la persoana-model.
