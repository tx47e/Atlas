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
$NameRoot = Join-Path $VaultPath 'Nume'

$concepts = @(
    @{
        Source = 'Matricea Numelui.md'
        Folder = 'Matricea Numelui'
        Title = 'Matricea Numelui'
        Prefix = 'MN'
        Tag = 'MatriceaNumelui'
        FormulaStatus = 'Metoda foloseste Patratul lui Pitagora si valorile numerologice ale literelor. Formula este pastrata din nota legacy, fara audit formal nou.'
    },
    @{
        Source = 'Matricea Numelui vs Matricea Datei de Nastere.md'
        Folder = 'Comparatia Matricea Datei de Nastere vs Matricea Numelui'
        Title = 'Comparatia Matricea Datei de Nastere vs Matricea Numelui'
        Prefix = 'CMN'
        Tag = 'ComparatieMatriceDataNume'
        FormulaStatus = 'Metoda compara cele doua matrici pe fiecare casuta si nu construieste o a treia matrice. Formula este pastrata din nota legacy, fara audit formal nou.'
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

foreach ($concept in $concepts) {
    $sourcePath = Join-Path $LegacyPath $concept.Source
    $destination = Join-Path $NameRoot $concept.Folder
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw "Sursa lipseste: $sourcePath"
    }
    if (Test-Path -LiteralPath $destination) {
        throw "Directorul-tinta exista deja: $destination"
    }
}

foreach ($concept in $concepts) {
    $sourcePath = Join-Path $LegacyPath $concept.Source
    $sourceName = [IO.Path]::GetFileNameWithoutExtension($concept.Source)
    $destination = Join-Path $NameRoot $concept.Folder
    $sections = @(Get-Sections -Text (Get-Content -Raw -Encoding UTF8 -LiteralPath $sourcePath))

    $modules = @(
        @{
            Number = '02'; Slug = 'Descriere'; Label = 'Descriere'; Type = 'descriere'
            Sections = @($sections | Where-Object Heading -eq 'Descriere')
        },
        @{
            Number = '03'; Slug = 'Calcul'; Label = 'Calcul'; Type = 'calcul'
            Sections = @($sections | Where-Object Heading -match '^(Formula|Calcule|Calcul|Principiu)')
        },
        @{
            Number = '04'; Slug = 'Metodica-si-Interpretari'
            Label = 'Metodica si interpretari'; Type = 'metodica-si-interpretari'
            Sections = @(
                $sections | Where-Object {
                    $_.Heading -ne 'Descriere' -and
                    $_.Heading -notmatch '^(Formula|Calcule|Calcul|Principiu)' -and
                    $_.Heading -notmatch '^Exempl'
                }
            )
        },
        @{
            Number = '05'; Slug = 'Exemple'; Label = 'Exemple'; Type = 'exemple'
            Sections = @($sections | Where-Object Heading -match '^Exempl')
        }
    )

    foreach ($module in $modules) {
        $status = if ($module.Type -eq 'calcul') {
            "## Statutul formulei`n`n$($concept.FormulaStatus)`n`n"
        } else {
            ''
        }
        $body = ($module.Sections.Text -join "`n`n")
        if ([string]::IsNullOrWhiteSpace($body)) {
            $body = "## Statut`n`nNota legacy nu contine o sectiune separata pentru acest modul."
        }
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

$status$body
"@
        $filename = "$($module.Number)-$($concept.Prefix)-$($module.Slug).md"
        Write-Utf8NoBom -Path (Join-Path $destination $filename) -Content $content
    }

    $relatedIndex = if ($concept.Source -eq 'Matricea Numelui.md') {
        @"
## Concepte asociate din Matricea Datei de Nastere

- [[../../Matricea Datei de Nastere/Casute/01-CA-Index|Casute]]
- [[../../Matricea Datei de Nastere/Curgerea Energiei/01-CE-Index|Curgerea Energiei]]
- [[../../Matricea Datei de Nastere/Figuri Geometrice/01-FG-Index|Figuri Geometrice]]

"@
    } else {
        ''
    }
    $index = @"
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

1. [[02-$($concept.Prefix)-Descriere|Descriere]]
2. [[03-$($concept.Prefix)-Calcul|Calcul]]
3. [[04-$($concept.Prefix)-Metodica-si-Interpretari|Metodica si interpretari]]
4. [[05-$($concept.Prefix)-Exemple|Exemple]]

$relatedIndex## Sursa pastrata
- [[$sourceName]]
"@
    Write-Utf8NoBom -Path (Join-Path $destination "01-$($concept.Prefix)-Index.md") -Content $index
}

$created = @(foreach ($concept in $concepts) {
    Get-ChildItem -LiteralPath (Join-Path $NameRoot $concept.Folder) -File
})
Write-Output "Directoare create: $($concepts.Count)"
Write-Output "Fisiere create: $($created.Count)"
