# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-TenNhomLab13-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics` (nhánh đang phát triển phần TV1: `sontpm`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trần Phạm Minh Sơn | 2A202603802 | 26ai.sontpm@vinuni.edu.vn | sontpm | Người viết code (nửa đầu: A, B) & Event (E1) |
|   2 |        |      |       |        |         |
|   3 |        |      |       |        |         |
|   4 | Đào Nguyễn Quang Thanh | 2A202603754 | 26ai.thanhdnq@vinuni.edu.vn | ThanhDao11 | Người gắn nhãn 2 kiêm giữ hồ sơ tổng |

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

## DaoNguyenQuangThanh-2A202603754

### Phần việc phụ trách

- Thành viên 4 — Người gắn nhãn 2: gắn nhãn độc lập 20 ca lỗi; sau khi đối chiếu với thành viên 3, tính đồng thuận và hoàn thiện bảng khắc phục 5 loại lỗi.
- Giữ hồ sơ tổng: tổng hợp `ho_so_launch_v0.md` và hoàn thiện `group_report.md` sau duyệt chéo.
- Cùng nhóm tham gia duyệt chéo và hoàn thiện `phieu_cham.md`.

### Đóng góp cụ thể

- Đang thực hiện theo phân công; cập nhật các kết quả và phần việc đã hoàn thành sau từng checkpoint.

### Bằng chứng

- Bổ sung file, commit hoặc kết quả cụ thể sau khi hoàn thành các phần việc.
