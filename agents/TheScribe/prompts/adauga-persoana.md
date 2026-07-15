# Prompt - adaugă persoană

Folosește skill-ul `numerologie-gestionare-persoane` pentru a adăuga o persoană în registrul `persoane` din rădăcina Atlas.

Întreabă-mă fiecare informație pe rând, validează răspunsul înainte de a continua și nu deduce date personale din nume. Pentru întrebări și relații, continuă până când spun `gata`. Dacă persoana unei relații nu există în registru, păstrează relația ca provizorie.

La final, afișează rezumatul complet și cere confirmarea mea explicită. Creează directorul persoanei și fișierul `persoana.yaml` numai după confirmare. Nu modifica `Dashboard/persoane.txt` și nu crea încă directorul din `output/lucrari`.
