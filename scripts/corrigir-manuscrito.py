#!/usr/bin/env python3
"""corrigir-manuscrito.py

Aplica correcoes automaticas:
  - Substitui travessao (—) por ": " ou ", e " conforme contexto
  - Substitui meia-risca (–) por " a " (intervalo) ou remove
  - Quebra linhas de codigo > 60 chars em argumentos/opcoes

Apos rodar, conferir visualmente cada substituicao antes de fechar.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRITO = ROOT / "manuscrito"

EN_DASH = "\u2013"   # –
EM_DASH = "\u2014"   # —

stats = {"em_dash": 0, "en_dash": 0, "long_lines": 0}


def fix_em_dash(text):
    """Substitui travessão por ", e " ou ": " dependendo do contexto."""
    # " — " entre palavras vira ", e " (conjunção) ou ": " (conclusivo)
    # Heuristica simples: se a palavra antes é curta (até 30 chars) e a depois
    # começa com maiuscula, eh conclusivo -> ": "
    # senao -> ", e "
    def repl(match):
        before = match.group(1)
        after = match.group(2)
        if before.endswith(".") or before.endswith("?") or before.endswith("!"):
            sep = " "
        elif after and after[0].isupper():
            sep = ": "
        else:
            sep = ", e "
        stats["em_dash"] += 1
        return f"{before}{sep}{after}"

    text = re.sub(r"(\S)\s+\u2014\s+(\S)", repl, text)
    return text


def fix_en_dash(text):
    """Substitui meia-risca por ' a ' quando eh intervalo (numero a numero)."""
    # intervalo "1-9" (sem espaços) ou "1 a 9" com meia-risca
    # mas o caso eh meia-risca U+2013
    def repl(match):
        a, b = match.group(1), match.group(2)
        # se ambos sao numericos ou palavras curtas, eh intervalo
        if (a.isdigit() or a.isalpha() and len(a) <= 4) and (b.isdigit() or b.isalpha() and len(b) <= 6):
            stats["en_dash"] += 1
            return f"{a} a {b}"
        return match.group(0)

    text = re.sub(r"(\S)\u2013(\S)", repl, text)
    # meia-risca cercada de espacos -> remove e poe virgula
    text = re.sub(r"\s+\u2013\s+", ", ", text)
    return text


def fix_long_lines(text):
    """Quebra linhas de codigo > 60 chars em multiplas tentativas."""
    lines = text.splitlines(keepends=True)
    in_code = False
    fence_re = re.compile(r"^```")
    out = []
    for line in lines:
        stripped = line.rstrip("\n")
        if fence_re.match(stripped):
            in_code = not in_code
            out.append(line)
            continue
        if in_code and len(stripped) > 60:
            # tentar quebrar em multiplos separadores, do mais proximo de 50 ao mais distante
            candidates = []
            for sep in ["; ", ", ", " e ", " ou ", " | "]:
                idx = 0
                while True:
                    idx = stripped.find(sep, idx)
                    if idx == -1:
                        break
                    cut = idx + len(sep)
                    if 40 <= cut <= 65:
                        candidates.append((abs(60 - cut), cut, sep))
                    idx += 1
            if candidates:
                candidates.sort()
                _, cut, sep = candidates[0]
                out.append(stripped[:cut] + "\n")
                rest = stripped[cut:].lstrip()
                # continua quebrando recursivamente o resto
                while len(rest) > 60:
                    broken2 = False
                    for sep2 in ["; ", ", ", " e ", " ou ", " | "]:
                        idx = rest.find(sep2)
                        if 40 <= idx + len(sep2) <= 65:
                            out.append("    " + rest[:idx + len(sep2)] + "\n")
                            rest = rest[idx + len(sep2):].lstrip()
                            broken2 = True
                            stats["long_lines"] += 1
                            break
                    if not broken2:
                        break
                out.append("    " + rest + "\n")
                stats["long_lines"] += 1
            else:
                # tenta quebrar em espaco
                for i in range(50, min(65, len(stripped))):
                    if stripped[i] == " ":
                        out.append(stripped[:i] + "\n")
                        out.append("    " + stripped[i+1:] + "\n")
                        stats["long_lines"] += 1
                        break
                else:
                    out.append(line)
        else:
            out.append(line)
    return "".join(out)


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else [str(p) for p in MANUSCRITO.glob("*.md")]
    for path in targets:
        p = Path(path)
        text = p.read_text()
        before = text
        text = fix_em_dash(text)
        text = fix_en_dash(text)
        text = fix_long_lines(text)
        if text != before:
            p.write_text(text)
            print(f"CORRIGIDO: {p.name}")

    print(f"\nEstatisticas:")
    print(f"  Travessoes (—) substituidas: {stats['em_dash']}")
    print(f"  Meias-riscas (–) substituidas: {stats['en_dash']}")
    print(f"  Linhas longas quebradas: {stats['long_lines']}")


if __name__ == "__main__":
    main()
