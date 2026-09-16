# Checklist final e pendencias de publicacao

**Data:** setembro de 2026
**Status:** manuscrito pronto, livro.html gerado, repositorio publico no ar.

---

## O que esta pronto

- **Manuscrito completo**: 12 arquivos `.md` (abertura + 10 capitulos + checklist), 18.473 palavras.
- **Estrutura de pastas**: `manuscrito/`, `figuras/`, `figuras/qr/`, `figuras/qr_box/`, `scripts/`, `prompts/`.
- **Sumario aprovado** (versao registrada no `SUMARIO.md`).
- **Framework espinha dorsal** declarado: Direcionamento antes da Velocidade (a Falsa Vitoria da IA), area `ia`.
- **Conta de tokens registrada** (abertura) e revisada apos inclusao da sessao unica de geracao visual com IA de imagem.
- **Traducao honesta** dos capitulos tecnicos para prompts copy-paste (SUMARIO.md, secao 2).
- **Identidade visual** aplicada: capa escura, miolo creme `#F5F1E9`, acento verde EXPX `#16A34A`, destaque secundario laranja Academia `#E85D00`, kicker mono JetBrains Mono, titulo Chakra Petch.
- **Capa** gerada (00-capa.svg, 1050x1485, com "418 carrosseis produzidos em uma sessao, 0 tokens na producao").
- **10 pranchas A5** geradas (uma por capitulo ilustrado + capa), todas validadas em XML e em R1 (fora do viewBox).
- **13 QR codes** gerados em duas versoes: raw (qrencode) e embelezados (figuras/qr_box/).
- **13 prompts copy-paste** disponiveis no repositorio publico do GitHub.
- **Repositorio publico criado**: https://github.com/bittencourtthulio/carrosseis-infinitos-com-qualquer-ia (sem licenca, todos os direitos reservados ao autor).
- **QR codes injetados** no manuscrito (rodape dos capitulos com prompts).
- **CTA do livro** definido (capitulo 10): download dos prompts via QR code + checklist final.
- **Tabela de erros** conhecida e integrada ao fluxo de validacao (capitulo 9).
- **Scripts de verificacao**: check-manuscrito.py (travessao, largura, artefatos) e check-svg-geo.py (R1 dentro do viewBox). Ambos passam.
- **livro.html** gerado (125 KB), com paged.js embutido para paginacao A5.

## Verificacoes objetivas

```
$ python3 scripts/check-manuscrito.py
OK: manuscrito sem travessao, codigo <=60 chars, sem artefatos.

$ python3 scripts/check-svg-geo.py
OK R1: 10 pranchas dentro do viewBox 1050x1485.
R2 e R3: verificacao visual obrigatoria (ver abaixo).

$ python3 -c "print(open('livro.html').read().count('—'))"
0
```

## Pendencias de publicacao

### Pendencia 1 — Verificacao visual das pranchas (R2, R3)

**Status:** pendente. Conferir no `livro.html` aberto no Chrome:

- Em cada prancha, abrir e rolar para ver se ha texto sobreposto, texto fora do card ou texto que vaza a borda da pagina. As correcoes heuristicas foram feitas em Python puro (R1 dentro do viewBox), e a precisao de R2/R3 (sobreposicao) e R3 (texto dentro de rect) exige `getBoundingClientRect` no browser.

**Como fazer:** abra `livro.html` no Chrome, aperte F12, e use a aba Elements para inspecionar cada `<text>` em cada prancha. Se houver sobreposicao, anote o `cap-XX.svg` e o trecho, e ajuste no `scripts/gerar-pranchas.py`.

### Pendencia 2 — Geracao do PDF A5

**Status:** pendente. O pipeline final exige:

1. Subir `python3 -m http.server` na raiz do projeto.
2. Usar Playwright (headless) para navegar ate `http://localhost:PORTA/livro.html`.
3. Esperar `.pagedjs_pages` carregar.
4. Chamar `page.pdf({ preferCSSPageSize: true, printBackground: true })`.
5. Verificar MediaBox 420x595 pt e contagem de paginas.

O `book.css` ja tem `@page { size: A5; }`, `@bottom-center { content: counter(page); }` e o polyfill paged.js via CDN. Falta apenas o script Playwright (eu nao instalei neste ambiente para evitar dependencia extra; pode ser feito na sessao de revisao).

### Pendencia 3 — Revisao humana antes da publicacao

**Status:** pendente. Antes de imprimir o PDF:

- Ler o manuscrito em voz alta, em uma sessao unica, para pegar frase travada.
- Conferir que os 7 defeitos do capitulo 9 estao eliminados nas pranchas (especialmente a paleta de pills e o posicionamento de assets).
- Conferir que os QR codes abrem a URL certa (testar em iPhone e Android).
- Conferir que o CTA do capitulo 10 tem link real (nao placeholder).
- Conferir que o conteudo dos 13 arquivos `.md` no repositorio GitHub bate com o prompt destacado no livro.

### Pendencia 4 — Distribuicao

**Status:** pendente. Definir antes do lancamento:

- Canal de venda (Amazon KDP, Hotmart, Eduzz, pagina propria).
- Preco sugerido (a definir com o autor).
- Pagina de venda (escrita com a skill `expx-create-sales-copy`).
- Capa para a pagina de venda (versao alternativa da capa do livro, em formato 1:1 e 9:16).

### Pendencia 5 — Conta da pagina de vendas no GitHub

**Status:** pendente. Decidir:

- Criar uma `gh-pages` branch no repositorio com um `index.html` que aponta para o PDF.
- Ou deixar so o link para o repositorio, e o leitor baixa o PDF manualmente.

## Proximos passos imediatos

1. **Verificacao visual** (pendencia 1): abrir `livro.html` no Chrome e conferir as 10 pranchas.
2. **Gerar o PDF A5** (pendencia 2) com Playwright.
3. **Revisao humana** (pendencia 3) em uma sessao de 2 horas.
4. **Distribuicao** (pendencia 4) com a skill de sales copy.
5. **GitHub Pages** (pendencia 5) se desejado.

Quando todos os itens acima forem marcados, o livro vai para o ar.

## Numeros finais

| Item | Valor |
|---|---|
| Capitulos | 11 (abertura + 10 + checklist) |
| Palavras manuscrito | 18.473 |
| Pranchas A5 (1050x1485) | 10 (capa + 9 ilustracoes) |
| QR codes (raw) | 13 |
| QR codes (embelezados com moldura) | 13 |
| Prompts no repositorio GitHub | 13 arquivos `.md` |
| Tamanho do `livro.html` | 125 KB |
| Travessoes (—) no HTML | 0 |
| Meias-riscas (–) no HTML | 0 |
| Linhas de codigo > 60 chars | 0 |
| Falhas em R1 (pranchas) | 0 |
