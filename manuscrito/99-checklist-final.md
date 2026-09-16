# Checklist final e pendências de publicação

**Data:** setembro de 2026
**Status:** manuscrito pronto para diagramação, faltando publicação.

## O que está pronto

- Manuscrito completo: 11 arquivos `.md` (abertura + 10 capítulos), 1 arquivo de checklist.
- Estrutura de pastas: `manuscrito/`, `figuras/`, `scripts/`, `prompts/`.
- Sumário aprovado (versão registrada no `SUMARIO.md`).
- Framework espinha dorsal declarado: Direcionamento antes da Velocidade (a Falsa Vitória da IA).
- Conta de tokens registrada (abertura) e revisada após inclusão da sessão única de geração visual.
- Tradução honesta dos capítulos técnicos para prompts copy-paste (SUMARIO.md, seção 2).
- CTA do livro definido (capítulo 10): download dos prompts + checklist final.
- Tabela de erros conhecida e integrada ao fluxo de validação (capítulo 9).

## Pendências de publicação

### Pendência 1 — Repositório público no GitHub

**Status:** pendente. Decidir com o autor:

- Nome do repositório (sugestão: `carrosseis-infinitos-ia-sem-tokens` ou `fabrica-carrosseis-ia`).
- Owner (usuário ou organização no GitHub).
- Visibilidade (público, conforme pedido do autor).
- Licença (sugestão: MIT para os prompts, CC-BY para o livro).
- Estrutura inicial da pasta `prompts/` (um arquivo `.md` por prompt, com nome alinhado com o livro: `cap-01-armadilha.md`, `cap-02-cinco-estagios.md`, etc.).

**Por que importa:** o livro aponta para `prompts/cap-NN-nome.md` em cada capítulo. Sem o repositório público, os QR codes do livro apontam para URLs quebradas.

### Pendência 2 — QR codes por capítulo

**Status:** pendente. Gerar após o repositório estar no ar.

- 11 QR codes (1 por capítulo + checklist final), um por prompt destacado no livro.
- Formato: SVG, viewBox 200×200, módulo escuro sobre fundo creme, com 16% de margem de borda (regra ISO/IEC 18004).
- Posição no miolo: rodapé da página onde o prompt aparece, com legenda curta (ex.: "Prompt 04 · teses por combinação").
- Geração: usar a ferramenta `qrencode -t SVG -l M -o cap-04.svg "https://github.com/OWNER/REPO/blob/main/prompts/cap-04-teses.md"` ou similar.
- Verificação: cada QR code testado em pelo menos 2 leitores (iPhone, Android) antes de ir para o PDF.

### Pendência 3 — Identidade visual das pranchas SVG

**Status:** pendente. Validar com o autor.

- Paleta verde EXPX (`#16A34A` texto, `#15803D` borda) + laranja Academia (`#E85D00`) para destaques secundários.
- Tipografia: Chakra Petch para títulos, JetBrains Mono para kickers e labels, Inter para corpo, com fallbacks de sistema.
- Capa escura (regra do livro) com título em verde, subtítulo em laranja.
- 10 pranchas A5 (1050×1485 viewBox) mais a capa.

### Pendência 4 — Pipeline do PDF

**Status:** pendente. Construir e testar.

- `book.css` (estilo A5 do miolo).
- `build-html.py` (monta `livro.html` a partir de `manuscrito/` e `figuras/`).
- `check-manuscrito.py` (largura de código, travessão, artefatos).
- `check-svg-geo.py` (R1/R2/R3 das pranchas).
- `print-pdf.py` (sobe servidor, mede DOM, imprime PDF).
- Regra da casa: zero travessão (U+2014) e zero meia-risca (U+2013) em todo o livro.

### Pendência 5 — Revisão humana antes da publicação

**Status:** pendente. Antes de imprimir o PDF:

- Ler o manuscrito em voz alta, em uma sessão única, para pegar frase travada.
- Conferir que os 7 erros do capítulo 9 estão eliminados nas pranchas (especialmente a paleta de pills e o posicionamento de assets).
- Conferir que os QR codes abrem a URL certa.
- Conferir que o CTA do capítulo 10 tem link real (não placeholder).

### Pendência 6 — Distribuição

**Status:** pendente. Definir antes do lançamento.

- Canal de venda (Amazon KDP, Hotmart, Eduzz, página própria).
- Preço sugerido (a definir com o autor).
- Página de venda (escrita com a skill `expx-create-sales-copy`).
- Capa para a página de venda (versão alternativa da capa do livro, em formato 1:1 e 9:16).

## Próximos passos imediatos

1. Autor responde sobre o repositório GitHub (pendência 1).
2. Após o repositório estar no ar, gerar os QR codes (pendência 2) e validar com 2 leitores.
3. Construir as 10 pranchas SVG (pendência 3) seguindo a paleta e tipografia definidas.
4. Construir o pipeline do PDF (pendência 4) e rodar os verificadores.
5. Revisão humana (pendência 5) em uma sessão de 2 horas.
6. Distribuição (pendência 6) com a skill de sales copy.

Quando todos os itens acima forem marcados, o livro vai para o ar.
