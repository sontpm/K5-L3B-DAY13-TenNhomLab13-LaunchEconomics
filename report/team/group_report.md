# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: TenNhomLab13
- Lớp: L3B
- Thành viên: xem `TEAM.md` (4 thành viên)

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá trợ lý hoàn phí LogiX-VN theo chi phí mỗi việc thành công, mức sử dụng, lỗi và khả năng thiết kế một pilot có đối chứng. Nhóm phân tích 1.200 yêu cầu và 1.624 lần chạy agent (dữ liệu giả lập), tính chi phí từ mọi lần chạy, tách kết quả theo loại yêu cầu, rồi dùng kết quả đó để chọn phạm vi pilot. Hai thành viên gắn nhãn 20 ca lỗi độc lập trước khi đối chiếu.

## 3. Giải pháp

- **A–B:** triển khai mô hình chi phí và độ nhạy trong `src/lab13.py`; tổng hợp tại `report/team/bang_chi_phi.md`.
- **C:** phân loại lỗi theo Google PAIR, đối chiếu nhãn và đề xuất phát hiện/khắc phục trong `report/team/bang_loi.md`.
- **D:** thiết kế pilot chia ngẫu nhiên theo nhân viên, có đối chứng, cỡ mẫu và luật dừng trong `report/team/pilot_plan.yaml`.
- **E:** đặc tả chỉ số, event và rủi ro trong `report/team/chi_so.md`; tổng hợp đề xuất tại `report/team/ho_so_launch_v0.md`.

## 4. Kết quả

- **Kinh tế (simulated):** tổng chi phí 4.373.585 đ cho 978 việc thành công, tương đương 4.472 đ/việc; cao gấp 16,3× hoá đơn token/tool chia mỗi yêu cầu. `noi_dia` là 2.696 đ/việc (0,22× nhân viên), `hang_nang` 8.221 đ (0,69×), `quoc_te` 22.515 đ (1,88×); pilot chọn hai loại đầu, loại `doi_tac` vì điều khoản riêng.
- **Độ nhạy (simulated):** làm lại tăng gấp đôi làm chi phí tăng 51,8%; xem lại tăng gấp đôi tăng 40,7%. Giới hạn 2 lần chạy có tổng chi phí cả hệ thống thấp nhất: 6.901.220 đ.
- **Xem lại 100% (simulated):** CPS 11.743–12.415 đ, tức 0,98–1,03× chi phí nhân viên; lợi ích kinh tế có thể mất nếu thời gian làm lại theo mức quan sát cao hơn.
- **Lỗi:** hai người đồng thuận 18/20 ca (90%); hai ca lệch được thống nhất là lỗi đầu vào người dùng.
- **Pilot:** chia theo nhân viên, 20 cụm mỗi nhóm; MDE 6 điểm, cỡ mẫu hiệu dụng 859 mỗi nhóm. Nếu hiệu quả thật là 5 điểm, power khoảng 0,64.
- **Chỉ số trong mẫu giả lập:** chính 82,83%, dùng 27,12%, an toàn 4,25%. Đây là số mô tả, không chứng minh tác động nhân quả.
- **Đề xuất:** Go có điều kiện; điều kiện cụ thể nằm trong `report/team/ho_so_launch_v0.md`.
- **Kết quả duyệt chéo của hội đồng:** ...

## 5. Khó khăn và cách xử lý

- Hai ca gắn nhãn độc lập (6, 9) khác nhau; nhóm thống nhất dựa trên nguyên nhân gốc: đầu vào khách hàng sai được xếp là “Do người dùng”, còn cách trợ lý xử lý là phần cần khắc phục.
- Thiết kế cụm không đủ cỡ mẫu để phát hiện mức chênh 5 điểm với 40 nhân viên; nhóm ghi rõ đánh đổi sang MDE 6 điểm và power 0,64 nếu tác động thật là 5 điểm.

## 6. Tổng hợp đóng góp

- **Trần Phạm Minh Sơn (2A202603802):** viết và chạy code cho mô hình chi phí A–B; xây dựng danh sách event và đối chiếu event với chỉ số E1.
- **Nguyễn Quang Huy (2A202603768):** kiểm tra chéo các phép tính A–B; viết code tính cỡ mẫu/power cho D và các chỉ số E1; điền, đối chiếu bảng số liệu.
- **Đỗ Minh Thanh (2A202603793):** gắn nhãn độc lập 20 ca lỗi, đối chiếu nhãn và xây dựng bảng khắc phục; hoàn thiện kế hoạch pilot, gồm thiết kế chia nhóm và luật dừng.
- **Đào Nguyễn Quang Thanh (2A202603754):** gắn nhãn độc lập 20 ca lỗi; tổng hợp hồ sơ launch và báo cáo nhóm từ các kết quả đã được kiểm tra; phối hợp hoàn thiện bảng khắc phục và hồ sơ duyệt chéo.

## 7. Hạn chế và hướng cải thiện

- Toàn bộ dữ liệu phân tích là giả lập; đợt chạy thử không có nhóm đối chứng nên chưa thể kết luận trợ lý gây ra mức thay đổi chỉ số.
- Thiết kế có 20 cụm mỗi nhóm chỉ đủ lực cho MDE 6 điểm; kết quả không thấy khác biệt không đồng nghĩa không có tác động 5 điểm.

## 8. Tài liệu tham khảo

- [Tài liệu dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md).
- [Hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- Google PAIR, “Errors + Graceful Failure”, People + AI Guidebook.
- Erol và cộng sự, “Cost-of-Pass: An Economic Framework for Evaluating Language Models”.
