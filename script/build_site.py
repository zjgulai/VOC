#!/usr/bin/env python3
"""
VOC 静态网站构建脚本
将 html_report 中的报告注入全局导航栏后输出到 docs/reports/
"""
import os
import re
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = PROJECT_ROOT / "html_report"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "reports"

SITE_NAV = """
<div class="site-global-nav" style="
    position:fixed;top:0;left:0;right:0;z-index:1001;height:36px;
    background:var(--fr-800);display:flex;align-items:center;justify-content:center;
    gap:20px;font-size:12px;box-shadow:0 1px 6px rgba(0,0,0,0.15);
">
    <a href="../index.html" style="color:#FCF6F7;text-decoration:none;padding:4px 10px;border-radius:4px;transition:all 0.3s;">首页</a>
    <a href="../strategy.html" style="color:#FCF6F7;text-decoration:none;padding:4px 10px;border-radius:4px;transition:all 0.3s;">策略与洞察</a>
    <a href="../product.html" style="color:#FCF6F7;text-decoration:none;padding:4px 10px;border-radius:4px;transition:all 0.3s;">产品与定义</a>
    <a href="../execution.html" style="color:#FCF6F7;text-decoration:none;padding:4px 10px;border-radius:4px;transition:all 0.3s;">落地与执行</a>
    <a href="../index.html" style="color:var(--rg-500);text-decoration:none;padding:4px 10px;border-radius:4px;transition:all 0.3s;font-weight:600;">E2E报告库</a>
</div>
<style>
.site-global-nav a:hover{background:rgba(255,255,255,0.12);}
</style>
"""

NAV_TOP_OFFSET = """
.nav-bar { top: 36px !important; }
"""

REPORT_MAP = {
    "VOC喂养电器E2E洞察报告_V5.html": "e2e-v5.html",
    "VOC竞品格局与用户口碑分析报告.html": "stage1-competitor.html",
    "VOC用户需求深潜与痛点机会报告.html": "stage2-user-needs.html",
    "VOC产品机会挖掘与企划方案报告.html": "stage3-opportunity.html",
    "VOC超级产品定义与视觉转化企划书.html": "stage4-product-definition.html",
    "VOC产品网站设计与SEO优化方案.html": "stage6-website-seo.html",
    "VOC产品六视图与视频制作方案.html": "stage7-sixview-video.html",
}


def inject_nav(content):
    """向 HTML 注入全局站点导航栏 + 调整原有 nav-bar 偏移"""

    if "site-global-nav" in content:
        print("  [跳过] 已有全局导航栏")
        return content

    if "</style>" not in content:
        print("  [警告] 未找到 </style> 标签，跳过注入")
        return content

    while True:
        offset = content.find(".nav-bar { top: 36px !important; }")
        if offset == -1:
            break
        content = content[:offset] + content[offset + len(NAV_TOP_OFFSET):]

    nav_bar_pos = content.find(".nav-bar {")
    if nav_bar_pos != -1:
        close_brace = content.find("}", nav_bar_pos)
        if close_brace != -1:
            section_end = content.find("}", close_brace)
            content = content[:section_end + 1] + NAV_TOP_OFFSET + content[section_end + 1:]
    else:
        content = content.replace("</style>", "</style>\n<style>" + NAV_TOP_OFFSET + "</style>")

    injection = SITE_NAV
    body_match = re.search(r'<body[^>]*>', content)
    if body_match:
        pos = body_match.end()
        content = content[:pos] + "\n" + injection + "\n" + content[pos:]
    else:
        style_end = content.find("</style>")
        if style_end != -1:
            pos = style_end + len("</style>")
            content = content[:pos] + "\n" + injection + "\n" + content[pos:]

    return content


def build():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    built = []

    for src_name, dst_name in REPORT_MAP.items():
        src_path = SOURCE_DIR / src_name
        if not src_path.exists():
            print(f"[跳过] 源文件不存在: {src_path}")
            continue

        dst_path = OUTPUT_DIR / dst_name
        print(f"[构建] {src_name} -> {dst_name}")

        content = src_path.read_text(encoding="utf-8")
        content = inject_nav(content)
        dst_path.write_text(content, encoding="utf-8")

        size_kb = dst_path.stat().st_size / 1024
        print(f"  [完成] {size_kb:.0f} KB")
        built.append(dst_name)

    print(f"\n构建完成。共处理 {len(built)} 个报告文件。")
    for f in built:
        print(f"  docs/reports/{f}")



if __name__ == "__main__":
    build()
