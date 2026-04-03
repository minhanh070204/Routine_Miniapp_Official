$rootDir = "c:\Users\Le Minh Anh\Downloads\stitch_duplicate_of_t_ch_i_m_n_s_n\stitch_duplicate_of_t_ch_i_m_n_s_n"

$styleBlock = @"
<style>
    /* Styling according to user requirement */
    button:not(.rounded-full):not([class*="rounded-full"]), 
    a:not(.rounded-full)[class*="bg-[#222222]"], 
    a:not(.rounded-full)[class*="bg-black"],
    .card-rounded:not(.rounded-full) {
        border-radius: 8px !important;
    }
</style>
</head>
"@

$logoTag = '<img src="https://media.routine.vn/0x0/prod/media/52ba65a3-e085-45a6-bf5e-fb9c359abff7.webp" alt="ROUTINE" class="h-4 sm:h-5 object-contain mx-auto" />'

# Get all HTML files
$files = Get-ChildItem -Path $rootDir -Recurse -Filter "code.html"

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $modified = $false

    # 1. Round buttons
    if ($content -notmatch "\/\* Styling according to user requirement \*\/") {
        $content = $content -replace '(?i)</head>', $styleBlock
        $modified = $true
    }

    # 2. Add Routine logo
    # Find the top header/nav blocks
    # Using Regex to find the first <header ... > ... </header> or <nav ... top-0 ... > ... </nav>
    $headerPattern = '(?is)(<header[^>]*>|<nav[^>]*top-0[^>]*>)(.*?)(</header>|</nav>)'
    if ($content -match $headerPattern) {
        $fullMatch = $matches[0]
        $startTag = $matches[1]
        $innerContent = $matches[2]
        $endTag = $matches[3]

        $newInner = $innerContent

        # Substitute <h1>...</h1> with the logo if it exists
        if ($newInner -match '<h1[^>]*>.*?</h1>') {
            $newInner = $newInner -replace '<h1[^>]*>.*?</h1>', $logoTag
        } elseif ($newInner -match '<img[^>]*alt="ROUTINE[^"]*"[^>]*>') {
            $newInner = $newInner -replace '<img[^>]*alt="ROUTINE[^"]*"[^>]*>', $logoTag
        }

        if ($newInner -ne $innerContent) {
            $newHeader = $startTag + $newInner + $endTag
            # Replace only the first occurrence
            $content = $content.Substring(0, $content.IndexOf($fullMatch)) + $newHeader + $content.Substring($content.IndexOf($fullMatch) + $fullMatch.Length)
            $modified = $true
        }
    }

    if ($modified) {
        # Note: PowerShell Out-File often saves as UTF-8 with BOM. Best to use .NET explicit write to prevent BOM.
        [System.IO.File]::WriteAllText($file.FullName, $content, (New-Object System.Text.UTF8Encoding $false))
        Write-Host "Updated $($file.FullName)"
    }
}
