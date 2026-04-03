import os
import re

count_doctype = 0
count_style = 0

style_block = '''
<style>
    /* Absolute perfect centering for the Routine logo */
    nav, header { position: relative; }
    nav img[alt="ROUTINE"], header img[alt="ROUTINE"] {
        position: absolute !important;
        left: 50% !important;
        top: 50% !important;
        transform: translate(-50%, -50%) !important;
        margin: 0 !important;
        max-height: 20px !important;
        z-index: 10 !important;
    }
    nav a:has(img[alt="ROUTINE"]), header a:has(img[alt="ROUTINE"]) {
        position: static !important;
        display: block !important;
        flex-grow: 0 !important;
    }
</style>
'''

for root, dirs, files in os.walk('.'):
    for f in files:
        if f == 'code.html':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            original_content = content
            
            # 1. Fix DOCTYPE
            if '!DOCTYPE html>' in content:
                content = content.replace('!DOCTYPE html>', '<!DOCTYPE html>')
            
            # 2. Inject Style for centering
            if '/* Absolute perfect centering' not in content:
                content = content.replace('</head>', style_block + '</head>')
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as wfile:
                    wfile.write(content)
                count_doctype += 1

print(f"Fixed DOCTYPE and injected CSS in {count_doctype} files.")