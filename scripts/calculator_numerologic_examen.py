"""Calculator numerologic agregat pentru lucrarea de examen.

Scriptul urmeaza ordinea din `templates/Cuprins_Lucrare_Numerologica.md` si
`templates/Template_Lucrare_Numerologica_Examen.md`. Este o baza de lucru:
formulele documentate in proiect sunt implementate, iar rubricile ramase fara
metoda operationala completa sunt marcate cu `status: de_completat`.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date, datetime
from typing import Any


ALFABET_PITAGOREIC = {
    **dict.fromkeys("AJS", 1),
    **dict.fromkeys("BKT", 2),
    **dict.fromkeys("CLU", 3),
    **dict.fromkeys("DMV", 4),
    **dict.fromkeys("ENW", 5),
    **dict.fromkeys("FOX", 6),
    **dict.fromkeys("GPY", 7),
    **dict.fromkeys("HQZ", 8),
    **dict.fromkeys("IR", 9),
}

VOCALE = set("AEIOU")
VECTORI = {
    "123": "Energie",
    "456": "Vointa",
    "789": "Creativitate",
    "147": "Spiritualitate",
    "258": "Social",
    "369": "Bunastare materiala",
    "159": "Cariera",
    "357": "Scopuri",
}
ORDINE_MATRICE = ((1, 4, 7), (2, 5, 8), (3, 6, 9))
TRASEU_PATRAT_AUR = [4, 9, 2, 3, 5, 7, 8, 1, 6]


@dataclass
class TraseuReducere:
    intrare: int
    pasi: list[str]
    rezultat: int


def cifre(numar: int | str) -> list[int]:
    return [int(cifra) for cifra in str(numar) if cifra.isdigit()]


def reducere_numerologica(numar: int) -> TraseuReducere:
    pasi: list[str] = []
    curent = abs(numar)
    while curent > 9:
        componente = cifre(curent)
        urmator = sum(componente)
        pasi.append(f"{' + '.join(map(str, componente))} = {urmator}")
        curent = urmator
    return TraseuReducere(intrare=numar, pasi=pasi, rezultat=curent)


def reducere_o_singura_data(numar: int) -> TraseuReducere:
    componente = cifre(abs(numar))
    rezultat = sum(componente)
    pas = f"{' + '.join(map(str, componente))} = {rezultat}"
    return TraseuReducere(intrare=numar, pasi=[pas], rezultat=rezultat)


def reducere_22(numar: int) -> dict[str, Any]:
    pasi = []
    curent = numar
    while curent > 22:
        urmator = curent - 22
        pasi.append(f"{curent} - 22 = {urmator}")
        curent = urmator
    return {"intrare": numar, "pasi": pasi, "rezultat": curent}


def arcana_majora(numar: int) -> int:
    return 0 if numar == 22 else numar


def normalizare_text(text: str) -> str:
    fara_diacritice = unicodedata.normalize("NFD", text or "")
    fara_diacritice = "".join(
        caracter for caracter in fara_diacritice if unicodedata.category(caracter) != "Mn"
    )
    return re.sub(r"[^A-Z]", "", fara_diacritice.upper())


def componente_nume(nume: str) -> list[str]:
    return [componenta for componenta in re.split(r"\s+", (nume or "").strip()) if componenta]


def valori_litere(text: str) -> list[dict[str, Any]]:
    litere = normalizare_text(text)
    return [
        {"litera": litera, "valoare": ALFABET_PITAGOREIC[litera]}
        for litera in litere
        if litera in ALFABET_PITAGOREIC
    ]


def suma_litere(text: str, doar: str | None = None) -> dict[str, Any]:
    valori = valori_litere(text)
    if doar == "vocale":
        valori = [item for item in valori if item["litera"] in VOCALE]
    elif doar == "consoane":
        valori = [item for item in valori if item["litera"] not in VOCALE]
    total = sum(item["valoare"] for item in valori)
    redus = reducere_numerologica(total) if total else TraseuReducere(0, [], 0)
    return {"valori": valori, "total": total, "reducere": asdict(redus)}


def parse_data_nasterii(text: str) -> date:
    for format_data in ("%d.%m.%Y", "%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(text, format_data).date()
        except ValueError:
            pass
    raise ValueError("Data nasterii trebuie sa fie in format DD.MM.YYYY, DD-MM-YYYY sau YYYY-MM-DD.")


def data_compacta(data_nasterii: date) -> str:
    return f"{data_nasterii.day:02d}{data_nasterii.month:02d}{data_nasterii.year:04d}"


def prima_cifra_nenula(numar: int) -> int:
    for cifra in cifre(numar):
        if cifra != 0:
            return cifra
    return 0


def vibratii(data_nasterii: date) -> dict[str, Any]:
    zi = data_nasterii.day
    luna = data_nasterii.month
    an = data_nasterii.year
    suma_data = sum(cifre(data_compacta(data_nasterii)))
    zi_redusa = reducere_numerologica(zi)
    luna_redusa = reducere_numerologica(luna)
    an_redus = reducere_numerologica(sum(cifre(an)))
    calea = suma_data
    vibratia_destinului = reducere_numerologica(calea)
    aspecte = calea - 2 * prima_cifra_nenula(zi)

    return {
        "vibratia_interioara": {
            "formula": "reducere_numerologica(ziua nasterii)",
            "calcul": asdict(zi_redusa),
        },
        "vibratia_interioara_karmica": {
            "status": "de_completat",
            "observatie": "Trebuie validata regula de karma pentru zi in versiunea finala.",
        },
        "linii_de_tensiune": {
            "status": "de_completat",
            "observatie": "Rubrica exista in cuprins, dar formula operationala trebuie confirmata.",
        },
        "vibratia_exterioara": {
            "formula": "reducere_numerologica(luna nasterii)",
            "calcul": asdict(luna_redusa),
        },
        "vibratia_exterioara_karmica": {
            "status": "de_completat",
            "observatie": "Trebuie validata regula de karma pentru luna.",
        },
        "vibratia_globala": {
            "formula": "reducere_numerologica(ziua nasterii + luna nasterii)",
            "calcul": asdict(reducere_numerologica(zi + luna)),
        },
        "puntea_interior_exterior": punte(zi_redusa.rezultat, luna_redusa.rezultat),
        "vibratia_cosmica_fixa": {
            "formula": "primele doua cifre ale anului",
            "calcul": str(an)[:2],
            "rezultat": int(str(an)[:2]),
        },
        "vibratia_cosmica_variabila": {
            "formula": "reducere_numerologica(ultimele doua cifre ale anului)",
            "calcul": asdict(reducere_numerologica(int(str(an)[-2:]))),
        },
        "vibratia_cosmica_totala": {
            "formula": "reducere_numerologica(suma cifrelor anului)",
            "calcul": asdict(an_redus),
        },
        "calea_destinului": {
            "formula": "suma cifrelor din data nasterii, neredusa complet",
            "calcul": f"{' + '.join(map(str, cifre(data_compacta(data_nasterii))))} = {calea}",
            "rezultat": calea,
        },
        "calea_destinului_karmica": {
            "formula": "aceeasi baza ca la calea destinului; interpretare karmica",
            "calcul": calea,
            "rezultat": calea,
        },
        "destinul_vibratia_destinului": {
            "formula": "reducere_numerologica(calea destinului)",
            "calcul": asdict(vibratia_destinului),
        },
        "puntea_interior_destin": punte(zi_redusa.rezultat, vibratia_destinului.rezultat),
        "aspecte_de_indreptat": {
            "formula": "calea destinului - 2 x prima cifra din ziua nasterii",
            "calcul": f"{calea} - 2 x {prima_cifra_nenula(zi)} = {aspecte}",
            "rezultat": aspecte,
        },
        "solutia_aspectelor_de_indreptat": {
            "formula": "insumarea cifrelor o singura data (aspecte de indreptat)",
            "calcul": asdict(reducere_o_singura_data(aspecte)),
        },
    }


def punte(a: int, b: int) -> dict[str, Any]:
    diferenta = abs(a - b)
    return {
        "formula": "valoare_absoluta(vibratie_a - vibratie_b)",
        "calcul": f"|{a} - {b}| = {diferenta}",
        "rezultat": diferenta,
    }


def matrice_data_nasterii(data_nasterii: date) -> dict[str, Any]:
    data = data_compacta(data_nasterii)
    n1 = sum(cifre(data))
    n2 = reducere_o_singura_data(n1).rezultat
    n3 = n1 - 2 * prima_cifra_nenula(data_nasterii.day)
    n4 = reducere_o_singura_data(n3).rezultat
    sir = data + str(n1) + str(n2) + str(n3) + str(n4)
    return construieste_matrice(
        [int(cifra) for cifra in sir if cifra.isdigit() and cifra != "0"],
        {
            "data_compacta": data,
            "numere_de_lucru": {"n1": n1, "n2": n2, "n3": n3, "n4": n4},
            "sir_complet": sir,
        },
    )


def construieste_matrice(lista_cifre: list[int], meta: dict[str, Any] | None = None) -> dict[str, Any]:
    aparitii = Counter(lista_cifre)
    casute = {
        str(cifra): {
            "cifre": str(cifra) * aparitii[cifra] if aparitii[cifra] else "-",
            "cantitate": aparitii[cifra],
            "valoare": cifra * aparitii[cifra],
        }
        for cifra in range(1, 10)
    }
    vectori = calculeaza_vectori(casute)
    return {
        "meta": meta or {},
        "casute": casute,
        "randuri": [[casute[str(cifra)]["cifre"] for cifra in rand] for rand in ORDINE_MATRICE],
        "pare_impare": {
            "pare": sum(aparitii[cifra] for cifra in (2, 4, 6, 8)),
            "impare": sum(aparitii[cifra] for cifra in (1, 3, 5, 7, 9)),
        },
        "vectori": vectori,
        "figuri_geometrice": figuri_geometrice(casute),
        "tendinte": tendinte(casute),
        "fixatia": fixatia(vectori),
        "caii_trasura_vizitiul": {
            "caii_123": vectori["123"],
            "trasura_456": vectori["456"],
            "vizitiul_789": vectori["789"],
        },
        "curgerea_energiei": {
            "status": "de_completat",
            "observatie": "Necesita formalizare completa din vault/Numerologie/Curgerea Energiei.md.",
        },
        "comparatia_cu_optimul": comparatie_cu_optimul(casute),
        "scara_bunastarii": scara_bunastarii(casute, vectori),
    }


def calculeaza_vectori(casute: dict[str, dict[str, Any]]) -> dict[str, Any]:
    vectori = {}
    for cod, denumire in VECTORI.items():
        cifre_vector = list(cod)
        valoare = sum(casute[cifra]["valoare"] for cifra in cifre_vector)
        cantitate = "".join(casute[cifra]["cifre"].replace("-", "") for cifra in cifre_vector) or "-"
        vectori[cod] = {
            "denumire": denumire,
            "cifre": cantitate,
            "valoare": valoare,
            "este_plin": all(casute[cifra]["cantitate"] > 0 for cifra in cifre_vector),
        }
    return vectori


def figuri_geometrice(casute: dict[str, dict[str, Any]]) -> dict[str, Any]:
    prezente = [int(cifra) for cifra, info in casute.items() if info["cantitate"] > 0]
    return {
        "cifre_prezente": prezente,
        "cantitate_casute_active": len(prezente),
        "status": "calcul_cantitativ_initial",
    }


def tendinte(casute: dict[str, dict[str, Any]]) -> dict[str, Any]:
    maxim = max(info["valoare"] for info in casute.values())
    dominante = [cifra for cifra, info in casute.items() if info["valoare"] == maxim and maxim > 0]
    lipsa = [cifra for cifra, info in casute.items() if info["cantitate"] == 0]
    return {"casute_dominante": dominante, "casute_lipsa": lipsa}


def fixatia(vectori: dict[str, Any]) -> dict[str, Any]:
    plini = {cod: info for cod, info in vectori.items() if info["este_plin"]}
    if not plini:
        return {"rezultat": None, "observatie": "Nu exista vector plin dominant."}
    maxim = max(info["valoare"] for info in plini.values())
    dominante = [cod for cod, info in plini.items() if info["valoare"] == maxim]
    return {"vectori_dominanti": dominante, "valoare": maxim}


def comparatie_cu_optimul(casute: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return {
        cifra: {
            "cantitate": info["cantitate"],
            "diferenta_fata_de_1_aparitie": info["cantitate"] - 1,
        }
        for cifra, info in casute.items()
    }


def scara_bunastarii(casute: dict[str, dict[str, Any]], vectori: dict[str, Any]) -> list[dict[str, Any]]:
    randuri = []
    for cod, info in vectori.items():
        randuri.append(
            {
                "tip": "vector",
                "denumire": f"{cod} - {info['denumire']}",
                "cantitate": info["cifre"],
                "formula": " + ".join(cod),
                "valoare": info["valoare"],
            }
        )
    for cifra, info in casute.items():
        randuri.append(
            {
                "tip": "casuta",
                "denumire": cifra,
                "cantitate": info["cifre"],
                "formula": " + ".join(info["cifre"]) if info["cifre"] != "-" else "0",
                "valoare": info["valoare"],
            }
        )
    return sorted(randuri, key=lambda rand: (-rand["valoare"], rand["denumire"]))


def numar_exprimare(nume: str) -> dict[str, Any]:
    componente = []
    for componenta in componente_nume(nume):
        calcul = suma_litere(componenta)
        componente.append({"componenta": componenta, **calcul})
    total_reduse = sum(item["reducere"]["rezultat"] for item in componente)
    return {
        "formula": "reducere(suma reducerilor componentelor numelui)",
        "componente": componente,
        "total_reduse": total_reduse,
        "reducere": asdict(reducere_numerologica(total_reduse)),
    }


def codul_numelui(nume_complet: str) -> dict[str, Any]:
    valori = valori_litere(nume_complet)
    exprimare = numar_exprimare(nume_complet)["reducere"]["rezultat"]
    cifre_cod = [item["valoare"] for item in valori] + ([exprimare] if exprimare else [])

    return {
        "formula": "sirul valorilor numerologice ale numelui complet + numarul de exprimare",
        "valori_nume": valori,
        "numar_exprimare": exprimare,
        "cifre": cifre_cod,
        "sir": "".join(map(str, cifre_cod)),
    }


def matrice_nume(
    nume: str,
    nume_familie: str | None = None,
    prenume: str | None = None,
) -> dict[str, Any]:
    cod = codul_numelui(nume)
    return construieste_matrice(
        cod["cifre"],
        {
            "nume": nume,
            "numar_exprimare_introdus_in_matrice": cod["numar_exprimare"],
            "codul_numelui": cod,
        },
    )


def profil_nume(
    nume_complet: str,
    nume_familie: str | None = None,
    prenume: str | None = None,
    prenume_activ: str | None = None,
    nume_anterior: str | None = None,
) -> dict[str, Any]:
    componente = componente_nume(nume_complet)
    familie = nume_familie or (componente[0] if componente else "")
    activ = prenume_activ or prenume or (componente[1] if len(componente) > 1 else (componente[0] if componente else ""))
    ereditar_total = suma_litere(familie)["total"]
    profil = {
        "nume_complet": nume_complet,
        "nume_normalizat": normalizare_text(nume_complet),
        "numarul_de_exprimare": numar_exprimare(nume_complet),
        "numarul_intim": {"formula": "reducere(suma vocalelor)", **suma_litere(nume_complet, "vocale")},
        "numarul_de_realizare": {"formula": "reducere(suma consoanelor)", **suma_litere(nume_complet, "consoane")},
        "numarul_activ": {"prenume_activ": activ, **suma_litere(activ)},
        "numarul_ereditar": {"nume_familie": familie, **suma_litere(familie)},
        "numarul_ereditar_karmic_neamul": {
            "nume_familie": familie,
            "total": ereditar_total,
            "reducere_22": reducere_22(ereditar_total),
            "arcana_majora": arcana_majora(reducere_22(ereditar_total)["rezultat"]),
        },
        "matricea_numelui": matrice_nume(nume_complet, familie, prenume),
        "cifra_energetica": {
            "status": "de_completat",
            "observatie": "Formula trebuie confirmata in documentatia de nume.",
        },
        "cifre_intense": cifre_intense(nume_complet),
        "primele_si_ultimele_litere": primele_ultimele_litere(nume_complet),
        "primele_vocale": primele_vocale(nume_complet),
        "cheile_de_bolta": {
            "status": "de_completat",
            "observatie": "Necesita validarea regulii finale pentru cheia de bolta.",
        },
        "structura_literelor": structura_literelor(nume_complet),
        "temperamentul": {
            "status": "de_completat",
            "observatie": "Metoda pentru numerele temperamentului trebuie formalizata.",
        },
        "cifrele_de_tensiune": {
            "status": "de_completat",
            "observatie": "Metoda pentru cifrele de tensiune ale numelui trebuie formalizata.",
        },
    }
    if nume_anterior:
        profil["nume_anterior_schimbat"] = profil_nume(nume_anterior)
    return profil


def cifre_intense(nume: str) -> dict[str, Any]:
    valori = [item["valoare"] for item in valori_litere(nume)]
    aparitii = Counter(valori)
    maxim = max(aparitii.values(), default=0)
    return {"aparitii": dict(sorted(aparitii.items())), "cifre_intense": [c for c, n in aparitii.items() if n == maxim]}


def primele_ultimele_litere(nume: str) -> list[dict[str, Any]]:
    rezultat = []
    for componenta in componente_nume(nume):
        litere = normalizare_text(componenta)
        if litere:
            rezultat.append(
                {
                    "componenta": componenta,
                    "prima": {"litera": litere[0], "valoare": ALFABET_PITAGOREIC.get(litere[0])},
                    "ultima": {"litera": litere[-1], "valoare": ALFABET_PITAGOREIC.get(litere[-1])},
                }
            )
    return rezultat


def primele_vocale(nume: str) -> list[dict[str, Any]]:
    rezultat = []
    for componenta in componente_nume(nume):
        litere = normalizare_text(componenta)
        vocale = [litera for litera in litere if litera in VOCALE]
        rezultat.append(
            {
                "componenta": componenta,
                "prima_vocala": vocale[0] if vocale else None,
                "valoare": ALFABET_PITAGOREIC.get(vocale[0]) if vocale else None,
            }
        )
    return rezultat


def structura_literelor(nume: str) -> dict[str, Any]:
    valori = valori_litere(nume)
    mentale = [item for item in valori if item["valoare"] in (1, 8)]
    fizice = [item for item in valori if item["valoare"] in (4, 5)]
    emotionale = [item for item in valori if item["valoare"] in (2, 3, 6)]
    intuitive = [item for item in valori if item["valoare"] in (7, 9)]
    litere = normalizare_text(nume)
    return {
        "mentale": mentale,
        "fizice": fizice,
        "emotionale": emotionale,
        "intuitive": intuitive,
        "initiatoare_continuatoare_finalizatoare": {
            "initiatoare": litere[0] if litere else None,
            "continuatoare": litere[1:-1] if len(litere) > 2 else "",
            "finalizatoare": litere[-1] if litere else None,
        },
        "observatie": "Clasificarea pe planuri este operationala si trebuie validata cu bibliografia finala.",
    }


def comparatie_matrici(matrice_data: dict[str, Any], matrice_nume_: dict[str, Any]) -> dict[str, Any]:
    rezultat = {}
    for cifra in map(str, range(1, 10)):
        data_count = matrice_data["casute"][cifra]["cantitate"]
        nume_count = matrice_nume_["casute"][cifra]["cantitate"]
        diferenta = nume_count - data_count
        if data_count == 0 and nume_count > 0:
            status = "potential_de_nume_fara_suport_nativ"
        elif diferenta >= 2:
            status = "exces_in_nume"
        elif data_count > 0 and nume_count == 0:
            status = "lipsa_in_nume"
        elif data_count > 0 and nume_count > 0:
            status = "sustinuta_sau_nuantata"
        else:
            status = "absenta"
        rezultat[cifra] = {"data": data_count, "nume": nume_count, "diferenta": diferenta, "status": status}
    return rezultat


def pinacluri(data_nasterii: date) -> dict[str, Any]:
    zi = reducere_numerologica(data_nasterii.day).rezultat
    luna = reducere_numerologica(data_nasterii.month).rezultat
    an = reducere_numerologica(sum(cifre(data_nasterii.year))).rezultat
    destin = reducere_numerologica(sum(cifre(data_compacta(data_nasterii)))).rezultat
    oportunitati = [
        reducere_numerologica(luna + zi).rezultat,
        reducere_numerologica(zi + an).rezultat,
        0,
        reducere_numerologica(luna + an).rezultat,
    ]
    oportunitati[2] = reducere_numerologica(oportunitati[0] + oportunitati[1]).rezultat
    provocari = [abs(zi - luna), abs(zi - an), 0, abs(luna - an)]
    provocari[2] = abs(provocari[0] - provocari[1])
    final_1 = 36 - destin
    final_2 = final_1 + 9
    final_3 = final_2 + 9
    intervale = [f"0-{final_1}", f"{final_1 + 1}-{final_2}", f"{final_2 + 1}-{final_3}", f"{final_3 + 1}+"]
    return {
        "baza": {"zi_redusa": zi, "luna_redusa": luna, "an_redus": an, "vibratia_destinului": destin},
        "zona_confort_oportunitati": sum(oportunitati) / 4,
        "zona_confort_provocari": sum(provocari) / 4,
        "randuri": [
            {
                "pinaclu": index + 1,
                "interval_varsta": intervale[index],
                "oportunitate": oportunitati[index],
                "provocare": provocari[index],
            }
            for index in range(4)
        ],
    }


def lectii_de_viata(data_nasterii: date, ani: int = 108) -> dict[str, Any]:
    produs = data_nasterii.day * data_nasterii.month * data_nasterii.year
    sir = [int(cifra) for cifra in str(produs) if cifra != "0"]
    return {
        "formula": "zi x luna x an; cifrele rezultatului se aplica ciclic pe anii de viata",
        "produs": produs,
        "sir_lectii": sir,
        "ani": [
            {"an_de_viata": index + 1, "lectie": sir[index % len(sir)] if sir else None}
            for index in range(ani)
        ],
    }


def ciclu_9_ani(data_nasterii: date, start: int | None = None, final: int | None = None) -> list[dict[str, Any]]:
    start = start or data_nasterii.year
    final = final or data_nasterii.year + 108
    lectii = lectii_de_viata(data_nasterii, max(1, final - data_nasterii.year + 2))["ani"]
    randuri = []
    for an in range(start, final + 1):
        varsta = an - data_nasterii.year
        an_personal = reducere_numerologica(data_nasterii.day + data_nasterii.month + an).rezultat
        lectie_index = max(varsta, 0)
        randuri.append(
            {
                "an": an,
                "varsta": varsta,
                "an_personal": an_personal,
                "lectie": lectii[lectie_index]["lectie"] if lectie_index < len(lectii) else None,
            }
        )
    return randuri


def cicluri_7_ani(data_nasterii: date, pana_la_varsta: int = 108) -> list[dict[str, Any]]:
    return [
        {
            "ciclu": index + 1,
            "interval_varsta": f"{index * 7}-{min(index * 7 + 6, pana_la_varsta)}",
            "inceput_varsta": index * 7,
            "sfarsit_varsta": min(index * 7 + 6, pana_la_varsta),
        }
        for index in range((pana_la_varsta // 7) + 1)
    ]


def cicluri_12_ani(data_nasterii: date, pana_la_varsta: int = 108) -> list[dict[str, Any]]:
    return [
        {
            "ciclu": index + 1,
            "interval_varsta": f"{index * 12}-{min(index * 12 + 11, pana_la_varsta)}",
            "inceput_varsta": index * 12,
            "sfarsit_varsta": min(index * 12 + 11, pana_la_varsta),
        }
        for index in range((pana_la_varsta // 12) + 1)
    ]


def ani_importanti(data_nasterii: date, final: int | None = None) -> dict[str, Any]:
    final = final or data_nasterii.year + 108
    return {
        "interiori": secventa_ani_importanti(data_nasterii.year, final, "interior"),
        "exteriori": secventa_ani_importanti(data_nasterii.year, final, "exterior"),
        "observatie": "Implementare initiala pe metoda iterativa din temp/calcule/timp-si-cicluri; trebuie validata pe exemple.",
    }


def secventa_ani_importanti(start: int, final: int, tip: str) -> list[int]:
    ani = []
    curent = start
    while curent <= final:
        suma = sum(cifre(curent))
        urmator = curent + suma if tip == "exterior" else curent + reducere_numerologica(suma).rezultat
        if urmator <= curent:
            break
        if urmator <= final:
            ani.append(urmator)
        curent = urmator
    return ani


def soarta_si_destin(data_nasterii: date) -> dict[str, Any]:
    zzll = int(f"{data_nasterii.day:02d}{data_nasterii.month:02d}")
    an = data_nasterii.year
    return {
        "soarta": {
            "status": "de_completat",
            "baza_posibila": zzll,
            "observatie": "Formula exacta pentru soarta trebuie confirmata din temp/calcule/soarta-si-destin.",
        },
        "destin_grafic": {
            "status": "de_completat",
            "baza_posibila": an,
            "observatie": "Template-ul mentioneaza formula ZZLL ajustat x AAAA ajustat; ajustarea trebuie finalizata.",
        },
    }


def inclinatii_profesionale(data_nasterii: date) -> dict[str, Any]:
    suma_cifre_an = sum(cifre(data_nasterii.year))
    suma_cifre_data = sum(int(cifra) for cifra in data_compacta(data_nasterii))
    da = reducere_arcane(data_nasterii.month + suma_cifre_an)
    nu = reducere_arcane(suma_cifre_data)
    return {
        "formula_operationala": "DA = luna + suma cifrelor anului; NU = suma tuturor cifrelor datei; rezultate pastrate in intervalul 1-22",
        "da": da,
        "nu": nu,
        "calcul_da": f"{data_nasterii.month} + {suma_cifre_an} = {data_nasterii.month + suma_cifre_an} -> {da}",
        "calcul_nu": f"{suma_cifre_data} -> {nu}",
    }


def reducere_arcane(numar: int) -> int:
    while numar > 22:
        numar -= 22
    return numar


def inclinatii_ezoterice(data_nasterii: date) -> dict[str, Any]:
    numar = int(data_compacta(data_nasterii))
    if numar % 7 == 0:
        return {"cod_principal": 0, "cod_secundar": None, "calcul": f"{numar} / 7 exact"}
    cat = numar // 7
    prima_zecimala = int(str((numar * 10) // 7)[-1])
    secundar = int(str((cat * 10) // 7)[-1])
    return {
        "formula": "prima cifra dupa virgula la impartirea datei compacte la 7; secundar din partea intreaga / 7",
        "data_compacta": numar,
        "cod_principal": prima_zecimala,
        "partea_intreaga": cat,
        "cod_secundar": secundar,
    }


def codul_spiritului(data_nasterii: date) -> dict[str, Any]:
    zi_luna = data_nasterii.day + data_nasterii.month
    cod = reducere_numerologica(zi_luna).rezultat
    return {
        "formula_initiala": "reducere_numerologica(ziua + luna)",
        "cod_spirit": cod,
        "status": "partial",
        "observatie": "Etapele, subetapele si varsta spiritului necesita transcrierea completa din vault/Numerologie/Codul Spiritului.md.",
    }


def semnatura_astrala(data_nasterii: date) -> dict[str, Any]:
    return {
        "status": "de_completat",
        "observatie": "Formula trebuie extrasa si validata din documentatia de ajutoare.",
    }


def directii_de_succes(data_nasterii: date, gen: str | None = None) -> dict[str, Any]:
    variabila = reducere_numerologica(int(str(data_nasterii.year)[-2:])).rezultat
    return {
        "baza": variabila,
        "gen": gen,
        "status": "partial",
        "observatie": "Formula pe gen trebuie completata din vault/Numerologie/Directiile de Succes.md.",
    }


def triunghi_financiar(data_nasterii: date) -> dict[str, Any]:
    zi = reducere_numerologica(data_nasterii.day).rezultat
    luna = reducere_numerologica(data_nasterii.month).rezultat
    an = reducere_numerologica(sum(cifre(data_nasterii.year))).rezultat
    destin = reducere_numerologica(zi + luna + an).rezultat
    return {
        "formula": "zi redusa + luna redusa + an redus + destin redus",
        "baza": [zi, luna, an, destin],
        "destin": destin,
    }


def patratul_de_aur(data_nasterii: date) -> dict[str, Any]:
    valori = {}
    valoare = data_nasterii.day
    for pozitie in TRASEU_PATRAT_AUR:
        valori[str(pozitie)] = valoare
        valoare += 1
    randuri = [[valori[str(cifra)] for cifra in rand] for rand in ORDINE_MATRICE]
    return {
        "traseu": TRASEU_PATRAT_AUR,
        "casute": valori,
        "randuri": randuri,
        "valoare_centrala": valori["5"],
        "suma_control": valori["5"] * 3,
    }


def raport_complet(
    data_nasterii: date,
    nume_complet: str,
    nume_familie: str | None = None,
    prenume: str | None = None,
    prenume_activ: str | None = None,
    gen: str | None = None,
    nume_anterior: str | None = None,
    an_start: int | None = None,
    an_final: int | None = None,
) -> dict[str, Any]:
    matrice_data = matrice_data_nasterii(data_nasterii)
    nume = profil_nume(nume_complet, nume_familie, prenume, prenume_activ, nume_anterior)
    an_final_calcul = data_nasterii.year + 108
    return {
        "date_intrare": {
            "data_nasterii": data_nasterii.isoformat(),
            "nume_complet": nume_complet,
            "nume_familie": nume_familie,
            "prenume": prenume,
            "prenume_activ": prenume_activ,
            "gen": gen,
            "nume_anterior": nume_anterior,
        },
        "interval_calculat": {
            "varsta_initiala": 0,
            "varsta_finala": 108,
            "an_initial": data_nasterii.year,
            "an_final": an_final_calcul,
            "observatie": "Toate seriile temporale sunt calculate complet; selectia pentru afisare se face numai la redactarea lucrarii.",
        },
        "selectie_afisare_solicitata": {
            "an_start": an_start,
            "an_final": an_final,
            "observatie": "Nu limiteaza calculele. Poate fi folosita de template pentru selectarea perioadei afisate.",
        },
        "capitolul_2_formule_calcule_tabele_grafice": {
            "2.1_codul_numerologic_personal_data_nasterii": vibratii(data_nasterii),
            "2.2_structura_matriciala": matrice_data,
            "2.3_codul_numerologic_personal_al_numelui": {
                **nume,
                "comparatie_matrice_data_vs_matrice_nume": comparatie_matrici(
                    matrice_data, nume["matricea_numelui"]
                ),
            },
            "2.4_ciclicitati": {
                "lectii_de_viata": lectii_de_viata(data_nasterii),
                "ciclul_de_7_ani": cicluri_7_ani(data_nasterii, 108),
                "ciclul_de_9_ani": ciclu_9_ani(data_nasterii, data_nasterii.year, an_final_calcul),
                "subcicluri": {"status": "de_completat"},
                "ciclul_de_12_ani": cicluri_12_ani(data_nasterii, 108),
                "ciclul_de_27_ani": {"status": "de_completat"},
                "pinacluri": pinacluri(data_nasterii),
                "ani_importanti_interiori_exteriori": ani_importanti(data_nasterii, an_final_calcul),
                "ani_de_criza_si_rascruce": {"status": "de_completat"},
                "soarta_si_destin": soarta_si_destin(data_nasterii),
            },
            "2.5_relatii": {
                "omuletul_relatiilor": {
                    "status": "de_completat",
                    "observatie": "Necesita datele celei de-a doua persoane.",
                }
            },
            "2.6_spiritul": {
                "inclinatii_profesionale": inclinatii_profesionale(data_nasterii),
                "inclinatii_ezoterice": inclinatii_ezoterice(data_nasterii),
                "codul_spiritului_si_varsta_spiritului": codul_spiritului(data_nasterii),
                "etape_si_subetape": {"status": "de_completat"},
            },
            "2.7_ajutoare": {
                "semnatura_astrala": semnatura_astrala(data_nasterii),
                "directiile_de_succes": directii_de_succes(data_nasterii, gen),
                "triunghiul_financiar": triunghi_financiar(data_nasterii),
                "patratul_de_aur_3x3": patratul_de_aur(data_nasterii),
            },
            "2.8_sinteza_finala": {
                "tabel_general": {"status": "de_completat"},
                "grafic_general": {"status": "de_completat"},
            },
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculator numerologic pentru lucrarea de examen.")
    parser.add_argument("--data-nasterii", required=True, help="DD.MM.YYYY, DD-MM-YYYY sau YYYY-MM-DD")
    parser.add_argument("--nume-complet", required=True)
    parser.add_argument("--nume-familie")
    parser.add_argument("--prenume")
    parser.add_argument("--prenume-activ")
    parser.add_argument("--gen", choices=["masculin", "feminin"])
    parser.add_argument("--nume-anterior")
    parser.add_argument("--an-start", type=int)
    parser.add_argument("--an-final", type=int)
    parser.add_argument("--pretty", action="store_true", help="Afiseaza JSON indentat.")
    args = parser.parse_args()

    rezultat = raport_complet(
        data_nasterii=parse_data_nasterii(args.data_nasterii),
        nume_complet=args.nume_complet,
        nume_familie=args.nume_familie,
        prenume=args.prenume,
        prenume_activ=args.prenume_activ,
        gen=args.gen,
        nume_anterior=args.nume_anterior,
        an_start=args.an_start,
        an_final=args.an_final,
    )
    print(json.dumps(rezultat, ensure_ascii=False, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
