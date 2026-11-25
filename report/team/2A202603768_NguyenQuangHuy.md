# Báo cáo cá nhân - Nguyễn Quang Huy-2A202603768

## 1. Thông tin thành viên

- Họ tên: Nguyễn Quang Huy
- MSSV: 2A202603768
- Email: 26ai.huynq13@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số (A, B) → Người viết code (nửa sau: D, E1)

## 2. Phần việc phụ trách

- Thiết lập môi trường `.venv` trên máy thứ hai để chạy kiểm chứng toàn bộ `src/lab13.py`.
- Tính tay đối chiếu A1, A4, B3, B4 và điền đầy đủ các bảng số liệu A1–A4, B1–B4 vào `report/team/bang_chi_phi.md`.
- Tiếp quản `src/lab13.py` viết code phần D (5 câu cỡ mẫu D1, power ở MDE 6 điểm, tỉ lệ `mo_lai_trong_7_ngay` hiện tại) và phần E1 (tính thử 3 chỉ số Chính, Dùng, An toàn).
- Điền kết quả 3 chỉ số E1 vào bảng đầu `report/team/chi_so.md` và cùng nhóm tham gia duyệt chéo Gate 2a (`report/team/phieu_cham.md`).

## 3. Đóng góp cụ thể

- Đối chiếu bằng tay các công thức A1 (1,20 · 1,25 · 1,25), A4 (cố định 40 triệu đ/tháng: 4.599 đ và 5.784 đ [simulated]), B3 (chi phí cả hệ thống 1–3 lần chạy: 7.449.781 · 6.901.220 · 7.037.585 đ [simulated]) và B4 (xem lại 100% ở 9 phút/ca: 11.743 đ = 0,98× và 15,3 phút/ca: 12.415 đ = 1,03× [simulated]).
- Hoàn thiện toàn bộ bảng số A1–A4 và B1–B4 có gắn nhãn `simulated` trong `report/team/bang_chi_phi.md`.
- Viết hàm `co_mau`, `in_nhiem_vu_d` (sử dụng `NormalDist` và `statsmodels` `NormalIndPower` / `proportion_effectsize`) và `in_nhiem_vu_e1` trong `src/lab13.py`.
- Cập nhật 3 con số tính thử vào bảng E1 của `report/team/chi_so.md` (giữ đúng cách diễn đạt "chỉ số trong đợt chạy thử là...").

## 4. Bằng chứng

- File code: `src/lab13.py` chạy trọn vẹn từ đầu đến cuối trên máy thứ hai (`Ba phép thử đáp án biết trước: ĐẠT`).
- Kết quả chạy phần D và E1:
  - D1: a) `1.251`/nhóm; b) `DE = 2,48`, `n = 3.103`/nhóm → `42` NV/nhóm (tổng 84 > 40, không đủ người); c) 20 NV/nhóm tối đa `1.000` < 1.251; d) 6 depot/nhóm tối đa `300`; e) MDE +6 điểm cần `859`/nhóm → `m ≥ 299` yc/người (`DE = 6,96`).
  - Power khi chọn MDE 6 điểm (`n = 859`) nếu tác động thật là 5 điểm: `0,64`.
  - Tỉ lệ `mo_lai_trong_7_ngay` hiện tại: `4,25%` (51/1.200) toàn mẫu và `3,97%` (39/982) trong phạm vi `noi_dia` + `hang_nang`.
  - E1 trên 1.200 yêu cầu: Chính `82,83%` (994/1.200), Dùng `27,12%` (48/177), An toàn `4,25%` (51/1.200).
- Các file hồ sơ đã cập nhật: `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `TEAM.md`.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để hướng dẫn quy trình làm bài, rà soát công thức cỡ mẫu cụm và cấu trúc code Python theo `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Tự kiểm tra bằng cách tính tay đối chiếu A1, A4, B3, B4, D1(e), chạy trực tiếp `python lab13.py` trong `src/` trên máy thứ hai và kiểm tra nhãn `simulated` cũng như không dùng từ cấm trong các file báo cáo.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần kiểm số A–B, code D–E1, cập nhật `bang_chi_phi.md`, `chi_so.md`, `TEAM.md` và báo cáo cá nhân; sẵn sàng bàn giao số D1 cho Thành viên 3 hoàn thiện `pilot_plan.yaml`.