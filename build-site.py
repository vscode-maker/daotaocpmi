"""
Build script: Convert training markdown files to a static HTML website.
Reads .md files from tai-lieu-dao-tao/ and plans/, outputs to site/.
"""

import os
import re
import shutil

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(PROJECT_ROOT, "site")
MATERIALS_DIR = os.path.join(PROJECT_ROOT, "tai-lieu-dao-tao")
PLANS_DIR = os.path.join(PROJECT_ROOT, "plans", "260409-1434-dao-tao-ai-google-cpmi")

GV_PASSWORD = "gvcpmi2026"

# SVG icons (Lucide-style, 16x16 viewBox)
ICONS = {
    "home": '<svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    "sparkles": '<svg viewBox="0 0 24 24"><path d="M12 2L9 12l-7 3 7 3 3 10 3-10 7-3-7-3z"/></svg>',
    "book-open": '<svg viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    "message": '<svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "file-text": '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
    "clipboard": '<svg viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>',
    "coins": '<svg viewBox="0 0 24 24"><circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><line x1="7" y1="6" x2="7.01" y2="6"/><line x1="16" y1="12" x2="16.01" y2="12"/></svg>',
    "bar-chart": '<svg viewBox="0 0 24 24"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>',
    "mail": '<svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
    "edit": '<svg viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>',
    "search": '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    "ruler": '<svg viewBox="0 0 24 24"><path d="M21.71 5.29l-3-3a1 1 0 0 0-1.42 0l-14 14a1 1 0 0 0 0 1.42l3 3a1 1 0 0 0 1.42 0l14-14a1 1 0 0 0 0-1.42z"/><line x1="7" y1="13.5" x2="9.5" y2="11"/><line x1="10" y1="10.5" x2="12.5" y2="8"/><line x1="13" y1="7.5" x2="15.5" y2="5"/></svg>',
    "lock": '<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    "graduation": '<svg viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 2 3 3 6 3s6-1 6-3v-5"/></svg>',
    "check-circle": '<svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
    "folder": '<svg viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>',
    "info": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>',
    "menu": '<svg viewBox="0 0 24 24"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
}


def icon(name):
    """Return an SVG icon wrapped in a span."""
    svg = ICONS.get(name, ICONS["file-text"])
    return f'<span class="nav-icon">{svg}</span>'


def card_icon(name):
    """Return an SVG icon for card display."""
    svg = ICONS.get(name, ICONS["file-text"])
    return f'<div class="card-icon">{svg}</div>'


def md_to_html(md_content):
    """Minimal markdown to HTML converter — no external deps."""
    lines = md_content.split("\n")
    html_lines = []
    in_code_block = False
    in_table = False
    in_list = False
    in_blockquote = False
    table_header_done = False

    for line in lines:
        # Code blocks
        if line.strip().startswith("```"):
            if in_code_block:
                html_lines.append("</code></pre>")
                in_code_block = False
            else:
                lang = line.strip()[3:].strip()
                html_lines.append(f'<pre><code class="language-{lang}">')
                in_code_block = True
            continue

        if in_code_block:
            html_lines.append(escape_html(line))
            continue

        # Close blockquote if line doesn't start with >
        if in_blockquote and not line.startswith(">"):
            html_lines.append("</blockquote>")
            in_blockquote = False

        # Blockquote
        if line.startswith("> "):
            if not in_blockquote:
                html_lines.append("<blockquote>")
                in_blockquote = True
            html_lines.append(f"<p>{inline_format(line[2:])}</p>")
            continue

        # Table
        if "|" in line and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(set(c.strip()) <= set("- :") for c in cells):
                table_header_done = True
                continue
            if not in_table:
                html_lines.append('<div class="table-wrap"><table>')
                in_table = True
                table_header_done = False
            tag = "th" if not table_header_done else "td"
            row = "".join(f"<{tag}>{inline_format(c)}</{tag}>" for c in cells)
            html_lines.append(f"<tr>{row}</tr>")
            continue
        elif in_table:
            html_lines.append("</table></div>")
            in_table = False
            table_header_done = False

        # Close list
        if in_list and not line.strip().startswith(("- ", "* ", "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")):
            if not line.strip().startswith("  "):
                html_lines.append("</ul>")
                in_list = False

        stripped = line.strip()

        # Empty line
        if not stripped:
            html_lines.append("")
            continue

        # Headings
        if stripped.startswith("######"):
            html_lines.append(f"<h6>{inline_format(stripped[6:].strip())}</h6>")
        elif stripped.startswith("#####"):
            html_lines.append(f"<h5>{inline_format(stripped[5:].strip())}</h5>")
        elif stripped.startswith("####"):
            html_lines.append(f"<h4>{inline_format(stripped[4:].strip())}</h4>")
        elif stripped.startswith("###"):
            html_lines.append(f"<h3>{inline_format(stripped[3:].strip())}</h3>")
        elif stripped.startswith("##"):
            html_lines.append(f"<h2>{inline_format(stripped[2:].strip())}</h2>")
        elif stripped.startswith("# "):
            html_lines.append(f"<h1>{inline_format(stripped[1:].strip())}</h1>")
        # Horizontal rule
        elif stripped in ("---", "***", "___"):
            html_lines.append("<hr>")
        # List items
        elif stripped.startswith(("- ", "* ")):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            content = stripped[2:]
            # Checkbox
            if content.startswith("[ ] "):
                html_lines.append(f'<li class="task"><input type="checkbox" disabled> {inline_format(content[4:])}</li>')
            elif content.startswith("[x] "):
                html_lines.append(f'<li class="task"><input type="checkbox" checked disabled> {inline_format(content[4:])}</li>')
            else:
                html_lines.append(f"<li>{inline_format(content)}</li>")
        # Numbered list
        elif re.match(r"^\d+\.\s", stripped):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            content = re.sub(r"^\d+\.\s", "", stripped)
            html_lines.append(f"<li>{inline_format(content)}</li>")
        # Paragraph
        else:
            html_lines.append(f"<p>{inline_format(stripped)}</p>")

    # Close open tags
    if in_table:
        html_lines.append("</table></div>")
    if in_list:
        html_lines.append("</ul>")
    if in_blockquote:
        html_lines.append("</blockquote>")
    if in_code_block:
        html_lines.append("</code></pre>")

    return "\n".join(html_lines)


def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline_format(text):
    """Handle inline markdown: bold, italic, code, links."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text


def wrap_page(title, body_html, nav_html, is_gv=False):
    """Wrap content in full HTML page with nav."""
    gv_script = ""
    if is_gv:
        gv_script = f"""
    <script>
    (function() {{
        var stored = sessionStorage.getItem('gv_auth');
        if (stored !== 'ok') {{
            var pw = prompt('Nhập mật khẩu giảng viên:');
            if (pw !== '{GV_PASSWORD}') {{
                document.body.innerHTML = '<div style="text-align:center;padding:100px"><h1>Sai mật khẩu</h1><p>Vui lòng liên hệ ban tổ chức.</p><a href="/">← Về trang chủ</a></div>';
                return;
            }}
            sessionStorage.setItem('gv_auth', 'ok');
        }}
    }})();
    </script>"""

    og_title = f"{title} — Đào Tạo AI CPMI"
    og_desc = "Chương trình đào tạo ứng dụng AI (Google Gemini & NotebookLM) cho ngành xây dựng và quản lý dự án. Tài liệu hướng dẫn, prompt templates, bài tập thực hành quy trình CBDA."
    og_img = "https://cpmi.vn/uploads/banners/22-logo.png"

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{og_title}</title>
    <meta name="description" content="{og_desc}">
    <meta name="author" content="CPMI - Công ty CP Quản lý dự án và Đầu tư xây dựng">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{og_desc}">
    <meta property="og:image" content="{og_img}">
    <meta property="og:locale" content="vi_VN">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{og_desc}">
    <meta name="twitter:image" content="{og_img}">

    <link rel="icon" type="image/png" href="{og_img}">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    {gv_script}
    <div class="layout">
        <nav class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <a href="/" class="logo-link">
                    <img src="https://cpmi.vn/uploads/banners/22-logo.png" alt="CPMI Logo" class="logo-img">
                </a>
                <div class="header-text">
                    <span class="brand-name">Đào Tạo AI</span>
                    <span class="brand-sub">CPMI &middot; Gemini &middot; NotebookLM</span>
                </div>
                <button class="menu-close" onclick="toggleMenu()" aria-label="Đóng menu">&times;</button>
            </div>
            {nav_html}
            <div class="sidebar-footer">
                <p>&copy; 2026 CPMI</p>
            </div>
        </nav>
        <main class="content">
            <button class="menu-toggle" onclick="toggleMenu()" aria-label="Mở menu">{ICONS["menu"]} Menu</button>
            <article>
                {body_html}
            </article>
            <footer class="content-footer">
                <p>CPMI &mdash; Công ty CP Quản lý dự án và Đầu tư xây dựng</p>
            </footer>
        </main>
    </div>
    <script>
    function toggleMenu() {{
        document.getElementById('sidebar').classList.toggle('open');
    }}
    // Close sidebar on click outside (mobile)
    document.addEventListener('click', function(e) {{
        var sb = document.getElementById('sidebar');
        var toggle = document.querySelector('.menu-toggle');
        if (sb.classList.contains('open') && !sb.contains(e.target) && !toggle.contains(e.target)) {{
            sb.classList.remove('open');
        }}
    }});
    </script>
</body>
</html>"""


def build_nav(current_page=""):
    """Build sidebar navigation HTML."""
    sections = [
        ("HỌC VIÊN", [
            ("index.html", "home", "Trang chủ"),
            ("agenda.html", "calendar", "Lịch trình 2 ngày"),
        ]),
        ("HƯỚNG DẪN NHANH", [
            ("qrg-gemini.html", "sparkles", "Gemini Workspace"),
            ("qrg-notebooklm.html", "book-open", "NotebookLM"),
            ("prompts.html", "message", "Prompt Templates"),
            ("checklist.html", "shield", "Checklist Bảo Mật"),
        ]),
        ("TÀI LIỆU THỰC HÀNH", [
            ("tai-lieu/to-trinh.html", "file-text", "Tờ trình CTrĐT"),
            ("tai-lieu/bao-cao.html", "clipboard", "BC đề xuất CTrĐT"),
            ("tai-lieu/du-toan.html", "coins", "Dự toán CBDA"),
            ("tai-lieu/ke-hoach-lcnt.html", "bar-chart", "KH LCNT"),
            ("tai-lieu/email.html", "mail", "Email thẩm định"),
            ("tai-lieu/y-kien.html", "edit", "Ý kiến sở ngành"),
            ("tai-lieu/nhiem-vu-ks.html", "search", "Nhiệm vụ khảo sát"),
            ("tai-lieu/khoi-luong.html", "ruler", "Khối lượng KS"),
        ]),
        ("GIẢNG VIÊN", [
            ("giang-vien/index.html", "graduation", "Portal Giảng Viên"),
            ("giang-vien/kich-ban-ngay-1.html", "book-open", "Kịch bản Ngày 1"),
            ("giang-vien/kich-ban-ngay-2.html", "book-open", "Kịch bản Ngày 2"),
            ("giang-vien/plan.html", "clipboard", "Kế hoạch tổng thể"),
            ("giang-vien/checklist-to-chuc.html", "check-circle", "Checklist tổ chức"),
        ]),
    ]

    html = ""
    for section_title, links in sections:
        html += f'<div class="nav-section"><h3>{section_title}</h3><ul>'
        for href, icon_name, label in links:
            active = ' class="active"' if href == current_page else ""
            prefix = "/" if not href.startswith("/") else ""
            html += f'<li><a href="{prefix}{href}"{active}>{icon(icon_name)}{label}</a></li>'
        html += "</ul></div>"
    return html


def read_md(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Strip YAML frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2]
    return content


def build_page(md_path, output_path, title, page_key, is_gv=False):
    """Read markdown, convert, wrap in template, write HTML."""
    md_content = read_md(md_path)
    body = md_to_html(md_content)
    nav = build_nav(page_key)
    html = wrap_page(title, body, nav, is_gv)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Built: {output_path}")


def build_index():
    """Build homepage."""
    body = f"""
    <h1>Chương Trình Đào Tạo Ứng Dụng AI</h1>
    <p class="lead">Google Gemini & NotebookLM cho Công Ty Thầu Xây Dựng</p>

    <div class="card-grid">
        <a href="/agenda.html" class="card">
            {card_icon("calendar")}
            <h3>Lịch Trình 2 Ngày</h3>
            <p>Agenda chi tiết Ngày 1 + Ngày 2, buổi chiều 13:30–16:30</p>
        </a>
        <a href="/qrg-gemini.html" class="card">
            {card_icon("sparkles")}
            <h3>Gemini Workspace</h3>
            <p>Hướng dẫn nhanh: Docs, Gmail, Sheets, Slides</p>
        </a>
        <a href="/qrg-notebooklm.html" class="card">
            {card_icon("book-open")}
            <h3>NotebookLM</h3>
            <p>Hướng dẫn nhanh: Upload, hỏi đáp, Audio Overview</p>
        </a>
        <a href="/prompts.html" class="card">
            {card_icon("message")}
            <h3>Prompt Templates</h3>
            <p>24 prompt mẫu cho ngành xây dựng & QLDA</p>
        </a>
        <a href="/checklist.html" class="card">
            {card_icon("shield")}
            <h3>Checklist Bảo Mật</h3>
            <p>5 NÊN + 5 KHÔNG khi sử dụng AI</p>
        </a>
        <a href="/tai-lieu/to-trinh.html" class="card">
            {card_icon("folder")}
            <h3>Tài Liệu Thực Hành</h3>
            <p>8 tài liệu mẫu: tờ trình, dự toán, KH LCNT...</p>
        </a>
    </div>

    <div class="info-box">
        <h3>Thông tin đào tạo</h3>
        <ul>
            <li><strong>Thời lượng:</strong> 2 buổi chiều x 3 tiếng (13:30–16:30)</li>
            <li><strong>Đối tượng:</strong> Nhân viên văn phòng tất cả phòng ban</li>
            <li><strong>Công cụ:</strong> Google Gemini, NotebookLM, Google Workspace</li>
            <li><strong>Ngày 1:</strong> Làm chủ công cụ AI</li>
            <li><strong>Ngày 2:</strong> Ứng dụng quy trình CBDA</li>
        </ul>
    </div>

    <div class="gv-link">
        <a href="/giang-vien/index.html">{ICONS["lock"]} Khu vực Giảng viên</a>
    </div>
    """
    nav = build_nav("index.html")
    html = wrap_page("Trang chủ", body, nav)
    path = os.path.join(SITE_DIR, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Built: {path}")


def build_agenda():
    """Build agenda page from plan.md summary."""
    body = """
    <h1>Lịch Trình Đào Tạo 2 Ngày</h1>

    <h2>Ngày 1 (13:30–16:30): Làm Chủ Công Cụ AI Google</h2>
    <div class="table-wrap"><table>
    <tr><th>Thời gian</th><th>Phiên</th><th>TL</th><th>Nội dung</th></tr>
    <tr><td>13:30–13:45</td><td><strong>Khai mạc + Demo WOW</strong></td><td>15'</td><td>Demo LIVE NotebookLM + Gemini Docs</td></tr>
    <tr><td>13:45–14:15</td><td><strong>Workshop Gemini Docs</strong></td><td>30'</td><td>Soạn tờ trình + tóm tắt văn bản</td></tr>
    <tr><td>14:15–14:35</td><td><strong>Demo Gmail + Sheets</strong></td><td>20'</td><td>Email hành chính + phân tích dự toán</td></tr>
    <tr><td>14:35–14:45</td><td><em>Giải lao</em></td><td>10'</td><td></td></tr>
    <tr><td>14:45–15:30</td><td><strong>Workshop NotebookLM</strong></td><td>45'</td><td>Upload PL, hỏi đáp, Audio Overview</td></tr>
    <tr><td>15:30–16:00</td><td><strong>Bài tập tổng hợp</strong></td><td>30'</td><td>Mô phỏng 2 bước CBDA (nhóm)</td></tr>
    <tr><td>16:00–16:30</td><td><strong>Q&A + Wrap-up</strong></td><td>30'</td><td>Tips, bài tập về nhà</td></tr>
    </table></div>

    <h2>Ngày 2 (13:30–16:30): Ứng Dụng Quy Trình CBDA</h2>
    <div class="table-wrap"><table>
    <tr><th>Thời gian</th><th>Phiên</th><th>TL</th><th>Nội dung</th></tr>
    <tr><td>13:30–13:40</td><td><strong>Ôn tập nhanh</strong></td><td>10'</td><td>Quiz + chia sẻ bài tập về nhà</td></tr>
    <tr><td>13:40–14:20</td><td><strong>Lab nhóm phòng ban</strong></td><td>40'</td><td>4 nhóm (KT, HC, ĐT, TH) thực hành nghiệp vụ</td></tr>
    <tr><td>14:20–14:30</td><td><em>Giải lao</em></td><td>10'</td><td></td></tr>
    <tr><td>14:30–15:30</td><td><strong>Mô phỏng CBDA E2E</strong></td><td>60'</td><td>Dự án "Cải tạo trụ sở UBND" — 3 bước</td></tr>
    <tr><td>15:30–15:45</td><td><strong>Trình bày nhanh</strong></td><td>15'</td><td>1-2 nhóm demo sản phẩm</td></tr>
    <tr><td>15:45–16:05</td><td><strong>Bảo mật + KH 30 ngày</strong></td><td>20'</td><td>Checklist BM, ghép buddy, nhóm chat</td></tr>
    <tr><td>16:05–16:30</td><td><strong>Đánh giá + Bế mạc</strong></td><td>25'</td><td>Khảo sát, chứng nhận, chụp ảnh</td></tr>
    </table></div>
    """
    nav = build_nav("agenda.html")
    html = wrap_page("Lịch trình 2 ngày", body, nav)
    path = os.path.join(SITE_DIR, "agenda.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Built: {path}")


def build_gv_index():
    """Build instructor portal index."""
    body = f"""
    <h1>Khu Vực Giảng Viên</h1>
    <p class="lead">Tài liệu nội bộ — kịch bản, kế hoạch, checklist tổ chức.</p>

    <div class="card-grid">
        <a href="/giang-vien/kich-ban-ngay-1.html" class="card">
            {card_icon("book-open")}
            <h3>Kịch Bản Ngày 1</h3>
            <p>Script phút-by-phút 6 phiên, phân công GV/trợ giảng</p>
        </a>
        <a href="/giang-vien/kich-ban-ngay-2.html" class="card">
            {card_icon("book-open")}
            <h3>Kịch Bản Ngày 2</h3>
            <p>Lab PB + CBDA E2E + bế mạc, script chi tiết</p>
        </a>
        <a href="/giang-vien/plan.html" class="card">
            {card_icon("clipboard")}
            <h3>Kế Hoạch Tổng Thể</h3>
            <p>8 phases, timeline T-14 — D+30</p>
        </a>
        <a href="/giang-vien/checklist-to-chuc.html" class="card">
            {card_icon("check-circle")}
            <h3>Checklist Tổ Chức</h3>
            <p>T-14 — D-day, ngân sách, phân công</p>
        </a>
    </div>
    """
    nav = build_nav("giang-vien/index.html")
    html = wrap_page("Giảng Viên", body, nav, is_gv=True)
    path = os.path.join(SITE_DIR, "giang-vien", "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Built: {path}")


def main():
    print("Building site...")

    # Clean output (handle locked dirs on Windows)
    if os.path.exists(SITE_DIR):
        try:
            shutil.rmtree(SITE_DIR)
        except PermissionError:
            # Fallback: remove files individually, recreate dirs
            import glob
            for f in glob.glob(os.path.join(SITE_DIR, "**", "*"), recursive=True):
                if os.path.isfile(f):
                    os.remove(f)
    os.makedirs(SITE_DIR, exist_ok=True)

    # Copy CSS
    css_dir = os.path.join(SITE_DIR, "css")
    os.makedirs(css_dir, exist_ok=True)
    css_src = os.path.join(PROJECT_ROOT, "site-css", "style.css")
    if os.path.exists(css_src):
        shutil.copy2(css_src, os.path.join(css_dir, "style.css"))
        print("  Copied CSS")

    # Build special pages
    build_index()
    build_agenda()
    build_gv_index()

    # Public pages from materials
    material_pages = [
        ("qrg-gemini-workspace.md", "qrg-gemini.html", "Gemini Workspace — QRG"),
        ("qrg-notebooklm.md", "qrg-notebooklm.html", "NotebookLM — QRG"),
        ("prompt-templates-nganh-xay-dung.md", "prompts.html", "Prompt Templates"),
        ("checklist-bao-mat-ai.md", "checklist.html", "Checklist Bảo Mật AI"),
    ]
    for md_name, html_name, title in material_pages:
        md_path = os.path.join(MATERIALS_DIR, md_name)
        out_path = os.path.join(SITE_DIR, html_name)
        build_page(md_path, out_path, title, html_name)

    # Simulated documents
    sim_pages = [
        ("to-trinh-de-xuat-chu-truong-dau-tu.md", "tai-lieu/to-trinh.html", "Tờ Trình Đề Xuất CTrĐT"),
        ("bao-cao-de-xuat-chu-truong-dau-tu-nhom-c.md", "tai-lieu/bao-cao.html", "BC Đề Xuất CTrĐT Nhóm C"),
        ("du-toan-chi-phi-cbda.md", "tai-lieu/du-toan.html", "Dự Toán Chi Phí CBDA"),
        ("ke-hoach-lcnt-giai-doan-cbda.md", "tai-lieu/ke-hoach-lcnt.html", "Kế Hoạch LCNT"),
        ("chuoi-email-mo-phong-tham-dinh.md", "tai-lieu/email.html", "Email Mô Phỏng Thẩm Định"),
        ("bang-tong-hop-y-kien-so-nganh.md", "tai-lieu/y-kien.html", "Tổng Hợp Ý Kiến Sở Ngành"),
        ("nhiem-vu-khao-sat-dia-hinh-mau.md", "tai-lieu/nhiem-vu-ks.html", "Nhiệm Vụ Khảo Sát"),
        ("khoi-luong-khao-sat.md", "tai-lieu/khoi-luong.html", "Khối Lượng Khảo Sát"),
    ]
    sim_dir = os.path.join(MATERIALS_DIR, "tai-lieu-gia-lap")
    for md_name, html_name, title in sim_pages:
        md_path = os.path.join(sim_dir, md_name)
        out_path = os.path.join(SITE_DIR, html_name)
        build_page(md_path, out_path, title, html_name)

    # GV pages (password protected)
    gv_pages = [
        ("phase-05-kich-ban-ngay-1.md", "giang-vien/kich-ban-ngay-1.html", "Kịch Bản Ngày 1"),
        ("phase-06-kich-ban-ngay-2.md", "giang-vien/kich-ban-ngay-2.html", "Kịch Bản Ngày 2"),
        ("plan.md", "giang-vien/plan.html", "Kế Hoạch Tổng Thể"),
        ("phase-07-checklist-to-chuc.md", "giang-vien/checklist-to-chuc.html", "Checklist Tổ Chức"),
    ]
    for md_name, html_name, title in gv_pages:
        md_path = os.path.join(PLANS_DIR, md_name)
        out_path = os.path.join(SITE_DIR, html_name)
        build_page(md_path, out_path, title, html_name, is_gv=True)

    print(f"\nDone! Site built at: {SITE_DIR}")
    file_count = sum(len(files) for _, _, files in os.walk(SITE_DIR))
    print(f"Total files: {file_count}")


if __name__ == "__main__":
    main()
