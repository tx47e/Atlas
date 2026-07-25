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
$MatrixRoot = Join-Path $VaultPath 'Matricea Datei de Nastere'
$NameRoot = Join-Path $VaultPath 'Nume'

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
    [System.IO.File]::WriteAllText($Path, ($normalized.TrimEnd() + "`n"), $encoding)
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

function Get-Subsection {
    param(
        [string]$Text,
        [string]$Heading
    )

    $pattern = "(?ms)^###\s+$([regex]::Escape($Heading))\s*$.*?(?=^###\s+|^##\s+|\z)"
    $match = [regex]::Match($Text, $pattern)
    if (-not $match.Success) {
        throw "Subsectiunea '$Heading' nu a fost gasita."
    }
    return $match.Value.Trim()
}

function Get-SectionLead {
    param([string]$SectionText)

    $match = [regex]::Match($SectionText, '(?ms)^##\s+.+?\s*$.*?(?=^###\s+|\z)')
    if (-not $match.Success) {
        return $SectionText.Trim()
    }
    return $match.Value.Trim()
}

function Get-BodyWithoutFrontmatterAndTitle {
    param([string]$Text)

    $body = [regex]::Replace($Text, '(?s)\A---\s*\r?\n.*?\r?\n---\s*\r?\n', '')
    $body = [regex]::Replace($body, '(?m)^#\s+.+?\s*$', '', 1)
    return $body.Trim("`r", "`n", ' ')
}

function New-ModuleFile {
    param(
        [string]$Directory,
        [string]$Filename,
        [string]$Title,
        [string]$Label,
        [string]$Type,
        [string]$Tag,
        [string]$SourceName,
        [string]$Body,
        [string]$FormulaStatus = ''
    )

    $status = if ($FormulaStatus) {
        "## Statutul formulei`n`n$FormulaStatus`n`n"
    } else {
        ''
    }
    if ([string]::IsNullOrWhiteSpace($Body)) {
        $Body = "## Statut`n`nNota legacy nu contine o sectiune separata pentru acest modul."
    }

    $content = @"
---
titlu: $Title - $Label
tip: $Type
tags:
  - numerologie
  - $Type
  - $Tag
  - documentatie-modulara
sursa: '[[$SourceName]]'
---

# $Title - $Label

$status$Body
"@
    Write-Utf8NoBom -Path (Join-Path $Directory $Filename) -Content $content
}

function New-StandardConcept {
    param(
        [string]$Root,
        [hashtable]$Concept
    )

    $sourcePath = Join-Path $LegacyPath $Concept.Source
    $sourceText = Get-Content -Raw -Encoding UTF8 -LiteralPath $sourcePath
    $sections = @(Get-Sections -Text $sourceText)
    $sourceName = [IO.Path]::GetFileNameWithoutExtension($Concept.Source)
    $destination = Join-Path $Root $Concept.Folder

    $description = @($sections | Where-Object Heading -eq 'Descriere')
    if ($description.Count -eq 0 -and $Concept.BodyAsDescription) {
        $descriptionBody = Get-BodyWithoutFrontmatterAndTitle -Text $sourceText
    } else {
        $descriptionBody = ($description.Text -join "`n`n")
    }

    $calculation = @(
        $sections | Where-Object {
            $_.Heading -match '^(Formula|Calcule|Calcul|Principiu)'
        }
    )
    $examples = @($sections | Where-Object Heading -match '^Exempl')
    $methodology = @(
        $sections | Where-Object {
            $_.Heading -ne 'Descriere' -and
            $_.Heading -notmatch '^(Formula|Calcule|Calcul|Principiu)' -and
            $_.Heading -notmatch '^Exempl'
        }
    )
    $methodologyBody = ($methodology.Text -join "`n`n")
    if ($Concept.Source -eq 'Matricea Datei de Nastere.md') {
        $giftPattern = '(?ms)^### Daruri si nevoi\s*$\s*Darurile si nevoile.*?nevoie de reglare constienta a temei\.'
        $methodologyBody = [regex]::Replace($methodologyBody, $giftPattern, '')
        $temperamentPattern = '(?ms)^Elementele se citesc prin gruparea frecventelor din casute:.*?se noteaza ca zona de echilibrare si dezvoltare\.'
        $methodologyBody = [regex]::Replace($methodologyBody, $temperamentPattern, '')
        $methodologyBody += @"

---

## Concepte folosite in interpretare

Interpretarea Matricei Datei de Nastere foloseste impreuna:

1. [[../Codul Numerologic Personal/01-CNP-Index|Codul Numerologic Personal]],
   ca sursa a sirului de cifre;
2. [[../Casute/01-CA-Index|Casutele]], pentru prezenta, absenta si frecventa
   fiecarei cifre;
3. [[../Daruri si Nevoi/01-DN-Index|Daruri si Nevoi]], pentru casutele care
   contin cel putin doua cifre;
4. [[../Temperament/01-TP-Index|Temperamentul]], pentru elementul dominant sau
   combinatia de elemente dominante;
5. [[../Figuri Geometrice/01-FG-Index|Figurile Geometrice]], pentru forma
   asociata frecventei din fiecare casuta;
6. [[../Vectori/01-VX-Index|Vectorii]], pentru relatiile dintre cate trei
   casute;
7. [[../Curgerea Energiei/01-CE-Index|Curgerea Energiei]], pentru traseele
   complete si intrerupte;
8. [[../Fixatia/01-FX-Index|Fixatia]], pentru vectorul orizontal plin dominant;
9. [[../Tendinta/01-TD-Index|Tendinta]], pentru vectorul diagonal plin
   dominant;
10. [[../Scara Bunastarii/01-SB-Index|Scara Bunastarii]], pentru ordonarea
   valorilor casutelor si vectorilor;
11. [[../Caii Trasura si Vizitiul/01-CTV-Index|Caii, Trasura si Vizitiul]],
    pentru raportul dintre pornire, sustinere si directie.

Aceste concepte se citesc impreuna in interpretarea finala. Niciun rezultat
izolat nu inlocuieste lectura ansamblului matricei.
"@
    }

    New-ModuleFile -Directory $destination -Filename "02-$($Concept.Prefix)-Descriere.md" `
        -Title $Concept.Title -Label 'Descriere' -Type 'descriere' -Tag $Concept.Tag `
        -SourceName $sourceName -Body $descriptionBody
    New-ModuleFile -Directory $destination -Filename "03-$($Concept.Prefix)-Calcul.md" `
        -Title $Concept.Title -Label 'Calcul' -Type 'calcul' -Tag $Concept.Tag `
        -SourceName $sourceName -Body ($calculation.Text -join "`n`n") `
        -FormulaStatus $Concept.FormulaStatus
    New-ModuleFile -Directory $destination -Filename "04-$($Concept.Prefix)-Metodica-si-Interpretari.md" `
        -Title $Concept.Title -Label 'Metodica si interpretari' `
        -Type 'metodica-si-interpretari' -Tag $Concept.Tag -SourceName $sourceName `
        -Body $methodologyBody
    New-ModuleFile -Directory $destination -Filename "05-$($Concept.Prefix)-Exemple.md" `
        -Title $Concept.Title -Label 'Exemple' -Type 'exemple' -Tag $Concept.Tag `
        -SourceName $sourceName -Body ($examples.Text -join "`n`n")

    $relatedIndex = if ($Concept.Source -eq 'Matricea Numelui.md') {
        @"
## Concepte asociate din Matricea Datei de Nastere

- [[../../Matricea Datei de Nastere/Casute/01-CA-Index|Casute]]
- [[../../Matricea Datei de Nastere/Curgerea Energiei/01-CE-Index|Curgerea Energiei]]
- [[../../Matricea Datei de Nastere/Figuri Geometrice/01-FG-Index|Figuri Geometrice]]

"@
    } else {
        ''
    }
    $indexContent = @"
---
titlu: $($Concept.Title) - Index
tip: index
tags:
  - numerologie
  - index
  - $($Concept.Tag)
  - documentatie-modulara
---

# $($Concept.Title)

## Cuprins

1. [[02-$($Concept.Prefix)-Descriere|Descriere]]
2. [[03-$($Concept.Prefix)-Calcul|Calcul]]
3. [[04-$($Concept.Prefix)-Metodica-si-Interpretari|Metodica si interpretari]]
4. [[05-$($Concept.Prefix)-Exemple|Exemple]]

$relatedIndex## Sursa pastrata
- [[$sourceName]]
"@
    Write-Utf8NoBom -Path (Join-Path $destination "01-$($Concept.Prefix)-Index.md") -Content $indexContent
}

function New-CustomConcept {
    param(
        [string]$Root,
        [hashtable]$Concept,
        [string]$Description,
        [string]$Calculation,
        [string]$Methodology,
        [string]$Examples
    )

    $destination = Join-Path $Root $Concept.Folder
    New-ModuleFile -Directory $destination -Filename "02-$($Concept.Prefix)-Descriere.md" `
        -Title $Concept.Title -Label 'Descriere' -Type 'descriere' -Tag $Concept.Tag `
        -SourceName $Concept.SourceName -Body $Description
    New-ModuleFile -Directory $destination -Filename "03-$($Concept.Prefix)-Calcul.md" `
        -Title $Concept.Title -Label 'Calcul' -Type 'calcul' -Tag $Concept.Tag `
        -SourceName $Concept.SourceName -Body $Calculation `
        -FormulaStatus $Concept.FormulaStatus
    New-ModuleFile -Directory $destination -Filename "04-$($Concept.Prefix)-Metodica-si-Interpretari.md" `
        -Title $Concept.Title -Label 'Metodica si interpretari' `
        -Type 'metodica-si-interpretari' -Tag $Concept.Tag `
        -SourceName $Concept.SourceName -Body $Methodology
    New-ModuleFile -Directory $destination -Filename "05-$($Concept.Prefix)-Exemple.md" `
        -Title $Concept.Title -Label 'Exemple' -Type 'exemple' -Tag $Concept.Tag `
        -SourceName $Concept.SourceName -Body $Examples

    $indexContent = @"
---
titlu: $($Concept.Title) - Index
tip: index
tags:
  - numerologie
  - index
  - $($Concept.Tag)
  - documentatie-modulara
---

# $($Concept.Title)

## Cuprins

1. [[02-$($Concept.Prefix)-Descriere|Descriere]]
2. [[03-$($Concept.Prefix)-Calcul|Calcul]]
3. [[04-$($Concept.Prefix)-Metodica-si-Interpretari|Metodica si interpretari]]
4. [[05-$($Concept.Prefix)-Exemple|Exemple]]

## Surse pastrate

- [[Matricea Datei de Nastere]]
- [[Scara Bunastarii]]
"@
    Write-Utf8NoBom -Path (Join-Path $destination "01-$($Concept.Prefix)-Index.md") -Content $indexContent
}

$matrixConcepts = @(
    @{
        Source = 'Cod Numerologic Personal.md'; Folder = 'Codul Numerologic Personal'
        Title = 'Codul Numerologic Personal'; Prefix = 'CNP'; Tag = 'CodNumerologicPersonal'
        FormulaStatus = 'Formula N2 si N4 prin insumare exact o singura data este confirmata in Registru Validare Formule si este pastrata fara modificari.'
    },
    @{
        Source = 'Matricea Datei de Nastere.md'; Folder = 'Matricea Datei de Nastere'
        Title = 'Matricea Datei de Nastere'; Prefix = 'MDN'; Tag = 'MatriceaDateiDeNastere'
        FormulaStatus = 'Transpunerea este pastrata din nota legacy. Regula confirmata pentru N2 si N4 ramane in Codul Numerologic Personal.'
    },
    @{
        Source = 'Curgerea Energiei.md'; Folder = 'Curgerea Energiei'
        Title = 'Curgerea Energiei'; Prefix = 'CE'; Tag = 'CurgereaEnergiei'
        FormulaStatus = 'Metoda vectorilor este pastrata din nota legacy. Regula numarului de cai si a paritatii frecventei a fost furnizata explicit de utilizator si documentata in aceasta etapa.'
    },
    @{
        Source = 'Figuri Geometrice.md'; Folder = 'Figuri Geometrice'
        Title = 'Figuri Geometrice'; Prefix = 'FG'; Tag = 'FiguriGeometrice'
        FormulaStatus = 'Metoda este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Fixatia.md'; Folder = 'Fixatia'
        Title = 'Fixatia'; Prefix = 'FX'; Tag = 'Fixatia'
        FormulaStatus = 'Metoda este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Scara Bunastarii.md'; Folder = 'Scara Bunastarii'
        Title = 'Scara Bunastarii'; Prefix = 'SB'; Tag = 'ScaraBunastarii'
        FormulaStatus = 'Metoda este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Tendinta.md'; Folder = 'Tendinta'
        Title = 'Tendinta'; Prefix = 'TD'; Tag = 'Tendinta'
        FormulaStatus = 'Regula legacy este pastrata fara modificari. Nu a fost lansat un audit formal nou in aceasta etapa.'
        BodyAsDescription = $true
    },
    @{
        Source = 'Caii Trasura si Vizitiul.md'; Folder = 'Caii Trasura si Vizitiul'
        Title = 'Caii, Trasura si Vizitiul'; Prefix = 'CTV'; Tag = 'CaiiTrasuraVizitiul'
        FormulaStatus = 'Metoda este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    }
)

$nameConcepts = @(
    @{
        Source = 'Numarul Activ.md'; Folder = 'Numarul Activ'
        Title = 'Numarul Activ'; Prefix = 'NA'; Tag = 'NumarulActiv'
        FormulaStatus = 'Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Numarul de Exprimare.md'; Folder = 'Numarul de Exprimare'
        Title = 'Numarul de Exprimare'; Prefix = 'NE'; Tag = 'NumarulDeExprimare'
        FormulaStatus = 'Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Numarul de Realizare.md'; Folder = 'Numarul de Realizare'
        Title = 'Numarul de Realizare'; Prefix = 'NR'; Tag = 'NumarulDeRealizare'
        FormulaStatus = 'Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Numarul Intim.md'; Folder = 'Numarul Intim'
        Title = 'Numarul Intim'; Prefix = 'NI'; Tag = 'NumarulIntim'
        FormulaStatus = 'Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Numarul Ereditar.md'; Folder = 'Numarul Ereditar'
        Title = 'Numarul Ereditar'; Prefix = 'NER'; Tag = 'NumarulEreditar'
        FormulaStatus = 'Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Numarul Neamului.md'; Folder = 'Numarul Ereditar Karmic'
        Title = 'Numarul Ereditar Karmic'; Prefix = 'NEK'; Tag = 'NumarulEreditarKarmic'
        FormulaStatus = 'Formula Numarului Neamului este preluata ca formula a Numarului Ereditar Karmic, denumire alternativa indicata explicit in nota legacy. Nu a fost lansat un audit formal nou.'
    },
    @{
        Source = 'Matricea Numelui.md'; Folder = 'Matricea Numelui'
        Title = 'Matricea Numelui'; Prefix = 'MN'; Tag = 'MatriceaNumelui'
        FormulaStatus = 'Metoda foloseste Patratul lui Pitagora si valorile numerologice ale literelor. Formula este pastrata din nota legacy, fara audit formal nou.'
    },
    @{
        Source = 'Matricea Numelui vs Matricea Datei de Nastere.md'
        Folder = 'Comparatia Matricea Datei de Nastere vs Matricea Numelui'
        Title = 'Comparatia Matricea Datei de Nastere vs Matricea Numelui'
        Prefix = 'CMN'; Tag = 'ComparatieMatriceDataNume'
        FormulaStatus = 'Metoda compara cele doua matrici pe fiecare casuta si nu construieste o a treia matrice. Formula este pastrata din nota legacy, fara audit formal nou.'
    }
)

$allSources = @(
    $matrixConcepts.Source
    $nameConcepts.Source
    'Influentele Numelui.md'
)
foreach ($source in $allSources) {
    $sourcePath = Join-Path $LegacyPath $source
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw "Sursa lipseste: $sourcePath"
    }
}
if (Test-Path -LiteralPath $MatrixRoot) {
    throw "Directorul-tinta exista deja: $MatrixRoot"
}
if (Test-Path -LiteralPath $NameRoot) {
    throw "Directorul-tinta exista deja: $NameRoot"
}

foreach ($concept in $matrixConcepts) {
    New-StandardConcept -Root $MatrixRoot -Concept $concept
}

$matrixText = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $LegacyPath 'Matricea Datei de Nastere.md')
$matrixSections = @(Get-Sections -Text $matrixText)
$matrixInterpretation = ($matrixSections | Where-Object Heading -eq 'Interpretare generala').Text
$scaleText = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $LegacyPath 'Scara Bunastarii.md')
$scaleSections = @(Get-Sections -Text $scaleText)
$scaleFormula = ($scaleSections | Where-Object Heading -eq 'Formula de calcul').Text
$scaleVectors = ($scaleSections | Where-Object Heading -eq 'Vectorii bunastarii').Text
$scaleInterpretation = ($scaleSections | Where-Object Heading -eq 'Interpretare generala').Text
$scaleExample = ($scaleSections | Where-Object Heading -eq 'Exemplu de calcul').Text

$vectorConcept = @{
    Folder = 'Vectori'; Title = 'Vectori'; Prefix = 'VX'; Tag = 'Vectori'
    SourceName = 'Scara Bunastarii'
    FormulaStatus = 'Formula valorii vectorului este preluata din nota legacy Scara Bunastarii. Nu a fost lansat un audit formal nou.'
}
New-CustomConcept -Root $MatrixRoot -Concept $vectorConcept `
    -Description $scaleVectors `
    -Calculation (Get-Subsection -Text $scaleFormula -Heading 'Valoarea vectorului') `
    -Methodology $scaleInterpretation `
    -Examples (Get-Subsection -Text $scaleExample -Heading 'Valorile vectorilor')

$boxConcept = @{
    Folder = 'Casute'; Title = 'Casute'; Prefix = 'CA'; Tag = 'Casute'
    SourceName = 'Matricea Datei de Nastere'
    FormulaStatus = 'Formula valorii casutei este preluata din nota legacy Scara Bunastarii. Nu a fost lansat un audit formal nou.'
}
New-CustomConcept -Root $MatrixRoot -Concept $boxConcept `
    -Description (Get-SectionLead -SectionText $matrixInterpretation) `
    -Calculation (Get-Subsection -Text $scaleFormula -Heading 'Valoarea casutei') `
    -Methodology "## Corelare`n`nCitirea darurilor si nevoilor asociate casutelor este documentata separat in`n[[../Daruri si Nevoi/01-DN-Index|Daruri si Nevoi]]." `
    -Examples (Get-Subsection -Text $scaleExample -Heading 'Valorile casutelor')

$giftDir = Join-Path $MatrixRoot 'Daruri si Nevoi'
$giftDescription = @"
## Descriere

Darurile si nevoile se interpreteaza pentru casutele care contin cel putin doua
cifre. Darul este resursa accentuata a casutei, iar nevoia este ceea ce aceeasi
energie are nevoie sa primeasca si sa manifeste matur.

Casutele cu o singura cifra se citesc ca potential disponibil, iar cele absente
ca directii de dezvoltare; ele nu intra in lectura darurilor si nevoilor.
"@
$giftCalculation = @"
## Regula de identificare

~~~text
frecventa casutei >= 2 -> se interpreteaza darul si nevoia
frecventa casutei = 1  -> potential disponibil
frecventa casutei = 0  -> directie de dezvoltare
~~~

Se cauta, de regula, o frecventa impara pentru ca energia sa fie mai putin
oscilanta. Frecventele pare pot arata alternanta, tensiune sau nevoie de reglare
constienta a temei.
"@
$giftMethodology = @"
## Ordinea de lucru

1. Se construieste [[../Matricea Datei de Nastere/01-MDN-Index|Matricea Datei
   de Nastere]].
2. Se stabileste frecventa fiecarei [[../Casute/01-CA-Index|casute]].
3. Se selecteaza numai casutele cu cel putin doua cifre.
4. Pentru fiecare casuta selectata se noteaza darul, ca resursa accentuata.
5. Se noteaza nevoia aceleiasi energii, adica ceea ce trebuie primit si
   manifestat matur.
6. Se observa daca frecventa este para sau impara.

## Limite de interpretare

- o singura cifra nu este prezentata ca dar accentuat;
- absenta unei cifre nu este prezentata ca defect;
- darul si nevoia se citesc impreuna, nu ca doua rezultate independente;
- interpretarea ramane corelata cu ansamblul
  [[../01-MDN-Familie-Index|Matricei Datei de Nastere]].
"@
$giftExample = @"
## Exemplu de identificare

Pentru matricea exemplului 24.04.1982, frecventele sunt:

~~~text
1=1, 2=3, 3=2, 4=2, 5=0, 6=1, 7=0, 8=2, 9=1
~~~

Casutele `2`, `3`, `4` si `8` contin cel putin doua cifre, deci intra in lectura
darurilor si nevoilor. Casutele `1`, `6` si `9` se citesc ca potential
disponibil, iar casutele `5` si `7` ca directii de dezvoltare.
"@
New-ModuleFile -Directory $giftDir -Filename '02-DN-Descriere.md' `
    -Title 'Daruri si Nevoi' -Label 'Descriere' -Type 'descriere' `
    -Tag 'DaruriSiNevoi' -SourceName 'Matricea Datei de Nastere' `
    -Body $giftDescription
New-ModuleFile -Directory $giftDir -Filename '03-DN-Calcul.md' `
    -Title 'Daruri si Nevoi' -Label 'Regula de identificare' -Type 'calcul' `
    -Tag 'DaruriSiNevoi' -SourceName 'Matricea Datei de Nastere' `
    -Body $giftCalculation `
    -FormulaStatus 'Conceptul nu introduce un calcul numerologic nou. El foloseste frecventele deja obtinute in Casute.'
New-ModuleFile -Directory $giftDir -Filename '04-DN-Metodica-si-Interpretari.md' `
    -Title 'Daruri si Nevoi' -Label 'Metodica si interpretari' `
    -Type 'metodica-si-interpretari' -Tag 'DaruriSiNevoi' `
    -SourceName 'Matricea Datei de Nastere' -Body $giftMethodology
New-ModuleFile -Directory $giftDir -Filename '05-DN-Exemple.md' `
    -Title 'Daruri si Nevoi' -Label 'Exemple' -Type 'exemple' `
    -Tag 'DaruriSiNevoi' -SourceName 'Matricea Datei de Nastere' `
    -Body $giftExample
$giftIndex = @"
---
titlu: Daruri si Nevoi - Index
tip: index
tags:
  - numerologie
  - index
  - DaruriSiNevoi
  - documentatie-modulara
---

# Daruri si Nevoi

## Cuprins

1. [[02-DN-Descriere|Descriere]]
2. [[03-DN-Calcul|Regula de identificare]]
3. [[04-DN-Metodica-si-Interpretari|Metodica si interpretari]]
4. [[05-DN-Exemple|Exemple]]

## Sursa pastrata

- [[Matricea Datei de Nastere]]
"@
Write-Utf8NoBom -Path (Join-Path $giftDir '01-DN-Index.md') -Content $giftIndex

$temperamentDir = Join-Path $MatrixRoot 'Temperament'
$temperamentDescription = @"
## Descriere

Temperamentul este determinat de cantitatea cifrelor din fiecare element al
[[../Matricea Datei de Nastere/01-MDN-Index|Matricei Datei de Nastere]].

| Element | Casute | Temperament |
| --- | --- | --- |
| Foc | 1, 5, 9 | coleric |
| Aer | 3, 7 | sangvin |
| Apa | 2, 6 | flegmatic |
| Pamant | 4, 8 | melancolic |

Elementul cu cea mai mare cantitate de cifre determina temperamentul
predominant al persoanei.
"@
$temperamentCalculation = @"
## Formula de calcul

~~~text
Foc = cantitatea din casutele 1 + 5 + 9
Aer = cantitatea din casutele 3 + 7
Apa = cantitatea din casutele 2 + 6
Pamant = cantitatea din casutele 4 + 8
~~~

Se numara toate aparitiile cifrelor din casutele aceluiasi element, apoi se
compara cele patru totaluri.
"@
$temperamentMethodology = @"
## Ordinea de lucru

1. Se construiesc [[../Casute/01-CA-Index|casutele matricei]].
2. Se numara aparitiile cifrelor pentru fiecare element.
3. Se compara totalurile Foc, Aer, Apa si Pamant.
4. Elementul cu totalul cel mai mare indica temperamentul predominant.
5. Totalurile apropiate sau egale se citesc ca temperament mixt ori oscilant.
6. Elementele absente sau slab reprezentate se noteaza ca zone de echilibrare
   si dezvoltare.

## Regula de interpretare

Temperamentul se citeste impreuna cu celelalte concepte din
[[../Matricea Datei de Nastere/04-MDN-Metodica-si-Interpretari|metodica
Matricei Datei de Nastere]], nu ca rezultat izolat.
"@
$temperamentExample = @"
## Exemplu de calcul

Pentru matricea exemplului 24.04.1982:

~~~text
Foc = 1 + 0 + 1 = 2
Aer = 2 + 0 = 2
Apa = 3 + 1 = 4
Pamant = 2 + 2 = 4
~~~

Apa si Pamant au cele mai mari totaluri. Temperamentul predominant este mixt,
flegmatic-melancolic. Focul si Aerul sunt prezente egal, dar mai discret.
"@
New-ModuleFile -Directory $temperamentDir -Filename '02-TP-Descriere.md' `
    -Title 'Temperament' -Label 'Descriere' -Type 'descriere' `
    -Tag 'Temperament' -SourceName 'Matricea Datei de Nastere' `
    -Body $temperamentDescription
New-ModuleFile -Directory $temperamentDir -Filename '03-TP-Calcul.md' `
    -Title 'Temperament' -Label 'Calcul' -Type 'calcul' `
    -Tag 'Temperament' -SourceName 'Matricea Datei de Nastere' `
    -Body $temperamentCalculation `
    -FormulaStatus 'Conceptul nu introduce numere de lucru noi. El grupeaza frecventele deja obtinute in casutele matricei. Metoda este pastrata din nota legacy, fara audit formal nou.'
New-ModuleFile -Directory $temperamentDir -Filename '04-TP-Metodica-si-Interpretari.md' `
    -Title 'Temperament' -Label 'Metodica si interpretari' `
    -Type 'metodica-si-interpretari' -Tag 'Temperament' `
    -SourceName 'Matricea Datei de Nastere' -Body $temperamentMethodology
New-ModuleFile -Directory $temperamentDir -Filename '05-TP-Exemple.md' `
    -Title 'Temperament' -Label 'Exemple' -Type 'exemple' `
    -Tag 'Temperament' -SourceName 'Matricea Datei de Nastere' `
    -Body $temperamentExample
$temperamentIndex = @"
---
titlu: Temperament - Index
tip: index
tags:
  - numerologie
  - index
  - Temperament
  - documentatie-modulara
---

# Temperament

## Cuprins

1. [[02-TP-Descriere|Descriere]]
2. [[03-TP-Calcul|Calcul]]
3. [[04-TP-Metodica-si-Interpretari|Metodica si interpretari]]
4. [[05-TP-Exemple|Exemple]]

## Sursa pastrata

- [[Matricea Datei de Nastere]]
"@
Write-Utf8NoBom -Path (Join-Path $temperamentDir '01-TP-Index.md') -Content $temperamentIndex

foreach ($concept in $nameConcepts) {
    New-StandardConcept -Root $NameRoot -Concept $concept
}

$influenceSource = 'Influentele Numelui.md'
$influenceSourceName = 'Influentele Numelui'
$influenceText = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $LegacyPath $influenceSource)
$influenceSections = @(Get-Sections -Text $influenceText)
$influenceDir = Join-Path $NameRoot 'Influentele Numelui'

$influenceModules = @(
    @{
        Filename = '02-IN-Descriere.md'; Label = 'Descriere'; Type = 'descriere'
        Body = ($influenceSections | Where-Object Heading -eq 'Descriere').Text
    },
    @{
        Filename = '03-IN-Corelari.md'; Label = 'Corelari'; Type = 'corelari'
        Body = (@($influenceSections | Where-Object Heading -in @('Incadrare in raport', 'Compararea celor doua matrici')).Text -join "`n`n")
    },
    @{
        Filename = '04-IN-Utilizare-si-Observatii.md'; Label = 'Utilizare si observatii'; Type = 'metodica'
        Body = (@($influenceSections | Where-Object Heading -in @('Utilizare in lucrare', 'Observatii de redactare')).Text -join "`n`n")
    }
)
foreach ($module in $influenceModules) {
    New-ModuleFile -Directory $influenceDir -Filename $module.Filename `
        -Title 'Influentele Numelui' -Label $module.Label -Type $module.Type `
        -Tag 'InfluenteleNumelui' -SourceName $influenceSourceName -Body $module.Body
}

$topicDefinitions = @(
    @{ Number = '05'; Slug = 'Cifre-Intense'; Heading = 'Cifrele intense'; Title = 'Cifre Intense'; Status = '' },
    @{ Number = '06'; Slug = 'Primele-si-Ultimele-Litere'; Heading = 'Primele si ultimele litere'; Title = 'Primele si Ultimele Litere'; Status = '' },
    @{ Number = '07'; Slug = 'Primele-Vocale'; Heading = 'Primele vocale'; Title = 'Primele Vocale'; Status = '' },
    @{ Number = '08'; Slug = 'Cheia-de-Bolta'; Heading = 'Cheile de bolta'; Title = 'Cheia de Bolta'; Status = 'Registrul formulelor marcheaza Cheile de Bolta cu lipsa sursei operationale. Continutul legacy este pastrat fara audit formal nou.' },
    @{ Number = '09'; Slug = 'Litere-Mentale-Fizice-Emotionale-si-Intuitive'; Heading = 'Litere mentale, fizice, emotionale si intuitive'; Title = 'Litere Mentale, Fizice, Emotionale si Intuitive'; Status = '' },
    @{ Number = '10'; Slug = 'Cifrele-Temperamentului'; Heading = 'Cifrele temperamentului'; Title = 'Cifrele Temperamentului'; Status = 'Registrul formulelor marcheaza Temperamentul cu lipsa sursei operationale. Continutul legacy este pastrat fara audit formal nou.' },
    @{ Number = '11'; Slug = 'Cifrele-de-Tensiune'; Heading = 'Cifrele de tensiune'; Title = 'Cifrele de Tensiune'; Status = 'Registrul formulelor marcheaza Cifrele de Tensiune cu lipsa sursei operationale. Continutul legacy este pastrat fara audit formal nou.' },
    @{ Number = '12'; Slug = 'Cifra-Energetica'; Heading = 'Cifra energetica'; Title = 'Cifra Energetica'; Status = 'Registrul formulelor marcheaza Cifra Energetica cu lipsa sursei operationale. Continutul legacy este pastrat fara audit formal nou.' }
)
foreach ($topic in $topicDefinitions) {
    $section = @($influenceSections | Where-Object Heading -eq $topic.Heading)
    if ($section.Count -ne 1) {
        throw "Sectiunea '$($topic.Heading)' lipseste sau este duplicata in $influenceSource."
    }
    New-ModuleFile -Directory $influenceDir `
        -Filename "$($topic.Number)-IN-$($topic.Slug).md" `
        -Title $topic.Title -Label 'Concept' -Type 'subconcept' `
        -Tag 'InfluenteleNumelui' -SourceName $influenceSourceName `
        -Body $section.Text -FormulaStatus $topic.Status
}

$influenceTopicLinks = @(
    '4. [[05-IN-Cifre-Intense|Cifre intense]]',
    '5. [[06-IN-Primele-si-Ultimele-Litere|Primele si ultimele litere]]',
    '6. [[07-IN-Primele-Vocale|Primele vocale]]',
    '7. [[08-IN-Cheia-de-Bolta|Cheia de bolta]]',
    '8. [[09-IN-Litere-Mentale-Fizice-Emotionale-si-Intuitive|Litere mentale, fizice, emotionale si intuitive]]',
    '9. [[10-IN-Cifrele-Temperamentului|Cifrele temperamentului]]',
    '10. [[11-IN-Cifrele-de-Tensiune|Cifrele de tensiune]]',
    '11. [[12-IN-Cifra-Energetica|Cifra energetica]]'
)
$influenceIndex = @"
---
titlu: Influentele Numelui - Index
tip: index
tags:
  - numerologie
  - index
  - InfluenteleNumelui
  - documentatie-modulara
---

# Influentele Numelui

## Cuprins

1. [[02-IN-Descriere|Descriere]]
2. [[03-IN-Corelari|Corelari]]
3. [[04-IN-Utilizare-si-Observatii|Utilizare si observatii]]
$($influenceTopicLinks -join "`n")

## Concepte principale ale numelui

- [[../Numarul de Exprimare/01-NE-Index|Numarul de Exprimare]]
- [[../Numarul Intim/01-NI-Index|Numarul Intim]]
- [[../Numarul de Realizare/01-NR-Index|Numarul de Realizare]]
- [[../Numarul Activ/01-NA-Index|Numarul Activ]]
- [[../Numarul Ereditar/01-NER-Index|Numarul Ereditar]]
- [[../Matricea Numelui/01-MN-Index|Matricea Numelui]]
- [[../Comparatia Matricea Datei de Nastere vs Matricea Numelui/01-CMN-Index|Comparatia Matricea Datei de Nastere vs Matricea Numelui]]

## Sursa pastrata

- [[Influentele Numelui]]
"@
Write-Utf8NoBom -Path (Join-Path $influenceDir '01-IN-Index.md') -Content $influenceIndex

$matrixFamilyLinks = @(
    '- [[Codul Numerologic Personal/01-CNP-Index|Codul Numerologic Personal]]',
    '- [[Matricea Datei de Nastere/01-MDN-Index|Matricea Datei de Nastere]]',
    '- [[Curgerea Energiei/01-CE-Index|Curgerea Energiei]]',
    '- [[Figuri Geometrice/01-FG-Index|Figuri Geometrice]]',
    '- [[Fixatia/01-FX-Index|Fixatia]]',
    '- [[Vectori/01-VX-Index|Vectori]]',
    '- [[Casute/01-CA-Index|Casute]]',
    '- [[Daruri si Nevoi/01-DN-Index|Daruri si Nevoi]]',
    '- [[Temperament/01-TP-Index|Temperament]]',
    '- [[Scara Bunastarii/01-SB-Index|Scara Bunastarii]]',
    '- [[Tendinta/01-TD-Index|Tendinta]]',
    '- [[Caii Trasura si Vizitiul/01-CTV-Index|Caii, Trasura si Vizitiul]]'
)
$matrixFamilyIndex = @"
---
titlu: Matricea Datei de Nastere - Index
tip: index-familie
tags:
  - numerologie
  - index
  - MatriceaDateiDeNastere
  - documentatie-modulara
---

# Matricea Datei de Nastere

## Concepte

$($matrixFamilyLinks -join "`n")

## Regula structurala

- fiecare concept are propriul director modular;
- formulele si exemplele raman separate de descriere si metodica;
- notele legacy sunt pastrate pentru compatibilitate.
"@
Write-Utf8NoBom -Path (Join-Path $MatrixRoot '01-MDN-Familie-Index.md') -Content $matrixFamilyIndex

$nameFamilyLinks = @(
    '- [[Numarul Activ/01-NA-Index|Numarul Activ]]',
    '- [[Numarul de Exprimare/01-NE-Index|Numarul de Exprimare]]',
    '- [[Numarul de Realizare/01-NR-Index|Numarul de Realizare]]',
    '- [[Numarul Intim/01-NI-Index|Numarul Intim]]',
    '- [[Numarul Ereditar/01-NER-Index|Numarul Ereditar]]',
    '- [[Numarul Ereditar Karmic/01-NEK-Index|Numarul Ereditar Karmic]]',
    '- [[Matricea Numelui/01-MN-Index|Matricea Numelui]]',
    '- [[Comparatia Matricea Datei de Nastere vs Matricea Numelui/01-CMN-Index|Comparatia Matricea Datei de Nastere vs Matricea Numelui]]',
    '- [[Influentele Numelui/01-IN-Index|Influentele Numelui]]'
)
$nameFamilyIndex = @"
---
titlu: Nume - Index
tip: index-familie
tags:
  - numerologie
  - index
  - Nume
  - documentatie-modulara
---

# Nume

## Concepte

$($nameFamilyLinks -join "`n")

## Regula structurala

- fiecare numar al numelui are propriul director modular;
- Influentele Numelui pastreaza fiecare tema secundara intr-un fisier separat;
- notele legacy sunt pastrate pentru compatibilitate.
"@
Write-Utf8NoBom -Path (Join-Path $NameRoot '01-N-Index.md') -Content $nameFamilyIndex

$created = @(
    Get-ChildItem -LiteralPath $MatrixRoot -Recurse -File
    Get-ChildItem -LiteralPath $NameRoot -Recurse -File
)
Write-Output "Directoare conceptuale create: $(@(Get-ChildItem -LiteralPath $MatrixRoot -Directory).Count + @(Get-ChildItem -LiteralPath $NameRoot -Directory).Count)"
Write-Output "Fisiere create: $($created.Count)"
