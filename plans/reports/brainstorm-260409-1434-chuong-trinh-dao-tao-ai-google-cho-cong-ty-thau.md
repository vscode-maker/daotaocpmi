# Brainstorm Report: Chương Trình Đào Tạo Ứng Dụng AI Google Cho Công Ty Thầu

**Date:** 2026-04-09
**Type:** Training Program Design
**Duration:** 2 ngày x 6 tiếng (8:30–16:30)
**Đối tượng:** 20-50 nhân viên văn phòng (tất cả phòng ban)
**Trình độ:** Khá tốt (đã biết dùng một số công cụ AI)
**Công cụ:** Google Gemini, NotebookLM, Google Workspace

---

## 1. Vấn đề & Bối cảnh

### Pain Points hiện tại trong quy trình CBDA
- **Tra cứu pháp lý**: 36+ văn bản pháp luật (Luật, NĐ, TT, QĐ), thay đổi liên tục → mất thời gian tìm kiếm, dễ sót
- **Soạn thảo hồ sơ**: Tờ trình, BCNCTKT, BCKTKT, KH LCNT → lặp đi lặp lại, tốn thời gian format
- **Thẩm định & tổng hợp**: Xin ý kiến nhiều sở ngành, tổng hợp ý kiến → dễ bỏ sót, chậm trễ
- **Phân tích chi phí**: Dự toán, so sánh phương án → thủ công trên Excel, thiếu tự động hóa
- **Giao tiếp**: Email trao đổi sở ngành, nội bộ → soạn thảo chậm, thiếu chuyên nghiệp

### Giải pháp AI mapping

| Pain Point | Công cụ AI | Ứng dụng cụ thể |
|---|---|---|
| Tra cứu 36 VB pháp luật | NotebookLM | Upload PDF các NĐ, TT → hỏi đáp, tổng hợp, Audio Overview |
| Soạn tờ trình, BCKTKT | Gemini Docs | Draft từ template, chỉnh sửa, format chuyên nghiệp |
| Tổng hợp ý kiến thẩm định | Gemini Docs | Tóm tắt VB góp ý, tạo bảng tổng hợp |
| Dự toán, phân tích chi phí | Gemini Sheets | Công thức tự động, phân tích xu hướng, dashboard |
| Email sở ngành | Gemini Gmail | Soạn email chuyên nghiệp, tóm tắt email dài |
| Slide báo cáo | Gemini Slides | Tạo slide từ nội dung, speaker notes |
| Đào tạo nội bộ | NotebookLM | Audio Overview từ quy trình → NV mới nghe hiểu nhanh |

---

## 2. Thiết Kế Chương Trình Đào Tạo

### Nguyên tắc thiết kế
- **Hands-on first**: Lý thuyết < 15 phút mỗi phiên, còn lại thực hành
- **Real work output**: Mỗi workshop tạo ra 1 sản phẩm thật dùng được
- **Tài liệu thật + giả lập**: VB pháp luật dùng thật (công khai), tờ trình/dự toán dùng mẫu
- **Human-in-the-loop**: Luôn nhấn mạnh AI = bản nháp đầu, con người = quyết định cuối

---

## NGÀY 1: LÀM CHỦ CÔNG CỤ AI GOOGLE
**Mục tiêu**: Thành thạo Gemini + NotebookLM, tạo được sản phẩm thực tế

### Phiên 1 (8:30–9:00) — Khai mạc & Demo "WOW Effect"
**Thời lượng**: 30 phút | **Hình thức**: Toàn thể

**Nội dung:**
- Giảng viên demo LIVE: upload Nghị định 175/2024 vào NotebookLM → tạo Audio Overview bằng tiếng Việt → hỏi "tóm tắt 5 bước CBDA" → AI trả lời chính xác
- Demo Gemini Docs: nhập prompt "soạn tờ trình đề nghị phê duyệt chủ trương đầu tư dự án cải tạo trụ sở UBND phường X" → 30 giây có bản nháp
- Giới thiệu agenda 2 ngày
- **Lưu ý**: Không dạy "AI là gì" (NV đã biết), vào thẳng demo thực tế

### Phiên 2 (9:00–10:30) — Workshop: Gemini Cơ Bản
**Thời lượng**: 90 phút | **Hình thức**: Thực hành cá nhân + cặp đôi

**Nội dung chi tiết:**

**A. Gemini trong Google Docs (40 phút)**
- Kỹ thuật prompt hiệu quả cho văn bản hành chính/xây dựng
- Thực hành:
  - Soạn tờ trình đề xuất chủ trương đầu tư (Bước 1 CBDA)
  - Chỉnh sửa tone, format theo mẫu hành chính
  - Tóm tắt văn bản dài (NĐ 175 → 1 trang)
- Mẹo: "Hãy viết theo format tờ trình hành chính Việt Nam, kính gửi..., căn cứ..., đề nghị..."

**B. Gemini trong Gmail (25 phút)**
- Thực hành:
  - Soạn email gửi Sở QHKT đề nghị cung cấp chỉ giới đường đỏ
  - Tóm tắt chuỗi email dài (mô phỏng trao đổi thẩm định)
  - Điều chỉnh tone (trang trọng ↔ thân thiện)

**C. Gemini trong Slides (25 phút)**
- Thực hành:
  - Tạo slide báo cáo tiến độ dự án từ bullet points
  - Thêm speaker notes tự động
  - Generate hình ảnh minh họa (nếu cần)

**Sản phẩm đầu ra**: 1 tờ trình + 1 email + 1 slide deck (mỗi người)

### ☕ Giải lao (10:30–10:45)

### Phiên 3 (10:45–11:30) — Workshop: Gemini Sheets & Phân Tích Dữ Liệu
**Thời lượng**: 45 phút | **Hình thức**: Thực hành theo nhóm 3-4 người

**Nội dung:**
- Gemini tạo công thức phức tạp từ mô tả tiếng Việt
- Thực hành với file dự toán mẫu:
  - "Tính tổng chi phí xây dựng theo hạng mục, highlight hạng mục vượt 10%"
  - "Tạo biểu đồ so sánh dự toán vs thực tế theo quý"
  - "Phân tích xu hướng chi phí vật liệu 12 tháng gần nhất"
- Tạo dashboard tóm tắt tình hình dự án

**Sản phẩm đầu ra**: 1 file Sheets có dashboard phân tích chi phí

### 🍽️ Nghỉ trưa (11:30–13:00)

### Phiên 4 (13:00–14:30) — Workshop: NotebookLM Chuyên Sâu
**Thời lượng**: 90 phút | **Hình thức**: Thực hành cá nhân → nhóm

**Nội dung chi tiết:**

**A. Thiết lập Notebook pháp luật xây dựng (30 phút)**
- Upload nguồn: 5-8 văn bản pháp luật chính (NĐ 175, Luật ĐTC 58, NĐ 85, NĐ 10, TT 79...)
- Thực hành hỏi đáp:
  - "Thời gian thẩm định dự án nhóm B là bao lâu?"
  - "So sánh quy trình phê duyệt dự án nhóm A vs nhóm C"
  - "Liệt kê các biểu mẫu cần dùng cho Bước 3 CBDA"
- Hiểu cách NotebookLM trích dẫn nguồn → xác minh được

**B. Audio Overview (30 phút)**
- Tạo Audio Overview từ quy trình CBDA
- Tùy chỉnh: focus vào phần nào, tone nào
- Ứng dụng: tạo podcast đào tạo nội bộ cho NV mới

**C. Notebook cộng tác (30 phút)**
- Tạo Notebook chung cho nhóm dự án
- Chia sẻ, phân quyền (xem/chỉnh sửa)
- Use case: nhóm đấu thầu review hồ sơ mời thầu cùng nhau

**Sản phẩm đầu ra**: 1 Notebook pháp luật XD cá nhân + 1 Audio Overview

### ☕ Giải lao (14:30–14:45)

### Phiên 5 (14:45–16:00) — Workshop: Kết Hợp Gemini + NotebookLM Workflow
**Thời lượng**: 75 phút | **Hình thức**: Thực hành nhóm 4-5 người

**Bài tập tổng hợp — Mô phỏng Bước 1-2 CBDA:**
1. Dùng NotebookLM tra cứu: "Nội dung BCNCTKT theo Điều 34 Luật ĐTC 58 gồm những gì?"
2. Dùng Gemini Docs soạn tờ trình đề nghị giao nhiệm vụ lập BCNCTKT
3. Dùng Gemini Gmail soạn email xin ý kiến cơ quan thẩm định
4. Dùng Gemini Sheets lập bảng tổng hợp chi phí sơ bộ giai đoạn CBDA

**Sản phẩm đầu ra**: 1 bộ hồ sơ mini CBDA (tờ trình + email + bảng chi phí)

### Phiên 6 (16:00–16:30) — Wrap-up Ngày 1
**Thời lượng**: 30 phút

- Q&A mở
- Chia sẻ tips & tricks hay nhất từ các nhóm
- **Bài tập về nhà**: Mỗi người thử dùng Gemini/NotebookLM cho 1 việc thực tế ở cơ quan ngày hôm sau

---

## NGÀY 2: ỨNG DỤNG AI VÀO QUY TRÌNH CBDA
**Mục tiêu**: Áp dụng AI trực tiếp vào quy trình CBDA, tạo workflow thực tế

### Phiên 7 (8:30–9:00) — Ôn tập & Chia nhóm
**Thời lượng**: 30 phút

- Quick quiz tương tác (Gemini tips, NotebookLM tricks)
- Chia sẻ trải nghiệm bài tập về nhà
- Chia 4 nhóm theo phòng ban:
  - **Nhóm KT+QLDA**: Focus khảo sát, giám sát, kỹ thuật
  - **Nhóm HC+KT**: Focus văn thư, kế toán, tài chính
  - **Nhóm ĐT+PC**: Focus đấu thầu, hợp đồng, pháp chế
  - **Nhóm Tổng hợp**: Ban lãnh đạo, trợ lý, tổng hợp

### Phiên 8 (9:00–10:30) — Lab 1: Tra Cứu Pháp Lý & Chuẩn Bị Hồ Sơ CBDA
**Thời lượng**: 90 phút | **Hình thức**: Theo nhóm phòng ban

**Bài tập theo nhóm:**

| Nhóm | Bài tập cụ thể | Công cụ |
|---|---|---|
| KT+QLDA | Tra cứu yêu cầu khảo sát địa hình, địa chất theo NĐ 175. Lập nhiệm vụ khảo sát mẫu | NotebookLM + Gemini Docs |
| HC+KT | Tra cứu quy trình phê duyệt dự toán CBDA (Bước 2). Soạn tờ trình thẩm định dự toán | NotebookLM + Gemini Docs |
| ĐT+PC | Tra cứu quy trình LCNT theo Luật ĐT 2023. Lập KH LCNT giai đoạn CBDA | NotebookLM + Gemini Docs/Sheets |
| Tổng hợp | Tổng hợp quy trình 5 bước Quyết định CTrĐT. Soạn slide báo cáo cho lãnh đạo | NotebookLM + Gemini Slides |

### ☕ Giải lao (10:30–10:45)

### Phiên 9 (10:45–11:30) — Lab 2: Soạn Thảo Hồ Sơ Dự Án Với AI
**Thời lượng**: 45 phút | **Hình thức**: Nhóm phòng ban

**Mỗi nhóm soạn 1 bộ hồ sơ thực tế:**

**Nhóm KT+QLDA:**
- Lập thiết kế kỹ thuật-dự toán đo đạc 1/500 (tóm tắt)
- Dùng Gemini Sheets tổng hợp khối lượng khảo sát

**Nhóm HC+KT:**
- Soạn QĐ phê duyệt dự toán chi phí CBDA
- Dùng Gemini Sheets lập bảng tổng hợp chi phí tư vấn

**Nhóm ĐT+PC:**
- Soạn hồ sơ yêu cầu LCNT tư vấn khảo sát (theo Mẫu TT79)
- Dùng NotebookLM kiểm tra tính pháp lý

**Nhóm Tổng hợp:**
- Soạn BCKTKT tóm tắt (outline + nội dung chính)
- Tạo Audio Overview cho CBDA training nội bộ

### 🍽️ Nghỉ trưa (11:30–13:00)

### Phiên 10 (13:00–14:30) — Lab 3: Mô Phỏng Quy Trình CBDA End-to-End
**Thời lượng**: 90 phút | **Hình thức**: Nhóm hỗn hợp (mỗi nhóm có đủ phòng ban)

**Kịch bản**: Dự án "Cải tạo nâng cấp Trụ sở UBND phường X" – nhóm C, vốn ĐTC

**Quy trình mô phỏng:**
1. **Bước 1** (15'): Lập tờ trình đề xuất CTrĐT → Gemini Docs
2. **Bước 2** (15'): Tra cứu yêu cầu thẩm định → NotebookLM → Tổng hợp ý kiến
3. **Bước 3** (15'): Hoàn chỉnh hồ sơ theo ý kiến → Gemini Docs (chỉnh sửa)
4. **Bước 4** (15'): Lập KH LCNT, phê duyệt → Gemini Sheets + Docs
5. **Bước 5** (15'): Tổ chức thực hiện khảo sát, lập BCKTKT → Tổng hợp all tools
6. **Tổng kết** (15'): Review lại sản phẩm, so sánh quy trình thủ công vs AI

**Sản phẩm đầu ra**: 1 bộ hồ sơ CBDA hoàn chỉnh bằng AI (mỗi nhóm)

### ☕ Giải lao (14:30–14:45)

### Phiên 11 (14:45–15:45) — Trình Bày & Phản Biện
**Thời lượng**: 60 phút

- Mỗi nhóm trình bày sản phẩm CBDA (10 phút/nhóm)
- Các nhóm khác phản biện: chất lượng AI output, cần chỉnh sửa gì?
- Giảng viên tổng kết: "AI cho output 70-80%, con người hoàn thiện 20-30%"
- **Key message**: AI = trợ lý đắc lực, KHÔNG thay thế chuyên môn

### Phiên 12 (15:45–16:30) — Bảo Mật, Kế Hoạch 30 Ngày & Bế Mạc
**Thời lượng**: 45 phút

**A. Lưu ý bảo mật & rủi ro (15 phút)**
- KHÔNG upload thông tin mật, dữ liệu nhạy cảm lên AI công cộng
- Luôn kiểm tra lại output AI trước khi phát hành chính thức
- AI có thể sai → trách nhiệm thuộc về người dùng, không phải AI
- Chính sách sử dụng AI của công ty (nếu có)

**B. Kế hoạch hành động 30 ngày (15 phút)**
- Mỗi người viết 3 việc cụ thể sẽ dùng AI trong 30 ngày tới
- Ghép cặp buddy (2 người/cặp) → check-in sau 2 tuần
- Tạo nhóm chat hỗ trợ (Google Chat/Zalo)
- Lịch follow-up: tuần 2, tuần 4 (kiểm tra tiến độ áp dụng)

**C. Đánh giá & Bế mạc (15 phút)**
- Khảo sát hài lòng (Google Forms)
- Cấp chứng nhận hoàn thành
- Phát tài liệu Quick Reference Guide (1 trang/tool)

---

## 3. Tài Liệu Cần Chuẩn Bị

### Tài liệu thật (công khai)
- [ ] Nghị định 175/2024/NĐ-CP (PDF)
- [ ] Luật Đầu tư công số 58/2024/QH15 (PDF)
- [ ] Nghị định 85/2025/NĐ-CP (PDF)
- [ ] Nghị định 10/2021/NĐ-CP (PDF)
- [ ] Thông tư 79/2025/TT-BTC (PDF)
- [ ] Luật Đấu thầu 2023 (PDF)
- [ ] Slide Quy trình QLDA giai đoạn CBDA-2026 (PPTX)

### Tài liệu giả lập (cần tạo)
- [ ] Mẫu tờ trình đề xuất CTrĐT (dự án giả lập)
- [ ] Bảng dự toán chi phí CBDA mẫu (Sheets)
- [ ] Mẫu KH LCNT giai đoạn CBDA (Sheets)
- [ ] Chuỗi email mô phỏng trao đổi thẩm định
- [ ] Bảng tổng hợp ý kiến sở ngành mẫu
- [ ] File khối lượng khảo sát mẫu (Sheets)

### Tài liệu phát cho học viên
- [ ] Quick Reference Guide: Gemini trong Workspace (1 trang)
- [ ] Quick Reference Guide: NotebookLM (1 trang)
- [ ] Bảng prompt templates cho ngành xây dựng
- [ ] Checklist bảo mật khi dùng AI

---

## 4. Yêu Cầu Kỹ Thuật

### Cho ban tổ chức
- Google Workspace (Business Standard trở lên) cho tất cả học viên
- Gemini được bật trong Admin Console
- Máy chiếu + loa
- WiFi ổn định (50+ thiết bị đồng thời)

### Cho học viên
- Laptop hoặc máy tính bàn có trình duyệt Chrome
- Tài khoản Google Workspace của công ty
- Đã đăng nhập trước buổi học

---

## 5. Metrics Đánh Giá Thành Công

| Metric | Mục tiêu | Thời điểm đo |
|---|---|---|
| Hài lòng sau đào tạo | ≥ 4/5 | Ngày 2 |
| NV dùng Gemini/NotebookLM hàng tuần | ≥ 70% | Sau 30 ngày |
| Thời gian soạn tờ trình giảm | ≥ 30% | Sau 30 ngày |
| Thời gian tra cứu VB pháp luật giảm | ≥ 50% | Sau 30 ngày |
| Zero sự cố bảo mật do AI | 100% | Liên tục |

---

## 6. Rủi Ro & Giảm Thiểu

| Rủi ro | Mức độ | Giảm thiểu |
|---|---|---|
| WiFi yếu | Cao | Test trước, có backup 4G, chuẩn bị offline materials |
| NV chưa có tài khoản Google | Trung bình | IT setup trước 1 tuần |
| Gemini không hỗ trợ tốt tiếng Việt | Thấp | Chuẩn bị prompt song ngữ, test trước |
| NV lo ngại AI thay thế công việc | Trung bình | Frame: AI = trợ lý, tăng năng suất = có giá trị hơn |
| Lãnh đạo không tham gia | Cao | Mời LD làm đồng facilitator, không chỉ là học viên |

---

## 7. Bảng Prompt Templates Tham Khảo

### Cho Gemini Docs
```
1. "Soạn tờ trình [loại tờ trình] theo format hành chính Việt Nam. 
   Kính gửi: [đơn vị]. Căn cứ: [liệt kê VB]. Nội dung đề nghị: [nội dung]."

2. "Tóm tắt văn bản sau trong 10 bullet points, highlight các deadline 
   và đơn vị chịu trách nhiệm: [paste văn bản]"

3. "Chuyển nội dung sau thành format báo cáo kinh tế kỹ thuật đầu tư 
   xây dựng theo Điều 5 NĐ 175/2024: [nội dung]"
```

### Cho Gemini Sheets
```
1. "Tạo công thức tính tổng chi phí xây dựng = chi phí vật liệu + nhân công 
   + máy thi công + chi phí quản lý dự án + chi phí tư vấn"

2. "Phân tích dữ liệu trong sheet này: so sánh dự toán ban đầu vs chi phí 
   thực tế, highlight hạng mục chênh lệch >10%"

3. "Tạo biểu đồ tiến độ giải ngân theo tháng từ dữ liệu cột A-D"
```

### Cho NotebookLM
```
1. "Theo các nguồn tài liệu, thời gian thẩm định dự án nhóm B là bao lâu? 
   Trích dẫn điều khoản cụ thể."

2. "So sánh quy trình phê duyệt BCKTKT và BCNCKT: khác nhau ở điểm nào?"

3. "Liệt kê TẤT CẢ biểu mẫu cần nộp trong giai đoạn CBDA, kèm số hiệu 
   thông tư quy định."
```

### Cho Gemini Gmail
```
1. "Soạn email gửi Sở QHKT đề nghị cung cấp chỉ giới đường đỏ cho dự án 
   [tên dự án] tại [địa chỉ]. Tone trang trọng, kèm danh mục hồ sơ đính kèm."

2. "Tóm tắt chuỗi email này trong 5 điểm chính, highlight action items 
   và deadline."
```

---

## Unresolved Questions

1. **Google Workspace license**: Công ty đã dùng Google Workspace chưa? Nếu dùng Microsoft 365 thì cần điều chỉnh chương trình sang Copilot hoặc cần setup trial Google Workspace.
2. **Chính sách bảo mật nội bộ**: Công ty có chính sách về việc upload tài liệu lên cloud AI không? Cần check trước để điều chỉnh nội dung bài tập.
3. **Giảng viên/Facilitator**: Cần bao nhiêu trợ giảng? Khuyến nghị 1 giảng viên chính + 2-3 trợ giảng cho 20-50 người.
4. **Budget**: Chi phí license Google AI Ultra (nếu cần NotebookLM Plus) cho 50 người?
5. **Ngày tổ chức**: Cần ít nhất 2 tuần chuẩn bị tài liệu giả lập + test kỹ thuật.
