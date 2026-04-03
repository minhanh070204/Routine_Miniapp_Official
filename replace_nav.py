import os
import re

nav_replacement = """<nav class="fixed bottom-0 w-full flex justify-around items-center px-4 py-3 pb-safe bg-[#F9F9F9]/90 dark:bg-neutral-900/90 backdrop-blur-xl border-t-[0.5px] border-[#222222]/10 z-50">
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
</nav>"""

base_dir = r"c:\Users\Le Minh Anh\Downloads\stitch_duplicate_of_t_ch_i_m_n_s_n\stitch_duplicate_of_t_ch_i_m_n_s_n"

files_modified = 0

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f == "code.html":
            file_path = os.path.join(root, f)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # The bottom nav often has 'bottom-0' inside its class
            # Let's find the nav tag that contains 'bottom-0' and replace it including its matching closing tag
            
            # A regex that matches <nav ... bottom-0 ... > ... </nav>
            # (Dotall makes . match newlines)
            new_content = re.sub(
                r'<nav[^>]*bottom-0[^>]*>.*?</nav>', 
                nav_replacement, 
                content, 
                flags=re.DOTALL
            )
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Updated {file_path}")
                files_modified += 1

print(f"Done. Modified {files_modified} files.")
