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
$DestinationRoot = Join-Path $VaultPath 'Spirit si Karma'

$concepts = @(
    @{
        Source = 'Aplicabilitate Profesionala.md'
        Folder = 'Aplicabilitate Profesionala'
        Title = 'Aplicabilitate Profesionala'
        Prefix = 'AP'
        Tag = 'AplicabilitateProfesionala'
        CalculationHeadings = @('Formula de calcul')
        FormulaStatus = 'Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Codul Spiritului.md'
        Folder = 'Codul Spiritului'
        Title = 'Codul Spiritului'
        Prefix = 'CS'
        Tag = 'CodulSpiritului'
        CalculationHeadings = @('Calcule', 'Varsta Spiritului', 'Matricea lectiilor')
        FormulaStatus = 'Registrul formulelor marcheaza Codul Spiritului ca neconform, iar etapele si Varsta Spiritului ca neimplementate sau partiale. Continutul legacy este pastrat fara a fi promovat la formula confirmata.'
    },
    @{
        Source = 'Deschidere spre Ezoterism.md'
        Folder = 'Deschidere catre Ezoterism'
        Title = 'Deschidere catre Ezoterism'
        Prefix = 'DE'
        Tag = 'DeschidereCatreEzoterism'
        CalculationHeadings = @('Formula de calcul')
        FormulaStatus = 'Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
    },
    @{
        Source = 'Karma din Ziua Nasterii.md'
        Folder = 'Karma din Ziua Nasterii'
        Title = 'Karma din Ziua Nasterii'
        Prefix = 'KZN'
        Tag = 'KarmaZiuaNasterii'
        CalculationHeadings = @('Formula de calcul')
        FormulaStatus = 'Formula este marcata confirmata in Registru Validare Formule si este pastrata fara modificari.'
        InterpretationFolder = 'KZN - Interpretari'
        InterpretationIndex = '01-KZNI-Index.md'
        InterpretationRange = '1-31'
        InterpretationNaming = 'KZNI-ZZ-[zi].md'
        InterpretationFields = @(
            'ziua calendaristica',
            'arcana karmica',
            'procentul karmei implinite',
            'tema karmica',
            'polaritatea negativa',
            'solutia sau calitatea de dezvoltat'
        )
    },
    @{
        Source = 'Karma din Luna Nasterii.md'
        Folder = 'Karma din Luna Nasterii'
        Title = 'Karma din Luna Nasterii'
        Prefix = 'KLN'
        Tag = 'KarmaLunaNasterii'
        CalculationHeadings = @('Formula de calcul')
        FormulaStatus = 'Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.'
        InterpretationFolder = 'KLN - Interpretari'
        InterpretationIndex = '01-KLNI-Index.md'
        InterpretationRange = '1-12'
        InterpretationNaming = 'KLNI-LL-[luna].md'
        InterpretationFields = @(
            'luna nasterii',
            'tema karmica',
            'persoana, relatia sau planul vizat',
            'directia de lucru',
            'manifestarea dezechilibrata',
            'recomandarea de maturizare'
        )
    },
    @{
        Source = 'Karma din Calea Destinului.md'
        Folder = 'Karma din Calea Destinului'
        Title = 'Karma din Calea Destinului'
        Prefix = 'KCD'
        Tag = 'KarmaCaleaDestinului'
        CalculationHeadings = @('Formula de calcul')
        FormulaStatus = 'Formula este pastrata din nota legacy si foloseste aceeasi baza ca Calea Destinului. Nu a fost lansat un audit formal nou in aceasta etapa.'
        InterpretationFolder = 'KCD - Interpretari'
        InterpretationIndex = '01-KCDI-Index.md'
        InterpretationRange = '4-48'
        InterpretationNaming = 'KCDI-NN-[valoare].md'
        InterpretationFields = @(
            'valoarea completa a Caii Destinului',
            'categoria karmica mare',
            'tema karmica specifica',
            'obstacolele',
            'ajutoarele',
            'directia de curatare sau dezvoltare'
        )
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

if (Test-Path -LiteralPath $DestinationRoot) {
    throw "Directorul-tinta exista deja: $DestinationRoot"
}

foreach ($concept in $concepts) {
    $sourcePath = Join-Path $LegacyPath $concept.Source
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw "Sursa lipseste: $sourcePath"
    }

    $sections = Get-Sections -Text (Get-Content -Raw -Encoding UTF8 -LiteralPath $sourcePath)
    if (-not ($sections.Heading -contains 'Descriere')) {
        throw "Sectiunea Descriere lipseste din $sourcePath"
    }
    if (-not ($sections.Heading -match '^Exempl')) {
        throw "Sectiunea Exemple lipseste din $sourcePath"
    }
    foreach ($heading in $concept.CalculationHeadings) {
        if (-not ($sections.Heading -contains $heading)) {
            throw "Sectiunea de calcul '$heading' lipseste din $sourcePath"
        }
    }
}

New-Item -ItemType Directory -Path $DestinationRoot | Out-Null
$familyLinks = [System.Collections.Generic.List[string]]::new()
$written = [System.Collections.Generic.List[string]]::new()

foreach ($concept in $concepts) {
    $sourcePath = Join-Path $LegacyPath $concept.Source
    $destinationPath = Join-Path $DestinationRoot $concept.Folder
    $sections = Get-Sections -Text (Get-Content -Raw -Encoding UTF8 -LiteralPath $sourcePath)
    $sourceName = [System.IO.Path]::GetFileNameWithoutExtension($concept.Source)

    $description = @($sections | Where-Object Heading -eq 'Descriere')
    $calculation = @($sections | Where-Object { $concept.CalculationHeadings -contains $_.Heading })
    $examples = @($sections | Where-Object Heading -match '^Exempl')
    $methodology = @(
        $sections | Where-Object {
            $_.Heading -ne 'Descriere' -and
            $concept.CalculationHeadings -notcontains $_.Heading -and
            $_.Heading -notmatch '^Exempl'
        }
    )

    $modules = @(
        @{ Number = '02'; Slug = 'Descriere'; Label = 'Descriere'; Type = 'descriere'; Sections = $description },
        @{ Number = '03'; Slug = 'Calcul'; Label = 'Calcul'; Type = 'calcul'; Sections = $calculation },
        @{ Number = '04'; Slug = 'Metodica-si-Interpretari'; Label = 'Metodica si interpretari'; Type = 'metodica-si-interpretari'; Sections = $methodology },
        @{ Number = '05'; Slug = 'Exemple'; Label = 'Exemple'; Type = 'exemple'; Sections = $examples }
    )

    $indexLinks = [System.Collections.Generic.List[string]]::new()
    foreach ($module in $modules) {
        $filename = "$($module.Number)-$($concept.Prefix)-$($module.Slug).md"
        $extra = if ($module.Type -eq 'calcul') {
            "## Statutul formulei`n`n$($concept.FormulaStatus)`n`n"
        } else {
            ''
        }
        $body = ($module.Sections.Text -join "`n`n")
        $content = @"
---
titlu: $($concept.Title) - $($module.Label)
tip: $($module.Type)
tags:
  - numerologie
  - $($module.Type)
  - $($concept.Tag)
  - documentatie-modulara
sursa: '[[$sourceName]]'
---

# $($concept.Title) - $($module.Label)

$extra$body
"@
        $modulePath = Join-Path $destinationPath $filename
        Write-Utf8NoBom -Path $modulePath -Content $content
        $written.Add($modulePath)
        $indexLinks.Add("$([int]$module.Number - 1). [[$([System.IO.Path]::GetFileNameWithoutExtension($filename))|$($module.Label)]]")
    }

    if ($concept.InterpretationFolder) {
        $indexLinks.Add("5. [[$($concept.InterpretationFolder)/$([System.IO.Path]::GetFileNameWithoutExtension($concept.InterpretationIndex))|Interpretari predefinite]]")
    }

    $indexContent = @"
---
titlu: $($concept.Title) - Index
tip: index
tags:
  - numerologie
  - index
  - $($concept.Tag)
  - documentatie-modulara
---

# $($concept.Title)

## Cuprins

$($indexLinks -join "`n")

## Sursa pastrata

- [[$sourceName]]
"@
    $indexPath = Join-Path $destinationPath "01-$($concept.Prefix)-Index.md"
    Write-Utf8NoBom -Path $indexPath -Content $indexContent
    $written.Add($indexPath)

    if ($concept.InterpretationFolder) {
        $fieldLines = [System.Collections.Generic.List[string]]::new()
        for ($fieldIndex = 0; $fieldIndex -lt $concept.InterpretationFields.Count; $fieldIndex++) {
            $fieldLines.Add("$($fieldIndex + 1). $($concept.InterpretationFields[$fieldIndex]);")
        }

        $interpretationContent = @"
---
titlu: $($concept.Title) - Interpretari - Index
tip: index-interpretari
tags:
  - numerologie
  - karma
  - index
  - interpretari
  - $($concept.Tag)
  - documentatie-modulara
---

# $($concept.Title) - Interpretari

## Scop

Acest director va pastra interpretarile predefinite pentru fiecare rezultat al
conceptului $($concept.Title).

## Interval

- valori prevazute: $($concept.InterpretationRange);
- fiecare rezultat va avea propriul fisier;
- interpretarile se adauga numai dupa validarea continutului.

## Regula de denumire

~~~text
$($concept.InterpretationNaming)
~~~

## Structura obligatorie

Fiecare interpretare viitoare va consemna:

$($fieldLines -join "`n")

## Statut

Interpretarile individuale nu sunt completate in aceasta etapa.

## Sursa conceptului

- [[$sourceName]]
- [[../01-$($concept.Prefix)-Index|Indexul modular $($concept.Title)]]
"@
        $interpretationPath = Join-Path (Join-Path $destinationPath $concept.InterpretationFolder) $concept.InterpretationIndex
        Write-Utf8NoBom -Path $interpretationPath -Content $interpretationContent
        $written.Add($interpretationPath)
    }

    $familyLinks.Add("- [[$($concept.Folder)/01-$($concept.Prefix)-Index|$($concept.Title)]]")
}

$familyIndex = @"
---
titlu: Spirit si Karma - Index
tip: index-familie
tags:
  - numerologie
  - index
  - SpiritSiKarma
  - documentatie-modulara
---

# Spirit si Karma

## Concepte

$($familyLinks -join "`n")

## Referinte asociate

- [[../Nume/Numarul Ereditar Karmic/01-NEK-Index|Numarul Ereditar Karmic]]

## Regula structurala

- fiecare concept are propriul director modular;
- Aplicabilitatea Profesionala, Codul Spiritului si Deschiderea catre Ezoterism
  nu folosesc directoare de interpretari in aceasta etapa;
- fiecare concept Karma are propriul director de interpretari predefinite;
- notele legacy sunt pastrate pentru compatibilitate.
"@
$familyIndexPath = Join-Path $DestinationRoot '01-SK-Index.md'
Write-Utf8NoBom -Path $familyIndexPath -Content $familyIndex
$written.Add($familyIndexPath)

Write-Output "Directoare conceptuale create: $($concepts.Count)"
Write-Output "Fisiere create: $($written.Count)"
