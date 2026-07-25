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
$DestinationRoot = Join-Path $VaultPath 'Ciclicitati'

$concepts = @(
    @{
        Source = 'Anii Importanti Int-Ext.md'
        Folder = 'Anii Importanti Interior si Exterior'
        Title = 'Ani Importanti Interior si Exterior'
        Prefix = 'AIIE'
        Tag = 'AniImportantiInteriorExterior'
        FormulaStatus = 'Seriile se pastreaza pe intervalul operational aprobat 0-108 ani. Formula este preluata din nota legacy, fara audit formal nou.'
    },
    @{
        Source = 'Ciclul de 7 Ani.md'
        Folder = 'Ciclul de 7 Ani'
        Title = 'Ciclul de 7 Ani'
        Prefix = 'C7'
        Tag = 'CiclulDe7Ani'
        FormulaStatus = 'Ciclul se pastreaza pe intervalul operational aprobat 0-108 ani. Formula este preluata din nota legacy, fara audit formal nou.'
        Subconcepts = @(
            @{ Folder = 'Septagrama'; Index = '01-SPT-Index'; Label = 'Septagrama' },
            @{ Folder = 'Harta Suprapusa'; Index = '01-HS-Index'; Label = 'Harta Suprapusa' }
        )
    },
    @{
        Source = 'Ciclul de 9 Ani.md'
        Folder = 'Ciclul de 9 Ani'
        Title = 'Ciclul de 9 Ani'
        Prefix = 'C9'
        Tag = 'CiclulDe9Ani'
        FormulaStatus = 'Ciclul se pastreaza pe intervalul operational aprobat 0-108 ani. Formula este preluata din nota legacy, fara audit formal nou.'
    },
    @{
        Source = 'Ciclul de 12 Ani.md'
        Folder = 'Ciclul de 12 Ani'
        Title = 'Ciclul de 12 Ani'
        Prefix = 'C12'
        Tag = 'CiclulDe12Ani'
        FormulaStatus = 'Ciclul se pastreaza pe intervalul operational aprobat 0-108 ani. Formula este preluata din nota legacy, fara audit formal nou.'
    },
    @{
        Source = 'Soarta si Destin.md'
        Folder = 'Soarta si Destin'
        Title = 'Soarta si Destin'
        Prefix = 'SD'
        Tag = 'SoartaSiDestin'
        FormulaStatus = 'Registrul formulelor marcheaza Soarta, Destinul grafic si zona de confort ca documentate, dar neimplementate. Continutul legacy este pastrat fara audit formal nou.'
    },
    @{
        Source = 'Pinacluri - Oportunitati si Provocari.md'
        Folder = 'Pinacluri Oportunitati si Provocari'
        Title = 'Pinacluri, Oportunitati si Provocari'
        Prefix = 'POP'
        Tag = 'PinacluriOportunitatiProvocari'
        FormulaStatus = 'Formula este preluata din nota legacy. Unde calculul cere o singura cifra, se foloseste cifra finala de interpretare a Destinului. Nu a fost lansat un audit formal nou.'
    },
    @{
        Source = 'Lectii de Viata.md'
        Folder = 'Lectii de Viata'
        Title = 'Lectii de Viata'
        Prefix = 'LV'
        Tag = 'LectiiDeViata'
        FormulaStatus = 'Formula este preluata din nota legacy si folosita de Harta Suprapusa. Nu a fost lansat un audit formal nou.'
    }
)

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
        [hashtable]$Concept
    )

    $sourcePath = Join-Path $LegacyPath $Concept.Source
    $sourceName = [IO.Path]::GetFileNameWithoutExtension($Concept.Source)
    $destination = Join-Path $Root $Concept.Folder
    $sections = @(Get-Sections -Text (Get-Content -Raw -Encoding UTF8 -LiteralPath $sourcePath))

    $description = @($sections | Where-Object Heading -eq 'Descriere')
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
            Label = 'Metodica si interpretari'; Type = 'metodica-si-interpretari'
            Body = ($methodology.Text -join "`n`n")
        },
        @{
            Number = '05'; Slug = 'Exemple'; Label = 'Exemple'
            Type = 'exemple'; Body = ($examples.Text -join "`n`n")
        }
    )

    foreach ($module in $modules) {
        $status = if ($module.Type -eq 'calcul') {
            "## Statutul formulei`n`n$($Concept.FormulaStatus)`n`n"
        } else {
            ''
        }
        $body = $module.Body
        if ([string]::IsNullOrWhiteSpace($body)) {
            $body = "## Statut`n`nNota legacy nu contine o sectiune separata pentru acest modul."
        }
        $content = @"
---
titlu: $($Concept.Title) - $($module.Label)
tip: $($module.Type)
tags:
  - numerologie
  - ciclicitati
  - $($module.Type)
  - $($Concept.Tag)
  - documentatie-modulara
sursa: '[[$sourceName]]'
---

# $($Concept.Title) - $($module.Label)

$status$body
"@
        $filename = "$($module.Number)-$($Concept.Prefix)-$($module.Slug).md"
        Write-Utf8NoBom -Path (Join-Path $destination $filename) -Content $content
    }

    $subconceptSection = ''
    if ($Concept.Subconcepts) {
        $links = @(
            foreach ($subconcept in $Concept.Subconcepts) {
                "- [[$($subconcept.Folder)/$($subconcept.Index)|$($subconcept.Label)]]"
            }
        )
        $subconceptSection = @"
## Subconcepte

$($links -join "`n")

"@
    }
    $indexContent = @"
---
titlu: $($Concept.Title) - Index
tip: index
tags:
  - numerologie
  - ciclicitati
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

$subconceptSection## Sursa pastrata

- [[$sourceName]]
"@
    Write-Utf8NoBom -Path (Join-Path $destination "01-$($Concept.Prefix)-Index.md") -Content $indexContent
}

if (Test-Path -LiteralPath $DestinationRoot) {
    throw "Directorul-tinta exista deja: $DestinationRoot"
}
foreach ($concept in $concepts) {
    $sourcePath = Join-Path $LegacyPath $concept.Source
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw "Sursa lipseste: $sourcePath"
    }
}
if (-not (Test-Path -LiteralPath (Join-Path $LegacyPath 'Septagrama.md') -PathType Leaf)) {
    throw 'Sursa Septagrama.md lipseste.'
}

foreach ($concept in $concepts) {
    New-StandardConcept -Root $DestinationRoot -Concept $concept
}

$septagramaConcept = @{
    Source = 'Septagrama.md'
    Folder = 'Septagrama'
    Title = 'Septagrama'
    Prefix = 'SPT'
    Tag = 'Septagrama'
    FormulaStatus = 'Metoda este preluata din nota legacy. Nu a fost lansat un audit formal nou.'
}
$cycle7Root = Join-Path $DestinationRoot 'Ciclul de 7 Ani'
New-StandardConcept -Root $cycle7Root -Concept $septagramaConcept

$hartaRoot = Join-Path $cycle7Root 'Harta Suprapusa'
$hartaDescription = @"
## Descriere

Harta Suprapusa este sinteza vizuala Soarta-Destin-Ciclicitati. Ea reuneste pe
acelasi interval seriile Sortii si Destinului, zonele de confort, lectiile de
viata, anii importanti interiori si exteriori, ciclurile de 7, 9 si 12 ani,
precum si pinaclurile, oportunitatile si provocarile.

Intervalul operational implicit este 0-108 ani.
"@
$hartaCalculation = @"
## Statutul formulei

Calculul operational este pastrat in skill-ul si generatorul
numerologie-SVG-harta-suprapusa. Continutul este documentat aici fara audit
formal nou.

## Calcul

1. Soarta se formeaza din produsul dintre ZZLL si anul nasterii.
2. Destinul grafic inlocuieste fiecare zero din ZZLL si an cu 1 inaintea
   inmultirii.
3. Cifrele seriilor Soarta si Destin se repeta pe toate punctele graficului.
4. Zona de confort este media cifrelor fiecarei serii de sapte cifre.
5. Lectiile de viata folosesc cifrele produsului zi x luna x an, repetate pe ani.
6. Anii interiori folosesc valoarea redusa a anului curent, iar anii exteriori
   suma bruta a cifrelor anului curent.
7. Pinaclurile folosesc vibratia interioara, vibratia exterioara, vibratia
   redusa a anului si cifra finala a Destinului.
8. Ciclurile se marcheaza la 7, 9 si 12 ani; crizele ciclului de 7 ani apar la
   3,5 + 7n ani.
"@
$hartaMethodology = @"
## Concepte suprapuse

- [[../../Soarta si Destin/01-SD-Index|Soarta si Destin]]
- [[../../Anii Importanti Interior si Exterior/01-AIIE-Index|Ani Importanti Interior si Exterior]]
- [[../../Lectii de Viata/01-LV-Index|Lectii de Viata]]
- [[../01-C7-Index|Ciclul de 7 Ani]]
- [[../../Ciclul de 9 Ani/01-C9-Index|Ciclul de 9 Ani]]
- [[../../Ciclul de 12 Ani/01-C12-Index|Ciclul de 12 Ani]]
- [[../../Pinacluri Oportunitati si Provocari/01-POP-Index|Pinacluri, Oportunitati si Provocari]]
- [[../Septagrama/01-SPT-Index|Septagrama]]

## Metodica de interpretare

1. Se identifica varsta sau intervalul analizat.
2. Se citesc impreuna Soarta, Destinul si zonele lor de confort.
3. Se verifica lectia de viata si anii importanti activi.
4. Se observa suprapunerile ciclurilor de 7, 9 si 12 ani.
5. Se adauga pinaclul, oportunitatea si provocarea intervalului.
6. Coincidentele dintre repere se interpreteaza ca ferestre simbolice de
   intensificare, nu ca predictii fixe.
"@
$hartaResources = @"
## Generare si verificare

Harta se genereaza cu skill-ul numerologie-SVG-harta-suprapusa si cu scriptul
inclus generate_harta_suprapusa.py. SVG-ul rezultat trebuie sa fie autonom si
valid XML.

## Sursa operationala

- skill: skills/numerologie-SVG-harta-suprapusa/SKILL.md;
- generator: skills/numerologie-SVG-harta-suprapusa/scripts/generate_harta_suprapusa.py;
- referinta vizuala: skills/numerologie-SVG-harta-suprapusa/assets/reference.svg.
"@

$hartaModules = @(
    @{ File = '02-HS-Descriere.md'; Label = 'Descriere'; Type = 'descriere'; Body = $hartaDescription },
    @{ File = '03-HS-Calcul.md'; Label = 'Calcul'; Type = 'calcul'; Body = $hartaCalculation },
    @{ File = '04-HS-Metodica-si-Interpretari.md'; Label = 'Metodica si interpretari'; Type = 'metodica-si-interpretari'; Body = $hartaMethodology },
    @{ File = '05-HS-Resurse-si-Verificare.md'; Label = 'Resurse si verificare'; Type = 'resurse'; Body = $hartaResources }
)
foreach ($module in $hartaModules) {
    $content = @"
---
titlu: Harta Suprapusa - $($module.Label)
tip: $($module.Type)
tags:
  - numerologie
  - ciclicitati
  - HartaSuprapusa
  - $($module.Type)
  - documentatie-modulara
sursa: skill numerologie-SVG-harta-suprapusa
---

# Harta Suprapusa - $($module.Label)

$($module.Body)
"@
    Write-Utf8NoBom -Path (Join-Path $hartaRoot $module.File) -Content $content
}

$hartaIndex = @"
---
titlu: Harta Suprapusa - Index
tip: index
tags:
  - numerologie
  - ciclicitati
  - index
  - HartaSuprapusa
  - documentatie-modulara
---

# Harta Suprapusa

## Cuprins

1. [[02-HS-Descriere|Descriere]]
2. [[03-HS-Calcul|Calcul]]
3. [[04-HS-Metodica-si-Interpretari|Metodica si interpretari]]
4. [[05-HS-Resurse-si-Verificare|Resurse si verificare]]

## Concepte suprapuse

- [[../../Soarta si Destin/01-SD-Index|Soarta si Destin]]
- [[../../Anii Importanti Interior si Exterior/01-AIIE-Index|Ani Importanti Interior si Exterior]]
- [[../../Lectii de Viata/01-LV-Index|Lectii de Viata]]
- [[../01-C7-Index|Ciclul de 7 Ani]]
- [[../../Ciclul de 9 Ani/01-C9-Index|Ciclul de 9 Ani]]
- [[../../Ciclul de 12 Ani/01-C12-Index|Ciclul de 12 Ani]]
- [[../../Pinacluri Oportunitati si Provocari/01-POP-Index|Pinacluri, Oportunitati si Provocari]]
- [[../Septagrama/01-SPT-Index|Septagrama]]

## Sursa operationala

- skill numerologie-SVG-harta-suprapusa;
- generator generate_harta_suprapusa.py.
"@
Write-Utf8NoBom -Path (Join-Path $hartaRoot '01-HS-Index.md') -Content $hartaIndex

$familyIndex = @"
---
titlu: Ciclicitati - Index
tip: index-familie
tags:
  - numerologie
  - ciclicitati
  - index
  - documentatie-modulara
---

# Ciclicitati

## Concepte

- [[Anii Importanti Interior si Exterior/01-AIIE-Index|Ani Importanti Interior si Exterior]]
- [[Ciclul de 7 Ani/01-C7-Index|Ciclul de 7 Ani]]
  - [[Ciclul de 7 Ani/Septagrama/01-SPT-Index|Septagrama]]
  - [[Ciclul de 7 Ani/Harta Suprapusa/01-HS-Index|Harta Suprapusa]]
- [[Ciclul de 9 Ani/01-C9-Index|Ciclul de 9 Ani]]
- [[Ciclul de 12 Ani/01-C12-Index|Ciclul de 12 Ani]]
- [[Soarta si Destin/01-SD-Index|Soarta si Destin]]
- [[Pinacluri Oportunitati si Provocari/01-POP-Index|Pinacluri, Oportunitati si Provocari]]
- [[Lectii de Viata/01-LV-Index|Lectii de Viata]]

## Regula structurala

- fiecare concept principal are propriul director modular;
- Septagrama si Harta Suprapusa apartin Ciclului de 7 Ani;
- intervalul operational al seriilor este 0-108 ani;
- notele legacy sunt pastrate pentru compatibilitate.
"@
Write-Utf8NoBom -Path (Join-Path $DestinationRoot '01-CIC-Index.md') -Content $familyIndex

$created = @(Get-ChildItem -LiteralPath $DestinationRoot -Recurse -File)
Write-Output "Directoare conceptuale create: 9"
Write-Output "Fisiere create: $($created.Count)"
