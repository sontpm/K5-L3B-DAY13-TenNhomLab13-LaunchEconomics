# Báo cáo cá nhân — DoMinhThanh-2A202603793

## 1. Thông tin thành viên

- Họ tên: Đỗ Minh Thanh
- MSSV: 2A202603793
- Email: 26ai.thanhdm@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Nhiệm vụ C: gắn nhãn 20 ca lỗi theo năm loại của Google PAIR, đối chiếu với Người gắn nhãn 2, tính đồng thuận, viết quy tắc phân biệt cho ca lệch, điền bảng khắc phục 5 ca.
- Viết phần chữ A, B: câu trả lời ngắn có số trong `report/team/bang_chi_phi.md`, kiểm nhãn simulated.
- Nhiệm vụ D: hoàn thiện `report/team/pilot_plan.yaml` dựa trên số D1 của Thành viên 2.
- Nhiệm vụ E2: hai chỉ số mới (Dùng, An toàn) và bảng rủi ro kinh tế trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- Đồng thuận 18/20 = 90%, đạt ngưỡng 80%. Hai ca lệch:
  - Ca 6 (khách chọn nhầm mục "giao trễ" cho hàng vỡ) và ca 9 (khách nhập mã đơn sàn TMĐT): thống nhất là Do người dùng, vì đầu vào của khách sai là nguyên nhân gốc; việc trợ lý không hỏi lại hay không gợi ý thuộc phần khắc phục.
- Bảng khắc phục, mỗi loại một ca:
  - Ca 9 (Do người dùng): đếm `agent_run_completed` có mã không hợp lệ, cảnh báo khi vượt 2% số yêu cầu trong ngày; PM trợ lý hoàn phí phụ trách.
  - Ca 20 (Hệ thống): đối soát `refund_ledger_write` mỗi giờ, ngưỡng 0 ca hoàn trùng; bắt buộc `idempotency_key` = `request_id`; Kỹ sư trưởng agent phụ trách.
  - Ca 18 (Ngữ cảnh): `ticket_reopened` vì số tiền dù audit thấy đúng, cảnh báo khi vượt 1% số ticket đóng mỗi tuần; Trưởng nhóm CSKH phụ trách.
  - Ca 4 (Giới hạn hệ thống): `handoff_to_staff` vì thiếu dữ liệu theo loại; loại `quoc_te` khỏi pilot; PM trợ lý hoàn phí phụ trách.
  - Ca 12 (Ngầm): token mỗi yêu cầu theo depot, cảnh báo khi vượt 1,5× trung vị 2 ngày liên tiếp; Kỹ sư trưởng agent phụ trách.
- `bang_chi_phi.md`: CPS gấp 16,3× hoá đơn; làm lại chiếm 51,8%; `quoc_te` 1,88× và chạy lại không cứu (ok 30,0% → 11,4% → 2,2%); hoà vốn chi phí cố định ~6.200 yêu cầu/tháng; giới hạn 2 lần rẻ nhất cho cả hệ thống nhưng không trùng CPS thấp nhất (1 lần); xem lại 100% làm mất lợi thế (0,98–1,03×). Tất cả simulated.
- `chi_so.md`: chỉ số Dùng = trung vị `phut_xem_lai` (so với hoà vốn 5,1 phút); chỉ số An toàn = tỉ lệ hoàn sai số tiền hoặc hoàn trùng; ba dòng rủi ro (làm lại +51,8%, xem lại 100%, lương +23,1%), mỗi dòng có event theo dõi và vai trò phụ trách.
- `pilot_plan.yaml`:
  - Chia theo nhân viên, 20 cụm mỗi nhóm, MDE 6 điểm, DE 6,96. Chấp nhận đánh đổi: nếu tác động thật là 5 điểm thì power chỉ còn 0,64.
  - Ngưỡng an toàn so với đối chứng (+2 điểm) kèm trần tuyệt đối 6%, vì `mo_lai_trong_7_ngay` hiện đã là 4,25% (3,97% trong phạm vi); ngưỡng 3% sẽ dừng pilot ngay tuần đầu.
  - Ba luật dừng đủ bốn vế NẾU / TRONG / THÌ / KHÔNG THÌ, rollback trong 30 phút, ngày quyết định 2027-01-05.

## 4. Bằng chứng

- `report/team/bang_loi.md`: bảng hai bộ nhãn, tỉ lệ đồng thuận, quy tắc phân biệt, bảng khắc phục.
- `report/team/bang_chi_phi.md`, `report/team/chi_so.md`: số đối chiếu với output `src/lab13.py`.
- `report/team/pilot_plan.yaml`: `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy qua; không còn dấu hỏi ngoài dòng chú thích.
- Commit trên nhánh `dothanh`.

## 5. Công cụ AI đã dùng

- Claude Code: đọc hướng dẫn lab, soạn nháp bảng khắc phục và `pilot_plan.yaml`, kiểm YAML và kiểm từ cấm bằng grep.
- Tự kiểm tra: đối chiếu từng event với danh sách trong `report/team/chi_so.md`; đối chiếu số D1 với output `src/lab13.py`; mọi số lấy từ cột `_simulated` đều ghi nhãn simulated.

## 6. Tự đánh giá

- Làm đủ phần C, chữ A, B, D và E2 theo điều kiện "Xong khi".
- Hạn chế: hai ca lệch (6, 9) cho thấy định nghĩa "Do người dùng" và "Ngữ cảnh" còn dễ nhầm; pilot chọn MDE 6 điểm nên nếu tác động thật chỉ 5 điểm thì power còn 0,64 [simulated].
