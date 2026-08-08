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
> Dacă sunt furnizate date relaționale, adaugă aici numele complet, prenumele activ, data nașterii, genul și tipul relației. Dacă lipsesc, elimină integral acest callout, Capitolele 9 și 10 și intrările lor din Cuprins; Concluziile devin Capitolul 9.

Index: {{cod_lucrare}}-CAP-003
## Cuprins

Index: {{cod_lucrare}}-L-002
1. Vibrația interioară — Cine ești tu?
2. Vibrația exterioară — Rolul social
3. Destinul — Muntele de urcat
4. Matrița numerologică — Pătratul lui Pitagora
5. Numele — Eu și neamul
6. Spirit și karmă — Lecții și direcții de maturizare
7. Pinacluri: Oportunități și provocări
8. Ciclicități
9. Relații — numai dacă există date relaționale
10. Aplicabilitate profesională — numai dacă există date relaționale
11. Concluzii

Index: {{cod_lucrare}}-CAP-005
## Capitolul 1. Vibrația interioară — Cine ești tu?

Index: {{cod_lucrare}}-SUB-001
### 1.1. Definiție

Index: {{cod_lucrare}}-P-002
{{definitie_vibratie_interioara_si_metoda}}

Index: {{cod_lucrare}}-C-001
> [!example] Calcul
> Ziua din data de naștere = {{calcul_vibratie_interioara}}

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
<table class="polarities-table">
<tbody>
<tr><th scope="row">Polarități pozitive</th><td><ul>{{lumina_vibratie_bulleturi_html}}</ul></td></tr>
<tr><th scope="row">Polarități negative</th><td><ul>{{umbra_vibratie_bulleturi_html}}</ul></td></tr>
<tr><th scope="row">Direcții de dezvoltare</th><td><ul>{{directii_dezvoltare_bulleturi_html}}</ul></td></tr>
</tbody>
</table>

Index: {{cod_lucrare}}-CAP-006
## Capitolul 2. Vibrația exterioară — Rolul social

Index: {{cod_lucrare}}-SUB-008
### 2.1. Definiție

{{definitie_vibratie_exterioara_si_metoda}}

Index: {{cod_lucrare}}-C-002
> [!example] Calcul
> Luna din data de naștere = {{calcul_vibratie_exterioara}}

Index: {{cod_lucrare}}-SUB-009
### 2.2. Rolul social

{{interpretare_caracter_social}}

Index: {{cod_lucrare}}-SUB-010
### 2.3. Interior și exterior

Index: {{cod_lucrare}}-P-{{index_dialog_interior_exterior}}
{{interpretare_dialog_interior_exterior}}

Index: {{cod_lucrare}}-P-{{index_definitie_punte_interior_exterior}}
{{definitie_punte_interior_exterior_ca_distanta_si_ajustare}}

Index: {{cod_lucrare}}-C-{{index_calcul_punte_interior_exterior}}
> [!example] Calculul punții interior–exterior
> |**{{vibratie_interioara}}** − **{{vibratie_exterioara}}**| = **{{punte_interior_exterior}}**

Index: {{cod_lucrare}}-P-{{index_interpretare_punte_interior_exterior}}
{{interpretare_punte_interior_exterior_autenticitate_coerenta_rol_asumat}}

Index: {{cod_lucrare}}-CAP-007
## Capitolul 3. Destinul — Muntele de urcat

Index: {{cod_lucrare}}-SUB-011
### 3.1. Definiție și calcul

{{definitie_destin_si_metoda}}

Index: {{cod_lucrare}}-C-003
> [!example] Calcul
> Toate cifrele adunate din data de naștere = {{calcul_destin}}

Index: {{cod_lucrare}}-SUB-012
### 3.2. Interpretare

{{interpretare_destin_manifestare_umbra_maturizare}}

Index: {{cod_lucrare}}-CAP-008
## Capitolul 4. Matrița numerologică — Pătratul lui Pitagora

Index: {{cod_lucrare}}-SUB-013
### 4.1. Matricea datei de naștere

Index: {{cod_lucrare}}-P-{{index_introducere_matrice}}
{{definitie_matrice_si_metoda}}

- **Căsuța 1** — inteligența psihică;
- **Căsuța 2** — inteligența emoțională;
- **Căsuța 3** — inteligența prelucrării informațiilor;
- **Căsuța 4** — inteligența corporală;
- **Căsuța 5** — inteligența intuitivă;
- **Căsuța 6** — inteligența pragmatismului;
- **Căsuța 7** — inteligența spirituală;
- **Căsuța 8** — inteligența puterii și inteligența socială;
- **Căsuța 9** — inteligența mentală.

Index: {{cod_lucrare}}-C-004
> [!example] Calcul
> Data compactă: **{{data_compacta}}**  
> N1 = **{{N1}}**  
> N2 = **{{N2_o_singura_insumare}}**  
> N3 = **{{N3}}**  
> N4 = **{{N4_o_singura_insumare}}**  
> Șir complet / număr logic = **{{sir_complet}}**

Index: {{cod_lucrare}}-G-002

{{matrice_data_3x3_componenta_html_cu_geometrii_svg_si_clasa_matrix-grid-outlined}}

> [!important] Model matriceal
> Păstrează ordinea `1–4–7 / 2–5–8 / 3–6–9`, culorile elementelor și reperul optim. Pentru o cifră folosește un cerc; pentru exact două cifre folosește două cercuri unite printr-o linie care se oprește la contur și nu intră în cercuri; pentru exact trei cifre folosește un triunghi. Căsuțele fără cifre afișează `—` și starea `absent`.

Index: {{cod_lucrare}}-P-{{index_casuta_1}}
**Căsuța 1.** {{interpretare_casuta_1_dupa_numar_aparitii}}

Index: {{cod_lucrare}}-P-{{index_casuta_2}}
**Căsuța 2.** {{interpretare_casuta_2_dupa_numar_aparitii}}

Index: {{cod_lucrare}}-P-{{index_casuta_3}}
**Căsuța 3.** {{interpretare_casuta_3_dupa_numar_aparitii}}

Index: {{cod_lucrare}}-P-{{index_casuta_4}}
**Căsuța 4.** {{interpretare_casuta_4_dupa_numar_aparitii_sau_energie_conservata}}

Index: {{cod_lucrare}}-P-{{index_casuta_5}}
**Căsuța 5.** {{interpretare_casuta_5_dupa_numar_aparitii_sau_energie_conservata}}

Index: {{cod_lucrare}}-P-{{index_casuta_6}}
**Căsuța 6.** {{interpretare_casuta_6_dupa_numar_aparitii}}

Index: {{cod_lucrare}}-P-{{index_casuta_7}}
**Căsuța 7.** {{interpretare_casuta_7_dupa_numar_aparitii}}

Index: {{cod_lucrare}}-P-{{index_casuta_8}}
**Căsuța 8.** {{interpretare_casuta_8_dupa_numar_aparitii}}

Index: {{cod_lucrare}}-P-{{index_casuta_9}}
**Căsuța 9.** {{interpretare_casuta_9_dupa_numar_aparitii}}

Index: {{cod_lucrare}}-SUB-015
### 4.3. Elemente și temperament

<div class="element-analysis framed-panel">
<div class="element-indexes"><span>Index: {{cod_lucrare}}-T-012</span><span>Index: {{cod_lucrare}}-P-{{index_definitii_elemente}}</span></div>
<div class="element-chart">
<div class="element-bars" role="img" aria-label="Distribuția elementelor">
<div class="element-bar"><div class="element-bar-label"><span>Foc</span><strong>{{total_foc}}</strong></div><div class="element-bar-track"><span class="element-bar-fill element-foc" style="width:{{procent_foc}}%"></span></div></div>
<div class="element-bar"><div class="element-bar-label"><span>Pământ</span><strong>{{total_pamant}}</strong></div><div class="element-bar-track"><span class="element-bar-fill element-pamant" style="width:{{procent_pamant}}%"></span></div></div>
<div class="element-bar"><div class="element-bar-label"><span>Aer</span><strong>{{total_aer}}</strong></div><div class="element-bar-track"><span class="element-bar-fill element-aer" style="width:{{procent_aer}}%"></span></div></div>
<div class="element-bar"><div class="element-bar-label"><span>Apă</span><strong>{{total_apa}}</strong></div><div class="element-bar-track"><span class="element-bar-fill element-apa" style="width:{{procent_apa}}%"></span></div></div>
</div>

<ul class="element-definitions">
<li><strong>Focul</strong> este {{definitie_foc}}.</li>
<li><strong>Pământul</strong> este {{definitie_pamant}}.</li>
<li><strong>Aerul</strong> este {{definitie_aer}}.</li>
<li><strong>Apa</strong> este {{definitie_apa}}.</li>
</ul>
</div>
</div>

Index: {{cod_lucrare}}-P-{{index_temperament}}
{{interpretare_temperament_din_elemente}}

Index: {{cod_lucrare}}-SUB-016
### 4.4. Masculin și feminin

Index: {{cod_lucrare}}-P-{{index_par_impar}}
<div class="parity-chart framed-panel" style="width:100%;max-width:none" role="img" aria-label="Raportul cifrelor impare și pare">
<div class="parity-chart-total">Total: <strong>{{total_cifre_matrice}}</strong> cifre</div>
<div class="parity-chart-bar"><span class="parity-odd" style="width:{{procent_impare}}%"><strong>Impare · {{total_impare}}</strong></span><span class="parity-even" style="width:{{procent_pare}}%"><strong>Pare · {{total_pare}}</strong></span></div>
</div>
{{interpretare_par_impar_masculin_feminin}}

Index: {{cod_lucrare}}-SUB-017
### 4.5. Daruri și nevoi

Index: {{cod_lucrare}}-P-{{index_daruri_nevoi}}
{{interpretare_daruri_nevoi}}

Index: {{cod_lucrare}}-SUB-017a
### 4.6. Scara bunăstării

Index: {{cod_lucrare}}-P-{{index_interpretare_scara_bunastarii}}
{{interpretare_conversationala_lant_scara_bunastarii}}

Index: {{cod_lucrare}}-G-{{index_scara_bunastarii}}
{{grafic_scara_bunastarii}}

{{bloc_fixatie_conditionala}}

{{bloc_tendinta_conditionala}}

Index: {{cod_lucrare}}-CAP-009
## Capitolul 5. Numele — Eu și neamul

Index: {{cod_lucrare}}-SUB-018
### 5.1. Numărul activ

{{calcul_si_interpretare_numar_activ}}

Index: {{cod_lucrare}}-SUB-019
### 5.2. Numărul intim

{{definitie_calcul_si_interpretare_numar_intim_din_vocale}}

Index: {{cod_lucrare}}-SUB-020
### 5.3. Numărul ereditar

{{calcul_si_interpretare_numar_ereditar}}

Index: {{cod_lucrare}}-SUB-021
### 5.4. Numărul ereditar karmic

Index: {{cod_lucrare}}-P-{{index_definitie_numar_ereditar_karmic}}
{{definitie_numar_ereditar_karmic}}

Index: {{cod_lucrare}}-C-005
> [!example] Calcul în intervalul 1–22
> {{calcul_numar_neam}} → **{{numar_arcana_neam}}**

Index: {{cod_lucrare}}-T-013
<table class="tarot-profile-table"><tbody><tr><td><div>Index: {{cod_lucrare}}-G-003</div><img src="vault/tarot/imagini/{{fisier_arcana_neam}}" alt="Arcana {{numar_arcana_neam}} — {{nume_arcana_neam}}" width="190"><div class="tarot-image-caption"><em>Arcana <strong>{{numar_arcana_neam}}</strong> — {{nume_arcana_neam}}</em></div></td><td><ul><li><strong>Resursă moștenită:</strong> {{resursa_arcana_neam}}</li><li><strong>Manifestare:</strong> {{manifestare_arcana_neam}}</li><li><strong>Umbră:</strong> {{umbra_arcana_neam}}</li><li><strong>Maturizare:</strong> {{maturizare_arcana_neam}}</li></ul></td></tr></tbody></table>

Index: {{cod_lucrare}}-P-{{index_interpretare_numar_ereditar_karmic}}
{{interpretare_numar_ereditar_karmic_si_arcana}}

Index: {{cod_lucrare}}-P-{{index_umbra_numar_ereditar_karmic}}
{{umbra_si_maturizare_numar_ereditar_karmic}}

Index: {{cod_lucrare}}-SUB-022
### 5.5. Numărul de realizare

{{calcul_si_interpretare_numar_realizare_si_legatura_cu_vibratia_exterioara}}

Index: {{cod_lucrare}}-SUB-023
### 5.6. Numărul de exprimare

{{calcul_si_interpretare_numar_exprimare_si_armonizare_cu_destinul}}

Index: {{cod_lucrare}}-SUB-023a
### 5.7. Codul numerologic al numelui

#### Numele actual — {{nume_actual}}

Index: {{cod_lucrare}}-C-{{index_calcul_cod_nume}}
> [!example] Calcul
> {{calcul_cod_litere_componenta_1}}
>
> {{calcul_cod_litere_componenta_2}}
>
> {{calcul_cod_litere_componenta_3}}
>
> Codul literelor numelui = **{{cod_litere_nume}}**
>
> Codul numerologic personal al numelui = **{{cod_numerologic_personal_nume}}**

Index: {{cod_lucrare}}-G-002a

{{matrice_comparativa_data_si_nume_componenta_html_cu_geometrii_svg_si_clasa_matrix-grid-outlined}}

Index: {{cod_lucrare}}-P-{{index_comparatie_data_nume}}
{{interpretare_comparatie_data_nume_resurse_comune}}

{{bloc_nume_anterior_conditional}}

Index: {{cod_lucrare}}-CAP-010
## Capitolul 6. Spirit și karmă — Lecții și direcții de maturizare

Index: {{cod_lucrare}}-SUB-023b
### 6.1. Codul Spiritului și vârsta Spiritului

Index: {{cod_lucrare}}-P-{{index_definitie_cod_spirit}}
{{definitie_conversationala_cod_spirit}}

Index: {{cod_lucrare}}-P-{{index_pozitie_cod_spirit}}
În tabel, poziția ta este la ziua **{{zi_nastere}}** și luna **{{luna_romana}}**, unde apare codul **{{cod_spirit}}**.

Index: {{cod_lucrare}}-T-017
{{tabel_cod_spirit_zi_luna_markdown}}

> [!important] Contract vizual T-017
> Tabelul respectă calendarul: 29-31 februarie și ziua 31 din aprilie, iunie, septembrie și noiembrie rămân goale. Codurile sunt colorate după zonă: `spirit-zone-love` pentru `0-13`, `spirit-zone-reason` pentru `14-26`, `spirit-zone-material` pentru `27-39`, `spirit-zone-gifts` pentru `40-52`. Intersecția persoanei folosește exclusiv `spirit-cell-highlight`, turcoaz cu text alb ca în `BDR-19980219-v1.00r-T-017`, fără clasă de zonă pe același marcaj.

Index: {{cod_lucrare}}-P-{{index_interpretare_cod_spirit}}
{{interpretare_cod_spirit_si_zona_fara_repetarea_formulei}}

Index: {{cod_lucrare}}-T-018
| Zona | Interval cod | Nivel simbolic | Teme principale |
| --- | --- | --- | --- |
| Iubire | 1–13 | 0–2.500 ani | relații, emoții, atașamente, compasiune, vulnerabilitate |
| Rațiune | 14–26 | 2.500–5.000 ani | logică, discernământ, structură, analiză, minte |
| Material | 27–39 | 5.000–7.500 ani | bani, construcție, putere, manifestare, responsabilitate |
| Haruri | 40–52 | 7.500–10.000 ani | înțelepciune, haruri spirituale, ghidare, serviciu, intuiție |

Index: {{cod_lucrare}}-T-019
{{tabel_etape_si_subetape_spirit_markdown}}

> [!important] Contract vizual T-019
> Tabelul pastreaza structura validata din `BDR-19980219-v1.00r-T-019`: `Etapă`, `Descriere etapă`, `Subetapă`, `Lecție`, `Descriere subetapă`, cu `rowspan` pentru Etapă si Descriere etapă acolo unde etapa are mai multe subetape. Aplica `current-row` numai subetapei persoanei curente.

Index: {{cod_lucrare}}-P-{{index_interpretare_subetapa_spirit}}
{{interpretare_conversationala_subetapa_spirit}}

Index: {{cod_lucrare}}-P-{{index_definitie_varsta_spirit}}
{{definitie_concisa_varsta_spirit}}

Index: {{cod_lucrare}}-C-{{index_calcul_varsta_spirit}}
> [!example] Calcul
> Vârsta la naștere = ({{cod_spirit}} × 189) - 189 = **{{varsta_spirit_la_nastere}}**
>
> Vârsta actuală = {{varsta_spirit_la_nastere}} + {{varsta_biologica}} = **{{varsta_spirit_actuala}}**

Index: {{cod_lucrare}}-P-{{index_ghidare_practica_spirit}}
{{ghidare_practica_spirit_fara_repetarea_calculului}}

Index: {{cod_lucrare}}-SUB-023c
### 6.2. Karma din ziua de naștere

Index: {{cod_lucrare}}-P-{{index_definitie_karma_zi}}
{{interpretare_conversationala_karma_zi_interval_procent_si_arcana}}

Index: {{cod_lucrare}}-C-{{index_calcul_karma_zi}}
> [!example] Calcul
> Ziua nașterii = **{{zi_nastere}}**
>
> Arcana karmică = **{{arcana_karma_zi}} — {{nume_arcana_karma_zi}}**
>
> Intervalul {{interval_karma_zi}} = karma împlinită **{{procent_karma_zi}}**

Index: {{cod_lucrare}}-G-{{index_arcana_karma_zi}}
![Arcana {{arcana_karma_zi}} — {{nume_arcana_karma_zi}}, karma din ziua de naștere]({{fisier_arcana_karma_zi}})

_Arcana **{{arcana_karma_zi}}** — {{nume_arcana_karma_zi}}. Karma din ziua de naștere_

Index: {{cod_lucrare}}-P-{{index_resursa_karma_zi}}
{{resursa_si_manifestare_karma_zi}}

Index: {{cod_lucrare}}-P-{{index_umbra_karma_zi}}
{{umbra_karma_zi_ca_posibilitate_nu_predictie}}

Index: {{cod_lucrare}}-P-{{index_maturizare_karma_zi}}
{{maturizare_karma_zi}}

Index: {{cod_lucrare}}-SUB-023d
### 6.3. Karma din luna de naștere

Index: {{cod_lucrare}}-P-{{index_definitie_karma_luna}}
{{definitie_conversationala_karma_luna}}

Index: {{cod_lucrare}}-C-{{index_calcul_karma_luna}}
> [!example] Calcul
> Luna nașterii = **{{luna_nastere}}**
>
> Karma lunii = **{{denumire_karma_luna}}**

Index: {{cod_lucrare}}-P-{{index_interpretare_karma_luna}}
{{interpretare_karma_luna_resursa_umbra_limite_si_maturizare}}

Index: {{cod_lucrare}}-SUB-023e
### 6.4. Karma din Calea Destinului

Index: {{cod_lucrare}}-P-{{index_definitie_karma_calea_destinului}}
{{definitie_karma_calea_destinului_si_suma_compusa}}

Index: {{cod_lucrare}}-C-{{index_calcul_karma_calea_destinului}}
> [!example] Calcul
> {{calcul_suma_cifrelor_datei}} = **{{karma_calea_destinului}}**
>
> Karma din Calea Destinului = **{{karma_calea_destinului}}**
>
> Intervalul {{interval_karma_calea_destinului}} = categoria karmică **{{categoria_karma_calea_destinului}}**

Index: {{cod_lucrare}}-P-{{index_interpretare_karma_calea_destinului}}
{{interpretare_karma_calea_destinului_cu_directie_speciala_pentru_39_numarul_mintii}}

Index: {{cod_lucrare}}-SUB-023f
### 6.5. Concluzie: direcția de lucru

Index: {{cod_lucrare}}-P-{{index_concluzie_spirit_karma}}
{{concluzie_unica_spirit_zona_subetapa_varsta_si_trei_karme}}

Index: {{cod_lucrare}}-CAP-011
## Capitolul 7. Pinacluri: Oportunități și provocări

Index: {{cod_lucrare}}-P-024b
De-a lungul vieții, treci prin patru pinacluri, fiecare cu propria oportunitate și propria provocare. Oportunitatea arată direcția pe care viața o poate deschide, iar provocarea arată lecția care îți cere maturizare pentru a folosi constructiv acea direcție.

Index: {{cod_lucrare}}-C-013
> [!example] Calcul
> Calea Destinului: **{{calea_destinului}}**
> Destin compus: **{{destin_compus}}**
> Limita Pinaclului 1: 36 - **{{destin_compus}}** = **{{limita_pinaclu_1}}**
> Pinacluri: **{{interval_1}}** -> **{{interval_2}}** -> **{{interval_3}}** -> **{{interval_4}}**

Index: {{cod_lucrare}}-T-003
| Pinaclu | Interval | Oportunitate | Provocare | Interpretare |
| --- | --- | ---: | ---: | --- |
| 1 | {{interval_1}} | {{oportunitate_1}} | {{provocare_1}} | {{interpretare_tabel_pinaclu_1}} |
| 2 | {{interval_2}} | {{oportunitate_2}} | {{provocare_2}} | {{interpretare_tabel_pinaclu_2}} |
| 3 | {{interval_3}} | {{oportunitate_3}} | {{provocare_3}} | {{interpretare_tabel_pinaclu_3}} |
| 4 | {{interval_4}} | {{oportunitate_4}} | {{provocare_4}} | {{interpretare_tabel_pinaclu_4}} |

Index: {{cod_lucrare}}-P-024c
**Pinaclul 1: {{formulare_interval_pinaclu_1}}**, {{interpretare_pinaclu_1}}

Index: {{cod_lucrare}}-P-024d
**Pinaclul 2: {{formulare_interval_pinaclu_2}}**, {{interpretare_pinaclu_2}}

Index: {{cod_lucrare}}-P-024e
**Pinaclul 3: {{formulare_interval_pinaclu_3}}**, {{interpretare_pinaclu_3}}

Index: {{cod_lucrare}}-P-024f
**Pinaclul 4: {{formulare_interval_pinaclu_4}}**, {{interpretare_pinaclu_4}}

Index: {{cod_lucrare}}-CAP-012
## Capitolul 8. Ciclicități

Index: {{cod_lucrare}}-SUB-024
### 8.1. Soarta și Destinul

{{definitie_metoda_si_interpretare_soarta_destin}}

Index: {{cod_lucrare}}-C-006
> [!example] Sinteză
> Soartă: **{{sir_soarta}}**  
> Destin: **{{sir_destin}}**

Index: {{cod_lucrare}}-SUB-025
### 8.2. Anii importanți

Index: {{cod_lucrare}}-P-026a
**Anii importanți interiori** marchează momente în care schimbarea pornește mai ales din interiorul persoanei: decizii, maturizări, conștientizări, schimbări de perspectivă, nevoi sufletești sau transformări personale care apoi pot modifica viața din afară.

Index: {{cod_lucrare}}-P-026b
**Șirul anilor importanți interiori:** {{sir_ani_importanti_interiori}}.

Index: {{cod_lucrare}}-P-026c
**Anii importanți exteriori** marchează momente în care schimbarea vine mai ales din afara persoanei: contexte, oameni, evenimente, oportunități, pierderi, mutări, presiuni sau situații care cer reacție și adaptare.

Index: {{cod_lucrare}}-P-026d
**Șirul anilor importanți exteriori:** {{sir_ani_importanti_exteriori}}.

Index: {{cod_lucrare}}-SUB-025a
### 8.3. Lecțiile de viață

Index: {{cod_lucrare}}-T-008
{{tabel_lectii_de_viata_dinamic_dupa_sir_lectii}}

> [!important] Contract T-008
> Recalculează lecțiile de viață cu formula `zi x lună x an`, apoi folosește toate cifrele produsului, în ordine, inclusiv fiecare `0`. Numărul coloanelor este numărul cifrelor produsului; anii se distribuie consecutiv și șirul se repetă ciclic, după modelul `BDR-19980219-v1.00r-SUB-025a`.

{{interpretare_lectii_de_viata}}

Index: {{cod_lucrare}}-SUB-027
### 8.4. Ciclul de 9 ani

Index: {{cod_lucrare}}-T-007
| Ciclu | Anul 1 — început | Anul 2 | Anul 3 | Anul 4 | Anul 5 | Anul 6 | Anul 7 | Anul 8 | Anul 9 — încheiere |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| {{ciclu_9_1}} | **{{an_inceput}}** | {{an2}} | {{an3}} | {{an4}} | {{an5}} | {{an6}} | {{an7}} | {{an8}} | **{{an_final}}** |
| {{adauga_randuri_pentru_interval}} |  |  |  |  |  |  |  |  |  |

{{interpretare_ciclu_9_si_an_personal}}

Index: {{cod_lucrare}}-SUB-027a
### 8.5. Ciclul de 12 ani

Index: {{cod_lucrare}}-T-015
| Ciclu | Interval calendaristic | Vârste | Citire |
| --- | --- | ---: | --- |
| {{ciclu_12_1}} | {{interval_calendaristic_12_1}} | {{varste_12_1}} | {{interpretare_ciclu_12_1}} |
| {{adauga_randuri_ciclu_12_pentru_interval}} |  |  |  |

> [!important] Ciclul activ
> Marchează cu roșu și bold toate celulele rândului care conține data curentă. În HTML, aplică rândului clasa `active-cycle`.
> Coloana `Citire` trebuie redactată distinct pentru fiecare ciclu de 12 ani, în funcție de etapa de viață; nu repeta aceeași lectură generică pe mai multe rânduri.

{{interpretare_ciclu_12}}

> [!info] Capitol condițional
> Păstrează Capitolele 9 și 10 numai dacă există datele celei de-a doua persoane. Altfel elimină-le împreună cu intrările din Cuprins și renumerotează Concluziile ca Capitolul 9.

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
## Capitolul 10. Aplicabilitate profesională

Index: {{cod_lucrare}}-SUB-029
### 10.1. Aplicabilitate profesională

Index: {{cod_lucrare}}-P-035
{{descriere_aplicabilitate_profesionala}}

Index: {{cod_lucrare}}-P-046
> [!example] Calcul aplicabilitate profesională
> {{calcul_aplicabilitate_nu}}
> {{calcul_aplicabilitate_da}}

Index: {{cod_lucrare}}-T-016
| Aplicabilitate profesională DA | Aplicabilitate profesională NU |
| --- | --- |
| ![Arcana {{numar_arcana_da}} — {{nume_arcana_da}}]({{arcana_da_fisier}})  \n_Arcana {{numar_arcana_da}} — {{nume_arcana_da}}_ | ![Arcana {{numar_arcana_nu}} — {{nume_arcana_nu}}]({{arcana_nu_fisier}})  \n_Arcana {{numar_arcana_nu}} — {{nume_arcana_nu}}_ |
| **Index: {{cod_lucrare}}-P-047**  \n{{interpretare_aplicabilitate_da}} | **Index: {{cod_lucrare}}-P-048**  \n{{interpretare_aplicabilitate_nu}} |

Index: {{cod_lucrare}}-CAP-015
## Capitolul 11. Concluzii

Index: {{cod_lucrare}}-SUB-{{index_sub_cariera_bani}}
### 11.1. Carieră și bani

{{concluzie_cariera_bani_conform_metoda_concluzii_cu_paragrafe_indexate}}

Index: {{cod_lucrare}}-SUB-{{index_sub_iubire_relatii}}
### 11.2. Iubire și relație

{{concluzie_iubire_relatie_conform_metoda_concluzii_cu_paragrafe_indexate}}

Index: {{cod_lucrare}}-SUB-{{index_sub_momentul_prezent}}
### 11.3. Momentul prezent

{{concluzie_momentul_prezent_din_ciclicitati_cu_paragrafe_indexate}}

> [!info] Renumerotare fără relație
> Dacă nu există date relaționale, titlul devine `Capitolul 9. Concluzii`, iar ținta din Cuprins se actualizează identic. Elimină al doilea subcapitol sau păstrează numai o lectură generală `Iubire și relații`, fără partener ori valori inventate.

Index: {{cod_lucrare}}-CAP-016
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
- [ ] Cuprinsul Markdown folosește text simplu, fără wikilinkuri Obsidian.
- [ ] Cele șapte tabele provenite din imaginile-model sunt tabele editabile.
- [ ] Matricea 3×3 respectă modelul `BDR-19980219-v1.07r-G-001`.
- [ ] Paragrafele Căsuțelor 1-9 spun numărul de apariții și sensul energiei, fără comparația verbală cu optimul; absența este formulată ca energie conservată.
- [ ] Scara bunăstării are paragraf interpretativ indexat înaintea graficului și explică lanțul de sprijin dintre trepte.
- [ ] Capitolul 6 reunește Spiritul și cele trei karme, fără calcule ori explicații intermediare redundante, și se încheie cu o singură concluzie.
- [ ] Fiecare arcană numită are imagine în același subcapitol.
- [ ] Subcapitolul separat `1.7. Tarot` și vechiul tabel Tarot al Vibrației interioare lipsesc integral.
- [ ] Capitolul Relații este inclus numai când există date relaționale.
- [ ] Aplicabilitatea profesională este inclusă numai împreună cu Relațiile, iar T-016 are calcul unic, imagini și interpretări pe coloane egale.
- [ ] HTML-ul livrează toate SVG-urile și imaginile incorporate ca data URI.
- [ ] Subcapitolul Interior și exterior conține dialogul, definiția punții, calculul absolut în chenar și interpretarea autenticității.
- [ ] Capitolul 5 respectă ordinea Activ, Intim, Ereditar, Ereditar karmic, Realizare, Exprimare, Codul numelui.
- [ ] T-008 păstrează toate cifrele produsului `zi x lună x an`, inclusiv zerourile, și distribuie anii ciclic pe numărul real de poziții.
- [ ] T-015 are citiri distincte pe cicluri și marchează integral numai ciclul activ.
- [ ] T-017 lasă goale datele calendaristice inexistente, colorează `0` în albastru și folosește un singur marcaj turcoaz `spirit-cell-highlight`.
- [ ] T-019 păstrează cele cinci coloane Daniel, gruparea cu `rowspan` și un singur `current-row` pe subetapa persoanei.
- [ ] Diacriticele sunt UTF-8 fără mojibake.
- [ ] Concluziile includ Carieră și bani, Iubire și relație, apoi Momentul prezent când există sinteză temporală; Harta suprapusă este numai sursă de sinteză, nu subcapitol separat.
- [ ] SVG-ul Omulețului relațiilor este valid, are watermark `Atlas Numerologie` și nu a fost editat manual.
- [ ] Nu există date, ani, interpretări sau resurse rămase de la persoana-model.
