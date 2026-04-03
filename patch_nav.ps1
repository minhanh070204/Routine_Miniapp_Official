$base_dir = "c:\Users\Le Minh Anh\Downloads\stitch_duplicate_of_t_ch_i_m_n_s_n\stitch_duplicate_of_t_ch_i_m_n_s_n"

# Map from data-icon to target folder
$navMap = @{
    "home"         = "trang_ch_m_u_m_i"
    "home_app_logo"= "trang_ch_m_u_m_i"
    "grid_view"    = "k_t_qu_t_m_ki_m_flat_lay"
    "search"       = "k_t_qu_t_m_ki_m_flat_lay"
    "shopping_bag" = "gi_h_ng_m_u_m_i"
    "style"        = "gi_h_ng_m_u_m_i"
    "person"       = "trung_t_m_th_nh_vi_n_s_ch_s_c_p_nh_t"
}

$utf8NoBom = New-Object System.Text.UTF8Encoding $false

Get-ChildItem -Path $base_dir -Directory | ForEach-Object {
    $folderName = $_.Name
    $codePath = Join-Path $_.FullName "code.html"
    if (-not (Test-Path $codePath)) { return }

    $bytes = [System.IO.File]::ReadAllBytes($codePath)
    $content = [System.Text.Encoding]::UTF8.GetString($bytes)

    # For each nav icon, find its <a> parent and patch the href
    foreach ($icon in $navMap.Keys) {
        $target = $navMap[$icon]
        # Skip self-link
        if ($target -eq $folderName) {
            $relativePath = "#"
        } else {
            $relativePath = "../" + $target + "/code.html"
        }
        
        # Pattern: find <a ...> blocks containing data-icon="ICON"
        # Replace href="#" or href="..." within those blocks with our target
        # We use a targeted approach: find the nav <a> that wraps a span with this specific data-icon
        # Replace href attribute in <a> elements that contain spans with data-icon matching our nav icons
        
        # Simple regex: match <a ... href="..." ...> where the tag is followed soon by data-icon="icon"
        # We look for: <a class="...flex flex-col...href="..."...data-icon="ICON"
        $pattern = '(<a\s[^>]*?href=")[^"]*("[^>]*?>(?:[^<]|\n)*?<span[^>]*?data-icon="' + $icon + '")'
        $replacement = '${1}' + $relativePath + '${2}'
        $content = [regex]::Replace($content, $pattern, $replacement, [System.Text.RegularExpressions.RegexOptions]::Singleline)
    }

    [System.IO.File]::WriteAllText($codePath, $content, $utf8NoBom)
}

Write-Output "Done patching all nav hrefs."
