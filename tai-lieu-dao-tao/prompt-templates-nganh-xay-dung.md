# PROMPT TEMPLATES — NGÀNH XÂY DỰNG & QUẢN LÝ DỰ ÁN

> Bảng prompt mẫu | In 2 trang A4 | Dùng cho Gemini Docs, Gmail, Sheets, NotebookLM

---

## TRANG 1: GEMINI DOCS + GMAIL

### A. Soạn thảo văn bản hành chính

| # | Loại văn bản | Prompt mẫu |
|---|-------------|------------|
| 1 | **Tờ trình CTrĐT** | "Soạn tờ trình đề nghị phê duyệt chủ trương đầu tư dự án [tên DA], nhóm [A/B/C]. Kính gửi: [đơn vị]. Căn cứ: NĐ 175/2024, Luật ĐTC số 58. Nội dung: [mô tả DA, quy mô, TMĐT]. Format tờ trình hành chính Việt Nam." |
| 2 | **Tờ trình thẩm định dự toán** | "Soạn tờ trình thẩm định và phê duyệt dự toán chi phí giai đoạn chuẩn bị dự án. Căn cứ: K1,2 Điều 10 NĐ số 10/2021. Tổng dự toán: [X đồng], gồm [liệt kê hạng mục]." |
| 3 | **QĐ phê duyệt CTrĐT** | "Soạn quyết định phê duyệt chủ trương đầu tư dự án [tên], nhóm [C]. Căn cứ: K2 Điều 28 Luật ĐTC 58. Nội dung: tên DA, mục tiêu, quy mô, TMĐT, nguồn vốn, thời gian, CĐT." |
| 4 | **QĐ giao CĐT** | "Soạn quyết định giao chủ đầu tư dự án [tên DA]. Căn cứ: K4 Đ1 Luật XD số 62. Giao [đơn vị] làm CĐT." |
| 5 | **Nhiệm vụ khảo sát** | "Soạn nhiệm vụ khảo sát địa hình tỷ lệ 1/500 cho dự án [tên] tại [địa chỉ], diện tích [X]m2. Gồm: mục đích, phạm vi, yêu cầu kỹ thuật, sản phẩm giao nộp, thời gian." |
| 6 | **BCKTKT outline** | "Lập outline Báo cáo kinh tế kỹ thuật đầu tư xây dựng theo Điều 5 NĐ 175/2024 cho dự án [loại], nhóm C, TMĐT [X tỷ]. Liệt kê đầy đủ các mục cần có." |

### B. Tóm tắt & Phân tích văn bản

| # | Mục đích | Prompt mẫu |
|---|----------|------------|
| 7 | **Tóm tắt Nghị định** | "Tóm tắt NĐ [số] trong 10 điểm chính. Highlight: thời gian thẩm định, đơn vị thực hiện, biểu mẫu áp dụng, điểm mới so với NĐ cũ." |
| 8 | **Tổng hợp ý kiến** | "Tổng hợp các ý kiến góp ý sau thành bảng gồm cột: Đơn vị, Nội dung ý kiến, Tiếp thu/Giải trình. Các ý kiến: [paste nội dung]" |
| 9 | **So sánh VB** | "So sánh [VB cũ] và [VB mới]: điểm khác nhau chính, tác động đến quy trình CBDA, cần lưu ý gì khi áp dụng." |

### C. Email hành chính

| # | Mục đích | Prompt mẫu |
|---|----------|------------|
| 10 | **Email sở ngành** | "Soạn email gửi [Sở X] đề nghị [cung cấp chỉ giới đường đỏ / thẩm định BCKTKT / góp ý hồ sơ]. Dự án: [tên]. Tone trang trọng, kèm danh mục hồ sơ đính kèm." |
| 11 | **Email xin ý kiến** | "Soạn email gửi [đơn vị] xin ý kiến về [hồ sơ CTrĐT / BCKTKT]. Thời hạn trả lời: [X ngày]. Kèm file đính kèm: [liệt kê]." |
| 12 | **Tóm tắt email thread** | "Tóm tắt chuỗi email này trong 5 điểm chính. Highlight: action items, deadline, ai chịu trách nhiệm." |

---

## TRANG 2: GEMINI SHEETS + NOTEBOOKLM

### D. Gemini Sheets — Phân tích chi phí & Dữ liệu

| # | Mục đích | Prompt mẫu |
|---|----------|------------|
| 13 | **Dự toán CBDA** | "Tạo bảng dự toán chi phí CBDA gồm cột: STT, Hạng mục, Đơn giá, Khối lượng, Thành tiền. Các hạng mục: TV lập BCKTKT, TV khảo sát (ĐH, ĐC), TV giám sát KS, TV môi trường, TV thẩm tra, chi phí khác." |
| 14 | **KH LCNT** | "Tạo kế hoạch LCNT theo Mẫu 02A TT79: cột STT, Tên gói thầu, Nguồn vốn, Hình thức LCNT, Phương thức, Thời gian BĐ, Loại HĐ, Thời gian TH. Gồm [X] gói thầu tư vấn CBDA." |
| 15 | **So sánh chi phí** | "So sánh cột Dự toán (B) vs Thực tế (C). Tính % chênh lệch ở cột D. Conditional formatting: xanh nếu ≤10%, đỏ nếu >10%. Tổng hợp cuối bảng." |
| 16 | **Dashboard** | "Tạo biểu đồ: (1) Cột so sánh dự toán vs thực tế theo hạng mục; (2) Tròn tỷ lệ cơ cấu chi phí; (3) Đường tiến độ giải ngân theo tháng. Từ dữ liệu [range]." |
| 17 | **Tổng hợp khối lượng** | "Tổng hợp khối lượng khảo sát: cột STT, Hạng mục, Đơn vị, Khối lượng, Đơn giá, Thành tiền. Gồm: đo đạc ĐH, khoan thăm dò ĐC, thí nghiệm mẫu đất, đo mực nước ngầm." |

### E. NotebookLM — Tra cứu pháp lý

| # | Mục đích | Prompt mẫu |
|---|----------|------------|
| 18 | **Tra cứu thời hạn** | "Thời gian thẩm định dự án nhóm [A/B/C] là bao lâu? Trích dẫn điều khoản cụ thể từ NĐ 85." |
| 19 | **Tra thẩm quyền** | "Ai có thẩm quyền quyết định CTrĐT dự án nhóm C sử dụng vốn ĐTC? Căn cứ điều nào của Luật ĐTC 58?" |
| 20 | **So sánh quy trình** | "So sánh quy trình lập BCKTKT và BCNCKT: đối tượng áp dụng, nội dung, đơn vị thẩm định, thời gian thẩm định, biểu mẫu. Trình bày dạng bảng." |
| 21 | **Checklist hồ sơ** | "Liệt kê TẤT CẢ hồ sơ cần nộp cho [Bước X] giai đoạn CBDA. Kèm: đơn vị lập, đơn vị nhận, biểu mẫu theo TT nào." |
| 22 | **Tìm biểu mẫu** | "Liệt kê tất cả biểu mẫu trong TT 79/2025 cần dùng cho giai đoạn CBDA. Kèm: số hiệu mẫu, tên mẫu, dùng cho bước nào." |
| 23 | **Phân tích điều khoản** | "Phân tích Điều [X] của [NĐ/Luật]: áp dụng cho trường hợp nào, ngoại lệ, điều kiện, thời hạn, chế tài nếu vi phạm." |
| 24 | **Tạo FAQ** | "Tạo 10 câu hỏi thường gặp nhất về quy trình CBDA dựa trên tài liệu đã upload. Kèm câu trả lời ngắn gọn." |

---

### 💡 MẸO PROMPT HIỆU QUẢ

```
CẤU TRÚC PROMPT TỐT:
[Vai trò] + [Hành động] + [Đối tượng] + [Ngữ cảnh] + [Format]

VÍ DỤ:
"Với tư cách Chủ đầu tư (vai trò),
 soạn tờ trình (hành động)
 đề nghị phê duyệt CTrĐT (đối tượng)
 dự án cải tạo trụ sở nhóm C, TMĐT 15 tỷ (ngữ cảnh).
 Format tờ trình hành chính VN, kính gửi UBND quận (format)."
```

| Kém | Tốt |
|-----|-----|
| "Soạn tờ trình" | "Soạn tờ trình CTrĐT dự án nhóm C, 15 tỷ, kính gửi UBND quận" |
| "Tra cứu luật" | "Thời gian thẩm định DA nhóm B theo NĐ 85? Trích dẫn điều khoản" |
| "Phân tích dữ liệu" | "So sánh cột B vs C, highlight chênh lệch >10%, tổng hợp cuối" |
