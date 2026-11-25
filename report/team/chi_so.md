# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: thời gian xem lại trung vị mỗi gợi ý (phút) | Trung vị `phut_xem_lai` của `staff_review_decision` trong nhóm trợ lý; so với ngưỡng hoà vốn 5,1 phút ở B4 (simulated) | Không cần tính |
| An toàn | Nhóm tự đề xuất: tỉ lệ hoàn tiền sai số tiền hoặc hoàn trùng | Số `refund_ledger_write` trùng `idempotency_key` cộng số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số giao dịch hoàn tiền | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện lên |
| `staff_review_decision` | Nhân viên | `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien_vnd`, `ket_qua`, `trace_id` | Khi ghi giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách hàng | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Khi kiểm tra mẫu đối soát hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h & không mở lại trong 7 ngày):** tính từ `refund_request_created`, `ticket_closed` và `ticket_reopened` (nối theo `trace_id` / `request_id`).
- **Chỉ số dùng (% bỏ qua gợi ý):** tính từ `agent_suggestion_shown` và `staff_review_decision` (`sua` hoặc `bo`).
- **Chỉ số an toàn (% mở lại trong 7 ngày):** tính từ `ticket_closed` và `ticket_reopened`.
- **Chi phí thật & thời gian nhân viên đo thật:** tính từ `agent_run_completed`, `staff_review_decision` (`phut_xem_lai`), `staff_rework_completed` (`phut_lam_lai`) và `handoff_to_staff`.
- **Phát hiện lỗi ngầm / hoàn trùng:** tính từ `refund_ledger_write` (kiểm tra `idempotency_key`) và `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng (gợi ý sai phải làm lại) | Làm lại gấp đôi: chi phí mỗi việc thành công 4.472 → 6.787 đ (+51,8%, simulated), yếu tố mạnh nhất ở B2 | `phut_lam_lai` từ `staff_rework_completed`, trung bình tuần vượt 9 phút/ca hoặc số ca làm lại tăng 50% so với tuần đầu | Thu hẹp phạm vi về `noi_dia`, giới hạn 2 lần chạy | PM trợ lý hoàn phí |
| Nhân viên phải xem lại gần như mọi gợi ý | Xem lại gấp đôi: +40,7% (6.292 đ, simulated); xem lại 100% `noi_dia` + `hang_nang`: 11.743–12.415 đ = 0,98–1,03× nhân viên tự làm (simulated) | Trung vị `phut_xem_lai` từ `staff_review_decision` vượt 5,1 phút/ca trong 1 tuần | Chuyển sang xem lại theo mẫu; nếu vẫn vượt thì đề xuất No-go ở ngày quyết định | Giám đốc vận hành LogiX-VN |
| Lương nhân viên tăng | Lương tăng 25%: 5.506 đ (+23,1%, simulated) | Bảng lương quý mới của CSKH | Tính lại mô hình chi phí trước khi mở rộng | Trưởng nhóm CSKH |