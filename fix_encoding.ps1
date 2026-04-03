$base_dir = "c:\Users\Le Minh Anh\Downloads\stitch_duplicate_of_t_ch_i_m_n_s_n\stitch_duplicate_of_t_ch_i_m_n_s_n"

$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$win1252   = [System.Text.Encoding]::GetEncoding(1252)
$utf8      = [System.Text.Encoding]::UTF8

$fixed = 0

Get-ChildItem -Path $base_dir -Directory | ForEach-Object {
    $codePath = Join-Path $_.FullName "code.html"
    if (Test-Path $codePath) {
        # 1. Read raw bytes from the currently corrupted file
        $bytes = [System.IO.File]::ReadAllBytes($codePath)

        # 2. Decode those bytes as UTF-8 -> gives us the mojibake Unicode string
        #    (e.g. "á»§" instead of "ủ")
        $mojibakeStr = $utf8.GetString($bytes)

        # Remove UTF-8 BOM character if present
        if ($mojibakeStr.StartsWith([char]0xFEFF)) {
            $mojibakeStr = $mojibakeStr.Substring(1)
        }

        # 3. Re-encode that mojibake string back to Windows-1252 bytes
        #    -> this reverses the misread and gives us the ORIGINAL UTF-8 bytes
        $originalUtf8Bytes = $win1252.GetBytes($mojibakeStr)

        # 4. Decode original UTF-8 bytes -> correct Vietnamese Unicode string
        $fixedStr = $utf8.GetString($originalUtf8Bytes)

        # 5. Ensure <meta charset="UTF-8"> is present right after <head>
        #    Remove any existing charset meta to avoid duplicates
        $fixedStr = $fixedStr -replace '(?i)<meta[^>]+charset[^>]*/?>', ''
        # Add it right after opening <head> tag
        $fixedStr = $fixedStr -replace '(?i)(<head[^>]*>)', '$1<meta charset="UTF-8">'

        # 6. Save as UTF-8 without BOM
        [System.IO.File]::WriteAllText($codePath, $fixedStr, $utf8NoBom)

        $fixed++
        Write-Output "Fixed: $($_.Name)"
    }
}

Write-Output ""
Write-Output "=== DONE! Fixed $fixed files ==="
