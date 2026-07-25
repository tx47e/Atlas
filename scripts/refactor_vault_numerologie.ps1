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

$concepts = @(
    @{ Source='Vibratie Interioara.md'; Folder='Vibratia Interioara'; Prefix='VI'; Interpretari=$true },
    @{ Source='Vibratie Exterioara.md'; Folder='Vibratia Exterioara'; Prefix='VE' },
    @{ Source='Vibratie Globala.md'; Folder='Vibratia Globala'; Prefix='VG' },
    @{ Source='Destin.md'; Folder='Destin'; Prefix='D' },
    @{ Source='Vibratie Cosmica Fixa.md'; Folder='Vibratia Cosmica Fixa'; Prefix='VCF' },
    @{ Source='Vibratie Cosmica Variabila.md'; Folder='Vibratia Cosmica Variabila'; Prefix='VCV' },
    @{ Source='Vibratie Cosmica Totala.md'; Folder='Vibratia Cosmica Totala'; Prefix='VCT' },
    @{ Source='Calea Destinului.md'; Folder='Calea Destinului'; Prefix='CD' },
    @{ Source='Aspecte de Indreptat.md'; Folder='Aspecte de Indreptat'; Prefix='AI' },
    @{ Source='Punti.md'; Folder='Punti'; Prefix='PU' },
    @{ Source='Lectii de Viata.md'; Folder='Lectii de Viata'; Prefix='LV' },
    @{ Source='Soarta si Destin.md'; Folder='Soarta si Destin'; Prefix='SD' },
    @{ Source='Karma din Ziua Nasterii.md'; Folder='Karma din Ziua Nasterii'; Prefix='KZN' },
    @{ Source='Karma din Luna Nasterii.md'; Folder='Karma din Luna Nasterii'; Prefix='KLN' },
    @{ Source='Karma din Calea Destinului.md'; Folder='Karma din Calea Destinului'; Prefix='KCD' },
    @{ Source='Numarul Activ.md'; Folder='Numarul Activ'; Prefix='NA' },
    @{ Source='Numarul Intim.md'; Folder='Numarul Intim'; Prefix='NI' },
    @{ Source='Numarul Ereditar.md'; Folder='Numarul Ereditar'; Prefix='NE' },
    @{ Source='Numarul de Realizare.md'; Folder='Numarul de Realizare'; Prefix='NR' },
    @{ Source='Numarul de Exprimare.md'; Folder='Numarul de Exprimare'; Prefix='NX' },
    @{ Source='Numarul Neamului.md'; Folder='Numarul Neamului'; Prefix='NN' },
    @{ Source='Cod Numerologic Personal.md'; Folder='Cod Numerologic Personal'; Prefix='CNP' },
    @{ Source='Influentele Numelui.md'; Folder='Influentele Numelui'; Prefix='IN' },
    @{ Source='Codul Spiritului.md'; Folder='Codul Spiritului'; Prefix='CS' },
    @{ Source='Matricea Datei de Nastere.md'; Folder='Matricea Datei de Nastere'; Prefix='MDN' },
    @{ Source='Matricea Numelui.md'; Folder='Matricea Numelui'; Prefix='MN' },
    @{ Source='Matricea Numelui vs Matricea Datei de Nastere.md'; Folder='Matricea Numelui vs Matricea Datei de Nastere'; Prefix='MNC' },
    @{ Source='Figuri Geometrice.md'; Folder='Figuri Geometrice'; Prefix='FG' },
    @{ Source='Scara Bunastarii.md'; Folder='Scara Bunastarii'; Prefix='SB' },
    @{ Source='Fixatia.md'; Folder='Fixatia'; Prefix='FX' },
    @{ Source='Tendinta.md'; Folder='Tendinta'; Prefix='TD' },
    @{ Source='Curgerea Energiei.md'; Folder='Curgerea Energiei'; Prefix='CE' },
    @{ Source='Caii Trasura si Vizitiul.md'; Folder='Caii Trasura si Vizitiul'; Prefix='CTV' },
    @{ Source='Pinacluri - Oportunitati si Provocari.md'; Folder='Pinacluri - Oportunitati si Provocari'; Prefix='POC' },
    @{ Source='Ciclul de 7 Ani.md'; Folder='Ciclul de 7 Ani'; Prefix='C7' },
    @{ Source='Septagrama.md'; Folder='Septagrama'; Prefix='SPT' },
    @{ Source='Ciclul de 9 Ani.md'; Folder='Ciclul de 9 Ani'; Prefix='C9' },
    @{ Source='Ciclul de 12 Ani.md'; Folder='Ciclul de 12 Ani'; Prefix='C12' },
    @{ Source='Anii Importanti Int-Ext.md'; Folder='Anii Importanti Int-Ext'; Prefix='AII' },
    @{ Source='Omuletul Relatiilor.md'; Folder='Omuletul Relatiilor'; Prefix='OR' },
    @{ Source='Deschidere spre Ezoterism.md'; Folder='Deschidere spre Ezoterism'; Prefix='DE' },
    @{ Source='Aplicabilitate Profesionala.md'; Folder='Aplicabilitate Profesionala'; Prefix='AP' },
    @{ Source='Semnatura Astrala.md'; Folder='Semnatura Astrala'; Prefix='SA' },
    @{ Source='Directiile de Succes.md'; Folder='Directiile de Succes'; Prefix='DS' },
    @{ Source='Triunghiul Financiar.md'; Folder='Triunghiul Financiar'; Prefix='TF' },
    @{ Source='Patratul de Aur.md'; Folder='Patratul de Aur'; Prefix='PA' }
)

function Get-DocumentParts {
    param([string]$Path)
    $text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    $frontmatter = ''
    if ($text -match '(?s)\A---\r?\n.*?\r?\n---\r?\n') {
        $frontmatter = $Matches[0].TrimEnd()
        $text = $text.Substring($Matches[0].Length)
    }
    $title = [regex]::Match($text, '(?m)^#\s+(.+)$').Groups[1].Value.Trim()
    $matches = [regex]::Matches($text, '(?m)^##\s+(.+)$')
    $sections = @()
    $h1 = [regex]::Match($text, '(?m)^#\s+.+(?:\r?\n|$)')
    if ($h1.Success) {
        $preambleEnd = if ($matches.Count -gt 0) { $matches[0].Index } else { $text.Length }
        $preamble = $text.Substring($h1.Index + $h1.Length, $preambleEnd - ($h1.Index + $h1.Length)).Trim()
        if ($preamble -and $preamble -ne '---') {
            $sections += [pscustomobject]@{
                Heading = 'Descriere'
                Text = "## Descriere`r`n`r`n$preamble"
            }
        }
    }
    for ($i = 0; $i -lt $matches.Count; $i++) {
        $start = $matches[$i].Index
        $end = if ($i + 1 -lt $matches.Count) { $matches[$i + 1].Index } else { $text.Length }
        $sections += [pscustomobject]@{
            Heading = $matches[$i].Groups[1].Value.Trim()
            Text = $text.Substring($start, $end - $start).Trim()
        }
    }
    return [pscustomobject]@{ Frontmatter=$frontmatter; Title=$title; Sections=$sections }
}

function Get-Bucket {
    param([string]$Heading)
    $h = $Heading.ToLowerInvariant()
    if ($h -match 'descriere|incadrare') { return 'description' }
    if ($h -match 'exempl|studiu') { return 'examples' }
    if ($h -match 'utilizare|corelar|observa|domenii secundare') { return 'correlations' }
    if ($h -match 'formula|calcul|principiu|schema|tabel|traseu|multiplicare|varsta spiritului|matricea lectiilor|regula de verificare') { return 'calculation' }
    return 'methodology'
}

function Write-Utf8 {
    param([string]$Path, [string]$Content)
    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }
    Set-Content -LiteralPath $Path -Value $Content.TrimEnd() -Encoding UTF8
}

$migrationRows = @()
foreach ($concept in $concepts) {
    $sourcePath = Join-Path $LegacyPath $concept.Source
    if (-not (Test-Path -LiteralPath $sourcePath)) {
        Write-Warning "Sursa lipseste: $($concept.Source)"
        continue
    }

    $parts = Get-DocumentParts -Path $sourcePath
    # Denumirea canonica este cea din harta de migrare; multe note legacy nu au H1.
    $parts.Title = $concept.Folder
    $folderPath = Join-Path $VaultPath $concept.Folder
    New-Item -ItemType Directory -Path $folderPath -Force | Out-Null

    $buckets = @{
        description = [System.Collections.Generic.List[string]]::new()
        calculation = [System.Collections.Generic.List[string]]::new()
        methodology = [System.Collections.Generic.List[string]]::new()
        correlations = [System.Collections.Generic.List[string]]::new()
        examples = [System.Collections.Generic.List[string]]::new()
    }
    foreach ($section in $parts.Sections) {
        $buckets[(Get-Bucket -Heading $section.Heading)].Add($section.Text)
    }

    $moduleDefinitions = @(
        @{ Number='01'; Slug='Descriere'; Bucket='description'; Label='Descriere' },
        @{ Number='02'; Slug='Calcul'; Bucket='calculation'; Label='Calcul' },
        @{ Number='03'; Slug='Metodologie-Interpretare'; Bucket='methodology'; Label='Metodologie de interpretare' },
        @{ Number='04'; Slug='Corelari'; Bucket='correlations'; Label='Corelari' },
        @{ Number='05'; Slug='Exemple-si-Studii-de-Caz'; Bucket='examples'; Label='Exemple si studii de caz' }
    )

    $moduleLinks = [System.Collections.Generic.List[string]]::new()
    foreach ($module in $moduleDefinitions) {
        $filename = "$($concept.Prefix)-$($module.Number)-$($module.Slug).md"
        $bodySections = $buckets[$module.Bucket]
        $statusText = if ($bodySections.Count -gt 0) {
            $bodySections -join "`r`n`r`n"
        } else {
            "> Sectiune structurala creata. Continutul nu exista in nota-sursa si nu a fost completat automat."
        }
        $content = @"
---
titlu: "$($parts.Title) - $($module.Label)"
concept: "$($parts.Title)"
tip_document: "$($module.Bucket)"
sursa_legacy: "[[$([IO.Path]::GetFileNameWithoutExtension($concept.Source))]]"
status_migrare: "structura implementata"
tags:
  - numerologie
  - documentatie-modulara
---

# $($parts.Title) - $($module.Label)

> Continut migrat din [[$([IO.Path]::GetFileNameWithoutExtension($concept.Source))]]. Nota-sursa este pastrata pentru compatibilitate.

$statusText
"@
        Write-Utf8 -Path (Join-Path $folderPath $filename) -Content $content
        $moduleLinks.Add("- [[$($concept.Folder)/$([IO.Path]::GetFileNameWithoutExtension($filename))|$($module.Label)]]")
    }

    if ($concept.Interpretari) {
        $interpretariPath = Join-Path $folderPath 'interpretari'
        New-Item -ItemType Directory -Path $interpretariPath -Force | Out-Null
        $values = @('0','1','2','3','4','5','6','7','8','9','11','22','33')
        $legacyLinks = ($values | ForEach-Object { "- [[Vibratia $_]] - sursa existenta; migrarea modulara este amanata." }) -join "`r`n"
        Write-Utf8 -Path (Join-Path $interpretariPath "$($concept.Prefix)-00-Index.md") -Content @"
# Interpretari - $($parts.Title)

Interpretarile individuale nu sunt completate in aceasta etapa.

## Surse existente

$legacyLinks

## Regula etapei curente

- Nu se creeaza fisiere numerotate de interpretare pana la aprobarea continutului.
- Notele Vibratia 0, Vibratia 1 ... Vibratia 33 raman sursele de lucru.
- La migrare, continutul se verifica individual; nu se genereaza interpretari automat.
"@
        Write-Utf8 -Path (Join-Path $interpretariPath "$($concept.Prefix)-00-Template.md") -Content @"
---
titlu: "Template interpretare - $($parts.Title)"
status: "template"
---

# $($concept.Prefix)-NN - [valoare]

> Template necompletat. Se foloseste numai dupa aprobarea etapei de interpretari.

## Descriere

## Arhetip

## Lumina vibratiei

## Umbra vibratiei

## Lectii

## Directii de dezvoltare

## Exemple

## Corelari
"@
        $moduleLinks.Add("- [[$($concept.Folder)/interpretari/$($concept.Prefix)-00-Index|Interpretari (index; continut amanat)]]")
        $moduleLinks.Add("- [[$($concept.Folder)/interpretari/$($concept.Prefix)-00-Template|Template interpretare]]")
    }

    $indexContent = @"
---
titlu: "$($parts.Title)"
tip_document: "index modular"
sursa_legacy: "[[$([IO.Path]::GetFileNameWithoutExtension($concept.Source))]]"
status_migrare: "structura implementata"
tags:
  - numerologie
  - index
  - documentatie-modulara
---

# $($parts.Title)

## Documente

$($moduleLinks -join "`r`n")

## Compatibilitate

- Nota-sursa pastrata: [[$([IO.Path]::GetFileNameWithoutExtension($concept.Source))]]
- Continutul factual existent a fost distribuit modular; nu s-au inventat interpretari.
"@
    Write-Utf8 -Path (Join-Path $folderPath "$($concept.Prefix)-00-Index.md") -Content $indexContent
    $migrationRows += "| $($concept.Source) | $($concept.Folder)/$($concept.Prefix)-00-Index.md | $($concept.Prefix) |"
}

$standardPath = Join-Path $VaultPath '_Standard-Modular'
New-Item -ItemType Directory -Path $standardPath -Force | Out-Null
Write-Utf8 -Path (Join-Path $standardPath '00-Standard-Documentatie-Modulara.md') -Content @"
# Standard documentatie modulara

## Structura

Fiecare concept foloseste, dupa caz:

- XX-00-Index.md
- XX-01-Descriere.md
- XX-02-Calcul.md
- XX-03-Metodologie-Interpretare.md
- XX-04-Corelari.md
- XX-05-Exemple-si-Studii-de-Caz.md
- interpretari/XX-00-Index.md si interpretari/XX-00-Template.md, numai unde exista o familie de interpretari individuale.

## Reguli

1. Nota-sursa ramane disponibila pana la verificarea completa a legaturilor.
2. Continutul existent se muta fara reformulare automata.
3. Sectiunile lipsa sunt marcate explicit; nu sunt completate prin presupuneri.
4. Interpretarile individuale nu se genereaza automat.
5. Formula ramane identica sursei aprobate si Registrului de validare.
6. Exemplele sunt separate de formula si de metodologia de interpretare.
7. Indexul modular este punctul nou de intrare pentru concept.
"@

$mapHeader = @"
# Harta de migrare - Numerologie

| Nota-sursa | Index modular | Prefix |
|---|---|---|
"@
Write-Utf8 -Path (Join-Path $standardPath '01-Harta-de-Migrare.md') -Content ($mapHeader + "`r`n" + ($migrationRows -join "`r`n"))

Write-Output "Concepte procesate: $($migrationRows.Count)"
Write-Output "Indexuri modulare: $((Get-ChildItem -LiteralPath $VaultPath -Recurse -Filter '*-00-Index.md').Count)"
