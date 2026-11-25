# Báo cáo cá nhân — TranPhamMinhSon-2A202603802

## 1. Thông tin thành viên

- Họ tên: Trần Phạm Minh Sơn
- MSSV: 2A202603802
- Email: sontpmit@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code (nửa đầu: Nhiệm vụ A, B) & thiết kế danh sách event (Nhiệm vụ E1)

## 2. Phần việc phụ trách

- Thiết lập nhánh `sontpm` và chạy kiểm tra code cho phần đầu của nhóm.
- Viết code cho Nhiệm vụ A (A1, A2, A3, A4) và Nhiệm vụ B (B1, B2, B3, B4) trong `src/lab13.py` trước khi bàn giao cho Thành viên 2 tiếp quản Nhiệm vụ D.
- Xây dựng danh sách event có `trace_id` và kiểm tra chéo với các chỉ số E1 trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt 3/3 phép thử bắt buộc (1,20 · 1,25 · 1,25).
- Viết hàm `mo_hinh(runs, reqs, ...)` cho A2 và gọi lại cho A3 (tách theo `noi_dia`, `hang_nang`, `quoc_te`, `doi_tac` kèm tỉ lệ `status == 'ok'` theo từng lần thử `attempt`) và A4 (cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` ở mức 45.000 và 22.500 yêu cầu/tháng).
- Viết hàm `in_nhiem_vu_b` tính 9 kịch bản độ nhạy B1, cặp kết hợp B2 (`gia_vao=52, gia_ra=260, he_so_xem_lai=2.0`), so sánh giới hạn 1–3 lần chạy cả hệ thống B3, và kịch bản xem lại 100% ở cả 2 mức thời gian làm lại (9 phút và 15,3 phút/ca) kèm mức hoà vốn B4.
- Điền bảng 10 event có `trace_id` và phần kiểm tra chéo event ↔ chỉ số vào `report/team/chi_so.md`.

## 4. Bằng chứng

- File code: `src/lab13.py` (đã chạy trên `src/logix_runs.csv` và `src/logix_requests.csv` với `keep_default_na=False`).
- Kết quả chạy `python lab13.py` trong `src/`:
  - `Ba phép thử đáp án biết trước: ĐẠT`
  - A2: `token = 245.585 đ`, `tool = 84.000 đ`, `chay_lai = 93.804 đ`, `xem_lai = 1.780.000 đ` [simulated], `lam_lai = 2.264.000 đ` [simulated], `tong = 4.373.585 đ` [simulated], `thanh_cong = 978`, `cps = 4.472 đ` [simulated] (gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu).
  - A3: `noi_dia = 2.696 đ` (0,22×), `hang_nang = 8.221 đ` (0,69×), `quoc_te = 22.515 đ` (1,88×), `doi_tac = 10.215 đ` (0,85×) [simulated].
  - A4: 45.000 yc/tháng → `4.599 đ` (0,38×); 22.500 yc/tháng → `5.784 đ` (0,48×) [simulated].
  - B3: giới hạn 2 lần chạy cho chi phí cả hệ thống thấp nhất `6.901.220 đ` [simulated] (so với `7.449.781 đ` ở 1 lần và `7.037.585 đ` ở 3 lần).
  - B4: xem lại 100% ra `11.743 đ` (0,98×) với 9 phút/ca và `12.415 đ` (1,03×) với 15,3 phút/ca [simulated].
- File hồ sơ đã cập nhật: `report/team/chi_so.md` (mục `Danh sách event` và `Kiểm tra chéo`).

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để hỗ trợ viết code Python theo cấu trúc sẵn có trong `src/lab13.py` và rà soát cấu trúc event theo `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Tự kiểm tra bằng cách chạy trực tiếp `python lab13.py` trong `src/` xác nhận 3 phép thử A1 in `ĐẠT`, đối chiếu từng bảng số A2–A4 và B1–B4 với công thức trong `docs/du_lieu_va_cong_thuc.md`, và kiểm tra chéo các event với từng chỉ số E1.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần code A, B, phần event trong `chi_so.md` và báo cáo cá nhân.