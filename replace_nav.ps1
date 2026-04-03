$baseDir = "c:\Users\Le Minh Anh\Downloads\stitch_duplicate_of_t_ch_i_m_n_s_n\stitch_duplicate_of_t_ch_i_m_n_s_n"
$navReplacement = @"
<nav class="fixed bottom-0 w-full flex justify-around items-center px-4 py-3 pb-safe bg-[#F9F9F9]/90 dark:bg-neutral-900/90 backdrop-blur-xl border-t-[0.5px] border-[#222222]/10 shadow-[0_-20px_40px_rgba(34,34,34,0.05)] z-50">
<!-- Trang chủ -->
<a class="flex flex-col items-center justify-center text-[#222222]/50 hover:text-[#D2A7A7] transition-colors duration-300 scale-95 active:scale-100" href="../trang_ch_m_u_m_i/code.html">
<span class="material-symbols-outlined mb-1" data-icon="home">home</span>
<span class="font-['Inter'] text-[10px] tracking-[1.2px] uppercase font-medium">Trang chủ</span>
</a>
<!-- Danh mục -->
<a class="flex flex-col items-center justify-center text-[#222222]/50 hover:text-[#D2A7A7] transition-colors duration-300 scale-95 active:scale-100" href="../k_t_qu_t_m_ki_m_flat_lay/code.html">
<span class="material-symbols-outlined mb-1" data-icon="grid_view">grid_view</span>
<span class="font-['Inter'] text-[10px] tracking-[1.2px] uppercase font-medium">Danh mục</span>
</a>
<!-- Giỏ hàng -->
<a class="flex flex-col items-center justify-center text-[#222222]/50 hover:text-[#D2A7A7] transition-colors duration-300 scale-95 active:scale-100" href="../gi_h_ng_m_u_m_i/code.html">
<span class="material-symbols-outlined mb-1" data-icon="shopping_bag">shopping_bag</span>
<span class="font-['Inter'] text-[10px] tracking-[1.2px] uppercase font-medium">Giỏ hàng</span>
</a>
<!-- Thành viên -->
<a class="flex flex-col items-center justify-center text-[#222222]/50 hover:text-[#D2A7A7] transition-colors duration-300 scale-95 active:scale-100" href="../trung_t_m_th_nh_vi_n_s_ch_s_c_p_nh_t/code.html">
<span class="material-symbols-outlined mb-1" data-icon="person">person</span>
<span class="font-['Inter'] text-[10px] tracking-[1.2px] uppercase font-medium">Thành viên</span>
</a>
</nav>
"@

$filesModified = 0

Get-ChildItem -Path $baseDir -Filter "code.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    
    # Regex to replace the <nav> block carrying bottom-0
    $regex = [regex]::new('<nav[^>]*bottom-0[^>]*>[\s\S]*?<\/nav>', 'IgnoreCase')
    $newContent = $regex.Replace($content, $navReplacement)
    
    if ($newContent -ne $content) {
        # Write back as UTF-8 without BOM using .NET IO class
        [System.IO.File]::WriteAllText($filePath, $newContent, (New-Object System.Text.UTF8Encoding $False))
        Write-Host "Updated $filePath"
        $filesModified++
    }
}

Write-Host "Done. Modified $filesModified files."
