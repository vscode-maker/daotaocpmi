# Brainstorm: Website Đào Tạo AI - Static HTML

**Date:** 2026-04-09
**Decision:** Multi-page static HTML, password-protected GV section, deploy Vercel

## Architecture
- Pure HTML/CSS/JS, no framework
- ~20 pages: public (HV) + password-protected (GV)
- Markdown content embedded as HTML
- Client-side JS password for GV portal (sessionStorage)
- Deploy: Vercel static

## Pages
**Public**: index, agenda, qrg-gemini, qrg-notebooklm, prompts, checklist, 8 tài liệu giả lập
**GV only**: kịch bản ngày 1-2, plan, checklist tổ chức

## Tech
- CSS: modern, responsive, Vietnamese
- Nav: sidebar + breadcrumb
- Password: JS prompt → sessionStorage → redirect
