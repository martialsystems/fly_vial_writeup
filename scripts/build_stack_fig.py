#!/usr/bin/env python3
# Copyright (c) 2026 Martial Systems LLC
"""F versus generation on the seed-1 lock. Numbers copied from locked JSON."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT_PDF = ROOT / "figures" / "stack.pdf"
OUT_PNG = ROOT / "figures" / "stack.png"

# Copied from logs/assort_80.json and logs/random_80.json. Do not restamp.
T = (0, 1, 8, 20, 40, 80)
ASSORT = (0.000, 0.000, 0.131, 0.217, 0.399, 0.524)
RAND = (0.000, 0.000, 0.005, 0.008, 0.021, 0.034)
WRIGHT_T80 = 0.039


def main() -> None:
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    W, H = 7.2 * inch, 4.2 * inch
    c = canvas.Canvas(str(OUT_PDF), pagesize=(W, H))
    left, right = 0.85 * inch, W - 0.4 * inch
    bot, top = 0.7 * inch, H - 0.45 * inch
    c.setFont("Times-Bold", 10)
    c.drawString(left, H - 0.32 * inch, "Seed-1 IBD F versus generation")
    c.setFont("Times-Roman", 8)
    c.drawString(left, H - 0.48 * inch, "Copied from logs/assort_80.json and logs/random_80.json. @e2e22b7.")

    def x_of(t: float) -> float:
        return left + (t / 80.0) * (right - left)

    def y_of(f: float) -> float:
        return bot + (f / 0.56) * (top - bot)

    c.setStrokeColorRGB(0.2, 0.2, 0.2)
    c.line(left, bot, right, bot)
    c.line(left, bot, left, top)
    c.setFont("Times-Roman", 8)
    for t in T:
        x = x_of(t)
        c.line(x, bot, x, bot - 4)
        c.drawCentredString(x, bot - 14, str(t))
    for f in (0.0, 0.2, 0.4, 0.524):
        y = y_of(f)
        c.setStrokeColorRGB(0.85, 0.85, 0.85)
        c.line(left, y, right, y)
        c.setFillColorRGB(0, 0, 0)
        c.drawRightString(left - 6, y - 3, f"{f:.3f}" if f != 0.524 else "0.524")
    c.setFillColorRGB(0, 0, 0)
    c.drawCentredString((left + right) / 2, 0.28 * inch, "generation t")
    c.saveState()
    c.translate(0.32 * inch, (bot + top) / 2)
    c.rotate(90)
    c.drawCentredString(0, 0, "F")
    c.restoreState()

    def polyline(xs, ys, r, g, b, width=1.4) -> None:
        c.setStrokeColorRGB(r, g, b)
        c.setFillColorRGB(r, g, b)
        c.setLineWidth(width)
        p = c.beginPath()
        p.moveTo(x_of(xs[0]), y_of(ys[0]))
        for t, f in zip(xs[1:], ys[1:]):
            p.lineTo(x_of(t), y_of(f))
        c.drawPath(p, stroke=1, fill=0)
        for t, f in zip(xs, ys):
            c.circle(x_of(t), y_of(f), 2.2, fill=1, stroke=0)

    polyline(T, ASSORT, 0.15, 0.15, 0.15)
    polyline(T, RAND, 0.45, 0.45, 0.45, width=1.2)
    c.setStrokeColorRGB(0.3, 0.3, 0.3)
    c.setDash(3, 2)
    c.line(x_of(80), y_of(WRIGHT_T80), x_of(72), y_of(WRIGHT_T80))
    c.setDash()
    c.setFillColorRGB(0.2, 0.2, 0.2)
    c.setFont("Times-Italic", 8)
    c.drawString(x_of(52), y_of(WRIGHT_T80) + 6, "Wright random t=80 ~ 0.039")
    c.setFont("Times-Roman", 8)
    c.drawString(left + 8, top - 12, "k=3 assortative")
    c.setFillColorRGB(0.45, 0.45, 0.45)
    c.drawString(left + 8, top - 24, "random")
    c.save()

    try:
        from PIL import Image as PILImage
        import subprocess

        subprocess.run(
            ["pdftoppm", "-png", "-r", "140", "-singlefile", str(OUT_PDF), str(OUT_PNG.with_suffix(""))],
            check=False,
        )
        if not OUT_PNG.is_file():
            # fallback: rasterize via pypdfium2
            import pypdfium2 as pdfium

            pdf = pdfium.PdfDocument(str(OUT_PDF))
            page = pdf[0]
            bitmap = page.render(scale=2)
            pil = bitmap.to_pil()
            pil.save(OUT_PNG)
    except Exception:
        import pypdfium2 as pdfium

        pdf = pdfium.PdfDocument(str(OUT_PDF))
        page = pdf[0]
        bitmap = page.render(scale=2)
        pil = bitmap.to_pil()
        pil.save(OUT_PNG)
    print("wrote", OUT_PDF, OUT_PNG)


if __name__ == "__main__":
    main()
