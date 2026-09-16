#!/usr/bin/env python3
"""Gera versões embelezadas dos QR codes com moldura visual EXPX."""
import os
import re
import subprocess
from pathlib import Path

ROOT = Path("/Users/thuliobittencourt/Documents/Projetos/Livros/Livro - Carroseis com IA sem gastar tokens")
QR_DIR = ROOT / "figuras" / "qr"
QR_BOX_DIR = ROOT / "figuras" / "qr_box"
QR_BOX_DIR.mkdir(parents=True, exist_ok=True)

REPO_URL = "https://github.com/bittencourtthulio/carrosseis-infinitos-com-qualquer-ia/blob/main/prompts"

CAPS = [
    ("cap-01-armadilha", "Prompt 01 · A armadilha do token na peça"),
    ("cap-02-cinco-estagios", "Prompt 02 · A fábrica em cinco estágios"),
    ("cap-03-catalogo", "Prompt 03 · A fonte de dados"),
    ("cap-04-teses", "Prompt 04 · Teses por combinação"),
    ("cap-04-pools", "Prompt 04 · Pools de variações"),
    ("cap-05-anatomia", "Prompt 05 · Anatomia dos 8 slides"),
    ("cap-05-assets", "Prompt 05 · Briefing para IA de imagem"),
    ("cap-06-prints", "Prompt 06 · Captura de prints em escala"),
    ("cap-07-renderizador", "Prompt 07 · Renderizador em lote"),
    ("cap-08-automacao", "Prompt 08 · Bloco de automação (3 itens)"),
    ("cap-08-automacao-massa", "Prompt 08 · Bloco de automação em massa"),
    ("cap-09-defeitos", "Prompt 09 · Validação dos 7 defeitos"),
    ("cap-10-prontidao", "Prompt 10 · Auditoria de prontidão"),
]

def extract_modules(svg_path):
    """Lê o SVG gerado pelo qrencode e extrai a lista de retângulos."""
    with open(svg_path) as f:
        content = f.read()
    rects = re.findall(r'<rect\s+x="(\d+)"\s+y="(\d+)"\s+width="1"\s+height="1"\s+fill="(#[0-9a-fA-F]+)"', content)
    black = []
    for x, y, color in rects:
        if color.lower() == "#000000":
            black.append((int(x), int(y)))
    return 53, black

def make_qr_box(cap_id, label, qr_svg_path, out_path):
    """Gera SVG 320x360 com QR centralizado, moldura e legenda."""
    grid_size, modules = extract_modules(qr_svg_path)

    box_w, box_h = 320, 360
    qr_size = 240
    qr_offset_x = (box_w - qr_size) // 2
    qr_offset_y = 30
    module_size = qr_size / grid_size

    bg = "#F5F1E9"
    accent = "#16A34A"
    text = "#1B1714"
    muted = "#6B6358"

    rects = []
    for x, y in modules:
        sx = qr_offset_x + x * module_size
        sy = qr_offset_y + y * module_size
        rects.append(f'    <rect x="{sx:.2f}" y="{sy:.2f}" width="{module_size:.3f}" height="{module_size:.3f}" fill="{text}"/>')

    kicker_y = qr_offset_y + qr_size + 32
    url_y = qr_offset_y + qr_size + 56

    label_short = cap_id
    url_display = f"github.com/.../{cap_id}.md"

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {box_w} {box_h}" width="{box_w}" height="{box_h}">
  <rect x="0" y="0" width="{box_w}" height="{box_h}" fill="{bg}" rx="16"/>
  <rect x="1" y="1" width="{box_w-2}" height="{box_h-2}" fill="none" stroke="{accent}" stroke-width="1.5" rx="16"/>
{chr(10).join(rects)}
  <text x="{box_w//2}" y="{kicker_y}" text-anchor="middle" font-family="'JetBrains Mono', 'Menlo', monospace" font-size="14" font-weight="600" fill="{accent}" letter-spacing="0.05em">PROMPT 0{cap_id[4:6].lstrip('0') if cap_id[4:6].lstrip('0') else '0'}</text>
  <text x="{box_w//2}" y="{url_y}" text-anchor="middle" font-family="'JetBrains Mono', 'Menlo', monospace" font-size="11" fill="{muted}">{url_display}</text>
  <text x="{box_w//2}" y="{url_y + 16}" text-anchor="middle" font-family="'Inter', sans-serif" font-size="10" fill="{muted}">aponte a câmera para abrir</text>
</svg>
'''
    with open(out_path, 'w') as f:
        f.write(svg)

for cap_id, label in CAPS:
    src = QR_DIR / f"{cap_id}.svg"
    dst = QR_BOX_DIR / f"{cap_id}.svg"
    if src.exists():
        make_qr_box(cap_id, label, src, dst)
        print(f"OK: {dst.name}")
    else:
        print(f"MISSING: {src}")

print(f"\nTotal: {len(list(QR_BOX_DIR.glob('*.svg')))} QR boxes gerados em {QR_BOX_DIR}")
