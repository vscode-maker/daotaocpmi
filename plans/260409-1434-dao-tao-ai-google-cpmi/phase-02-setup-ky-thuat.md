# Phase 2: Setup Kỹ Thuật & Tài Khoản

**Priority**: P0 (song song với Phase 1)
**Status**: pending
**Effort**: 2-3 ngày
**Deadline**: T-7

## Overview
Đảm bảo hạ tầng kỹ thuật sẵn sàng: Google Workspace license, Gemini enabled, tài khoản học viên, WiFi, thiết bị.

## Checklist Setup

### A. Google Workspace & Gemini
- [ ] Xác nhận license Google Workspace (Business Standard trở lên)
- [ ] Bật Gemini trong Admin Console (Settings > Gemini)
- [ ] Bật NotebookLM cho tất cả user (Apps > Additional Google Services)
- [ ] Tạo/kiểm tra tài khoản Google cho từng học viên (20-50 TK)
- [ ] Tạo Organizational Unit "DaoTaoAI" trong Admin Console để quản lý quyền
- [ ] Test: đăng nhập 1 TK mẫu → mở Gemini Docs/Sheets/Gmail/Slides → xác nhận Gemini sidebar hiện
- [ ] Test: mở notebooklm.google.com → xác nhận tạo notebook + Audio Overview được

### B. Google Drive — Thư mục chia sẻ
- [ ] Tạo Shared Drive: "Đào Tạo AI - CPMI"
- [ ] Cấu trúc thư mục:
  ```
  Đào Tạo AI - CPMI/
  ├── 01-Van-Ban-Phap-Luat/       (8 PDF)
  ├── 02-Tai-Lieu-Gia-Lap/        (8 files mẫu)
  ├── 03-Bai-Tap-Thuc-Hanh/       (template cho HV copy)
  ├── 04-Slides-Bai-Giang/        (12 phiên)
  ├── 05-Quick-Reference-Guides/  (2 QRG + prompt templates)
  └── 06-Ket-Qua-Hoc-Vien/       (HV lưu bài tập tại đây)
  ```
- [ ] Set quyền: học viên = Editor cho thư mục 06, Viewer cho còn lại
- [ ] Test: HV mẫu truy cập → copy file → chỉnh sửa được

### C. Phòng đào tạo & Thiết bị
- [ ] Phòng đào tạo: sức chứa 50 người, có ổ cắm điện đủ
- [ ] Máy chiếu + loa (test trước: play Audio Overview NotebookLM)
- [ ] WiFi: test với 50+ devices đồng thời (download speed ≥ 50Mbps)
- [ ] Backup: 2-3 USB 4G hotspot (phòng WiFi chết)
- [ ] Bảng trắng/flipchart cho Q&A

### D. Laptop học viên
- [ ] Gửi email trước 3 ngày: yêu cầu mang laptop, sạc đầy pin
- [ ] Chrome browser cập nhật mới nhất
- [ ] Đã đăng nhập Google Workspace trước buổi học
- [ ] Chuẩn bị 5 laptop dự phòng cho người không mang

## Rủi ro & Giảm thiểu

| Rủi ro | Giảm thiểu |
|--------|------------|
| Công ty dùng M365 không có Google Workspace | Dùng TK Google cá nhân + trial Workspace 14 ngày |
| Admin Console không bật Gemini | IT admin bật trước 3 ngày, test ngay |
| WiFi quá tải | 4G backup + giảm số HV mỗi phiên |
| HV quên laptop | 5 máy dự phòng |
| Gemini không khả dụng tại VN | Test trước; fallback: dùng gemini.google.com trực tiếp |

## Todo
- [ ] Liên hệ IT admin xác nhận Google Workspace license
- [ ] Bật Gemini + NotebookLM trong Admin Console
- [ ] Tạo/kiểm tra 50 tài khoản học viên
- [ ] Tạo Shared Drive với cấu trúc thư mục
- [ ] Test toàn bộ workflow trên 1 TK mẫu
- [ ] Kiểm tra phòng đào tạo + WiFi + thiết bị
- [ ] Gửi email thông báo + yêu cầu chuẩn bị cho học viên

## Success Criteria
- 100% học viên có TK Google Workspace + Gemini enabled
- Shared Drive truy cập được từ mọi TK
- WiFi test OK với 50 devices
- Dry run: 1 người chạy thử toàn bộ flow Phiên 1-6 không lỗi
