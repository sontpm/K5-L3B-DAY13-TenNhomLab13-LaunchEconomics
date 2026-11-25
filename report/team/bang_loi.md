# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đỗ Minh Thanh (2A202603793) (gắn độc lập từ định nghĩa PAIR, không trao đổi) · Người gắn nhãn 2: Đào Nguyễn Quang Thanh (2A202603754) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Ngữ cảnh | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Ngữ cảnh | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90% (đạt ngưỡng 80%, không cần viết lại định nghĩa). Hai ca lệch: 6 và 9.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6 → Do người dùng (người 2 gắn Ngữ cảnh):** khách tự chọn sai mục "Hoàn phí giao trễ" cho ca hàng vỡ, nên đầu vào sai là nguyên nhân gốc; Ngữ cảnh chỉ dùng khi đầu vào đúng mà giả định thiết kế không khớp hoàn cảnh khách.
- **Ca 9 → Do người dùng (người 2 gắn Ngữ cảnh):** khách nhập mã đơn của sàn TMĐT thay vì mã vận đơn; việc trợ lý dừng mà không gợi ý là chỗ cần sửa (ghi ở cột khắc phục), không phải nguyên nhân gốc.
- **Quy tắc chung rút ra:** hỏi trước "đầu vào của khách có sai không?"; có sai thì gắn Do người dùng, kể cả khi trợ lý xử lý đầu vào sai đó kém.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | `agent_run_completed` với `status = ma_khong_hop_le`, đếm theo ngày; cảnh báo khi vượt 2% số `refund_request_created` trong ngày | Nhận diện mẫu mã đơn sàn TMĐT và tra sang mã vận đơn; không tra được thì hiện hướng dẫn kèm ảnh chỗ lấy mã vận đơn, không dừng im lặng | PM trợ lý hoàn phí |
| 20 | Hệ thống | `refund_ledger_write` có từ 2 bản ghi `ket_qua = ok` cho cùng `request_id`, đối soát mỗi giờ; ngưỡng 0 ca (1 ca là dừng, khớp luật dừng an toàn trong `pilot_plan.yaml`) | Bắt buộc `idempotency_key` = `request_id` cho mọi lệnh ghi sổ cái; sổ cái từ chối khoá trùng; yêu cầu gửi lại trong 24 giờ gộp vào ticket cũ | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | `ticket_reopened` với `reason = so_tien` mà `audit_sample_checked` cho thấy `so_tien_da_hoan = so_tien_dung`; tính theo tuần, cảnh báo khi vượt 1% số `ticket_closed` | Mẫu tin nhắn luôn ghi cách tính, ví dụ "Phí 30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ", kèm link điều khoản | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | `handoff_to_staff` với `reason = thieu_du_lieu`, theo `loai`, mỗi ngày; cảnh báo khi một loại vượt 20% số yêu cầu của loại đó | Giữ cách nói rõ và chuyển nhân viên kèm tóm tắt; đưa `quoc_te` ra khỏi pilot (1,88× chi phí nhân viên tự làm, simulated) | PM trợ lý hoàn phí |
| 12 | Ngầm | Tổng `tokens_in + tokens_out` của `agent_run_completed` trên mỗi yêu cầu, theo depot, mỗi ngày; cảnh báo khi một depot vượt 1,5× trung vị các depot 2 ngày liên tiếp | Sửa tool tra đơn ở D05 trả đủ trường; thêm kiểm tra schema đầu ra của tool, thiếu trường thì báo lỗi thay vì gọi lại | Kỹ sư trưởng agent |
