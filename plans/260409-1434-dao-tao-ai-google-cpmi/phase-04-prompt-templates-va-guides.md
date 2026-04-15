# Phase 4: Prompt Templates & Quick Reference Guides

**Priority**: P1
**Status**: pending
**Effort**: 2-3 ngày
**Deadline**: T-3
**Depends on**: Phase 1 (test prompt với tài liệu thật)

## Overview
Tạo 4 tài liệu phát tay cho học viên: 2 Quick Reference Guides (QRG) + 1 bảng prompt templates + 1 checklist bảo mật. In A4 2 mặt, laminate.

## Deliverable 1: QRG Gemini trong Workspace (1 trang A4, 2 mặt)

### Mặt trước: Gemini Docs + Gmail
```
GEMINI TRONG GOOGLE WORKSPACE — HƯỚNG DẪN NHANH

GOOGLE DOCS
┌─────────────────────────────────────────┐
│ Mở: Biểu tượng ✨ bên phải → Side panel │
│                                         │
│ SOẠN MỚI:                               │
│ "Giúp tôi soạn [loại VB] về [chủ đề]   │
│  theo format hành chính VN"             │
│                                         │
│ TÓM TẮT:                                │
│ "Tóm tắt văn bản này trong [X] điểm,   │
│  highlight deadline và đơn vị thực hiện"│
│                                         │
│ CHỈNH SỬA:                              │
│ "Viết lại phần này ngắn gọn hơn / trang│
│  trọng hơn / thêm căn cứ pháp lý"      │
└─────────────────────────────────────────┘

GMAIL
┌─────────────────────────────────────────┐
│ Compose → "Help me write" hoặc ✨       │
│                                         │
│ SOẠN EMAIL:                              │
│ "Soạn email gửi [đơn vị] đề nghị       │
│  [nội dung]. Tone trang trọng."         │
│                                         │
│ TÓM TẮT THREAD:                         │
│ Mở email → ✨ → "Summarize this thread" │
└─────────────────────────────────────────┘
```

### Mặt sau: Gemini Sheets + Slides
```
GOOGLE SHEETS
┌─────────────────────────────────────────┐
│ Mở: Side panel ✨ hoặc cell prompt      │
│                                         │
│ CÔNG THỨC:                               │
│ "Tạo công thức tính [mô tả] từ cột [X]"│
│                                         │
│ PHÂN TÍCH:                               │
│ "Phân tích dữ liệu: so sánh [A] vs [B],│
│  highlight chênh lệch >10%"            │
│                                         │
│ BIỂU ĐỒ:                                │
│ "Tạo biểu đồ [loại] từ dữ liệu [range]"│
└─────────────────────────────────────────┘

GOOGLE SLIDES
┌─────────────────────────────────────────┐
│ Tạo mới: ✨ "Create slides about [topic]"│
│ Speaker notes: Chọn slide → ✨ →        │
│ "Generate speaker notes"                │
└─────────────────────────────────────────┘

💡 MẸO CHUNG
• Prompt tiếng Việt hoạt động tốt
• Càng cụ thể → output càng chính xác
• Prompt chaining: hỏi → chỉnh → hoàn thiện
• LUÔN kiểm tra lại output trước khi dùng
```

## Deliverable 2: QRG NotebookLM (1 trang A4, 2 mặt)

### Mặt trước: Tạo & Sử dụng Notebook
```
NOTEBOOKLM — HƯỚNG DẪN NHANH

TẠO NOTEBOOK MỚI
1. Mở notebooklm.google.com
2. [+ New notebook]
3. Upload nguồn: PDF, Docs, Slides, URL, text
   (tối đa 50 nguồn/notebook)

HỎI ĐÁP VỚI TÀI LIỆU
┌─────────────────────────────────────────┐
│ Gõ câu hỏi vào chat box phía dưới       │
│                                         │
│ VÍ DỤ:                                   │
│ "Thời gian thẩm định DA nhóm B là      │
│  bao lâu? Trích dẫn điều khoản."       │
│                                         │
│ "So sánh quy trình phê duyệt nhóm A    │
│  vs nhóm C: khác nhau ở điểm nào?"     │
│                                         │
│ "Liệt kê biểu mẫu cần nộp Bước 3 CBDA"│
│                                         │
│ ✅ AI trích dẫn nguồn → click để xác minh│
└─────────────────────────────────────────┘
```

### Mặt sau: Audio Overview & Chia sẻ
```
TẠO AUDIO OVERVIEW
1. Trong notebook → [Audio Overview]
2. Tùy chỉnh: gõ focus area (VD: "tập trung phần thẩm định")
3. Chờ 2-5 phút → nghe podcast tóm tắt
4. Interactive: click "Join" để hỏi thêm trong khi nghe

CHIA SẺ NOTEBOOK
1. [Share] → nhập email đồng nghiệp
2. Quyền: Viewer (chỉ xem) / Editor (chỉnh sửa)
3. Use case: nhóm dự án cùng review hồ sơ

TẠO NỘI DUNG KHÁC
• Study guide: tóm tắt cấu trúc tài liệu
• FAQ: câu hỏi thường gặp từ tài liệu
• Timeline: sự kiện theo thời gian
• Briefing doc: bản tóm tắt 1 trang

⚠️ LƯU Ý
• NotebookLM CHỈ trả lời dựa trên nguồn bạn upload
• Không bịa thông tin từ bên ngoài
• Nhưng vẫn cần kiểm tra lại với văn bản gốc
```

## Deliverable 3: Bảng Prompt Templates Ngành XD (2 trang A4)

### Trang 1: Gemini Docs + Gmail

| Mục đích | Prompt mẫu |
|----------|------------|
| Tờ trình CTrĐT | "Soạn tờ trình đề nghị phê duyệt chủ trương đầu tư dự án [tên]. Kính gửi: [đơn vị]. Căn cứ: NĐ 175/2024, Luật ĐTC 58. Nội dung: [mô tả]." |
| Tóm tắt NĐ | "Tóm tắt Nghị định [số] trong 10 điểm chính, highlight: thời gian thẩm định, đơn vị thực hiện, biểu mẫu áp dụng." |
| BCKTKT outline | "Lập outline Báo cáo KTKT theo Điều 5 NĐ 175 cho dự án [loại] quy mô [X tỷ đồng]." |
| Nhiệm vụ KS | "Soạn nhiệm vụ khảo sát địa hình tỷ lệ 1/500 cho khu vực [X] diện tích [Y]m2." |
| Email sở ngành | "Soạn email gửi [Sở X] đề nghị [nội dung]. Tone trang trọng, kèm danh mục hồ sơ." |
| Tổng hợp ý kiến | "Tổng hợp các ý kiến sau thành bảng: đơn vị góp ý, nội dung, tiếp thu/giải trình: [paste ý kiến]" |

### Trang 2: Gemini Sheets + NotebookLM

| Mục đích | Prompt mẫu |
|----------|------------|
| Dự toán CBDA | "Tạo bảng dự toán chi phí CBDA gồm: TV lập BCKTKT, TV khảo sát, TV giám sát KS, TV MT, TV thẩm tra. Cột: hạng mục, đơn giá, khối lượng, thành tiền." |
| KH LCNT | "Tạo kế hoạch LCNT theo Mẫu 02A TT79 cho giai đoạn CBDA gồm [X] gói thầu." |
| So sánh chi phí | "So sánh dự toán (cột B) vs thực tế (cột C), tính % chênh lệch, highlight >10%." |
| NLM: tra cứu | "Thời gian thẩm định dự án nhóm [A/B/C]? Trích dẫn điều khoản." |
| NLM: so sánh | "So sánh BCKTKT vs BCNCKT: đối tượng áp dụng, nội dung, đơn vị thẩm định?" |
| NLM: checklist | "Liệt kê TẤT CẢ hồ sơ cần nộp cho Bước [X] giai đoạn CBDA." |

## Deliverable 4: Checklist Bảo Mật AI (1 trang A4)

```
CHECKLIST BẢO MẬT KHI SỬ DỤNG AI

✅ NÊN LÀM:
□ Kiểm tra lại MỌI output AI trước khi gửi/trình ký
□ Dùng tài liệu công khai (luật, nghị định) upload NotebookLM
□ Xóa thông tin nhạy cảm trước khi paste vào Gemini
□ Ghi chú "Bản nháp tạo bởi AI, đã kiểm tra bởi [tên]"

❌ KHÔNG LÀM:
□ Upload hợp đồng có thông tin bảo mật
□ Upload dữ liệu tài chính chưa công bố
□ Upload thông tin cá nhân (CMND, tài khoản ngân hàng)
□ Tin 100% output AI mà không kiểm tra
□ Dùng AI output làm văn bản chính thức mà không review

⚠️ NHỚ:
• AI có thể SAI → trách nhiệm thuộc về NGƯỜI DÙNG
• AI = bản nháp đầu, Con người = quyết định cuối
• Khi nghi ngờ → hỏi chuyên gia, không hỏi AI
```

## Todo
- [ ] Thiết kế QRG Gemini Workspace (A4, 2 mặt)
- [ ] Thiết kế QRG NotebookLM (A4, 2 mặt)
- [ ] Soạn bảng prompt templates 2 trang
- [ ] Soạn checklist bảo mật 1 trang
- [ ] Test tất cả prompt mẫu → đảm bảo output tốt
- [ ] Layout đẹp, dễ đọc, font ≥ 10pt
- [ ] In ấn: 50 bộ x 4 tài liệu = 200 tờ (laminate QRG)
- [ ] Upload bản digital lên Shared Drive

## Success Criteria
- 4 tài liệu hoàn chỉnh, sẵn sàng in
- Tất cả prompt mẫu đã test → output chất lượng
- HV có thể dùng ngay QRG mà không cần nhớ bài giảng
