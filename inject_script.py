import re
import codecs

path = 'k_t_qu_t_m_ki_m_flat_lay/code.html'
with codecs.open(path, 'r', 'utf-8') as f:
    html = f.read()

# Remove the broken script
html = re.sub(r'<script>\s*document\.addEventListener\(''DOMContentLoaded'', \(\) => \{\s*// 1\. Make all cards clickable.*?</script>\r?\n', '', html, flags=re.DOTALL)

js_content = """<script>
document.addEventListener('DOMContentLoaded', () => {
    // 1. Make all cards clickable
    const setupCards = () => {
        document.querySelectorAll('.group.cursor-pointer').forEach(card => {
            if(card.dataset.clickableSet) return;
            card.dataset.clickableSet = 'true';
            
            // Prevent the add to cart button from triggering the card click
            const addToCartBtn = card.querySelector('a[href*="gi_h_ng"]');
            if(addToCartBtn) {
                addToCartBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                });
            }

            card.addEventListener('click', () => {
                const img = card.querySelector('img');
                const title = card.querySelector('h3');
                const priceMatch = card.querySelector('p.font-bold');
                
                if(img && title && priceMatch) {
                    const params = new URLSearchParams();
                    params.set('img', img.src);
                    params.set('name', title.textContent.trim());
                    params.set('price', priceMatch.textContent.trim());
                    
                    window.location.href = '../chi_ti_t_s_n_ph_m_c_p_nh_t_m_u_n_n/code.html?' + params.toString();
                }
            });
        });
    };
    setupCards();

    // 2. Load more 7 items
    const newItemsData = [
        { img: 'https://media.routine.vn/1200x1500/prod/media/10s25shs016-m-blue-ao-so-mi-nam-1-jpg-8og0.webp', name: 'Áo Sơ Mi Nam Tay Ngắn', price: '400.000₫' },
        { img: 'https://media.routine.vn/1200x1500/prod/product/10s25tss007-americano-1-jpg-u0zk.webp', name: 'Áo Thun Nam Cổ Tròn', price: '250.000₫' },
        { img: 'https://media.routine.vn/1200x1500/prod/variant/10s26ttow001-black-1-jpg-7iic.webp', name: 'Áo Ba Lỗ Nam Đen', price: '150.000₫' },
        { img: 'https://media.routine.vn/1200x1500/prod/variant/10f25kniw058-white-1-jpg-80ws.webp', name: 'Áo Len Nữ Trắng', price: '550.000₫' },
        { img: 'https://media.routine.vn/1200x1500/prod/variant/10s26dpsw014-beige-4-jpg-rely.webp', name: 'Váy Nữ Beige Dáng Dài', price: '850.000₫' },
        { img: 'https://media.routine.vn/1200x1500/prod/variant/10f25skiw020-white-3-jpg-u6ze.webp', name: 'Chân Váy Trắng Xếp Ly', price: '650.000₫' },
        { img: 'https://media.routine.vn/1200x1500/prod/variant/10f25dpaw041-mindigo-1-jpg-cdgi.webp', name: 'Quần Nữ Xanh Indigo', price: '700.000₫' }
    ];

    const loadMoreBtn = document.querySelector('button.mt-4.px-10');
    if(loadMoreBtn) {
        loadMoreBtn.addEventListener('click', () => {
            const grid = document.querySelector('.grid.grid-cols-2');
            
            newItemsData.forEach(data => {
                const div = document.createElement('div');
                div.className = 'group cursor-pointer hidden transition-opacity duration-500 opacity-0';
                div.innerHTML = `
<div class="relative aspect-[3/4] overflow-hidden rounded-[14px] product-card-shadow bg-surface-container-lowest">
<img alt="New Product" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="${data.img}">
</div>
<div class="mt-4 px-1">
<h3 class="text-on-surface font-medium text-sm leading-tight group-hover:underline underline-offset-4 decoration-1 mt-2">${data.name}</h3>
<div class="flex items-center justify-between mt-1">
<p class="text-on-surface font-bold text-sm">${data.price}</p>
<a class="min-w-6 min-h-6 w-6 h-6 rounded-full bg-[#222222] flex flex-col items-center justify-center text-white hover:opacity-80 transition-opacity" href="../gi_h_ng_m_u_m_i/code.html">
<span class="material-symbols-outlined text-[14px] leading-none" style="font-variation-settings: 'wght' 500;">add</span>
</a>
</div>
</div>
                `;
                grid.appendChild(div);
                
                // Fade in animation
                requestAnimationFrame(() => {
                    div.classList.remove('hidden');
                    requestAnimationFrame(() => {
                        div.classList.remove('opacity-0');
                    });
                });
            });

            setupCards();

            const counterText = document.querySelector('p.text-on-surface-variant');
            if(counterText && counterText.textContent.includes('Bạn đang xem')) {
                counterText.textContent = 'Bạn đang xem 13 cua 124 san pham'.replace(/cua 124 san pham/, 'của 124 sản phẩm');
            }
            
            loadMoreBtn.style.display = 'none';
        });
    }
});
</script>
</body>"""

html = html.replace('</body>', js_content)

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(html)
print('Done injecting JS')
