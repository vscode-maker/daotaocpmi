# Brainstorm: Rút Gọn Chương Trình Đào Tạo AI Google

**Date:** 2026-04-09
**Ref:** [Brainstorm gốc](brainstorm-260409-1434-chuong-trinh-dao-tao-ai-google-cho-cong-ty-thau.md)
**Thay đổi**: 2x6h → 2x3h (buổi chiều 13:30–16:30)

---

## Phân tích cắt giảm

| Phiên gốc | Thời lượng gốc | Quyết định | Thời lượng mới | Lý do |
|---|---|---|---|---|
| Demo WOW | 30' | **GIỮ** ngắn lại | 15' | Bắt buộc, tạo hứng thú |
| Gemini Docs | 40' | **GIỮ** | 30' | Core tool, cắt bài tập phụ |
| Gemini Gmail | 25' | **GỘP** demo nhanh | 10' | Demo + 1 bài tập |
| Gemini Slides | 25' | **CẮT** | 0' | HV tự khám phá, ít dùng nhất |
| Gemini Sheets | 45' | **GỘP** demo nhanh | 10' | Demo + 1 bài tập |
| NotebookLM | 90' | **GIỮ** rút gọn | 45' | Core tool, cắt Audio cộng tác |
| Workflow combo | 75' | **GIỮ** rút gọn | 30' | Quan trọng, giảm scope |
| Q&A Ngày 1 | 30' | **GIỮ** | 15' | |
| Ôn tập | 30' | **GIỮ** ngắn | 10' | |
| Lab 1 PB | 90' | **GỘP** vào Lab ngắn | 40' | 1 bài tập/nhóm thay vì 4 bước |
| Lab 2 Hồ sơ | 45' | **CẮT** gộp Lab 1 | 0' | Gộp vào Lab PB |
| Lab 3 CBDA E2E | 90' | **GIỮ** rút gọn | 60' | Core, giảm 5→3 bước |
| Trình bày | 60' | **GIỮ** ngắn | 15' | 1-2 nhóm thay vì tất cả |
| Bế mạc | 45' | **GIỮ** | 25' | |

**Tổng gốc**: 720' (12h) → **Tổng mới**: 305' (~5.1h, phù hợp 2x3h có giải lao)

---

## CHƯƠNG TRÌNH RÚT GỌN

### NGÀY 1 (13:30–16:30): LÀM CHỦ CÔNG CỤ AI GOOGLE

| Thời gian | Phiên | TL | Nội dung |
|-----------|-------|-----|----------|
| 13:30–13:45 | **Khai mạc + Demo WOW** | 15' | Demo LIVE NotebookLM (hỏi NĐ 175) + Gemini Docs (soạn tờ trình 30s). Không dạy lý thuyết. |
| 13:45–14:15 | **Workshop Gemini Docs** | 30' | 5' demo → 20' thực hành (soạn tờ trình CTrĐT + tóm tắt VB) → 5' chia sẻ |
| 14:15–14:35 | **Demo nhanh Gmail + Sheets** | 20' | Gmail: demo soạn email Sở QHKT + 1 bài tập 5' (10'). Sheets: demo phân tích dự toán + 1 bài tập 5' (10'). |
| 14:35–14:45 | ☕ **Giải lao** | 10' | |
| 14:45–15:30 | **Workshop NotebookLM** | 45' | 5' demo upload PDF → 15' thực hành hỏi đáp PL XD → 10' Audio Overview (demo + tạo) → 15' bài tập: hỏi 5 câu về CBDA |
| 15:30–16:00 | **Bài tập tổng hợp** | 30' | Nhóm 4-5 người, mô phỏng 2 bước CBDA: (1) NLM tra cứu Đ35 Luật ĐTC → (2) Gemini Docs soạn tờ trình → (3) Gemini Gmail soạn email thẩm định |
| 16:00–16:15 | **Q&A + Tips** | 15' | Tips hay nhất, prompt cheat sheet |
| 16:15–16:30 | **Wrap-up** | 15' | Bài tập về nhà: dùng AI cho 1 việc thật. Preview Ngày 2. |

**Sản phẩm Ngày 1**: 1 tờ trình + 1 email + 1 Notebook PL + 1 bộ hồ sơ mini nhóm

---

### NGÀY 2 (13:30–16:30): ỨNG DỤNG QUY TRÌNH CBDA

| Thời gian | Phiên | TL | Nội dung |
|-----------|-------|-----|----------|
| 13:30–13:40 | **Ôn tập nhanh** | 10' | 3 câu quiz + 2-3 HV chia sẻ bài tập về nhà |
| 13:40–14:20 | **Lab nhóm phòng ban** | 40' | 4 nhóm (KT, HC, ĐT, TH), mỗi nhóm 1 bài tập nghiệp vụ: |
| | | | **KT+QLDA**: NLM tra cứu KS theo NĐ 175 → Docs soạn nhiệm vụ KS |
| | | | **HC+KT**: NLM tra cứu dự toán CBDA → Docs soạn tờ trình dự toán |
| | | | **ĐT+PC**: NLM tra cứu LCNT theo Luật ĐT → Sheets lập KH LCNT |
| | | | **Tổng hợp**: NLM tổng hợp quy trình CTrĐT → Slides báo cáo LD |
| 14:20–14:30 | ☕ **Giải lao** | 10' | |
| 14:30–15:30 | **Mô phỏng CBDA E2E** | 60' | Nhóm hỗn hợp (đủ PB). Dự án "Cải tạo trụ sở UBND phường X" |
| | | | **Bước 1** (15'): Lập BC đề xuất CTrĐT (NLM + Docs) |
| | | | **Bước 2** (15'): Thẩm định + tổng hợp ý kiến (NLM + Gmail + Sheets) |
| | | | **Bước 3** (15'): Hoàn chỉnh + QĐ CTrĐT (Docs chỉnh sửa) |
| | | | **Tổng kết** (15'): Review sản phẩm, so sánh thủ công vs AI |
| 15:30–15:45 | **Trình bày nhanh** | 15' | 1-2 nhóm demo sản phẩm CBDA (7'/nhóm) |
| 15:45–16:05 | **Bảo mật + KH 30 ngày** | 20' | 5 điều NÊN / 5 điều KHÔNG. Mỗi HV viết 3 việc dùng AI. Ghép buddy. |
| 16:05–16:20 | **Đánh giá** | 15' | Google Forms 10 câu (QR code). Điền tại chỗ. |
| 16:20–16:30 | **Bế mạc** | 10' | Phát chứng nhận, chụp ảnh, cảm ơn. |

**Sản phẩm Ngày 2**: 1 hồ sơ nghiệp vụ riêng + 1 bộ hồ sơ CBDA E2E nhóm

---

## So sánh gốc vs rút gọn

| Tiêu chí | Gốc (12h) | Rút gọn (6h) |
|----------|-----------|---------------|
| Gemini Docs | Chuyên sâu (40') | Đủ dùng (30') |
| Gemini Gmail | Workshop riêng (25') | Demo + 1 bài tập (10') |
| Gemini Slides | Workshop riêng (25') | CẮT (self-learn) |
| Gemini Sheets | Workshop riêng (45') | Demo + 1 bài tập (10') |
| NotebookLM | Chuyên sâu (90') | Core features (45') |
| CBDA E2E | 5 bước đầy đủ (90') | 3 bước chính (60') |
| Lab phòng ban | 90' + 45' riêng | 1 bài tập 40' |
| Trình bày | 60' tất cả nhóm | 15' chọn lọc |
| Follow-up | Đầy đủ | Giữ nguyên |

## Trade-offs chấp nhận được

| Mất | Được |
|-----|------|
| Slides deep dive | HV tự học (QRG đủ) |
| Sheets deep dive | Demo đủ gợi ý, HV tự khám phá |
| NotebookLM cộng tác | Chỉ cần biết share, tự dùng |
| Audio Overview thực hành | Demo đủ hiểu, tự làm sau |
| Lab PB dài | 1 bài tập tập trung, vẫn đủ context |
| CBDA 5 bước → 3 bước | 3 bước chính đủ nắm workflow |

## Tài liệu cần điều chỉnh

| Tài liệu | Thay đổi |
|-----------|----------|
| Slides bài giảng | 12 bộ → 8 bộ (gộp Gmail+Sheets, bỏ Slides) |
| Prompt templates | Giữ nguyên (HV dùng self-learn) |
| QRG | Giữ nguyên |
| Kịch bản dự án Lab 3 | 5 bước → 3 bước |
| Tài liệu giả lập | Giữ nguyên (dùng cho self-learn) |
| Checklist bảo mật | Giữ nguyên |

## Unresolved Questions
1. Slides deep dive + Sheets deep dive: có cần tổ chức thêm 1 buổi nâng cao riêng cho power users?
