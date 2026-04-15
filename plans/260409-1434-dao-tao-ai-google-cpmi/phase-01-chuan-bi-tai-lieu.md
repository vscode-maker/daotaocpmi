# Phase 1: Chuẩn Bị Tài Liệu Pháp Luật & Giả Lập

**Priority**: P0 (phải hoàn thành trước tất cả)
**Status**: pending
**Effort**: 3-5 ngày
**Deadline**: T-7 (1 tuần trước đào tạo)

## Context
- [Brainstorm report](../reports/brainstorm-260409-1434-chuong-trinh-dao-tao-ai-google-cho-cong-ty-thau.md) — Mục 3: Tài liệu cần chuẩn bị
- Tài liệu gốc: `Quy trình QLDA giai đoạn CBDA-2026.pptx`

## Overview
Thu thập văn bản pháp luật thật (PDF) và tạo bộ tài liệu giả lập (tờ trình, dự toán, email mẫu) phục vụ thực hành 2 ngày.

## A. Tài liệu pháp luật thật (Thu thập PDF)

Tải từ nguồn công khai (thuvienphapluat.vn, vanban.chinhphu.vn):

| # | Văn bản | Dùng cho phiên |
|---|---------|----------------|
| 1 | Nghị định 175/2024/NĐ-CP | Demo khai mạc, NotebookLM, Lab CBDA |
| 2 | Luật Đầu tư công số 58/2024/QH15 | NotebookLM tra cứu, Lab 1 |
| 3 | Nghị định 85/2025/NĐ-CP (chi tiết Luật ĐTC) | Lab 1, Lab 3 |
| 4 | Nghị định 10/2021/NĐ-CP (quản lý chi phí XD) | Gemini Sheets, Lab 2 |
| 5 | Luật Đấu thầu 2023 | Nhóm ĐT+PC, Lab 1-2 |
| 6 | Thông tư 79/2025/TT-BTC (mẫu hồ sơ đấu thầu) | Nhóm ĐT+PC, Lab 2 |
| 7 | Nghị định 37/2015/NĐ-CP (hợp đồng xây dựng) | Tham khảo |
| 8 | Luật Xây dựng 2014 + sửa đổi số 62/2020 | Tham khảo |

**Yêu cầu**: PDF có text (searchable), không phải scan ảnh. Test upload vào NotebookLM trước.

## B. Tài liệu giả lập (Cần tạo mới)

### B1. Kịch bản dự án mẫu
**Dự án**: "Cải tạo nâng cấp Trụ sở UBND phường Đông Ngạc, quận Bắc Từ Liêm"
- Nhóm dự án: C
- Nguồn vốn: Đầu tư công (ngân sách quận)
- Tổng mức đầu tư dự kiến: 15 tỷ đồng
- Quy mô: Cải tạo 3 tầng, diện tích ~800m2

### B2. Danh sách tài liệu giả lập

| # | Tài liệu | Format | Dùng cho | Nội dung |
|---|----------|--------|----------|----------|
| 1 | Tờ trình đề xuất CTrĐT | Google Docs | Phiên 2, 5 | Tờ trình UBND quận đề nghị phê duyệt CTrĐT dự án mẫu |
| 2 | Báo cáo đề xuất CTrĐT (nhóm C) | Google Docs | Lab 1, Lab 3 | Nội dung theo Đ35 Luật ĐTC 58, dự án mẫu |
| 3 | Bảng dự toán chi phí CBDA | Google Sheets | Phiên 3, Lab 2 | 10-15 hạng mục: tư vấn KS, tư vấn lập BCKTKT, TV giám sát, TV MT... |
| 4 | KH LCNT giai đoạn CBDA | Google Sheets | Phiên 5, Lab 2 | 5-8 gói thầu tư vấn, theo Mẫu 02A TT79 |
| 5 | Chuỗi email thẩm định | Gmail draft | Phiên 2 Gmail | 5-6 email mô phỏng trao đổi CĐT ↔ Sở XD ↔ Sở QHKT |
| 6 | Bảng tổng hợp ý kiến sở ngành | Google Sheets | Lab 2, Lab 3 | Ý kiến 4-5 sở: Sở XD, QHKT, TC, NNMT, Công an PCCC |
| 7 | File khối lượng khảo sát | Google Sheets | Lab 2 nhóm KT | Khối lượng: địa hình, địa chất, thủy văn |
| 8 | Nhiệm vụ khảo sát mẫu | Google Docs | Lab 1 nhóm KT | Nhiệm vụ KS địa hình tỷ lệ 1/500 |

### B3. Nguyên tắc tạo tài liệu giả lập
- Dùng tên dự án, địa chỉ, đơn vị giả lập (không dùng thông tin thật)
- Số liệu chi phí hợp lý (tham khảo đơn giá Hà Nội)
- Format đúng mẫu hành chính VN (kính gửi, căn cứ, đề nghị)
- Test trước trên Google Workspace đảm bảo Gemini xử lý được

## Todo

- [ ] Tải 8 văn bản PDF pháp luật
- [ ] Test upload từng PDF vào NotebookLM (kiểm tra searchable)
- [ ] Viết kịch bản dự án mẫu chi tiết
- [ ] Tạo 8 tài liệu giả lập (B2)
- [ ] Upload tất cả lên Google Drive thư mục "Đào tạo AI"
- [ ] Chia sẻ quyền truy cập cho tất cả tài khoản học viên
- [ ] Test thử NotebookLM + Gemini với tài liệu → đảm bảo output tốt

## Success Criteria
- 8 PDF pháp luật searchable, upload NotebookLM thành công
- 8 tài liệu giả lập hoàn chỉnh, format chuẩn
- Tất cả nằm trên Google Drive, học viên truy cập được
- Demo test: hỏi NotebookLM câu hỏi mẫu → trả lời chính xác có trích dẫn
