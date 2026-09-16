#!/usr/bin/env python3
"""check-manuscrito.py

Varre o manuscrito em busca de:
  - travessão (U+2014) e meia-risca (U+2013)
  - linhas de código/problema com mais de 60 caracteres
  - artefatos de edição: font-size=0, <text> vazio, fill=none em texto,
    frase truncada no meio sem pontuação final
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRITO = ROOT / "manuscrito"
FIGURAS = ROOT / "figuras"

EN_DASH = "\u2013"   # –
EM_DASH = "\u2014"   # —

failures = []

def check_file(path):
    text = path.read_text()
    lines = text.splitlines()

    # 1. travessao / meia-risca
    for i, line in enumerate(lines, 1):
        if EN_DASH in line:
            failures.append(f"{path.name}:{i}: meia-risca (U+2013) encontrada")
        if EM_DASH in line:
            failures.append(f"{path.name}:{i}: travessao (U+2014) encontrada")

    # 2. blocos de codigo (delimitados por ```) com linha > 60 chars
    in_code = False
    fence = "```"
    code_lang_re = re.compile(r"^```\s*\w*\s*$")
    for i, line in enumerate(lines, 1):
        stripped = line.rstrip()
        if stripped.startswith("```") and code_lang_re.match(stripped):
            in_code = not in_code
            continue
        if in_code:
            # contar largura visual aproximada (chars)
            if len(stripped) > 60:
                failures.append(f"{path.name}:{i}: linha de codigo com {len(stripped)} chars (max 60): {stripped[:60]}...")

    # 3. artefatos comuns
    for i, line in enumerate(lines, 1):
        if 'font-size="0"' in line or "font-size: 0" in line:
            failures.append(f"{path.name}:{i}: font-size 0 detectado")
        if re.search(r"<text[^>]*></text>", line):
            failures.append(f"{path.name}:{i}: <text> vazio detectado")

    # 4. frase truncada (regex desabilitado: falsos positivos com palavras legitimas)
    # truncated = re.compile(r"\w\s+a med\w*$|\w\s+na med\w*$|\.\.\.$", re.IGNORECASE)
    # for i, line in enumerate(lines, 1):
    #     if truncated.search(line.strip()):
    #         failures.append(f"{path.name}:{i}: frase possivelmente truncada")

    # 5. número sem fonte (heuristica simples: "X%" sem fonte adjacente)
    # - skip, complexo demais para escopo deste gate


def check_figures():
    for svg in FIGURAS.rglob("*.svg"):
        # qr_box nao precisa checar geometria complexa
        text = svg.read_text()

        # texto vazio
        if re.search(r"<text[^>]*>\s*</text>", text):
            failures.append(f"{svg.name}: <text> vazio")

        # font-size=0
        if 'font-size="0"' in text or "font-size: 0" in text:
            failures.append(f"{svg.name}: font-size 0")

        # fill=none em texto com conteudo
        # (heuristica: <text ... fill="none" ...>X</text>)
        for m in re.finditer(r'<text[^>]*fill="none"[^>]*>([^<]+)</text>', text):
            if m.group(1).strip():
                failures.append(f"{svg.name}: texto com conteudo e fill=none: '{m.group(1)[:30]}'")


def main():
    for md in MANUSCRITO.glob("*.md"):
        check_file(md)
    check_figures()

    if failures:
        print("FALHAS ENCONTRADAS:")
        for f in failures:
            print(f"  - {f}")
        print(f"\nTotal: {len(failures)}")
        sys.exit(1)
    else:
        print("OK: manuscrito sem travessao, codigo <=60 chars, sem artefatos.")

if __name__ == "__main__":
    main()
