import os
import re

root_dir = r"c:\Users\Le Minh Anh\Downloads\stitch_duplicate_of_t_ch_i_m_n_s_n\stitch_duplicate_of_t_ch_i_m_n_s_n"

style_block = """
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
"""

logo_tag = '<img src="https://media.routine.vn/0x0/prod/media/52ba65a3-e085-45a6-bf5e-fb9c359abff7.webp" alt="ROUTINE" class="h-4 sm:h-5 object-contain" />'

header_rx = re.compile(r'(<header[^>]*>|<nav[^>]*top-0[^>]*>)(.*?)(</header>|</nav>)', re.DOTALL | re.IGNORECASE)

for subdir, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(subdir, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            modified = False
            
            # 1. Round buttons
            if '/* Styling according to user requirement */' not in content:
                content = content.replace('</head>', style_block)
                modified = True
                
            # 2. Add Routine logo
            match = header_rx.search(content)
            if match:
                inner_content = match.group(2)
                # Replace h1 or img with logo
                if '<h1' in inner_content:
                    new_inner = re.sub(r'<h1[^>]*>.*?</h1>', logo_tag, inner_content, flags=re.DOTALL)
                else:
                    new_inner = inner_content

                if new_inner == inner_content:
                    new_inner = re.sub(r'<img[^>]*alt="ROUTINE[^>]*>', logo_tag, inner_content)
                
                # If there's no h1 or known img, inject directly to the center
                if new_inner == inner_content:
                    # Let's see if we can find a div central
                    pass

                if new_inner != inner_content:
                    # Replace only the first occurrence
                    new_header = match.group(1) + new_inner + match.group(3)
                    content = content[:match.start()] + new_header + content[match.end():]
                    modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated {filepath}")
