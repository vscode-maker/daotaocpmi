---
title: Chương Trình Đào Tạo Ứng Dụng AI Google Cho Công Ty Thầu CPMI
status: pending
created: 2026-04-09
updated: 2026-04-09
type: training-program
duration: 2 ngày x 3 tiếng buổi chiều (13:30-16:30)
audience: 20-50 NV văn phòng
tools: Google Gemini, NotebookLM, Google Workspace
blockedBy: []
blocks: []
---

# Kế Hoạch Triển Khai Đào Tạo AI Google Cho Công Ty Thầu

## Tổng quan
Chương trình đào tạo 2 buổi chiều (3h/buổi) ứng dụng AI (Gemini + NotebookLM) vào quy trình QLDA giai đoạn CBDA cho công ty thầu xây dựng.

**Cấu trúc**: Tool-First → Ngày 1 làm chủ công cụ, Ngày 2 ứng dụng quy trình CBDA
**Tài liệu**: VB pháp luật thật (công khai) + tờ trình/dự toán giả lập
**Version**: Rút gọn từ 2x6h → 2x3h (Balanced Cut)

## Agenda tóm tắt

### Ngày 1 (13:30–16:30): Làm Chủ Công Cụ
| Thời gian | Phiên | TL |
|-----------|-------|-----|
| 13:30–13:45 | Khai mạc + Demo WOW | 15' |
| 13:45–14:15 | Workshop Gemini Docs | 30' |
| 14:15–14:35 | Demo nhanh Gmail + Sheets | 20' |
| 14:35–14:45 | Giải lao | 10' |
| 14:45–15:30 | Workshop NotebookLM | 45' |
| 15:30–16:00 | Bài tập tổng hợp (2 bước CBDA) | 30' |
| 16:00–16:30 | Q&A + Wrap-up | 30' |

### Ngày 2 (13:30–16:30): Ứng Dụng CBDA
| Thời gian | Phiên | TL |
|-----------|-------|-----|
| 13:30–13:40 | Ôn tập nhanh | 10' |
| 13:40–14:20 | Lab nhóm phòng ban | 40' |
| 14:20–14:30 | Giải lao | 10' |
| 14:30–15:30 | Mô phỏng CBDA E2E (3 bước) | 60' |
| 15:30–15:45 | Trình bày nhanh | 15' |
| 15:45–16:05 | Bảo mật + KH 30 ngày | 20' |
| 16:05–16:30 | Đánh giá + Bế mạc | 25' |

## Context
- Brainstorm gốc: [brainstorm report](../reports/brainstorm-260409-1434-chuong-trinh-dao-tao-ai-google-cho-cong-ty-thau.md)
- Brainstorm rút gọn: [condensed report](../reports/brainstorm-260409-2121-rut-gon-chuong-trinh-dao-tao-ai.md)
- Research: [research report](../reports/researcher-260409-1432-ai-training-program-research.md)
- Tài liệu gốc: `Quy trình QLDA giai đoạn CBDA-2026.pptx`

## Phases

| # | Phase | Trạng thái | Ưu tiên | Effort |
|---|-------|-----------|---------|--------|
| 1 | [Chuẩn bị tài liệu pháp luật & giả lập](phase-01-chuan-bi-tai-lieu.md) | pending | P0 | 3-5 ngày |
| 2 | [Setup kỹ thuật & tài khoản](phase-02-setup-ky-thuat.md) | pending | P0 | 2-3 ngày |
| 3 | [Thiết kế slide bài giảng 8 phiên](phase-03-slide-bai-giang.md) | pending | P1 | 3-4 ngày |
| 4 | [Prompt templates & Quick Reference Guides](phase-04-prompt-templates-va-guides.md) | pending | P1 | 2-3 ngày |
| 5 | [Kịch bản chi tiết Ngày 1](phase-05-kich-ban-ngay-1.md) | pending | P1 | 1 ngày |
| 6 | [Kịch bản chi tiết Ngày 2](phase-06-kich-ban-ngay-2.md) | pending | P1 | 1 ngày |
| 7 | [Checklist tổ chức & Logistics](phase-07-checklist-to-chuc.md) | pending | P0 | 1-2 ngày |
| 8 | [Đánh giá & Kế hoạch follow-up 30 ngày](phase-08-danh-gia-follow-up.md) | pending | P2 | 1 ngày |

## Timeline tổng thể

```
Tuần 1 (T-14): Phase 1 + 2 (song song) — Thu thập tài liệu + Setup kỹ thuật
Tuần 2 (T-7):  Phase 3 + 4 + 5 + 6 (song song) — Slide + Guides + Kịch bản
T-3 ngày:      Phase 7 — Checklist logistics cuối
T-1 ngày:      Dry run (chạy thử toàn bộ, ~1h đủ)
Ngày D:        Đào tạo Ngày 1 (13:30–16:30)
Ngày D+1:      Đào tạo Ngày 2 (13:30–16:30)
D+14:          Phase 8 — Follow-up lần 1
D+30:          Follow-up lần 2
```

## Dependencies
- Google Workspace license (Business Standard+) cho tất cả học viên
- Gemini enabled trong Admin Console
- WiFi ổn định (50+ devices)
- 1 giảng viên chính + 1-2 trợ giảng (giảm từ 2-3)
