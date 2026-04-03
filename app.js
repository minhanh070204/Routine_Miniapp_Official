(function () {
    // Nav Icons Mapping
    var iconRoutes = {
        'home':           '../trang_ch_m_u_m_i/code.html',
        'home_app_logo':  '../trang_ch_m_u_m_i/code.html',
        'grid_view':      '../k_t_qu_t_m_ki_m_flat_lay/code.html',
        'search':         '../k_t_qu_t_m_ki_m_flat_lay/code.html',
        'shopping_bag':   '../gi_h_ng_m_u_m_i/code.html',
        'shopping_cart':  '../gi_h_ng_m_u_m_i/code.html',
        'style':          '../gi_h_ng_m_u_m_i/code.html',
        'person':         '../trung_t_m_th_nh_vi_n_s_ch_s_c_p_nh_t/code.html',  // Màn 1: Dashboard thành viên
        'favorite':       '../s_n_ph_m_y_u_th_ch_n_n_tr_ng/code.html',
        'favorite_border':'../s_n_ph_m_y_u_th_ch_n_n_tr_ng/code.html',
        'local_activity': '../u_i_c_a_t_i_n_n_tr_ng/code.html',
        'arrow_back':     'BACK',
        'chevron_left':   'BACK',
        'close':          'BACK'
    };

    // Text mapping
    var textRoutes = [
        // =========== NEW MEMBERSHIP FLOW ===========
        // 1. Màn 1 -> "membership circle" -> Màn Chào mừng (ng_k_th_nh_c_ng_n_n_tr_ng)
        { snippet: 'membership circle', url: '../ng_k_th_nh_c_ng_n_n_tr_ng/code.html' },
        
        // 2. Màn 2 -> "xác nhận đăng ký" -> Màn 3 (ng_k_th_nh_c_ng_n_n_tr_ng)
        { snippet: 'xac nhan dang ky',  url: '../ng_k_th_nh_c_ng_n_n_tr_ng/code.html' },
        
        // 3. Màn 3 -> "bắt đầu mua sắm" -> Về Trang Chủ (trang_ch_m_u_m_i)
        { snippet: 'bat dau mua sam',   url: '../trang_ch_m_u_m_i/code.html' },
        
        // 4. Màn 3 -> "xem trang thành viên" -> Màn 4 (u_i_c_a_t_i_n_n_tr_ng)
        { snippet: 'xem trang thanh vien', url: '../u_i_c_a_t_i_n_n_tr_ng/code.html' },
        
        // 5. Màn 1 -> "lịch sử điểm" -> Màn 5 (l_ch_s_t_ch_i_m_c_p_nh_t_menu)
        { snippet: 'lich su diem',      url: '../l_ch_s_t_ch_i_m_c_p_nh_t_menu/code.html' },
        
        // 6. Màn 1 -> "ưu đãi của tôi" -> Màn 4 (u_i_c_a_t_i_n_n_tr_ng)
        { snippet: 'uu dai cua toi',    url: '../u_i_c_a_t_i_n_n_tr_ng/code.html' },
        
        // 7. Màn 1 -> "tích điểm đơn sàn" -> Màn có chữ "Tích điểm sàn" (t_ch_i_m_n_s_n_c_p_nh_t)
        { snippet: 'tich diem don san', url: '../t_ch_i_m_n_s_n_c_p_nh_t/code.html' },
        
        // 8. Màn Ưu Đãi -> "Dùng mã" -> Màn Trang chủ (trang_ch_m_u_m_i)
        { snippet: 'dung ma',           url: '../trang_ch_m_u_m_i/code.html' },


        // =========== EXISTING SALES FLOW ===========
        // Chào mừng -> Lấy voucher
        { snippet: 'lay voucher ngay',  url: '../ch_c_m_ng_nh_n_voucher_1/code.html' },
        
        // Voucher -> Trang chủ
        { snippet: 'mua hang ngay',     url: '../trang_ch_m_u_m_i/code.html' },
        { snippet: 'tiep tuc mua sam',  url: '../trang_ch_m_u_m_i/code.html' },
        { snippet: 'kham pha cua hang', url: '../trang_ch_m_u_m_i/code.html' },
        
        // Trang chủ -> Danh mục
        { snippet: 'kham pha ngay',     url: '../k_t_qu_t_m_ki_m_flat_lay/code.html' },
        { snippet: 'xem them san pham', url: '../k_t_qu_t_m_ki_m_flat_lay/code.html' },
        
        // Chi tiết SP -> Giỏ hàng
        { snippet: 'them vao',          url: '../gi_h_ng_m_u_m_i/code.html' },
        
        // Giỏ hàng -> Checkout Success
        { snippet: 'dat hang',          url: '../t_h_ng_th_nh_c_ng_n_n_tr_ng/code.html' },
        { snippet: 'thanh toan',        url: '../t_h_ng_th_nh_c_ng_n_n_tr_ng/code.html' }, 
        
        // Checkout Success -> Xem Chi Tiết
        { snippet: 'xem chi tiet',      url: '../chi_ti_t_n_h_ng_rt9921/code.html' },
        { snippet: 'xem don hang',      url: '../chi_ti_t_n_h_ng_rt9921/code.html' },
        
        // Khác
        { snippet: 'xem voucher',       url: '../ch_c_m_ng_nh_n_voucher_1/code.html' },
        { snippet: 'dang ky',           url: '../ng_k_th_nh_vi_n/code.html' },
        { snippet: 'ap dung',           url: '../ch_n_m_gi_m_gi/code.html' },
        { snippet: 'chon ma',           url: '../ch_n_m_gi_m_gi/code.html' }
    ];

    function removeAccents(str) {
        return str
            .replace(/[àáạảãâầấậẩẫăằắặẳẵ]/g, 'a')
            .replace(/[èéẹẻẽêềếệểễ]/g, 'e')
            .replace(/[ìíịỉĩ]/g, 'i')
            .replace(/[òóọỏõôồốộổỗơờớợởỡ]/g, 'o')
            .replace(/[ùúụủũưừứựửữ]/g, 'u')
            .replace(/[ỳýỵỷỹ]/g, 'y')
            .replace(/[đ]/g, 'd')
            .replace(/[ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴ]/g, 'a')
            .replace(/[ÈÉẸẺẼÊỀẾỆỂỄ]/g, 'e')
            .replace(/[ÌÍỊỈĨ]/g, 'i')
            .replace(/[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]/g, 'o')
            .replace(/[ÙÚỤỦŨƯỪỨỰỬỮ]/g, 'u')
            .replace(/[ỲÝỴỶỸ]/g, 'y')
            .replace(/[Đ]/g, 'd');
    }

    function findIcon(el) {
        if (!el) return null;
        var icon = el.getAttribute('data-icon');
        if (icon) return icon;
        var iconEl = el.querySelector('.material-symbols-outlined');
        if (iconEl && iconEl.textContent) return iconEl.textContent.trim();
        return null;
    }

    document.addEventListener('click', function (e) {
        var target = e.target;

        // ── 1. CLICK PRODUCT IMAGE / ITEMS ──
        var gridItem = target.closest('[class*="aspect-[3/4]"], [class*="aspect-square"], [class*="aspect-[4/5]"]');
        var isImgOrWithinImg = target.tagName === 'IMG' || !!target.closest('img');
        if (isImgOrWithinImg && !!gridItem) {
            var url = window.location.href;
            if (url.indexOf('k_t_qu_t_m_ki_m_flat_lay') > -1 || url.indexOf('trang_ch_m_u_m_i') > -1) {
                e.preventDefault();
                var img = gridItem.querySelector('img');
                if (img && img.src) {
                    localStorage.setItem('selectedProductImg', img.src);
                }
                window.location.href = '../chi_ti_t_s_n_ph_m_c_p_nh_t_m_u_n_n/code.html';
                return;
            }
        }

        // ── 2. FIND CLICKABLE ELEMENT ──
        var el = target;
        for (var i = 0; i < 6; i++) {
            if (!el || el === document.documentElement) break;
            if (el.tagName === 'A' || el.tagName === 'BUTTON' || 
               (el.tagName === 'DIV' && el.querySelector('.material-symbols-outlined') && el.closest('nav')) || 
               (el.tagName === 'DIV' && el.classList && el.classList.contains('flex') && el.closest('.space-y-4')) ||
               (el.tagName === 'DIV' && el.classList && el.classList.contains('cursor-pointer'))) break;
            el = el.parentElement;
        }
        
        // Treat generic div rows inside menus as clickable too
        if (!el || (el.tagName !== 'A' && el.tagName !== 'BUTTON' && el.tagName !== 'DIV')) return;

        // ── 3. NAV ICON ROUTING ──
        var icon = findIcon(el);
        if (icon && iconRoutes[icon]) {
            e.preventDefault();
            var dest = iconRoutes[icon];
            if (dest === 'BACK') { window.history.back(); }
            else { window.location.href = dest; }
            return;
        }

        // Ignore native anchor links with actual hrefs
        var href = el.getAttribute('href');
        if (el.tagName === 'A' && href && href !== '#' && href !== '') {
            return;
        }

        // ── 4. TEXT MAPPING ROUTING ──
        var rawText = (el.innerText || el.textContent || '').trim();
        var text = removeAccents(rawText).toLowerCase();
        
        for (var j = 0; j < textRoutes.length; j++) {
            var rule = textRoutes[j];
            if (text.indexOf(rule.snippet) !== -1) {
                e.preventDefault();
                window.location.href = rule.url;
                return;
            }
        }
    });

    // Make clickable lists cursor pointer
    setTimeout(function() {
        var clickableItems = document.querySelectorAll('[class*="aspect-["] img, [class*="aspect-square"] img');
        for (var k = 0; k < clickableItems.length; k++) {
            clickableItems[k].style.cursor = 'pointer';
        }
        
        // Add pointer cursor to central hub menu items
        var menuItems = document.querySelectorAll('.bg-surface-container-low, .bg-white.rounded-xl');
        for (var m = 0; m < menuItems.length; m++) {
            if(menuItems[m].innerText && menuItems[m].innerText.length > 5) {
                menuItems[m].style.cursor = 'pointer';
            }
        }
    }, 500);

    // ── 5. DYNAMIC PRODUCT IMAGE REPLACEMENT ──
    if (window.location.href.indexOf('chi_ti_t_s_n_ph_m_c_p_nh_t_m_u_n_n') > -1) {
        var savedImgUrl = localStorage.getItem('selectedProductImg');
        if (savedImgUrl) {
            var mainImg = document.querySelector('img[alt="Textured Merino Wool Polo"]');
            var zoomImg = document.querySelector('img[alt="Macro Texture Detail"]');
            if (mainImg) mainImg.src = savedImgUrl;
            if (zoomImg) zoomImg.src = savedImgUrl;

            var secondaryImagesCode = document.querySelector('.grid.grid-cols-2.gap-4');
            if (secondaryImagesCode) {
                if (savedImgUrl.indexOf('10f24kniw003-pink-cream') === -1) {
                    secondaryImagesCode.style.display = 'none';
                } else {
                    secondaryImagesCode.style.display = 'grid';
                }
            }
        }
    }
})();
