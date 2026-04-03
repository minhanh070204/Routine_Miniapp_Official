import os

base_dir = r"c:\Users\Le Minh Anh\Downloads\stitch_duplicate_of_t_ch_i_m_n_s_n\stitch_duplicate_of_t_ch_i_m_n_s_n"

app_js_content = """
document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('click', (e) => {
        let el = e.target.closest('a, button, [class*="cursor-pointer"], .product-card');
        
        // Product image
        if (!el && e.target.tagName === 'IMG' && e.target.closest('.aspect-\\\\[3\\\\/4\\\\]')) {
            el = e.target;
        }
        
        if (!el) return;

        let href = el.getAttribute('href');
        if (el.tagName === 'A' && href && href !== '#' && href.endsWith('.html')) {
            return; // Native navigation
        }

        e.preventDefault();

        let text = (el.innerText || '').trim().toLowerCase();
        let icon = el.getAttribute('data-icon') || 
                   (el.querySelector('[data-icon]') ? el.querySelector('[data-icon]').getAttribute('data-icon') : null);

        let target = null;
        
        // Back navigation
        if (icon === 'arrow_back' || icon === 'chevron_left' || text === 'quay lại' || text === 'trở lại') {
            window.history.back();
            return;
        }

        // Bottom Nav
        if (icon === 'home' || text === 'trang chủ') target = 'trang_ch_m_u_m_i';
        else if (icon === 'grid_view' || text === 'danh mục') target = 'k_t_qu_t_m_ki_m_flat_lay'; 
        else if (icon === 'shopping_bag' || text === 'giỏ hàng') target = 'gi_h_ng_m_u_m_i';
        else if ((icon === 'person' || text === 'thành viên') && !text.includes('đăng ký')) target = 'trung_t_m_th_nh_vi_n_s_ch_s_c_p_nh_t';
        
        // Top Nav Icons
        else if (icon === 'search') target = 'k_t_qu_t_m_ki_m_flat_lay';
        else if (icon === 'favorite' || icon === 'favorite_border') target = 's_n_ph_m_y_u_th_ch_n_n_tr_ng';

        // Order & Checkout
        else if (text.includes('thanh toán') || text.includes('mua ngay')) target = 'x_c_nh_n_i_n_th_ng_tin_shopee';
        else if (text.includes('xác nhận trên shopee') || text.includes('xác nhận') && window.location.href.includes('x_c_nh_n')) target = 'h_ng_d_n_l_y_m_shopee_c_p_nh_t_icon';
        else if (text.includes('lấy mã shopee') || text.includes('đóng')) target = 't_h_ng_th_nh_c_ng_n_n_tr_ng';
        else if (text.includes('đặt hàng')) target = 't_h_ng_th_nh_c_ng_n_n_tr_ng';
        else if (text.includes('xem đơn hàng')) target = 'chi_ti_t_n_h_ng_rt9921';
        else if (text.includes('lịch sử mua hàng') || text.includes('tra cứu đơn hàng') || text === 'đơn hàng') target = 'tra_c_u_n_h_ng_r_t_g_n';
        
        // Promotions & Voucher
        else if (text.includes('áp dụng') || text.includes('chọn mã') || text.includes('mã giảm') || text.includes('khuyến mãi')) target = 'ch_n_m_gi_m_gi';
        else if (text.includes('nhận voucher') || text.includes('lưu voucher') || text === 'lưu') target = 'nh_n_voucher_th_nh_c_ng';
        else if (text.includes('xem voucher')) target = 'ch_c_m_ng_nh_n_voucher_1';
        else if (icon === 'local_activity' || text.includes('ưu đãi') || text.includes('voucher của tôi')) target = 'u_i_c_a_t_i_n_n_tr_ng';
        
        // Member & Points
        else if (text.includes('lịch sử') && text.includes('điểm')) target = 'l_ch_s_t_ch_i_m_c_p_nh_t_menu';
        else if (text.includes('điểm') || text.includes('cấp bậc')) target = 't_ch_i_m_n_s_n_c_p_nh_t';
        else if (text.includes('hoàn tất đăng ký') || text.includes('xác nhận đăng ký')) target = 'ng_k_th_nh_c_ng_n_n_tr_ng';
        else if (text.includes('đăng ký')) target = 'ng_k_th_nh_vi_n';
        
        // Products
        else if (el.tagName === 'IMG' || text.includes('chi tiết') || text.includes('thêm vào giỏ') || el.closest('.aspect-\\\\[3\\\\/4\\\\]')) target = 'chi_ti_t_s_n_ph_m_c_p_nh_t_m_u_n_n';

        if (target) {
            window.location.href = `../${target}/code.html`;
        } else if (href && href !== '#') {
            window.location.href = href;
        }
    });

    // Add pointer cursor to all clickable elements that look like buttons
    document.querySelectorAll('.aspect-\\\\[3\\\\/4\\\\] img, .product-card').forEach(el => {
        el.style.cursor = 'pointer';
    });
});
"""

with open(os.path.join(base_dir, "app.js"), "w", encoding="utf-8") as f:
    f.write(app_js_content)

for dname in os.listdir(base_dir):
    dpath = os.path.join(base_dir, dname)
    if os.path.isdir(dpath):
        cpath = os.path.join(dpath, "code.html")
        if os.path.isfile(cpath):
            with open(cpath, "r", encoding="utf-8") as f:
                content = f.read()
            if '<script src="../app.js"></script>' not in content:
                content = content.replace("</body>", '<script src="../app.js"></script>\n</body>')
                with open(cpath, "w", encoding="utf-8") as f:
                    f.write(content)
print("Injecting links successful.")
