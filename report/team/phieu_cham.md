# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): TenNhomLab13
- Nhóm được chấm: H123

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp số liệu (cả hệ thống 5.865 đ = 0,49×, simulated), nêu đủ số bất lợi (power ~0,64 ở mức 5 điểm; xem lại 100% tốn 11.743–12.414 đ = 0,98×–1,03×) và có 4 điều kiện gắn rõ vai trò + mốc kiểm tra. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Gắn nhãn `simulated` đầy đủ trên mọi số giả lập (mục 1, 2, 3, 7 ghi trạng thái `Giả lập`); thu hẹp phạm vi về `noi_dia` (0,22×) + `hang_nang` (0,69×), loại `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên 20 + 20 nhân viên (đạt ≥ 20 cụm/nhóm), đối chứng cùng thời gian, đủ cỡ mẫu MDE 6 điểm (`n=859/nhóm`, `m≥299`, `DE=6,96`); đủ 3 luật dừng đúng mẫu NẾU–TRONG–THÌ–KHÔNG THÌ dựa trên nền mở lại 4,25% (3,97% phạm vi), rollback 30 phút do Giám đốc vận hành thực hiện. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ đạt đủ bằng chứng định lượng cho phạm vi `noi_dia` + `hang_nang` (4.599 đ = 0,38× đã cộng cố định 40 triệu đ/tháng, simulated), nhận diện rõ rủi ro xem lại 100% (0,98×–1,03×) và đánh đổi MDE 6 điểm (power ~0,64 ở mức 5 điểm). Cần hoàn tất sửa khoá chống trùng sổ cái (ca 7, 20), bổ sung event `input_validation_failed` vào đặc tả event và đo phút thực tế sau tuần 1 trước khi mở rộng bước rollout.

**Một câu hỏi cho đội trình:** Trong `bang_loi.md` (ca 9), nhóm đặt cách phát hiện lỗi người dùng bằng event `input_validation_failed` (ngưỡng > 2%/ngày), nhưng bảng 10 event trong `chi_so.md` chưa có event này — nhóm dự định bổ sung event nào để đo được ca 9 và ở bước rollout 0.50 (20 nhân viên, `m ≥ 299` yêu cầu/người), pilot cần chạy ít nhất bao nhiêu ngày để đủ cỡ mẫu?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm thống nhất bổ sung event `input_validation_failed` (do App khách/API tạo, gồm thuộc tính `request_id`, `reason`, `trace_id` khi khách nhập sai định dạng mã vận đơn) vào `chi_so.md` trước ngày bắt đầu pilot. Về thời lượng bước rollout 0.50: phạm vi `noi_dia + hang_nang` chiếm 982/1.200 = 81,8% của 1.500 yc/ngày (~1.228 yc/ngày cho 40 nhân viên, tức ~30,7 yc/người/ngày), nên để đạt `m ≥ 299` yc/người cần chạy ít nhất **10 ngày** thu thập dữ liệu (cộng 7 ngày cửa sổ theo dõi `mo_lai_trong_7_ngay`, tổng khoảng 17 ngày ~ 2,5 tuần) trước ngày chốt quyết định.