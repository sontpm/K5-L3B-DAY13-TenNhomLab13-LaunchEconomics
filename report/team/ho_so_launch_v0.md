# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: TenNhomLab13 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc; 978 việc thành công (simulated) | Giả lập | Người kiểm số (TV2) |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,8%; xem lại ×2: +40,7%; lương +25%: +23,1% (simulated) | Giả lập | Người viết code (TV1) |
| 3 · So với nhân viên tự làm | `noi_dia` 2.696 đ (0,22×), `hang_nang` 8.221 đ (0,69×), `quoc_te` 22.515 đ (1,88×), `doi_tac` 10.215 đ (0,85×); phí cố định trong phạm vi: 4.599 đ ở 45.000 và 5.784 đ ở 22.500 yêu cầu/tháng (simulated) | Giả lập | Người kiểm số (TV2) |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong mẫu: 82,83% (994/1.200); 27,12% (48/177); 4,25% (51/1.200); không suy luận tác động nhân quả (simulated) | Giả lập | Người viết code (TV2) |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 18/20 (90%); ca 6 và 9 thống nhất Do người dùng; có biện pháp cho năm loại lỗi | Xong, có bằng chứng | Người gắn nhãn 2 (TV4) |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, 20 cụm/nhóm; MDE 6 điểm, n hiệu dụng 859/nhóm, DE 6,96; power 0,64 nếu tác động thật là 5 điểm | Xong, có bằng chứng | Người gắn nhãn 1 (TV3) |
| 7 · Rủi ro kinh tế | Làm lại ×2: CPS 6.787 đ (+51,8%); xem lại 100%: 11.743–12.415 đ (0,98–1,03×) (simulated) | Giả lập | PM trợ lý hoàn phí |

Điều kiện trước và trong pilot:

- Trước 2027-01-05, Kỹ sư trưởng agent sửa khoá chống hoàn trùng và đối soát sổ cái cho các ca 7, 20; kiểm thử không còn xác nhận hoàn tiền khi sổ cái chưa thành công.
- Trước 2027-01-05, Giám đốc vận hành xác nhận chấp nhận MDE 6 điểm; nếu tác động thật là 5 điểm, power chỉ khoảng 0,64.
- Trước ngày bắt đầu, PM bật đủ event có `trace_id`; sau tuần 1, PM thay các thời lượng `simulated` bằng số đo thực tế.
- Cuối bước rollout 25%, Trưởng nhóm CSKH rà tỉ lệ xem lại; không giảm xem lại nếu chưa đạt ngưỡng an toàn trong pilot plan.

**Đề xuất: Go có điều kiện.**
