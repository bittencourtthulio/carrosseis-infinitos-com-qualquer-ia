#!/usr/bin/env python3
"""Gera as 10 pranchas SVG A5 (viewBox 1050x1485) do livro.

Paleta:
  Fundo escuro: #141210
  Texto claro: #F1EBE1
  Acento verde EXPX: #16A34A (texto), #15803D (borda/seta)
  Acento laranja Academia: #E85D00 (destaque secundario), #C64A00 (texto forte)
  Muted: #6B6358 (claro), #A69D8F (escuro)
"""

import os
from pathlib import Path

OUT = Path("/Users/thuliobittencourt/Documents/Projetos/Livros/Livro - Carroseis com IA sem gastar tokens/figuras")
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1050, 1485

# Cores
BG_DARK = "#141210"
BG_LIGHT = "#F5F1E9"
TXT_DARK = "#1B1714"
TXT_LIGHT = "#F1EBE1"
GREEN = "#16A34A"
GREEN_DARK = "#15803D"
ORANGE = "#E85D00"
ORANGE_DARK = "#C64A00"
MUTED_DARK = "#6B6358"
MUTED_LIGHT = "#A69D8F"

FONT_HEAD = "'Chakra Petch', 'Arial Black', sans-serif"
FONT_MONO = "'JetBrains Mono', 'Menlo', monospace"
FONT_BODY = "'Inter', 'Helvetica', sans-serif"

# -----------------------------------------------------------------------------
# 00 - CAPA
# -----------------------------------------------------------------------------
def svg_capa():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <linearGradient id="capabg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{BG_DARK}"/>
      <stop offset="1" stop-color="#0a0908"/>
    </linearGradient>
    <pattern id="grid" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
      <rect x="0" y="0" width="40" height="40" fill="none"/>
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{GREEN}" stroke-width="0.4" opacity="0.18"/>
    </pattern>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#capabg)"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>

  <!-- kicker superior -->
  <text x="80" y="120" font-family="{FONT_MONO}" font-size="20" fill="{GREEN}" letter-spacing="3">ACADEMIA DO CODIGO  ·  METODOLOGIAS  ·  2026</text>

  <!-- traco verde decorativo -->
  <line x1="80" y1="155" x2="200" y2="155" stroke="{GREEN}" stroke-width="3"/>

  <!-- titulo principal empilhado -->
  <text x="80" y="380" font-family="{FONT_HEAD}" font-size="98" font-weight="700" fill="{TXT_LIGHT}" letter-spacing="-2">Carrosseis</text>
  <text x="80" y="490" font-family="{FONT_HEAD}" font-size="98" font-weight="700" fill="{TXT_LIGHT}" letter-spacing="-2">Infinitos</text>
  <text x="80" y="600" font-family="{FONT_HEAD}" font-size="98" font-weight="700" fill="{TXT_LIGHT}" letter-spacing="-2">com Qualquer IA</text>

  <!-- faixa laranja de destaque -->
  <rect x="80" y="660" width="880" height="78" fill="{ORANGE}"/>
  <text x="110" y="717" font-family="{FONT_HEAD}" font-size="44" font-weight="700" fill="#FFFFFF" letter-spacing="-1">PRATICAMENTE SEM GASTAR TOKENS</text>

  <!-- subtitulo -->
  <text x="80" y="820" font-family="{FONT_BODY}" font-size="24" fill="{MUTED_LIGHT}">Passo a passo para leigo montar uma fabrica de 100, 200, 500 carrosseis</text>
  <text x="80" y="852" font-family="{FONT_BODY}" font-size="24" fill="{MUTED_LIGHT}">sem instalar programa e sem chamar modelo de linguagem na producao.</text>

  <!-- icones de tier (mini) -->
  <g transform="translate(80, 1020)">
    <circle cx="40" cy="40" r="40" fill="none" stroke="{GREEN}" stroke-width="3"/>
    <text x="40" y="50" text-anchor="middle" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{GREEN}">F</text>

    <circle cx="180" cy="40" r="40" fill="none" stroke="{GREEN}" stroke-width="3"/>
    <text x="180" y="50" text-anchor="middle" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{GREEN}">B</text>

    <circle cx="320" cy="40" r="40" fill="none" stroke="{GREEN}" stroke-width="3"/>
    <text x="320" y="50" text-anchor="middle" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{GREEN}">M</text>

    <circle cx="460" cy="40" r="40" fill="none" stroke="{GREEN}" stroke-width="3"/>
    <text x="460" y="50" text-anchor="middle" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{GREEN}">C</text>

    <text x="540" y="35" font-family="{FONT_MONO}" font-size="14" fill="{MUTED_LIGHT}">FREE</text>
    <text x="540" y="55" font-family="{FONT_MONO}" font-size="14" fill="{MUTED_LIGHT}">BARATO</text>
    <text x="620" y="35" font-family="{FONT_MONO}" font-size="14" fill="{MUTED_LIGHT}">MEDIO</text>
    <text x="620" y="55" font-family="{FONT_MONO}" font-size="14" fill="{MUTED_LIGHT}">CARO</text>
  </g>

  <!-- numero 418 destacado -->
  <text x="80" y="1230" font-family="{FONT_HEAD}" font-size="180" font-weight="800" fill="{GREEN}" letter-spacing="-4">418</text>
  <text x="370" y="1180" font-family="{FONT_MONO}" font-size="20" fill="{TXT_LIGHT}">carrosseis</text>
  <text x="370" y="1210" font-family="{FONT_MONO}" font-size="20" fill="{TXT_LIGHT}">produzidos</text>
  <text x="370" y="1240" font-family="{FONT_MONO}" font-size="20" fill="{TXT_LIGHT}">em uma sessao</text>
  <text x="370" y="1270" font-family="{FONT_MONO}" font-size="20" fill="{ORANGE}">0 tokens na producao</text>

  <!-- rodape -->
  <line x1="80" y1="1390" x2="970" y2="1390" stroke="{GREEN}" stroke-width="1" opacity="0.4"/>
  <text x="80" y="1430" font-family="{FONT_MONO}" font-size="16" fill="{MUTED_LIGHT}" letter-spacing="2">THULIO BITTENCOURT</text>
  <text x="970" y="1430" text-anchor="end" font-family="{FONT_MONO}" font-size="16" fill="{MUTED_LIGHT}" letter-spacing="2">EXPX / ACADEMIA DO CODIGO</text>
</svg>
'''

# -----------------------------------------------------------------------------
# 01 - Jeito 1 vs Jeito 2
# -----------------------------------------------------------------------------
def svg_jeito1_vs_jeito2():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>

  <text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 01  ·  FIGURA 1</text>
  <text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">Dois jeitos de usar IA</text>
  <text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">O primeiro gasta em linha reta. O segundo gasta uma vez.</text>

  <!-- Coluna esquerda: JEITO 1 (ruim) -->
  <g transform="translate(80, 290)">
    <rect x="0" y="0" width="420" height="1000" fill="none" stroke="{ORANGE}" stroke-width="3" rx="20"/>
    <rect x="0" y="0" width="420" height="80" fill="{ORANGE}" rx="20"/>
    <rect x="0" y="20" width="420" height="60" fill="{ORANGE}"/>
    <text x="30" y="55" font-family="{FONT_HEAD}" font-size="28" font-weight="700" fill="#FFFFFF">JEITO 1</text>
    <text x="30" y="75" font-family="{FONT_MONO}" font-size="14" fill="#FFFFFF" opacity="0.85">gasta por peca</text>

    <text x="30" y="140" font-family="{FONT_HEAD}" font-size="24" font-weight="700" fill="{TXT_DARK}">IA escreve cada peca</text>

    <!-- passos verticais -->
    <g transform="translate(30, 180)">
      <circle cx="15" cy="15" r="15" fill="{ORANGE}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">1</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">prompt para IA</text>
    </g>
    <g transform="translate(30, 230)">
      <circle cx="15" cy="15" r="15" fill="{ORANGE}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">2</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">copia para Canva</text>
    </g>
    <g transform="translate(30, 280)">
      <circle cx="15" cy="15" r="15" fill="{ORANGE}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">3</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">ajusta template</text>
    </g>
    <g transform="translate(30, 330)">
      <circle cx="15" cy="15" r="15" fill="{ORANGE}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">4</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">exporta PNG</text>
    </g>
    <g transform="translate(30, 380)">
      <circle cx="15" cy="15" r="15" fill="{ORANGE}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">5</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">posta no feed</text>
    </g>

    <!-- setas verticais entre passos -->
    <line x1="45" y1="215" x2="45" y2="230" stroke="{ORANGE}" stroke-width="2"/>
    <line x1="45" y1="265" x2="45" y2="280" stroke="{ORANGE}" stroke-width="2"/>
    <line x1="45" y1="315" x2="45" y2="330" stroke="{ORANGE}" stroke-width="2"/>
    <line x1="45" y1="365" x2="45" y2="380" stroke="{ORANGE}" stroke-width="2"/>

    <text x="30" y="500" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}" font-style="italic">Repete para cada peca.</text>

    <!-- grafico de custo crescente -->
    <g transform="translate(30, 540)">
      <line x1="0" y1="200" x2="360" y2="200" stroke="{TXT_DARK}" stroke-width="2"/>
      <line x1="0" y1="0" x2="0" y2="200" stroke="{TXT_DARK}" stroke-width="2"/>
      <text x="-15" y="105" text-anchor="end" font-family="{FONT_MONO}" font-size="12" fill="{MUTED_DARK}">tokens</text>
      <text x="180" y="225" text-anchor="middle" font-family="{FONT_MONO}" font-size="12" fill="{MUTED_DARK}">pecas</text>
      <!-- linha crescente -->
      <polyline points="20,180 90,160 160,130 230,90 300,40" stroke="{ORANGE}" stroke-width="4" fill="none"/>
      <circle cx="20" cy="180" r="6" fill="{ORANGE}"/>
      <circle cx="90" cy="160" r="6" fill="{ORANGE}"/>
      <circle cx="160" cy="130" r="6" fill="{ORANGE}"/>
      <circle cx="230" cy="90" r="6" fill="{ORANGE}"/>
      <circle cx="300" cy="40" r="6" fill="{ORANGE}"/>
      <text x="310" y="45" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="{ORANGE}">cresce</text>
    </g>

    <text x="30" y="850" font-family="{FONT_HEAD}" font-size="20" font-weight="700" fill="{ORANGE_DARK}">418 pecas = 418 sessoes de IA</text>
  </g>

  <!-- Coluna direita: JEITO 2 (bom) -->
  <g transform="translate(550, 290)">
    <rect x="0" y="0" width="420" height="1000" fill="none" stroke="{GREEN}" stroke-width="3" rx="20"/>
    <rect x="0" y="0" width="420" height="80" fill="{GREEN}" rx="20"/>
    <rect x="0" y="20" width="420" height="60" fill="{GREEN}"/>
    <text x="30" y="55" font-family="{FONT_HEAD}" font-size="28" font-weight="700" fill="#FFFFFF">JEITO 2</text>
    <text x="30" y="75" font-family="{FONT_MONO}" font-size="14" fill="#FFFFFF" opacity="0.85">gasta uma vez</text>

    <text x="30" y="140" font-family="{FONT_HEAD}" font-size="24" font-weight="700" fill="{TXT_DARK}">IA escreve o sistema</text>

    <g transform="translate(30, 180)">
      <circle cx="15" cy="15" r="15" fill="{GREEN}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">1</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">IA escreve os prompts</text>
    </g>
    <g transform="translate(30, 230)">
      <circle cx="15" cy="15" r="15" fill="{GREEN}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">2</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">IA escreve o template</text>
    </g>
    <g transform="translate(30, 280)">
      <circle cx="15" cy="15" r="15" fill="{GREEN}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">3</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">IA escreve o script</text>
    </g>
    <g transform="translate(30, 330)">
      <circle cx="15" cy="15" r="15" fill="{GREEN}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">4</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">Python gera os 418</text>
    </g>
    <g transform="translate(30, 380)">
      <circle cx="15" cy="15" r="15" fill="{GREEN}"/>
      <text x="15" y="22" text-anchor="middle" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="#FFFFFF">5</text>
      <text x="50" y="22" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">posta no feed</text>
    </g>

    <line x1="45" y1="215" x2="45" y2="230" stroke="{GREEN}" stroke-width="2"/>
    <line x1="45" y1="265" x2="45" y2="280" stroke="{GREEN}" stroke-width="2"/>
    <line x1="45" y1="315" x2="45" y2="330" stroke="{GREEN}" stroke-width="2"/>
    <line x1="45" y1="365" x2="45" y2="380" stroke="{GREEN}" stroke-width="2"/>

    <text x="30" y="480" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}" font-style="italic">Depois disso, Python sozinho.</text>

    <!-- grafico de custo achatado -->
    <g transform="translate(30, 540)">
      <line x1="0" y1="200" x2="360" y2="200" stroke="{TXT_DARK}" stroke-width="2"/>
      <line x1="0" y1="0" x2="0" y2="200" stroke="{TXT_DARK}" stroke-width="2"/>
      <text x="-15" y="105" text-anchor="end" font-family="{FONT_MONO}" font-size="12" fill="{MUTED_DARK}">tokens</text>
      <text x="180" y="225" text-anchor="middle" font-family="{FONT_MONO}" font-size="12" fill="{MUTED_DARK}">pecas</text>
      <!-- linha que sobe uma vez e achatada -->
      <polyline points="20,180 90,40 160,40 230,40 300,40" stroke="{GREEN}" stroke-width="4" fill="none"/>
      <circle cx="20" cy="180" r="6" fill="{GREEN}"/>
      <circle cx="90" cy="40" r="6" fill="{GREEN}"/>
      <circle cx="160" cy="40" r="6" fill="{GREEN}"/>
      <circle cx="230" cy="40" r="6" fill="{GREEN}"/>
      <circle cx="300" cy="40" r="6" fill="{GREEN}"/>
      <text x="310" y="45" font-family="{FONT_HEAD}" font-size="16" font-weight="700" fill="{GREEN}">zero</text>
    </g>

    <text x="30" y="850" font-family="{FONT_HEAD}" font-size="20" font-weight="700" fill="{GREEN_DARK}">418 pecas = 1 sessao de IA</text>
  </g>

  <text x="525" y="1370" text-anchor="middle" font-family="{FONT_BODY}" font-size="20" fill="{MUTED_DARK}" font-style="italic">O grafico da esquerda cresce em linha reta. O da direita achatou no segundo passo.</text>
</svg>
'''

# -----------------------------------------------------------------------------
# 02 - Cinco estagios
# -----------------------------------------------------------------------------
def svg_cinco_estagios():
    nodes = [
        ("1", "Fonte", "catalogo bruto", 90),
        ("2", "Copy", "contrato de copy", 280),
        ("3", "Prints", "pasta de imagens", 470),
        ("4", "Render", "3.344 PNGs", 660),
        ("5", "Publica", "posts agendados", 850),
    ]
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>')
    parts.append(f'<text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 02  ·  FIGURA 2</text>')
    parts.append(f'<text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">A fabrica em 5 estagios</text>')
    parts.append(f'<text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">Cada estagio le o que o anterior escreveu. Nenhum conhece o interior do outro.</text>')

    # Linha horizontal base
    parts.append(f'<line x1="80" y1="500" x2="970" y2="500" stroke="{GREEN}" stroke-width="2" opacity="0.4"/>')

    for n, t, sub, x in nodes:
        parts.append(f'<rect x="{x}" y="380" width="170" height="240" fill="none" stroke="{GREEN}" stroke-width="3" rx="14"/>')
        parts.append(f'<text x="{x+85}" y="430" text-anchor="middle" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">ESTAGIO {n}</text>')
        parts.append(f'<text x="{x+85}" y="490" text-anchor="middle" font-family="{FONT_HEAD}" font-size="28" font-weight="700" fill="{TXT_DARK}">{t}</text>')
        parts.append(f'<text x="{x+85}" y="540" text-anchor="middle" font-family="{FONT_BODY}" font-size="16" fill="{MUTED_DARK}">{sub}</text>')
        # seta para o proximo
        if x < 850:
            parts.append(f'<line x1="{x+175}" y1="500" x2="{x+200}" y2="500" stroke="{GREEN}" stroke-width="2"/>')
            parts.append(f'<polyline points="{x+192},495 {x+200},500 {x+192},505" stroke="{GREEN}" stroke-width="2" fill="none"/>')

    # Descricao embaixo de cada caixa
    descs = [
        "API publica\nJSON bruto",
        "prompt-mestre\n8 slides por item",
        "4 prints por item\ncadeira de URLs",
        "Python no Colab\nloop k automatico",
        "Buffer / Later\nDM com link",
    ]
    for (n, t, sub, x), d in zip(nodes, descs):
        for i, line in enumerate(d.split("\n")):
            parts.append(f'<text x="{x+85}" y="{680+i*22}" text-anchor="middle" font-family="{FONT_MONO}" font-size="13" fill="{MUTED_DARK}">{line}</text>')

    # Setas em U
    parts.append(f'<path d="M 175 740 Q 175 850 525 850 L 935 850" stroke="{GREEN}" stroke-width="2" fill="none" stroke-dasharray="4,4" opacity="0.6"/>')
    parts.append(f'<text x="525" y="900" text-anchor="middle" font-family="{FONT_MONO}" font-size="14" fill="{MUTED_DARK}">loop de retorno: correcao no estagio N volta como ajuste no catalogo</text>')

    # Cards de volume
    parts.append(f'<text x="80" y="1050" font-family="{FONT_HEAD}" font-size="32" font-weight="700" fill="{TXT_DARK}">Numeros da serie OpenRouter</text>')
    stats = [
        ("437", "modelos na fonte"),
        ("418", "carrosseis gerados"),
        ("3.344", "PNGs (418 x 8)"),
        ("0", "tokens na producao"),
    ]
    for i, (num, label) in enumerate(stats):
        x = 80 + i * 230
        parts.append(f'<rect x="{x}" y="1100" width="200" height="160" fill="none" stroke="{GREEN}" stroke-width="2" rx="14"/>')
        parts.append(f'<text x="{x+100}" y="1180" text-anchor="middle" font-family="{FONT_HEAD}" font-size="56" font-weight="800" fill="{GREEN}">{num}</text>')
        parts.append(f'<text x="{x+100}" y="1220" text-anchor="middle" font-family="{FONT_MONO}" font-size="14" fill="{MUTED_DARK}">{label}</text>')

    return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{body}\n</svg>'.format(w=W, h=H, body="\n".join(parts))


# -----------------------------------------------------------------------------
# 03 - Catalogo no Sheets
# -----------------------------------------------------------------------------
def svg_catalogo_sheets():
    cols = ["id", "nome", "tier", "modalidade", "preco_M", "url", "descricao"]
    rows = [
        ["1", "Alpha Vision", "free", "visao", "0", "alpha.com", "Modelo de visao gratuito"],
        ["2", "Beta Code", "barato", "codigo", "0.3", "beta.dev", "Codigo com baixo custo"],
        ["3", "Gamma Pro", "caro", "texto", "15.0", "gamma.ai", "Modelo premium de elite"],
        ["4", "Delta Image", "medio", "imagem", "2.5", "delta.io", "Geracao de imagem media"],
        ["5", "Epsilon Audio", "barato", "audio", "0.5", "epsilon.ai", "Audio de baixo custo"],
        ["6", "Zeta Video", "caro", "video", "12.0", "zeta.tv", "Video premium"],
    ]
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>')
    parts.append(f'<text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 03  ·  FIGURA 3</text>')
    parts.append(f'<text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">O catalogo e o motor</text>')
    parts.append(f'<text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">Google Sheets com 1 linha por item. As colunas certas decidem a copy.</text>')

    # Tabela
    col_w = 130
    x0 = 80
    y0 = 320
    parts.append(f'<rect x="{x0}" y="{y0}" width="{col_w*7}" height="50" fill="{GREEN}"/>')
    for i, c in enumerate(cols):
        parts.append(f'<text x="{x0+i*col_w+15}" y="{y0+32}" font-family="{FONT_MONO}" font-size="14" font-weight="700" fill="#FFFFFF">{c}</text>')
    parts.append(f'<line x1="{x0}" y1="{y0+50}" x2="{x0+col_w*7}" y2="{y0+50}" stroke="{GREEN_DARK}" stroke-width="2"/>')

    for ri, row in enumerate(rows):
        ry = y0 + 50 + ri * 50
        bg = BG_LIGHT if ri % 2 == 0 else "#EEE9DD"
        parts.append(f'<rect x="{x0}" y="{ry}" width="{col_w*7}" height="50" fill="{bg}"/>')
        for ci, cell in enumerate(row):
            color = TXT_DARK if ci != 3 else GREEN_DARK
            weight = "400"
            if ci in (2, 3):
                weight = "600"
            parts.append(f'<text x="{x0+ci*col_w+15}" y="{ry+32}" font-family="{FONT_MONO}" font-size="14" font-weight="{weight}" fill="{color}">{cell}</text>')

    # Setas de "viram eixo"
    parts.append(f'<path d="M 240 600 Q 240 720 130 720" stroke="{ORANGE}" stroke-width="2" fill="none"/>')
    parts.append(f'<polyline points="138,714 130,720 138,726" stroke="{ORANGE}" stroke-width="2" fill="none"/>')
    parts.append(f'<text x="80" y="760" font-family="{FONT_MONO}" font-size="14" fill="{ORANGE_DARK}">coluna "tier"</text>')
    parts.append(f'<text x="80" y="780" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{TXT_DARK}">vira EIXO 1</text>')

    parts.append(f'<path d="M 370 600 Q 370 720 480 720" stroke="{ORANGE}" stroke-width="2" fill="none"/>')
    parts.append(f'<polyline points="472,714 480,720 472,726" stroke="{ORANGE}" stroke-width="2" fill="none"/>')
    parts.append(f'<text x="430" y="760" font-family="{FONT_MONO}" font-size="14" fill="{ORANGE_DARK}">coluna "modalidade"</text>')
    parts.append(f'<text x="430" y="780" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{TXT_DARK}">vira EIXO 2</text>')

    # Explicacao
    parts.append(f'<rect x="80" y="870" width="890" height="280" fill="none" stroke="{GREEN}" stroke-width="2" rx="14"/>')
    parts.append(f'<text x="110" y="920" font-family="{FONT_HEAD}" font-size="26" font-weight="700" fill="{GREEN_DARK}">Regra do catalogo</text>')
    parts.append(f'<text x="110" y="970" font-family="{FONT_BODY}" font-size="20" fill="{TXT_DARK}">Atributo que muda a copy quando muda o valor = eixo de classificacao.</text>')
    parts.append(f'<text x="110" y="1010" font-family="{FONT_BODY}" font-size="20" fill="{TXT_DARK}">Atributo que nao muda nada = metadado de impressao.</text>')
    parts.append(f'<text x="110" y="1060" font-family="{FONT_BODY}" font-size="20" fill="{TXT_DARK}">2 eixos com 3 a 6 valores cada = 9 a 36 combinacoes = 9 a 36 teses.</text>')
    parts.append(f'<text x="110" y="1100" font-family="{FONT_BODY}" font-size="20" fill="{TXT_DARK}">Cada combinacao recebe um pool de 8 a 10 variacoes por slide.</text>')

    return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{body}\n</svg>'.format(w=W, h=H, body="\n".join(parts))


# -----------------------------------------------------------------------------
# 04 - Eixos e teses (matriz)
# -----------------------------------------------------------------------------
def svg_eixos_teses():
    tiers = ["FREE", "BARATO", "MEDIO", "CARO"]
    modalidades = ["texto", "codigo", "visao", "video", "imagem", "audio"]
    teses = {
        "FREE": "Feature de IA a custo zero. Margem integral na entrega.",
        "BARATO": "Centavos por milhao de tokens. Margem recorrente na diferenca.",
        "MEDIO": "Produtividade. A hora do time volta para o que vende.",
        "CARO": "Entrega critica com modelo de elite. Cliente paga pelo resultado.",
    }
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>')
    parts.append(f'<text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 04  ·  FIGURA 4</text>')
    parts.append(f'<text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">Eixos, teses e combinacoes</text>')
    parts.append(f'<text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">2 eixos com 4 e 6 valores = 24 combinacoes. 1 tese por combinacao.</text>')

    # Cabecalho
    parts.append(f'<text x="600" y="295" text-anchor="middle" font-family="{FONT_MONO}" font-size="14" fill="{GREEN_DARK}" letter-spacing="2">MODALIDADE (eixo 2)</text>')

    cell_w = 115
    cell_h = 88
    grid_x = 280
    grid_y = 320
    for i, m in enumerate(modalidades):
        parts.append(f'<text x="{grid_x + i*cell_w + cell_w/2}" y="{grid_y-10}" text-anchor="middle" font-family="{FONT_MONO}" font-size="14" font-weight="700" fill="{TXT_DARK}">{m}</text>')
    for i, t in enumerate(tiers):
        y = grid_y + i * cell_h
        parts.append(f'<text x="{grid_x-15}" y="{y+cell_h/2+5}" text-anchor="end" font-family="{FONT_MONO}" font-size="14" font-weight="700" fill="{TXT_DARK}">{t}</text>')
        for j in range(len(modalidades)):
            x = grid_x + j*cell_w
            fill = "#E5F4E8" if (i+j) % 2 == 0 else BG_LIGHT
            parts.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill}" stroke="{GREEN}" stroke-width="1"/>')
            parts.append(f'<text x="{x+cell_w/2}" y="{y+cell_h/2+6}" text-anchor="middle" font-family="{FONT_BODY}" font-size="16" fill="{TXT_DARK}">t{j+1}</text>')

    # Eixo labels
    parts.append(f'<text x="80" y="420" font-family="{FONT_MONO}" font-size="14" fill="{ORANGE_DARK}" letter-spacing="2" transform="rotate(-90, 80, 420)">TIER (eixo 1)</text>')

    # Caixa de tese (exemplo)
    by = grid_y + 4*cell_h + 80
    parts.append(f'<rect x="80" y="{by}" width="890" height="380" fill="none" stroke="{GREEN}" stroke-width="2" rx="14"/>')
    parts.append(f'<text x="110" y="{by+40}" font-family="{FONT_HEAD}" font-size="24" font-weight="700" fill="{GREEN_DARK}">Tese por combinacao</text>')
    parts.append(f'<text x="110" y="{by+75}" font-family="{FONT_BODY}" font-size="16" fill="{MUTED_DARK}">Cada combinacao (tier, modalidade) recebe UMA frase. Os 8 slides pagam essa promessa.</text>')

    teses_list = [
        ("FREE", teses["FREE"]),
        ("BARATO", teses["BARATO"]),
        ("MEDIO", teses["MEDIO"]),
        ("CARO", teses["CARO"]),
    ]
    for i, (k, v) in enumerate(teses_list):
        y = by + 110 + i * 60
        parts.append(f'<text x="110" y="{y}" font-family="{FONT_HEAD}" font-size="18" font-weight="700" fill="{ORANGE_DARK}">{k}</text>')
        parts.append(f'<text x="220" y="{y}" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">{v}</text>')

    return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{body}\n</svg>'.format(w=W, h=H, body="\n".join(parts))


# -----------------------------------------------------------------------------
# 05 - Anatomia 8 slides
# -----------------------------------------------------------------------------
def svg_anatomia_8_slides():
    slides = [
        ("1", "GANCHO", "dor que termina no nome"),
        ("2", "O QUE E", "define e desarma a objecao"),
        ("3", "PRATICA", "cena de uso por modalidade"),
        ("4", "O QUE VENDER", "bullets que viram proposta"),
        ("5", "COMO COBRAR", "monetizacao que fecha o gancho"),
        ("6", "LINK", "preco real e link oficial"),
        ("7", "BENCHMARK", "numero com leitura por faixa"),
        ("8", "CTA", "promessa do tier + chamada"),
    ]
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>')
    parts.append(f'<text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 05  ·  FIGURA 5</text>')
    parts.append(f'<text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">Anatomia fixa dos 8 slides</text>')
    parts.append(f'<text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">A funcao e o unico campo que liga copy a layout. Trocar a regra nao regera nada.</text>')

    # 2 colunas de 4 cards
    col_w = 410
    row_h = 260
    x0 = 80
    y0 = 290
    for i, (n, title, desc) in enumerate(slides):
        col = i % 2
        row = i // 2
        x = x0 + col * (col_w + 30)
        y = y0 + row * (row_h + 20)
        # card
        parts.append(f'<rect x="{x}" y="{y}" width="{col_w}" height="{row_h}" fill="#FFFFFF" stroke="{GREEN}" stroke-width="2" rx="14"/>')
        # numero grande
        parts.append(f'<text x="{x+30}" y="{y+90}" font-family="{FONT_HEAD}" font-size="84" font-weight="800" fill="{GREEN}">{n}</text>')
        # kicker
        parts.append(f'<text x="{x+150}" y="{y+50}" font-family="{FONT_MONO}" font-size="14" fill="{ORANGE_DARK}" letter-spacing="2">SLIDE {n} / 8</text>')
        # funcao
        parts.append(f'<text x="{x+150}" y="{y+90}" font-family="{FONT_HEAD}" font-size="26" font-weight="700" fill="{TXT_DARK}">{title}</text>')
        # descricao
        parts.append(f'<text x="{x+150}" y="{y+130}" font-family="{FONT_BODY}" font-size="16" fill="{MUTED_DARK}">{desc}</text>')

        # icone simples
        ix = x + col_w - 60
        iy = y + 30
        parts.append(f'<rect x="{ix}" y="{iy}" width="40" height="40" fill="none" stroke="{GREEN}" stroke-width="2" rx="8"/>')
        parts.append(f'<line x1="{ix+10}" y1="{iy+20}" x2="{ix+30}" y2="{iy+20}" stroke="{GREEN}" stroke-width="2"/>')
        parts.append(f'<line x1="{ix+20}" y1="{iy+10}" x2="{ix+20}" y2="{iy+30}" stroke="{GREEN}" stroke-width="2"/>')

    return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{body}\n</svg>'.format(w=W, h=H, body="\n".join(parts))


# -----------------------------------------------------------------------------
# 06 - Pipeline de prints
# -----------------------------------------------------------------------------
def svg_pipeline_prints():
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>')
    parts.append(f'<text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 06  ·  FIGURA 6</text>')
    parts.append(f'<text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">Cadeia de URLs para captura</text>')
    parts.append(f'<text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">Cada print tenta 3 URLs antes de desistir. HEAD antes de abrir a pagina.</text>')

    # 3 colunas de URLs
    col_titles = ["Tela principal", "Funcionalidade", "Preco"]
    urls = [
        ["site oficial", "model card HF", "pagina OR"],
        ["site oficial", "docs", "demo gravada"],
        ["site oficial", "pagina de preco", "tabela"],
    ]
    cx0 = 80
    cw = 290
    gap = 20
    for i, (title, us) in enumerate(zip(col_titles, urls)):
        x = cx0 + i * (cw + gap)
        # header
        parts.append(f'<rect x="{x}" y="290" width="{cw}" height="60" fill="{GREEN}" rx="14"/>')
        parts.append(f'<text x="{x+cw/2}" y="330" text-anchor="middle" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="#FFFFFF">{title}</text>')
        # urls verticais
        for j, u in enumerate(us):
            y = 380 + j * 100
            fill = "#FFFFFF" if j == 0 else BG_LIGHT
            parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="80" fill="{fill}" stroke="{GREEN}" stroke-width="2" rx="10"/>')
            parts.append(f'<text x="{x+20}" y="{y+30}" font-family="{FONT_MONO}" font-size="14" fill="{ORANGE_DARK}">URL {j+1}</text>')
            parts.append(f'<text x="{x+20}" y="{y+60}" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">{u}</text>')
            if j < 2:
                # seta para baixo
                parts.append(f'<line x1="{x+cw/2}" y1="{y+88}" x2="{x+cw/2}" y2="{y+100}" stroke="{GREEN}" stroke-width="2"/>')
                parts.append(f'<polyline points="{x+cw/2-5},{y+95} {x+cw/2},{y+100} {x+cw/2+5},{y+95}" stroke="{GREEN}" stroke-width="2" fill="none"/>')

    # Caixa de decisao
    dx = 80
    dy = 720
    parts.append(f'<rect x="{dx}" y="{dy}" width="890" height="120" fill="#E5F4E8" stroke="{GREEN}" stroke-width="2" rx="14"/>')
    parts.append(f'<text x="{dx+30}" y="{dy+45}" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{GREEN_DARK}">HEAD antes de abrir</text>')
    parts.append(f'<text x="{dx+30}" y="{dy+80}" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">200 OK = abre a pagina.  404 / 403 / timeout = pula para a proxima URL da cadeia.</text>')
    parts.append(f'<text x="{dx+30}" y="{dy+105}" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">Se todas as URLs falharem = status "faltando" no catalogo, sem print quebrado no disco.</text>')

    # Caixa de salvamento
    sx = 80
    sy = 880
    parts.append(f'<rect x="{sx}" y="{sy}" width="890" height="280" fill="none" stroke="{ORANGE}" stroke-width="2" rx="14"/>')
    parts.append(f'<text x="{sx+30}" y="{sy+45}" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{ORANGE_DARK}">Padrao de arquivo</text>')
    parts.append(f'<text x="{sx+30}" y="{sy+90}" font-family="{FONT_MONO}" font-size="20" fill="{TXT_DARK}">[id-do-item]/[funcao-do-print].png</text>')
    parts.append(f'<text x="{sx+30}" y="{sy+135}" font-family="{FONT_MONO}" font-size="16" fill="{MUTED_DARK}">Exemplo:</text>')
    parts.append(f'<text x="{sx+30}" y="{sy+165}" font-family="{FONT_MONO}" font-size="16" fill="{MUTED_DARK}">001-alpha-3-5/tela.png</text>')
    parts.append(f'<text x="{sx+30}" y="{sy+190}" font-family="{FONT_MONO}" font-size="16" fill="{MUTED_DARK}">001-alpha-3-5/funcionalidade.png</text>')
    parts.append(f'<text x="{sx+30}" y="{sy+215}" font-family="{FONT_MONO}" font-size="16" fill="{MUTED_DARK}">001-alpha-3-5/preco.png</text>')
    parts.append(f'<text x="{sx+30}" y="{sy+240}" font-family="{FONT_MONO}" font-size="16" fill="{MUTED_DARK}">001-alpha-3-5/benchmark.png</text>')

    # Modo recheck
    rx = 80
    ry = 1200
    parts.append(f'<text x="{rx}" y="{ry}" font-family="{FONT_MONO}" font-size="16" fill="{ORANGE_DARK}" letter-spacing="2">MODO RECHECK (semanal)</text>')
    parts.append(f'<text x="{rx}" y="{ry+30}" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">Para cada print ja capturado: HEAD na URL. Se morreu, apaga o arquivo.</text>')

    return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{body}\n</svg>'.format(w=W, h=H, body="\n".join(parts))


# -----------------------------------------------------------------------------
# 07 - Loop k
# -----------------------------------------------------------------------------
def svg_loop_k():
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>')
    parts.append(f'<text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 07  ·  FIGURA 7</text>')
    parts.append(f'<text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">O loop k do renderizador</text>')
    parts.append(f'<text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">O browser mede o que o codigo nao adivinha. Python ajusta em 4% por rodada.</text>')

    # Fluxograma vertical
    nodes = [
        ("k = 1.00", "monta slide", GREEN),
        ("mede altura", "Chromium / JS", "#1B1714"),
        ("estourou?", "scrollHeight > 1350?", "#1B1714"),
        ("sim: k = k * 0.96", "encolhe texto", ORANGE),
        ("nao e sobra?", "espaco > 80px?", "#1B1714"),
        ("sim: k = k * 1.04", "cresce texto", ORANGE),
        ("salva PNG", "ate 14 rodadas", GREEN),
    ]

    cx = 525
    cw = 400
    ch = 110
    y = 290
    for i, (label, sub, color) in enumerate(nodes):
        # box
        parts.append(f'<rect x="{cx-cw/2}" y="{y}" width="{cw}" height="{ch}" fill="#FFFFFF" stroke="{color}" stroke-width="3" rx="14"/>')
        parts.append(f'<text x="{cx}" y="{y+45}" text-anchor="middle" font-family="{FONT_HEAD}" font-size="26" font-weight="700" fill="{color}">{label}</text>')
        parts.append(f'<text x="{cx}" y="{y+80}" text-anchor="middle" font-family="{FONT_MONO}" font-size="14" fill="{MUTED_DARK}">{sub}</text>')
        # seta para o proximo
        if i < len(nodes) - 1:
            parts.append(f'<line x1="{cx}" y1="{y+ch}" x2="{cx}" y2="{y+ch+30}" stroke="{GREEN}" stroke-width="2"/>')
            parts.append(f'<polyline points="{cx-5},{y+ch+25} {cx},{y+ch+30} {cx+5},{y+ch+25}" stroke="{GREEN}" stroke-width="2" fill="none"/>')
        y += ch + 40

    # Legenda lateral
    parts.append(f'<rect x="80" y="290" width="280" height="600" fill="none" stroke="{GREEN}" stroke-width="2" rx="14"/>')
    parts.append(f'<text x="100" y="325" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{GREEN_DARK}">Leitura do k</text>')
    ks = [
        ("1.00", "coube", GREEN),
        ("acima", "sobrava", GREEN),
        ("0.85 a 0.96", "encolheu sozinho", "#1B1714"),
        ("abaixo de 0.85", "copy comprida", ORANGE),
        ("14 rodadas", "nao coube", ORANGE_DARK),
    ]
    # Substituir < por &lt; para nao quebrar o XML
    ks = [(k.replace("<", "&lt;"), d, c) for (k, d, c) in ks]
    for i, (k, desc, c) in enumerate(ks):
        y2 = 380 + i * 70
        parts.append(f'<text x="100" y="{y2}" font-family="{FONT_HEAD}" font-size="20" font-weight="700" fill="{c}">{k}</text>')
        parts.append(f'<text x="100" y="{y2+22}" font-family="{FONT_BODY}" font-size="14" fill="{MUTED_DARK}">{desc}</text>')

    # Caixa de protecao
    parts.append(f'<rect x="700" y="290" width="280" height="600" fill="#E5F4E8" stroke="{GREEN}" stroke-width="2" rx="14"/>')
    parts.append(f'<text x="720" y="325" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{GREEN_DARK}">Protecoes</text>')
    prot = [
        "Fonte nao carregou = aborta",
        "Travessao na copy = aviso no log",
        "Browser reutilizado no lote",
        "Log com k por slide",
        "Filtro: k abaixo de 0.85 ou aviso",
        "Sem filtro = revisa 50 slides",
    ]
    for i, p in enumerate(prot):
        parts.append(f'<text x="720" y="{380+i*60}" font-family="{FONT_BODY}" font-size="15" fill="{TXT_DARK}">- {p}</text>')

    return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{body}\n</svg>'.format(w=W, h=H, body="\n".join(parts))


# -----------------------------------------------------------------------------
# 08 - Esteira de publicacao
# -----------------------------------------------------------------------------
def svg_esteira_publicacao():
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>')
    parts.append(f'<text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 08  ·  FIGURA 8</text>')
    parts.append(f'<text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">Da pasta ao direct</text>')
    parts.append(f'<text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">A peca de topo aponta para o proximo degrau, nao para o mais caro.</text>')

    # Escada 4 degraus
    steps = [
        ("Degrau 0", "carrossel", "peca de topo", "sem custo"),
        ("Degrau 1", "comentario", "palavra-chave", "engajamento"),
        ("Degrau 2", "DM", "link do material", "captura lead"),
        ("Degrau 3", "oferta", "produto principal", "venda"),
    ]
    bx0 = 80
    bw = 890
    bh = 140
    by0 = 290
    for i, (label, what, how, why) in enumerate(steps):
        y = by0 + i * (bh + 20)
        # caixa
        fill = "#E5F4E8" if i % 2 == 0 else "#FFFFFF"
        parts.append(f'<rect x="{bx0}" y="{y}" width="{bw}" height="{bh}" fill="{fill}" stroke="{GREEN}" stroke-width="2" rx="14"/>')
        # label
        parts.append(f'<text x="{bx0+30}" y="{y+40}" font-family="{FONT_MONO}" font-size="18" font-weight="700" fill="{ORANGE_DARK}" letter-spacing="2">{label.upper()}</text>')
        # what
        parts.append(f'<text x="{bx0+30}" y="{y+85}" font-family="{FONT_HEAD}" font-size="32" font-weight="700" fill="{TXT_DARK}">{what}</text>')
        # how
        parts.append(f'<text x="{bx0+30}" y="{y+115}" font-family="{FONT_BODY}" font-size="18" fill="{MUTED_DARK}">{how}</text>')
        # why (caixa lateral)
        parts.append(f'<rect x="{bx0+bw-220}" y="{y+25}" width="180" height="90" fill="{GREEN}" rx="10"/>')
        parts.append(f'<text x="{bx0+bw-130}" y="{y+55}" text-anchor="middle" font-family="{FONT_BODY}" font-size="16" fill="#FFFFFF">{why}</text>')
        parts.append(f'<text x="{bx0+bw-130}" y="{y+85}" text-anchor="middle" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="#FFFFFF">{["topo","engaja","captura","vende"][i]}</text>')

        # seta para o proximo
        if i < len(steps) - 1:
            parts.append(f'<line x1="{bx0+bw/2}" y1="{y+bh}" x2="{bx0+bw/2}" y2="{y+bh+15}" stroke="{GREEN}" stroke-width="2"/>')

    # Bloco automation
    ax = 80
    ay = by0 + 4*(bh+20) + 20
    parts.append(f'<rect x="{ax}" y="{ay}" width="890" height="200" fill="none" stroke="{ORANGE}" stroke-width="2" rx="14"/>')
    parts.append(f'<text x="{ax+30}" y="{ay+40}" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{ORANGE_DARK}">Bloco automation no JSON</text>')
    fields = [
        "keywords: lista de 1 a 2 palavras",
        "mensagem: DM ate 280 caracteres",
        "link: mesmo para todos os itens",
        "public_reply_enabled: true",
        "public_reply_text: 'Te chamei no direct!'",
    ]
    for i, f in enumerate(fields):
        parts.append(f'<text x="{ax+30}" y="{ay+80+i*22}" font-family="{FONT_MONO}" font-size="14" fill="{TXT_DARK}">{f}</text>')

    return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{body}\n</svg>'.format(w=W, h=H, body="\n".join(parts))


# -----------------------------------------------------------------------------
# 09 - Checklist de replicacao
# -----------------------------------------------------------------------------
def svg_checklist_replicacao():
    steps = [
        ("1", "Escolha a fonte", "catalogo com atributos que mudem a copy"),
        ("2", "Defina os eixos", "2 eixos com 3 a 6 valores cada"),
        ("3", "Desenhe o contrato", "campos, anatomia, automation"),
        ("4", "Peca o gerador de copy", "teses + pools de 8 a 10"),
        ("5", "Peca o renderizador", "Python no Colab, loop k"),
        ("6", "Gere os assets", "IA de imagem, sessao UNICA"),
        ("7", "Gere 3 amostras", "corrija no gerador, regenere"),
        ("8", "Capture os prints", "cadeia de URLs, recheck"),
        ("9", "Gere o lote", "filtre k abaixo de 0.85"),
        ("10", "Publique pelo JSON", "Buffer, Later, Meta"),
    ]
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG_LIGHT}"/>')
    parts.append(f'<text x="80" y="100" font-family="{FONT_MONO}" font-size="20" fill="{GREEN_DARK}" letter-spacing="3">CAP. 10  ·  FIGURA 9</text>')
    parts.append(f'<text x="80" y="170" font-family="{FONT_HEAD}" font-size="56" font-weight="700" fill="{TXT_DARK}">Playbook de 10 passos</text>')
    parts.append(f'<text x="80" y="215" font-family="{FONT_BODY}" font-size="22" fill="{MUTED_DARK}">Da proxima serie. A fabrica e o ativo, nao os posts.</text>')

    # Lista vertical numerada
    y0 = 290
    row_h = 90
    for i, (n, title, desc) in enumerate(steps):
        y = y0 + i * row_h
        # numero
        parts.append(f'<circle cx="120" cy="{y+40}" r="30" fill="{GREEN}"/>')
        parts.append(f'<text x="120" y="{y+52}" text-anchor="middle" font-family="{FONT_HEAD}" font-size="28" font-weight="800" fill="#FFFFFF">{n}</text>')
        # titulo
        parts.append(f'<text x="180" y="{y+38}" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{TXT_DARK}">{title}</text>')
        # descricao
        parts.append(f'<text x="180" y="{y+62}" font-family="{FONT_BODY}" font-size="16" fill="{MUTED_DARK}">{desc}</text>')
        # divisor
        if i < len(steps) - 1:
            parts.append(f'<line x1="180" y1="{y+row_h-5}" x2="970" y2="{y+row_h-5}" stroke="{GREEN}" stroke-width="1" opacity="0.3"/>')

    # destaque gasto de tokens
    cx = 80
    cy = y0 + 10*row_h + 30
    parts.append(f'<rect x="{cx}" y="{cy}" width="890" height="160" fill="none" stroke="{ORANGE}" stroke-width="3" rx="14"/>')
    parts.append(f'<text x="{cx+30}" y="{cy+45}" font-family="{FONT_HEAD}" font-size="22" font-weight="700" fill="{ORANGE_DARK}">Onde o token GASTA (3 sessoes)</text>')
    parts.append(f'<text x="{cx+30}" y="{cy+85}" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">- Sessao de design (texto): prompts mestres, template, roteiro de assets.</text>')
    parts.append(f'<text x="{cx+30}" y="{cy+115}" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">- Sessao unica de geracao visual (imagem): capa, icones, moldura, detalhe de marca.</text>')
    parts.append(f'<text x="{cx+30}" y="{cy+145}" font-family="{FONT_BODY}" font-size="18" fill="{TXT_DARK}">- Sessao de guia: runbook da serie para consulta futura.</text>')

    return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{body}\n</svg>'.format(w=W, h=H, body="\n".join(parts))


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
GENERATORS = [
    ("00-capa", svg_capa),
    ("01-jeito1-vs-jeito2", svg_jeito1_vs_jeito2),
    ("02-os-cinco-estagios", svg_cinco_estagios),
    ("03-catalogo-sheets", svg_catalogo_sheets),
    ("04-eixos-e-teses", svg_eixos_teses),
    ("05-anatomia-8-slides", svg_anatomia_8_slides),
    ("06-pipeline-prints", svg_pipeline_prints),
    ("07-loop-k", svg_loop_k),
    ("08-esteira-publicacao", svg_esteira_publicacao),
    ("09-checklist-replicacao", svg_checklist_replicacao),
]

if __name__ == "__main__":
    for name, gen in GENERATORS:
        path = OUT / f"{name}.svg"
        path.write_text(gen())
        print(f"OK: {path.name}  ({path.stat().st_size} bytes)")
