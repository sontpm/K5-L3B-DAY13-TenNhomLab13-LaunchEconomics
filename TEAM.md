# Team

## Thông tin nhóm

- Tên nhóm: TenNhomLab13
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-TenNhomLab13-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics` (nhánh đang phát triển phần TV1: `sontpm`)

## Thành viên

|  STT | Họ tên                 | MSSV        | Email                       | GitHub               | Vai trò                                                 |
| ---: | ---------------------- | ----------- | --------------------------- | -------------------- | ------------------------------------------------------- |
|    1 | Trần Phạm Minh Sơn     | 2A202603802 | 26ai.sontpm@vinuni.edu.vn   | sontpm               | Người viết code (nửa đầu: A, B) & Event (E1)            |
|    2 | Nguyễn Quang Huy       | 2A202603768 | 26ai.huynq13@vinuni.edu.vn  | nguyenquanghuy091204 | Người kiểm số (A, B) & Người viết code (nửa sau: D, E1) |
|    3 | Đỗ Minh Thanh          | 2A202603793 | 26ai.thanhdm@vinuni.edu.vn  | thd050810            | Người gắn nhãn 1 (C) & viết phần chữ (A, B, D, E2)      |
|    4 | Đào Nguyễn Quang Thanh | 2A202603754 | 26ai.thanhdnq@vinuni.edu.vn | ThanhDao11           | Người gắn nhãn 2 kiêm giữ hồ sơ tổng                    |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## TranPhamMinhSon-2A202603802

### Phần việc phụ trách

- Thành viên 1 — Người viết code (nửa đầu: Nhiệm vụ A, B) và thiết kế danh sách event (Nhiệm vụ E1).

### Đóng góp cụ thể

- Hoàn thành các hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), mô hình chi phí A2 (`mo_hinh`), phân tách theo `loai` và tỉ lệ ok theo lần thử (A3), chi phí cố định 40 triệu đ/tháng (A4), và phân tích độ nhạy B1–B4 trong `src/lab13.py`.
- Hoàn thiện bảng danh sách 10 event có `trace_id` và phần kiểm tra chéo event ↔ chỉ số trong `report/team/chi_so.md`.

### Bằng chứng

- `src/lab13.py` chạy qua cả 3 phép thử A1 (`Ba phép thử đáp án biết trước: ĐẠT`: 1,20 · 1,25 · 1,25), tính ra CPS = 4.472 đ [simulated] (16,3× hoá đơn 274,7 đ/yêu cầu), chi phí cả hệ thống thấp nhất ở giới hạn 2 lần chạy (6.901.220 đ [simulated]).
- Bảng event trong `report/team/chi_so.md` và báo cáo cá nhân `report/team/2A202603802_TranPhamMinhSon.md`.

## NguyenQuangHuy-2A202603768
### Phần việc phụ trách
- Thành viên 2 — Người kiểm số (Nhiệm vụ A, B) và chuyển sang Người viết code (nửa sau: Nhiệm vụ D, E1).
### Đóng góp cụ thể
- Cài môi trường Python trên máy thứ hai và chạy kiểm chứng toàn bộ `src/lab13.py` của Thành viên 1; tính tay đối chiếu A1, A4, B3, B4.
- Điền đầy đủ toàn bộ bảng số liệu A1, A2, A3, A4, B1, B2, B3, B4 (có nhãn `simulated`) vào `report/team/bang_chi_phi.md`.
- Viết code `TODO CP4` trong `src/lab13.py` (hàm `co_mau`, `in_nhiem_vu_d` tính 5 câu cỡ mẫu D1, power ở MDE 6 điểm, tỉ lệ `mo_lai_trong_7_ngay` hiện tại; và `in_nhiem_vu_e1` tính 3 chỉ số E1).
- Điền số tính thử 3 chỉ số (Chính, Dùng, An toàn) vào bảng E1 trong `report/team/chi_so.md`.
### Bằng chứng
- `src/lab13.py` chạy trọn vẹn từ A đến E1 trên máy thứ hai (D1: 1.251 · 3.103 / 42 NV · trần 1.000 · trần 300 · 859 / m ≥ 299 / DE 6,96; power 0,64 ở mức 5 điểm; `mo_lai_trong_7_ngay` = 4,25% toàn mẫu và 3,97% trong phạm vi; E1: 82,83% · 27,12% · 4,25%).
- Bảng số trong `report/team/bang_chi_phi.md`, bảng E1 trong `report/team/chi_so.md` và báo cáo cá nhân `report/team/2A202603768_NguyenQuangHuy.md`.

## DoMinhThanh-2A202603793

### Phần việc phụ trách

- Thành viên 3 — Người gắn nhãn 1: gắn nhãn 20 ca lỗi theo PAIR, đối chiếu với Người gắn nhãn 2, tính đồng thuận, viết quy tắc phân biệt và bảng khắc phục 5 loại lỗi (Nhiệm vụ C).
- Viết phần chữ: câu trả lời A, B trong `report/team/bang_chi_phi.md`; kế hoạch pilot `report/team/pilot_plan.yaml` (Nhiệm vụ D); hai chỉ số mới và bảng rủi ro kinh tế trong `report/team/chi_so.md` (Nhiệm vụ E2).

### Đóng góp cụ thể

- Gắn nhãn 20 ca, đồng thuận 18/20 = 90% với Người gắn nhãn 2; hai ca lệch (6, 9) thống nhất là Do người dùng, kèm quy tắc "đầu vào của khách sai thì gắn Do người dùng".
- Bảng khắc phục 5 ca (9, 20, 18, 4, 12): mỗi ca có event đo được, ngưỡng, tần suất và một vai trò phụ trách.
- `bang_chi_phi.md`: sáu câu trả lời A2–B4, mỗi câu có số và nhãn simulated (16,3× hoá đơn; làm lại 51,8%; loại `quoc_te` 1,88×; hoà vốn ~6.200 yêu cầu/tháng; 2 lần chạy rẻ nhất cho cả hệ thống; hoà vốn xem lại ≤ 5,1 phút).
- `chi_so.md`: thêm chỉ số Dùng (trung vị `phut_xem_lai`) và An toàn (tỉ lệ hoàn sai/hoàn trùng); ba dòng rủi ro kinh tế lấy số từ B1, B4.
- `pilot_plan.yaml`: chia theo nhân viên, 20 cụm mỗi nhóm, MDE 6 điểm (DE 6,96), năm câu D2, ba luật dừng đủ bốn vế, rollback, ngày quyết định 2027-01-05, danh sách số simulated.

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/pilot_plan.yaml` (đọc được bằng `yaml.safe_load`, không còn dấu hỏi ngoài chú thích), báo cáo cá nhân `report/team/2A202603793_DoMinhThanh.md`.

## DaoNguyenQuangThanh-2A202603754

### Phần việc phụ trách

- Thành viên 4 — Người gắn nhãn 2: gắn nhãn độc lập 20 ca lỗi; sau khi đối chiếu với thành viên 3, tính đồng thuận và hoàn thiện bảng khắc phục 5 loại lỗi.
- Giữ hồ sơ tổng: tổng hợp `ho_so_launch_v0.md` và hoàn thiện `group_report.md` sau duyệt chéo.
- Cùng nhóm tham gia duyệt chéo và hoàn thiện `phieu_cham.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca; đối chiếu với thành viên 3 đạt 18/20 ca (90%). Hai ca lệch là 6 và 9, thống nhất nguyên nhân gốc là đầu vào khách hàng sai.
- Phối hợp hoàn thiện bảng khắc phục cho năm loại lỗi trong `report/team/bang_loi.md`.
- Tổng hợp các kết quả đã có bằng chứng vào `report/team/ho_so_launch_v0.md`; báo cáo nhóm và phiếu chấm được hoàn thiện theo kết quả duyệt chéo.

### Bằng chứng

- `report/team/bang_loi.md`: hai bộ nhãn, đồng thuận 18/20 và bảng khắc phục năm ca.
- `report/team/ho_so_launch_v0.md`: tóm tắt các kết quả A–E đã được nhóm kiểm tra.
