# GEMINI TRONG GOOGLE WORKSPACE — HƯỚNG DẪN NHANH

> Quick Reference Guide | Chương trình đào tạo AI cho công ty thầu XD
> In A4, 2 mặt, laminate

---

## MẶT TRƯỚC

### GOOGLE DOCS — Soạn thảo văn bản với AI

**Cách mở:** Click biểu tượng ✨ (Gemini) ở thanh bên phải → Side panel mở ra

#### Soạn văn bản mới
```
Prompt: "Soạn tờ trình [loại] theo format hành chính Việt Nam.
Kính gửi: [đơn vị]. Căn cứ: [liệt kê VB pháp luật].
Nội dung đề nghị: [mô tả ngắn gọn]."
```

**Ví dụ thực tế:**
```
"Soạn tờ trình đề nghị phê duyệt chủ trương đầu tư dự án
cải tạo trụ sở UBND phường X. Kính gửi: UBND quận Y.
Căn cứ: NĐ 175/2024, Luật ĐTC 58. TMĐT: 15 tỷ đồng."
```

#### Tóm tắt văn bản dài
```
"Tóm tắt văn bản sau trong 10 điểm chính.
Highlight: deadline, đơn vị thực hiện, biểu mẫu áp dụng."
```

#### Chỉnh sửa & Hoàn thiện
```
"Viết lại phần căn cứ pháp lý, thêm NĐ 175/2024 và Luật ĐTC 58."
"Chuyển tone trang trọng hơn, format đúng mẫu hành chính."
"Rút gọn đoạn này còn 3 câu, giữ nguyên ý chính."
```

#### 💡 Mẹo Docs
- **Prompt chaining**: Hỏi → Nhận bản nháp → Chỉnh sửa → Hoàn thiện
- Càng **cụ thể** → output càng chính xác
- Ghi rõ **format mong muốn**: bullets, bảng, đánh số
- Nêu **vai trò**: "Viết với tư cách Chủ đầu tư gửi Sở Xây dựng"

---

### GMAIL — Soạn & Tóm tắt email

**Cách mở:** Compose email mới → Click "Help me write" hoặc ✨

#### Soạn email mới
```
"Soạn email gửi Sở QHKT Hà Nội đề nghị cung cấp chỉ giới
đường đỏ cho dự án [tên DA] tại [địa chỉ].
Tone trang trọng, kèm danh mục hồ sơ đính kèm."
```

#### Tóm tắt chuỗi email
Mở email thread → Click ✨ → "Summarize this email thread"
```
"Tóm tắt chuỗi email này: 5 điểm chính,
highlight action items và deadline."
```

#### Điều chỉnh tone
```
"Viết lại email này trang trọng hơn / ngắn gọn hơn /
thêm lời cảm ơn cuối email."
```

#### 💡 Mẹo Gmail
- Ghi rõ **người nhận** + **mục đích** + **tone** trong prompt
- Dùng "Formalize" để chuyển email sang tone hành chính

---

## MẶT SAU

### GOOGLE SHEETS — Phân tích dữ liệu với AI

**Cách mở:** Click ✨ ở thanh bên phải → Side panel

#### Tạo công thức từ mô tả
```
"Tạo công thức tính tổng chi phí xây dựng =
chi phí vật liệu + nhân công + máy thi công +
chi phí QLDA + chi phí tư vấn, từ cột B2:B6."
```

#### Phân tích dữ liệu
```
"Phân tích dữ liệu: so sánh cột Dự toán (B) vs Thực tế (C),
tính % chênh lệch, highlight hạng mục chênh >10%."
```

#### Tạo biểu đồ
```
"Tạo biểu đồ cột so sánh tiến độ giải ngân theo tháng
từ dữ liệu A1:D12."
```

#### 💡 Mẹo Sheets
- Mô tả bằng **tiếng Việt** → Gemini hiểu tốt
- Chỉ rõ **range** dữ liệu (VD: A1:D12)
- Dùng cho: dự toán, tổng hợp chi phí, theo dõi tiến độ

---

### GOOGLE SLIDES — Tạo bài thuyết trình

**Cách mở:** File mới → ✨ "Help me create"

#### Tạo slide từ prompt
```
"Tạo bài thuyết trình 5 slides về tiến độ dự án cải tạo
trụ sở UBND phường X. Bao gồm: tổng quan, tiến độ,
ngân sách, rủi ro, bước tiếp theo."
```

#### Thêm speaker notes
Chọn slide → ✨ → "Generate speaker notes for this slide"

---

### ⚠️ QUY TẮC VÀNG KHI DÙNG AI

| ✅ NÊN | ❌ KHÔNG |
|--------|----------|
| Kiểm tra MỌI output trước khi dùng | Tin 100% AI mà không review |
| Dùng AI cho bản nháp đầu tiên | Upload thông tin bảo mật |
| Ghi chú "Bản nháp AI, đã kiểm tra" | Bỏ qua bước review chuyên môn |
| Prompt càng cụ thể càng tốt | Prompt mơ hồ "soạn giúp cái gì đó" |

**AI = Trợ lý thông minh | Bạn = Người quyết định cuối cùng**
