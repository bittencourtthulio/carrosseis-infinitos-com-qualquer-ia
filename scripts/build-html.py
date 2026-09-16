#!/usr/bin/env python3
"""build-html.py

Monta livro.html a partir do manuscrito/ e das figuras/.
Capa em pagina cheia, miolo branco A5, numeração automatica via paged.js.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRITO = ROOT / "manusrito" if (ROOT / "manusrito").exists() else ROOT / "manuscrito"
FIGURAS = ROOT / "figuras"
OUT = ROOT / "livro.html"

# Ordem dos capitulos
ORDEM = [
    "00-abertura",
    "01-a-armadilha-do-token-na-peca",
    "02-a-fabrica-em-cinco-estagios",
    "03-a-fonte-de-dados",
    "04-eixos-teses-e-pools",
    "05-anatomia-dos-8-slides",
    "06-prova-visual",
    "07-renderizar-sem-surpresas",
    "08-publicacao-e-dm",
    "09-erros-que-a-serie-cometeu",
    "10-replicar-para-qualquer-serie",
    "99-checklist-final",
]


def md_to_html(text):
    """Conversao minima de markdown para HTML (sem deps externas).

    Suporta:
      - # / ## / ### / ####
      - listas com - ou *
      - negrito **x**
      - italico *x*
      - codigo `x`
      - bloco de codigo com ```
      - links [x](y)
      - imagens ![alt](src)
      - blockquote com >
      - hr com ---
      - tabelas |a|b|
    """
    html = text
    lines = html.split("\n")
    out = []
    in_code = False
    code_buf = []
    in_list = False
    in_table = False
    table_buf = []

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    def close_table():
        nonlocal in_table, table_buf
        if in_table and table_buf:
            out.append('<table class="md-table">')
            header = table_buf[0]
            out.append("<thead><tr>")
            for cell in header.split("|"):
                cell = cell.strip()
                if cell:
                    out.append(f"<th>{cell}</th>")
            out.append("</tr></thead><tbody>")
            for row in table_buf[2:]:
                out.append("<tr>")
                for cell in row.split("|"):
                    cell = cell.strip()
                    if cell:
                        out.append(f"<td>{cell}</td>")
                out.append("</tr>")
            out.append("</tbody></table>")
            in_table = False
            table_buf = []

    for line in lines:
        stripped = line.strip()

        # code fence
        if stripped.startswith("```"):
            if in_code:
                out.append("<pre><code>" + "\n".join(code_buf) + "</code></pre>")
                code_buf = []
                in_code = False
            else:
                close_list()
                close_table()
                in_code = True
            continue
        if in_code:
            code_buf.append(line)
            continue

        # table
        if "|" in stripped and stripped.startswith("|") and stripped.endswith("|"):
            close_list()
            in_table = True
            table_buf.append(stripped)
            continue
        elif in_table:
            close_table()

        # hr
        if stripped == "---":
            close_list()
            out.append("<hr/>")
            continue

        # headers
        m = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if m:
            close_list()
            level = len(m.group(1))
            content = m.group(2)
            out.append(f"<h{level}>{inline(content)}</h{level}>")
            continue

        # blockquote
        if stripped.startswith("> "):
            close_list()
            out.append(f"<blockquote>{inline(stripped[2:])}</blockquote>")
            continue

        # list
        if stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(stripped[2:])}</li>")
            continue
        elif stripped.startswith(tuple(f"{i}. " for i in range(10))):
            # ordered list simplificado
            close_list()
            content = stripped.split(". ", 1)[1]
            if not hasattr(out, "_ol"):
                out.append("<ol>")
                out.append(f"<li>{inline(content)}</li>")
            else:
                out.append(f"<li>{inline(content)}</li>")
            continue
        else:
            close_list()

        # paragrafo
        if stripped:
            out.append(f"<p>{inline(stripped)}</p>")

    close_list()
    close_table()
    if in_code:
        out.append("<pre><code>" + "\n".join(code_buf) + "</code></pre>")

    return "\n".join(out)


def inline(text):
    """Formatacao inline: negrito, italico, codigo, links, imagens."""
    # imagem primeiro (mais especifica)
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        r'<img class="md-img" src="\2" alt="\1"/>',
        text,
    )
    # link
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2">\1</a>',
        text,
    )
    # bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # italic
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    # code
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def build():
    body = []

    # Pagina de capa (full-bleed)
    cover_svg = FIGURAS / "00-capa.svg"
    body.append(f'''
<section class="capa">
  <img src="figuras/00-capa.svg" alt="Capa do livro"/>
</section>
''')

    # Pagina de ficha tecnica
    body.append('''
<section class="ficha">
  <div class="ficha-inner">
    <h2>Carrosseis Infinitos com Qualquer IA</h2>
    <h3>Praticamente Sem Gastar Tokens</h3>
    <p class="autor">Thulio Bittencourt</p>
    <p class="editora">Academia do Codigo &middot; Metodologias EXPX</p>
    <p class="edicao">1a edicao &middot; setembro de 2026</p>
    <p class="formato">Formato A5 &middot; PDF diagramado &middot; paginas numeradas</p>
    <p class="repositorio">Repositorio publico com todos os prompts:<br/>
      <a href="https://github.com/bittencourtthulio/carrosseis-infinitos-com-qualquer-ia">github.com/bittencourtthulio/carrosseis-infinitos-com-qualquer-ia</a>
    </p>
    <p class="marca-terceiros">OpenRouter e citado neste livro como fonte de dados publica, sem endosso. As marcas ChatGPT, Claude, Gemini, Midjourney, DALL-E, Imagen, Ideogram, Google Colab, Google Sheets, Google Drive, Canva, Buffer, Later e Meta Business Suite sao propriedades de seus respectivos donos. Este livro nao e oficial nem endossado por nenhuma dessas marcas.</p>
  </div>
</section>
''')

    # Sumario
    body.append('''
<section class="sumario-pagina">
  <h2>Sumario</h2>
  <ol>
    <li>Abertura</li>
    <li>1. A armadilha do token na peca</li>
    <li>2. A fabrica em cinco estagios</li>
    <li>3. A fonte de dados: o catalogo e o motor</li>
    <li>4. Eixos, teses e pools de frases</li>
    <li>5. Anatomia dos 8 slides como contrato (e os assets visuais)</li>
    <li>6. Prova visual em escala</li>
    <li>7. Renderizar sem surpreas</li>
    <li>8. Publicacao e DM na mesma chamada</li>
    <li>9. Erros que a serie cometeu</li>
    <li>10. Replicar para qualquer serie + checklist final</li>
    <li>99. Checklist final e pendencias de publicacao</li>
  </ol>
</section>
''')

    # Capitulos
    for i, cap in enumerate(ORDEM):
        path = MANUSCRITO / f"{cap}.md"
        if not path.exists():
            print(f"MISSING: {cap}.md")
            continue
        text = path.read_text()
        # remove H1 do inicio (vira titulo da pagina via classe)
        text = re.sub(r"^# .+\n", "", text, count=1)
        # quebra antes de "## QR codes dos prompts deste capitulo" para virar pagina propria
        parts = re.split(r"\n## QR codes dos prompts deste capitulo\n", text)
        main_text = parts[0]
        qr_section = parts[1] if len(parts) > 1 else None

        body.append(f'<section class="capitulo" data-cap="{cap}">')
        body.append(md_to_html(main_text))
        body.append("</section>")

        # Pagina de QR codes do capitulo (se houver)
        if qr_section:
            body.append(f'<section class="qr-page" data-cap="{cap}">')
            body.append("<h2>QR codes dos prompts deste capitulo</h2>")
            body.append(md_to_html(qr_section))
            body.append("</section>")

        # Pagina de figura (uma por capitulo com prancha)
        prancha_map = {
            "01-a-armadilha-do-token-na-peca": "01-jeito1-vs-jeito2",
            "02-a-fabrica-em-cinco-estagios": "02-os-cinco-estagios",
            "03-a-fonte-de-dados": "03-catalogo-sheets",
            "04-eixos-teses-e-pools": "04-eixos-e-teses",
            "05-anatomia-dos-8-slides": "05-anatomia-8-slides",
            "06-prova-visual": "06-pipeline-prints",
            "07-renderizar-sem-surpresas": "07-loop-k",
            "08-publicacao-e-dm": "08-esteira-publicacao",
            "10-replicar-para-qualquer-serie": "09-checklist-replicacao",
        }
        if cap in prancha_map:
            svg = FIGURAS / f"{prancha_map[cap]}.svg"
            if svg.exists():
                body.append(f'<section class="prancha"><img src="figuras/{prancha_map[cap]}.svg" alt="Prancha do capitulo"/></section>')

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <title>Carrosseis Infinitos com Qualquer IA - Praticamente Sem Gastar Tokens</title>
  <link rel="stylesheet" href="scripts/book.css"/>
  <script src="https://cdn.jsdelivr.net/npm/pagedjs/dist/paged.polyfill.js"></script>
</head>
<body>
{''.join(body)}
</body>
</html>
'''
    OUT.write_text(html)
    print(f"OK: {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build()
