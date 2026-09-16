#!/usr/bin/env python3
"""Adiciona secao de QR codes ao final de cada capitulo com prompts."""
import re
from pathlib import Path

ROOT = Path("/Users/thuliobittencourt/Documents/Projetos/Livros/Livro - Carroseis com IA sem gastar tokens")
MANUSCRITO = ROOT / "manuscrito"

REPO = "https://github.com/bittencourtthulio/carrosseis-infinitos-com-qualquer-ia/blob/main/prompts"

PROMPT_LABEL = {
    "cap-01-armadilha": "Prompt 01 - A armadilha do token na peca",
    "cap-02-cinco-estagios": "Prompt 02 - A fabrica em cinco estagios",
    "cap-03-catalogo": "Prompt 03 - A fonte de dados",
    "cap-04-teses": "Prompt 04 (1/2) - Teses por combinacao",
    "cap-04-pools": "Prompt 04 (2/2) - Pools de variacoes",
    "cap-05-anatomia": "Prompt 05 (1/2) - Anatomia dos 8 slides",
    "cap-05-assets": "Prompt 05 (2/2) - Briefing para IA de imagem",
    "cap-06-prints": "Prompt 06 - Captura de prints em escala",
    "cap-07-renderizador": "Prompt 07 - Renderizador em lote",
    "cap-08-automacao": "Prompt 08 (1/2) - Bloco de automacao (3 itens)",
    "cap-08-automacao-massa": "Prompt 08 (2/2) - Bloco de automacao em massa",
    "cap-09-defeitos": "Prompt 09 - Validacao dos 7 defeitos",
    "cap-10-prontidao": "Prompt 10 - Auditoria de prontidao",
}

PATTERN = re.compile(r"prompts/(cap-[a-z0-9-]+)\.md")

def section_for(prompt_ids):
    if not prompt_ids:
        return ""
    blocks = []
    blocks.append("\n\n## QR codes dos prompts deste capitulo\n\n")
    blocks.append("Aponte a camera do celular para cada QR code ou clique no link para abrir o arquivo `.md` completo no GitHub. O arquivo contem o prompt destacado, variacoes para Claude e Gemini, exemplos preenchidos e o checklist de validacao.\n\n")
    for pid in prompt_ids:
        label = PROMPT_LABEL.get(pid, pid)
        qr_box = f"../figuras/qr_box/{pid}.svg"
        url = f"{REPO}/{pid}.md"
        blocks.append(f"### {label}\n\n")
        blocks.append(f"![QR code do {label}]({qr_box})\n\n")
        blocks.append(f"[Abrir no GitHub]({url})  \n")
        blocks.append(f"Arquivo: `prompts/{pid}.md` no repositorio publico.\n\n")
    return "".join(blocks)

# Remove secao antiga se ja existir
SECTION_RE = re.compile(r"\n## QR codes dos prompts deste capitulo\n.*?(?=\n## |\Z)", re.DOTALL)

for md in sorted(MANUSCRITO.glob("*.md")):
    # Excluir o checklist final (nao tem prompt para leitor colar)
    if md.name.startswith("99-"):
        continue
    text = md.read_text()
    # Remove secao antiga
    text = SECTION_RE.sub("", text)
    # Coleta prompts mencionados (excluindo padroes genericos como cap-NN-nome.md)
    raw_ids = PATTERN.findall(text)
    ids = sorted(set(i for i in raw_ids if "-" in i and i.count("-") >= 2))
    # Remove IDs genericos do checklist (cap-NN)
    ids = [i for i in ids if not re.match(r"cap-\d{2}$", i)]
    if not ids:
        continue
    new_section = section_for(ids)
    text = text.rstrip() + new_section
    md.write_text(text)
    print(f"OK ({len(ids)} QR codes): {md.name}")

print("\nFinalizado.")
