# Copyright (c) 2026 Martial Systems LLC
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "NOTE.md"
README = REPO / "README.md"
INDEX = "12835f747d6360781f3cc7f91f243178"


def test_note_lede() -> None:
    text = NOTE.read_text(encoding="utf-8")
    assert text.startswith("# fly_vial: assortative IBD F\n")
    body = text.split("\n", 1)[1].lstrip()
    assert body.startswith("Locks stay on the trees.")
    assert "What this is not" not in text
    assert "What it is not" not in text
    assert "—" not in text
    assert INDEX in text
    assert "e2e22b7" in text
    assert "0.524" in text
    assert "0.034" in text
    assert "0.474" in text
    assert "0.463" in text
    assert "pre_specified: false" in text
    assert "unconstrained evolutionary toy" in text
    assert "templates, not the stepper" in text or "templates not the stepper" in text
    assert "Wright" in text
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'./_-]*", text)
    assert 1200 <= len(words) <= 2800


def test_readme_points_at_note_and_index() -> None:
    text = README.read_text(encoding="utf-8")
    assert text.startswith("# fly_vial_writeup\n")
    assert "NOTE.md" in text
    assert INDEX in text
    assert "—" not in text
    desc = (REPO / "description.txt").read_text(encoding="utf-8")
    assert "12835f74" in desc
    assert "—" not in desc
    agents = (REPO / "AGENTS.md").read_text(encoding="utf-8")
    assert "not a finding tree" in agents
    assert "citation columns" in agents


def test_pdf_and_figure_exist() -> None:
    import pypdfium2 as pdfium

    pdf_path = REPO / "docs" / "fly_vial_f_note.pdf"
    fig = REPO / "figures" / "stack.png"
    assert pdf_path.is_file() and pdf_path.stat().st_size > 1000
    assert fig.is_file() and fig.stat().st_size > 1000
    pdf = pdfium.PdfDocument(str(pdf_path))
    text = "\n".join(pdf[i].get_textpage().get_text_bounded() for i in range(len(pdf)))
    assert "Abstract" in text
    assert "e2e22b7" in text
    assert "Revisions" in text
    assert "2026-09-19" in text
    assert "Keywords" in text
    assert "What it is not" not in text
    assert "—" not in text
    assert len(pdf) >= 4
