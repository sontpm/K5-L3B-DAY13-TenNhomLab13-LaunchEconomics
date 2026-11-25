"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=float(tien_token.sum()),
        tool=float(tien_tool.sum()),
        chay_lai=float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
        xem_lai=float(xem_lai),
        lam_lai=float(lam_lai),
        tong=float(tong),
        thanh_cong=thanh_cong,
        cps=float(tong / thanh_cong),
        hoa_don_moi_yc=float((tien_token.sum() + tien_tool.sum()) / len(reqs)),
    )


def in_nhiem_vu_a(runs, reqs, ket_qua):
    """In kết quả chi tiết Nhiệm vụ A2, A3, A4."""
    print('\n=== A2 · Tóm tắt bổ sung ===')
    print(f"Hoá đơn mỗi yêu cầu: {ket_qua['hoa_don_moi_yc']:,.1f} đ")
    print(f"Tỉ lệ CPS / hoá đơn: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    print(f"Tỉ trọng xem lại [simulated]: {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}%")
    print(f"Tỉ trọng làm lại [simulated]: {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}%")
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f"Chi phí cả hệ thống / yêu cầu [simulated]: {he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}x)")

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        so_yc = len(sub)
        ti_le_tc = kq['thanh_cong'] / so_yc * 100
        lan_chay_tb = sub['so_lan_chay'].mean()
        print(
            f"{loai:10s} | yc={so_yc:4d} | tc={ti_le_tc:5.1f}% | "
            f"chay={lan_chay_tb:4.2f} | cps[sim]={kq['cps']:8,.0f} đ | "
            f"{kq['cps'] / BASELINE:4.2f}x"
        )

    print('\nTỉ lệ status == ok theo loại và lần thử:')
    ok_pivot = (
        runs.assign(ok=(runs['status'] == 'ok').astype(float))
        .merge(reqs[['request_id', 'loai']], on='request_id')
        .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    )
    print((ok_pivot * 100).round(1))

    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ti_le_tc_mau = kq_pv['thanh_cong'] / len(reqs)
    co_dinh_thang = 40_000_000
    for ten, kl in [('45.000 yc/tháng', 45_000), ('Một nửa (22.500)', 22_500)]:
        viec_tc = kl * ti_le_tc_mau
        co_dinh_moi_viec = co_dinh_thang / viec_tc
        tong_cps = kq_pv['cps'] + co_dinh_moi_viec
        print(
            f"{ten:20s} | tc/tháng={viec_tc:7,.0f} | co_dinh={co_dinh_moi_viec:6,.0f} đ | "
            f"cps+cd[sim]={tong_cps:6,.0f} đ ({tong_cps / BASELINE:.2f}x)"
        )
    return pham_vi, kq_pv


def in_nhiem_vu_b(runs, reqs, goc_cps, pham_vi, kq_pv):
    """In kết quả Nhiệm vụ B1, B2, B3, B4."""
    print('\n=== B1 · Độ nhạy từng yếu tố [simulated] ===')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2.0),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2.0),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"{ten:26s} | {cps:8,.0f} đ | {(cps / goc_cps - 1) * 100:+6.1f}%")

    print('\n=== B2 · Đổi một cặp & xếp hạng [simulated] ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f"Token x2 + Xem lại x2: {cps_cap:,.0f} đ ({(cps_cap / goc_cps - 1) * 100:+.1f}%)")

    print('\n=== B3 · Giới hạn chạy lại & chi phí cả hệ thống [simulated] ===')
    for k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq_k['thanh_cong']
        ca_he_thong = kq_k['tong'] + BASELINE * khong_tc
        print(
            f"{k} lần | trợ lý={kq_k['tong']:10,.0f} đ | không_tc={khong_tc:3d} | "
            f"cả hệ thống={ca_he_thong:10,.0f} đ | cps={kq_k['cps']:6,.0f} đ"
        )

    print('\n=== B4 · Xem lại 100% phạm vi noi_dia + hang_nang [simulated] ===')
    pv_runs = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_yc_co_ok = pv_runs.loc[pv_runs['status'] == 'ok', 'request_id'].nunique()
    so_ca_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    tien_token_tool_pv = kq_pv['token'] + kq_pv['tool']
    tien_xem_lai_100 = so_yc_co_ok * 5 * LUONG_PHUT
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for nhan, phut_ll in [('9 phút/ca (đề bài)', 9.0), (f'{phut_lam_lai_tb:.1f} phút/ca (dữ liệu)', phut_lam_lai_tb)]:
        tien_ll = so_ca_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = tien_token_tool_pv + tien_xem_lai_100 + tien_ll
        cps_b4 = tong_b4 / kq_pv['thanh_cong']
        hoa_von_phut = (BASELINE * kq_pv['thanh_cong'] - tien_token_tool_pv - tien_ll) / (so_yc_co_ok * LUONG_PHUT)
        print(
            f"{nhan:28s} | tổng={tong_b4:10,.0f} đ | cps={cps_b4:7,.0f} đ ({cps_b4 / BASELINE:.2f}x) | "
            f"hoà vốn <= {hoa_von_phut:.1f} phút"
        )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    pham_vi, kq_pv = in_nhiem_vu_a(runs, reqs, ket_qua)
    in_nhiem_vu_b(runs, reqs, ket_qua['cps'], pham_vi, kq_pv)
    # TODO CP4 · Nhiệm vụ D (Thành viên 2 tiếp quản sau giải lao): cỡ mẫu & tỉ lệ mở lại.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
