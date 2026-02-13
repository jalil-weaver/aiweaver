from __future__ import annotations

import argparse
from pathlib import Path

import markdown
from fpdf import FPDF, HTMLMixin

FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


class PDF(FPDF, HTMLMixin):
    pass


def md_file_to_pdf(md_path: Path, pdf_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        text,
        extensions=["extra", "tables", "sane_lists"],
    )

    css = """
    <style>
    body { font-family: 'ArialUnicode'; font-size: 11pt; line-height: 1.35; }
    h1 { color: #0B3558; font-size: 20pt; margin-bottom: 6pt; }
    h2 { color: #0B3558; font-size: 14pt; margin-top: 12pt; }
    h3 { color: #0B3558; font-size: 12pt; margin-top: 10pt; }
    p { margin: 4pt 0; }
    ul { margin: 0 0 6pt 18pt; }
    ol { margin: 0 0 6pt 20pt; }
    table { width: 100%; border-collapse: collapse; margin-bottom: 8pt; }
    th { background: #F0F4F8; font-weight: bold; }
    th, td { border: 0.5pt solid #D3DADF; padding: 4pt; }
    blockquote { border-left: 3pt solid #0B3558; padding-left: 6pt; color: #333; }
    </style>
    """

    pdf = PDF(format="A4")
    pdf.add_font("ArialUnicode", "", FONT_PATH)
    pdf.add_font("ArialUnicode", "B", FONT_PATH)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("ArialUnicode", size=11)
    pdf.write_html(css + html_body)
    pdf.output(str(pdf_path))


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF using fpdf2")
    parser.add_argument("md_file", type=Path)
    parser.add_argument("pdf_file", type=Path)
    args = parser.parse_args()
    md_file_to_pdf(args.md_file, args.pdf_file)


if __name__ == "__main__":
    main()
