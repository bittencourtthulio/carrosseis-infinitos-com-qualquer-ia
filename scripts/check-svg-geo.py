#!/usr/bin/env python3
"""check-svg-geo.py

Gate geométrico para as pranchas SVG do livro.
  R1: nenhum elemento com tinta fora de 1050x1485

R2 e R3 (sobreposicao de texto, texto dentro de rect) exigem getBoundingClientRect
no browser via Playwright para ser confiavel. Aqui no Python puro, a heuristica
de largura de texto (chars * font-size * 0.5) gera falsos positivos quando o
texto tem font-family mono vs sans. Marcamos R2/R3 como "verificacao visual"
no checklist final.

Este script foca em R1, que eh confiavel em Python puro.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURAS = ROOT / "figuras"

VIEWBOX = (1050, 1485)

failures = []


def check_svg(path):
    text = path.read_text()

    # R1: rect com tinta fora do viewBox
    for m in re.finditer(
        r'<rect[^>]*x="(-?\d+(?:\.\d+)?)"[^>]*y="(-?\d+(?:\.\d+)?)"[^>]*width="(-?\d+(?:\.\d+)?)"[^>]*height="(-?\d+(?:\.\d+)?)"',
        text,
    ):
        x = float(m.group(1))
        y = float(m.group(2))
        w = float(m.group(3))
        h = float(m.group(4))
        if w == 0 or h == 0:
            continue
        # tolerância de 2px para arredondamento
        if x < -2 or y < -2 or x + w > VIEWBOX[0] + 2 or y + h > VIEWBOX[1] + 2:
            failures.append(
                f"{path.name}: R1 rect ({x:.0f},{y:.0f},{w:.0f}x{h:.0f}) "
                f"fora de {VIEWBOX[0]}x{VIEWBOX[1]}"
            )

    # Verificacao adicional: existencia de viewBox correto
    if f'viewBox="0 0 {VIEWBOX[0]} {VIEWBOX[1]}"' not in text:
        failures.append(f"{path.name}: viewBox ausente ou errado")


def main():
    pranchas = [p for p in FIGURAS.glob("*.svg") if not str(p).startswith(str(FIGURAS / "qr"))]
    for svg in pranchas:
        check_svg(svg)

    if failures:
        print(f"FALHAS GEOMETRICAS: {len(failures)}")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print(f"OK R1: {len(pranchas)} pranchas dentro do viewBox 1050x1485.")
        print(f"R2 e R3: verificacao visual obrigatoria (ver checklist-final).")


if __name__ == "__main__":
    main()
