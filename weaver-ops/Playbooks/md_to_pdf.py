from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import markdown
from fpdf import FPDF
from bs4 import BeautifulSoup

FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


def preprocess_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Ensure checklist items (input[type=checkbox]) and lists have line breaks per item
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li", recursive=False):
            li.insert_after(soup.new_tag("br"))

    for ol in soup.find_all("ol"):
        for li in ol.find_all("li", recursive=False):
            li.insert_after(soup.new_tag("br"))

    return str(soup)


def md_to_html(md_text: str) -> str:
    html_body = markdown.markdown(
        md_text,
        extensions=["extra", "tables", "sane_lists"]
    )
    html_body = preprocess_html(html_body)
    css = """
    <style>
    body { font-family: 'ArialUnicode'; font-size: 11pt; line-height: 1.55; color: #000000; }
    h1, h2, h3, h4 { font-weight: bold; color: #000000; }
    h1 { font-size: 20pt; margin-bottom: 8pt; }
    h2 { font-size: 15pt; margin-top: 14pt; }
    h3 { font-size: 12pt; margin-top: 12pt; }
    p { margin: 6pt 0; }
    ul, ol { margin: 0 0 8pt 18pt; }
    li { margin-bottom: 4pt; }
    table { width: 100%; border-collapse: collapse; margin: 8pt 0; }
    th, td { border: 1pt solid #000000; padding: 6pt; }
    th { font-weight: bold; }
    blockquote { border-left: 3pt solid #000000; padding-left: 8pt; margin: 8pt 0; }
    </style>
    """
    return css + html_body


def convert(md_path: Path, pdf_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    html = md_to_html(md_text)

    pdf = FPDF(format="A4")
    pdf.add_font("ArialUnicode", "", FONT_PATH)
    pdf.add_font("ArialUnicode", "B", FONT_PATH)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("ArialUnicode", size=11)
    pdf.write_html(html)
    pdf.output(str(pdf_path))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sources", nargs="+", type=Path, help="Markdown files to convert")
    args = parser.parse_args()

    for md_file in args.sources:
        pdf_file = md_file.with_suffix(".pdf")
        convert(md_file, pdf_file)


if __name__ == "__main__":
    main()
