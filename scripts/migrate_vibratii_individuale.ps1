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
$DestinationRoot = Join-Path $VaultPath 'Vibratii\Vibratii Fundamentale'

$values = @('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '22', '33')
$modules = @(
    @{ Number = '02'; Slug = 'Descriere'; SourceHeading = 'Descriere'; Label = 'Descriere'; Type = 'descriere' },
    @{ Number = '03'; Slug = 'Arhetip'; SourceHeading = 'Arhetip'; Label = 'Arhetip'; Type = 'arhetip' },
    @{ Number = '04'; Slug = 'Lumina'; SourceHeading = 'Lumina vibratiei'; Label = 'Lumina'; Type = 'lumina' },
    @{ Number = '05'; Slug = 'Umbra'; SourceHeading = 'Umbra vibratiei'; Label = 'Umbra'; Type = 'umbra' },
    @{ Number = '06'; Slug = 'Lectii'; SourceHeading = 'Lectii'; Label = 'Lectii'; Type = 'lectii' },
    @{ Number = '07'; Slug = 'Dezvoltare'; SourceHeading = 'Directii de dezvoltare'; Label = 'Dezvoltare'; Type = 'dezvoltare' },
    @{ Number = '08'; Slug = 'Exemple'; SourceHeading = 'Exemple'; Label = 'Exemple'; Type = 'exemple' },
    @{ Number = '09'; Slug = 'Tarot'; SourceHeading = 'Tarot'; Label = 'Tarot'; Type = 'tarot' }
)

function Write-Utf8NoBom {
    param(
        [string]$Path,
        [string]$Content
    )

    $encoding = [System.Text.UTF8Encoding]::new($false)
    $normalized = [regex]::Replace(
        $Content,
        '[ \t]+(?=\r?$)',
        '',
        [System.Text.RegularExpressions.RegexOptions]::Multiline
    )
    [System.IO.File]::WriteAllText($Path, ($normalized.TrimEnd() + "`n"), $encoding)
}

function Get-Sections {
    param([string]$Text)

    $matches = [regex]::Matches($Text, '(?m)^##\s+(.+?)\s*$')
    $sections = @{}

    for ($index = 0; $index -lt $matches.Count; $index++) {
        $heading = $matches[$index].Groups[1].Value.Trim()
        $bodyStart = $matches[$index].Index + $matches[$index].Length
        $bodyEnd = if ($index + 1 -lt $matches.Count) {
            $matches[$index + 1].Index
        } else {
            $Text.Length
        }
        $body = $Text.Substring($bodyStart, $bodyEnd - $bodyStart).Trim()
        $sections[$heading] = $body
    }

    return $sections
}

# Preflight complet: nicio scriere daca lipseste o sursa, o sectiune sau exista
# deja unul dintre directoarele-tinta.
foreach ($value in $values) {
    $sourcePath = Join-Path $LegacyPath "Vibratia $value.md"
    $destinationPath = Join-Path $DestinationRoot "Vibratia $value"

    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw "Sursa lipseste: $sourcePath"
    }
    if (Test-Path -LiteralPath $destinationPath) {
        throw "Directorul-tinta exista deja: $destinationPath"
    }

    $text = Get-Content -Raw -Encoding UTF8 -LiteralPath $sourcePath
    $sections = Get-Sections -Text $text
    foreach ($module in $modules) {
        if (-not $sections.ContainsKey($module.SourceHeading)) {
            throw "Sectiunea '$($module.SourceHeading)' lipseste din $sourcePath"
        }
    }
    if ($sections.Count -ne $modules.Count) {
        throw "Numar neasteptat de sectiuni in ${sourcePath}: $($sections.Count)"
    }
}

$writtenFiles = [System.Collections.Generic.List[string]]::new()

foreach ($value in $values) {
    $concept = "Vibratia $value"
    $prefix = "V$value"
    $tag = "Vibratia$value"
    $sourcePath = Join-Path $LegacyPath "$concept.md"
    $destinationPath = Join-Path $DestinationRoot $concept
    $text = Get-Content -Raw -Encoding UTF8 -LiteralPath $sourcePath
    $sections = Get-Sections -Text $text

    New-Item -ItemType Directory -Path $destinationPath | Out-Null

    $indexLinks = foreach ($module in $modules) {
        "$([int]$module.Number - 1). [[$($module.Number)-$prefix-$($module.Slug)|$($module.Label)]]"
    }
    $indexContent = @"
---
titlu: $concept - Index
tip: index
tags:
  - numerologie
  - index
  - $tag
  - documentatie-modulara
---

# $concept

## Cuprins

$($indexLinks -join "`n")

## Sursa pastrata

- [[$concept]]
"@
    $indexPath = Join-Path $destinationPath "01-$prefix-Index.md"
    Write-Utf8NoBom -Path $indexPath -Content $indexContent
    $writtenFiles.Add($indexPath)

    foreach ($module in $modules) {
        $sourceBody = $sections[$module.SourceHeading]
        $moduleContent = @"
---
titlu: $concept - $($module.Label)
tip: $($module.Type)
tags:
  - numerologie
  - $($module.Type)
  - $tag
  - documentatie-modulara
sursa: '[[$concept]]'
---

# $concept - $($module.Label)

## $($module.SourceHeading)

$sourceBody
"@
        $modulePath = Join-Path $destinationPath "$($module.Number)-$prefix-$($module.Slug).md"
        Write-Utf8NoBom -Path $modulePath -Content $moduleContent
        $writtenFiles.Add($modulePath)
    }
}

Write-Output "Directoare create: $($values.Count)"
Write-Output "Fisiere create: $($writtenFiles.Count)"
