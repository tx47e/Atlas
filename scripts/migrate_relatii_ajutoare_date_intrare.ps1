param(
    [string]$VaultPath = (Join-Path $PSScriptRoot '..\vault\Numerologie')
)

$ErrorActionPreference = 'Stop'
$VaultPath = (Resolve-Path -LiteralPath $VaultPath).Path
$RepositoryRoot = Split-Path -Parent (Split-Path -Parent $VaultPath)
$ArchivedLegacyPath = Join-Path $RepositoryRoot 'Archive\Numerologie Legacy'
$LegacyPath = if (Test-Path -LiteralPath $ArchivedLegacyPath -PathType Container) {
    (Resolve-Path -LiteralPath $ArchivedLegacyPath).Path
} else {
    $VaultPath
}

function Write-Utf8NoBom {
    param(
        [string]$Path,
        [string]$Content
    )

    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }

    $normalized = [regex]::Replace(
        $Content,
        '[ \t]+(?=\r?$)',
        '',
        [System.Text.RegularExpressions.RegexOptions]::Multiline
    )
    $encoding = [System.Text.UTF8Encoding]::new($false)
    [IO.File]::WriteAllText($Path, ($normalized.TrimEnd() + "`n"), $encoding)
}

function Get-Sections {
    param([string]$Text)

    $matches = [regex]::Matches($Text, '(?m)^##\s+(.+?)\s*$')
    $sections = [System.Collections.Generic.List[object]]::new()
    for ($index = 0; $index -lt $matches.Count; $index++) {
        $start = $matches[$index].Index
        $end = if ($index + 1 -lt $matches.Count) {
            $matches[$index + 1].Index
        } else {
            $Text.Length
        }
        $sections.Add([pscustomobject]@{
            Heading = $matches[$index].Groups[1].Value.Trim()
            Text = $Text.Substring($start, $end - $start).Trim()
        })
    }
    return $sections
}

function New-StandardConcept {
    param(
        [string]$Root,
        [hashtable]$Concept,
        [string]$FamilyTag
    )

    $sourcePath = Join-Path $LegacyPath $Concept.Source
    $sourceName = [IO.Path]::GetFileNameWithoutExtension($Concept.Source)
    $destination = Join-Path $Root $Concept.Folder
    $sections = @(Get-Sections -Text (Get-Content -Raw -Encoding UTF8 -LiteralPath $sourcePath))

    $description = @($sections | Where-Object Heading -eq 'Descriere')
    $calculation = @($sections | Where-Object Heading -match $Concept.CalculationPattern)
    $examples = @($sections | Where-Object Heading -match '^Exempl')
    $methodology = @(
        $sections | Where-Object {
            $_.Heading -ne 'Descriere' -and
            $_.Heading -notmatch $Concept.CalculationPattern -and
            $_.Heading -notmatch '^Exempl'
        }
    )

    $modules = @(
        @{
            Number = '02'; Slug = 'Descriere'; Label = 'Descriere'
            Type = 'descriere'; Body = ($description.Text -join "`n`n")
        },
        @{
            Number = '03'; Slug = 'Calcul'; Label = 'Calcul'
            Type = 'calcul'; Body = ($calculation.Text -join "`n`n")
        },
        @{
            Number = '04'; Slug = 'Metodica-si-Interpretari'
            Label = 'Metodică și interpretări'; Type = 'metodica-si-interpretari'
            Body = ($methodology.Text -join "`n`n")
        },
        @{
            Number = '05'; Slug = 'Exemple'; Label = 'Exemple'
            Type = 'exemple'; Body = ($examples.Text -join "`n`n")
        }
    )

    foreach ($module in $modules) {
        $body = $module.Body
        if ([string]::IsNullOrWhiteSpace($body)) {
            $body = "## Statut`n`nNota legacy nu conține o secțiune separată pentru acest modul."
        }
        $status = if ($module.Type -eq 'calcul') {
            "## Statutul formulei`n`nFormula este preluată din nota legacy, fără audit formal nou.`n`n"
        } else {
            ''
        }
        $content = @"
---
titlu: $($Concept.Title) - $($module.Label)
tip: $($module.Type)
tags:
  - numerologie
  - $FamilyTag
  - $($module.Type)
  - $($Concept.Tag)
  - documentatie-modulara
sursa: '[[$sourceName]]'
---

# $($Concept.Title) - $($module.Label)

$status$body
"@
        $fileName = "$($module.Number)-$($Concept.Prefix)-$($module.Slug).md"
        Write-Utf8NoBom -Path (Join-Path $destination $fileName) -Content $content
    }

    $indexContent = @"
---
titlu: $($Concept.Title) - Index
tip: index-concept
tags:
  - numerologie
  - $FamilyTag
  - index
  - $($Concept.Tag)
  - documentatie-modulara
sursa: '[[$sourceName]]'
---

# $($Concept.Title)

## Capitole

- [[02-$($Concept.Prefix)-Descriere|Descriere]]
- [[03-$($Concept.Prefix)-Calcul|Calcul]]
- [[04-$($Concept.Prefix)-Metodica-si-Interpretari|Metodică și interpretări]]
- [[05-$($Concept.Prefix)-Exemple|Exemple]]

## Sursă legacy

- [[$sourceName]]
"@
    Write-Utf8NoBom -Path (Join-Path $destination "01-$($Concept.Prefix)-Index.md") -Content $indexContent
}

$relationsRoot = Join-Path $VaultPath 'Relatii'
$relationConcept = @{
    Source = 'Omuletul Relatiilor.md'
    Folder = 'Omuletul Relatiilor'
    Title = 'Omulețul Relațiilor'
    Prefix = 'OR'
    Tag = 'OmuletulRelatiilor'
    CalculationPattern = '^(Principiu de calcul|Ce se poate realiza impreuna|Ce este de rezolvat impreuna)$'
}
New-StandardConcept -Root $relationsRoot -Concept $relationConcept -FamilyTag 'relatii'

$relationsIndex = @'
---
titlu: Relații - Index
tip: index-familie
tags:
  - numerologie
  - relatii
  - index
  - documentatie-modulara
---

# Relații

## Concepte

- [[Omuletul Relatiilor/01-OR-Index|Omulețul Relațiilor]]

## Scop

Familia reunește conceptele folosite pentru analiza dintre două sau mai multe
persoane. Datele fiecărei persoane asociate sunt definite în
[[../Date de Intrare/01-DI-Index|Date de Intrare]].

## Compatibilitate

Nota [[Omuletul Relatiilor]] rămâne disponibilă ca sursă legacy.
'@
Write-Utf8NoBom -Path (Join-Path $relationsRoot '01-REL-Index.md') -Content $relationsIndex

$helpersRoot = Join-Path $VaultPath 'Spirit si Karma\Ajutoare'
$helperConcepts = @(
    @{
        Source = 'Directiile de Succes.md'
        Folder = 'Directiile de Succes'
        Title = 'Direcțiile de Succes'
        Prefix = 'DS'
        Tag = 'DirectiileDeSucces'
        CalculationPattern = '^Formula de calcul$'
    },
    @{
        Source = 'Patratul de Aur.md'
        Folder = 'Patratul de Aur'
        Title = 'Pătratul de Aur'
        Prefix = 'PA'
        Tag = 'PatratulDeAur'
        CalculationPattern = '^(Formula de calcul|Regula de verificare)$'
    },
    @{
        Source = 'Semnatura Astrala.md'
        Folder = 'Semnatura Astrala'
        Title = 'Semnătura Astrală'
        Prefix = 'SA'
        Tag = 'SemnaturaAstrala'
        CalculationPattern = '^Formula de constructie$'
    },
    @{
        Source = 'Triunghiul Financiar.md'
        Folder = 'Triunghiul Financiar'
        Title = 'Triunghiul Financiar'
        Prefix = 'TF'
        Tag = 'TriunghiulFinanciar'
        CalculationPattern = '^Formula de calcul$'
    }
)

foreach ($concept in $helperConcepts) {
    New-StandardConcept -Root $helpersRoot -Concept $concept -FamilyTag 'ajutoare'
}

$helpersIndex = @'
---
titlu: Ajutoare - Index
tip: index-familie
tags:
  - numerologie
  - SpiritSiKarma
  - ajutoare
  - index
  - documentatie-modulara
---

# Ajutoare

## Concepte

- [[Directiile de Succes/01-DS-Index|Direcțiile de Succes]]
- [[Patratul de Aur/01-PA-Index|Pătratul de Aur]]
- [[Semnatura Astrala/01-SA-Index|Semnătura Astrală]]
- [[Triunghiul Financiar/01-TF-Index|Triunghiul Financiar]]

## Rol

Aceste concepte sunt instrumente auxiliare folosite în cadrul familiei
[[../01-SK-Index|Spirit și Karma]].

## Compatibilitate

Notele legacy rămân disponibile pentru compatibilitate și trasabilitate.
'@
Write-Utf8NoBom -Path (Join-Path $helpersRoot '01-AJ-Index.md') -Content $helpersIndex

$inputRoot = Join-Path $VaultPath 'Date de Intrare'

$inputIndex = @'
---
titlu: Date de Intrare - Index
tip: index-familie
tags:
  - numerologie
  - date-de-intrare
  - formular
  - index
  - documentatie-modulara
sursa: '[[Datele de intrare]]'
---

# Date de Intrare

## Capitole

- [[02-DI-Descriere|Descriere]]
- [[03-DI-Persoana-Principala|Persoana principală]]
- [[04-DI-Persoane-Asociate-si-Relatii|Persoane asociate și relații]]
- [[05-DI-Intrebari|Întrebările persoanei]]
- [[Introducere/01-INT-Index|Introducere]]

## Regulă de colectare

Datele persoanei principale se colectează o singură dată. Pentru o analiză
relațională, structura persoanei asociate se repetă pentru fiecare persoană
inclusă în analiză.

## Sursă legacy

- [[Datele de intrare]]
'@
Write-Utf8NoBom -Path (Join-Path $inputRoot '01-DI-Index.md') -Content $inputIndex

$inputDescription = @'
---
titlu: Date de Intrare - Descriere
tip: descriere
tags:
  - numerologie
  - date-de-intrare
  - formular
  - documentatie-modulara
sursa: '[[Datele de intrare]]'
---

# Date de Intrare - Descriere

Datele de intrare reprezintă informațiile necesare pentru calculul și
personalizarea unei lucrări numerologice. Ele includ identitatea folosită în
analiză, data nașterii, numele active sau anterioare relevante și întrebările
persoanei.

Pentru o lucrare relațională se colectează aceleași date pentru fiecare
persoană asociată. Numărul persoanelor asociate nu este fix: lista poate conține
o persoană, mai multe persoane sau poate rămâne goală într-o analiză individuală.

Datele se notează exact cum sunt oferite și se clarifică înainte de calcul orice
variantă de nume, prenume activ sau dată ambiguă.
'@
Write-Utf8NoBom -Path (Join-Path $inputRoot '02-DI-Descriere.md') -Content $inputDescription

$primaryPerson = @'
---
titlu: Date de Intrare - Persoana Principală
tip: formular
tags:
  - numerologie
  - date-de-intrare
  - persoana-principala
  - documentatie-modulara
sursa: '[[Datele de intrare]]'
---

# Persoana principală

## Câmpuri

| Câmp | Obligatoriu | Regulă |
| --- | --- | --- |
| Nume și prenume | da | Se notează numele complet, în forma `Nume, Prenume`. |
| Data nașterii | da | Se folosește formatul `ZZ.LL.AAAA`. |
| Prenume activ | după caz | Prenumele sau forma de adresare prin care persoana este strigată cel mai des. |
| Nume anterior | după caz | Numele purtat anterior, inclusiv numele anterior căsătoriei, când este relevant. |
| Întrebările persoanei | recomandat | Întrebări generale sau specifice pentru orientarea lucrării. |

## Reguli pentru nume

- numele poate fi compus;
- persoana poate avea mai multe prenume;
- `prenume activ` clarifică formularea legacy `nume activ`;
- numele anterior nu înlocuiește numele actual, ci se păstrează ca informație
  distinctă pentru analiza influențelor numelui.

## Model de completare

```text
Nume și prenume:
Data nașterii: ZZ.LL.AAAA
Prenume activ:
Nume anterior:
Întrebări:
```
'@
Write-Utf8NoBom -Path (Join-Path $inputRoot '03-DI-Persoana-Principala.md') -Content $primaryPerson

$relatedPeople = @'
---
titlu: Date de Intrare - Persoane Asociate și Relații
tip: formular
tags:
  - numerologie
  - date-de-intrare
  - relatii
  - persoane-asociate
  - documentatie-modulara
---

# Persoane asociate și relații

## Structură repetabilă

Pentru fiecare persoană inclusă într-o analiză relațională se creează o
înregistrare separată. Structura poate fi repetată de oricâte ori este necesar.

| Câmp | Obligatoriu | Regulă |
| --- | --- | --- |
| Relația sau rolul | recomandat | Precizează legătura cu persoana principală. |
| Nume și prenume | da | Numele complet al persoanei asociate. |
| Data nașterii | da | Format `ZZ.LL.AAAA`. |
| Prenume activ | după caz | Prenumele sau forma de adresare folosită cel mai des. |
| Nume anterior | după caz | Numele purtat anterior, dacă este relevant. |

## Model pentru o persoană asociată

```text
Persoana asociată [număr]:
Relația sau rolul:
Nume și prenume:
Data nașterii: ZZ.LL.AAAA
Prenume activ:
Nume anterior:
```

## Utilizare

- pentru două persoane se adaugă o singură persoană asociată;
- pentru analize de familie, echipă sau alte relații se repetă blocul pentru
  fiecare persoană;
- aceeași sursă de date trebuie folosită consecvent pentru toate persoanele
  comparate;
- aceste date alimentează conceptele din [[../Relatii/01-REL-Index|Relații]],
  inclusiv [[../Relatii/Omuletul Relatiilor/01-OR-Index|Omulețul Relațiilor]].
'@
Write-Utf8NoBom -Path (Join-Path $inputRoot '04-DI-Persoane-Asociate-si-Relatii.md') -Content $relatedPeople

$questions = @'
---
titlu: Date de Intrare - Întrebările Persoanei
tip: formular
tags:
  - numerologie
  - date-de-intrare
  - intrebari
  - documentatie-modulara
sursa: '[[Datele de intrare]]'
---

# Întrebările persoanei

Întrebările pot fi generale sau specifice și ajută la stabilirea direcției
lucrării. Ele se păstrează în formularea persoanei, apoi pot fi grupate pe teme
precum relații, carieră, bani, dezvoltare, sănătate sau ciclicități.

## Model

```text
1. Întrebare:
   Temă:
   Persoane vizate:

2. Întrebare:
   Temă:
   Persoane vizate:
```

O întrebare relațională trebuie să indice persoana sau persoanele asociate la
care se referă.
'@
Write-Utf8NoBom -Path (Join-Path $inputRoot '05-DI-Intrebari.md') -Content $questions

$introSource = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $LegacyPath 'Introducere.md')
$introSections = @(Get-Sections -Text $introSource)
$introRoot = Join-Path $inputRoot 'Introducere'
$introModules = @(
    @{ File = '02-INT-Descriere.md'; Title = 'Introducere - Descriere'; Type = 'descriere'; Heading = 'Descriere' },
    @{ File = '03-INT-Text-Predefinit.md'; Title = 'Introducere - Text Predefinit'; Type = 'continut-predefinit'; Heading = 'Text predefinit' },
    @{ File = '04-INT-Utilizare.md'; Title = 'Introducere - Utilizare'; Type = 'metodica'; Heading = 'Utilizare în lucrare' }
)

foreach ($module in $introModules) {
    $section = @($introSections | Where-Object Heading -eq $module.Heading)
    $introContent = @"
---
titlu: $($module.Title)
tip: $($module.Type)
tags:
  - numerologie
  - date-de-intrare
  - introducere
  - documentatie-modulara
sursa: '[[Introducere]]'
---

# $($module.Title)

$($section.Text -join "`n`n")
"@
    Write-Utf8NoBom -Path (Join-Path $introRoot $module.File) -Content $introContent
}

$introIndex = @'
---
titlu: Introducere - Index
tip: index-concept
tags:
  - numerologie
  - date-de-intrare
  - introducere
  - index
  - documentatie-modulara
sursa: '[[Introducere]]'
---

# Introducere

## Capitole

- [[02-INT-Descriere|Descriere]]
- [[03-INT-Text-Predefinit|Text predefinit]]
- [[04-INT-Utilizare|Utilizare în lucrare]]

## Sursă legacy

- [[Introducere]]
'@
Write-Utf8NoBom -Path (Join-Path $introRoot '01-INT-Index.md') -Content $introIndex

Write-Output 'Migrarea Relații, Ajutoare și Date de Intrare s-a încheiat.'
