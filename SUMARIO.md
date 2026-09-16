# SUMARIO.md

**Projeto:** Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens
**Subtítulo:** Passo a passo para leigo montar uma fábrica de 100, 200, 500 carrosséis sem instalar programa e sem chamar modelo de linguagem na produção
**Marca:** Academia do Código (Metodologias de Thulio Bittencourt)
**Data:** setembro de 2026
**Status:** sumário para validação. Não escrever capítulos antes da aprovação.

---

## 1. Enquadramento interno

| Item | Definição |
|---|---|
| Marca | Academia do Código. O leitor sai sabendo o que montar. |
| Leitor | Dono de negócio, profissional liberal ou equipe de marketing que produz carrosséis para vender e gasta (ou gastaria) muito token para escrever cada peça com IA. Não é programador. Não vai instalar Python. Vai copiar e colar prompts em ChatGPT, Claude ou Gemini. |
| Área do DNA | Aquisição (principal): produção de conteúdo como motor de venda. Tecnologia e IA (secundária): uso inteligente de modelo de linguagem. |
| Framework espinha dorsal | **Direcionamento antes da Velocidade (a Falsa Vitória da IA)**. O time está na fase de descoberta da IA e usa o modelo para acelerar a produção de cada peça (velocidade sem direcionamento), quando deveria gastar tokens uma vez, com a IA, para construir o sistema que produz as peças (direcionamento antes da velocidade). |
| Tese em uma frase | Token se gasta uma vez, com a IA, para escrever o gerador. Depois, o gerador escreve as peças a custo zero, e a IA só é chamada de novo quando você precisa corrigir ou abrir uma série nova. |
| Consequência empresarial | O leitor sai com (a) uma série de centenas de carrosséis com custo marginal zero em token, (b) identidade visual estável porque mora no template, (c) revisão de copy em um só lugar (o prompt e o catálogo), (d) capacidade de abrir a próxima série em uma sessão de IA em vez de uma por peça. |
| CTA | Download do template de prompt inicial (referência no capítulo 10) + leitura do checklist final (capítulo 99). Link real a cadastrar antes da publicação; a lacuna vira pergunta, nunca invenção. |

### Por que esta tese sustenta o título

O título promete **praticamente sem gastar tokens**. Isso é uma promessa quantitativa, e o livro a argumenta em todas as páginas com a conta:

- **Sessão de design com IA de texto** (capítulos 4 e 5): uma conversa longa com ChatGPT, Claude ou Gemini para escrever os prompts mestres, o template dos 8 slides e o roteiro de geração dos assets visuais. Algumas horas, em um único dia.
- **Sessão única de geração visual com IA de imagem de ponta** (capítulo 5): uma única conversa com Midjourney, DALL-E, Imagen ou similar para produzir os assets do template do carrossel (capa, ícone do tier, moldura, detalhe de marca). Esse é o investimento pesado, e acontece uma única vez por série.
- **Sessão de ajuste por amostra** (capítulo 7): três peças geradas com os assets prontos, abre, ajusta o prompt, repete até as três passarem. Algumas horas de conversa, mais um dia.
- **Sessão de guia** (capítulo 9): a IA escreve o runbook da série para você consultar depois. Uma conversa curta.
- **Produção em lote** (capítulos 7 e 8): zero token. A IA de texto já escreveu um script Python para você. Você cola o script no Google Colab (gratuito, roda no navegador, sem instalar nada), aperta play, e o Python gera os 3.344 PNGs sozinho.
- **Manutenção** (correções, próxima série): sessão curta de IA por correção relevante, ou uma sessão para abrir série nova.

Total: **três a quatro sessões de IA na primeira série**, mais sessões curtas conforme você precisa corrigir ou abrir série nova. Em troca: uma série de centenas de carrosséis, mais a próxima série, e a seguinte.

A palavra "praticamente" do título reconhece dois investimentos: a sessão de design (texto) e a sessão de geração visual (imagem). "Sem gastar" seria mentira. "Gastando poucos" é o que a tese prova. A geração visual pesada acontece **uma vez** porque os assets viram parte do template — toda peça da série (e da próxima série, se você mantiver a marca) usa os mesmos assets.

### O leigo não programa. Mas roda o que a IA escreveu.

O leigo não escreve Python. O leigo também não instala Python, não abre terminal, não entende `pip install`. O que o leigo faz:

1. Pede para a IA de texto escrever o script Python (capítulo 7, prompt destacado).
2. Abre o Google Colab no navegador (`colab.research.google.com`, conta Google gratuita).
3. Cola o script numa célula.
4. Aperta o botão de play.

O Colab é gratuito, roda no navegador, não exige instalação. O script lê a planilha do Google Sheets, usa os assets gerados pela IA de imagem, e gera os PNGs. Quando o lote termina, o leigo baixa os arquivos. Nenhum terminal, nenhuma instalação.

Se mesmo o Colab for demais, o capítulo 7 mostra o caminho alternativo em Canva puro (mais lento, sem automação), e o caminho intermediário em Google Slides com macro do Apps Script.

---

## 2. Prova e honestidade

O livro documenta uma série real (LLMs do OpenRouter que viram receita para software house), com números contados nos arquivos gerados pelo time do autor. A tabela abaixo classifica cada afirmação factual em um dos três estados. Só o estado **executado** pode aparecer como verificado no texto.

| Recurso / afirmação | Estado | Versão / fonte |
|---|---|---|
| 437 modelos no dump da API do OpenRouter | executado (contado no JSON bruto) | snapshot de 2026 |
| 19 modelos descartados (aliases e roteadores) | executado (regra no `_gerar.py`) | snapshot de 2026 |
| 418 carrosséis gerados | executado (itens no JSON de copy) | snapshot de 2026 |
| 8 slides por carrossel | executado (anatomia fixa no código) | snapshot de 2026 |
| 3.344 PNGs finais | executado (418 × 8, contagem na pasta `saida/`) | snapshot de 2026 |
| 1.672 prints de prova | executado (4 por carrossel) | snapshot de 2026 |
| 3 MB de JSON de copy | executado (tamanho do arquivo gerado) | snapshot de 2026 |
| 0 chamadas a modelo de linguagem na produção | executado (nenhum dos três scripts importa cliente de API de LLM) | grep em `_gerar.py`, `capturar_prints.py`, `gerar_carrossel.py` |
| Formato 1080 × 1350 | executado (dimensão do PNG final) | Playwright `screenshot` |
| Algoritmo de escolha por hash determinístico | executado (lido no `_gerar.py`) | código da série |
| Tabela de eixos (tier × modalidade, 24 combinações) | executado (lido no `_gerar.py`) | código da série |
| Detecção automática de estouro via `evaluate` no Chromium | executado (lido no `gerar_carrossel.py`) | código da série |
| Loop `k` com 14 rodadas e limite 1,25 | executado (lido no `gerar_carrossel.py`) | código da série |
| Falha real: 254 de 418 slides 3 diziam "nota fiscal" | executado (declarado pelo autor da série no material-base) | capítulo do livro |
| Falha real: mancha de luz com `bottom` negativo | executado (declarado pelo autor da série no material-base) | capítulo do livro |
| Falha real: página do OpenRouter sem sufixo `:free` | executado (declarado pelo autor da série no material-base) | capítulo do livro |

**Princípio:** zero número sem fonte. Quando o número não foi conferido nesta sessão, ele não entra como verificado; entra como declarado pelo autor da série, com a fonte citada.

### Distância entre o livro técnico e o livro de leigo

A série original foi construída em Python. O leitor deste livro não escreve Python, mas roda Python que a IA escreveu para ele. A tradução é honesta:

| Capítulo | Série original (Python) | Livro de leigo (prompts + IA) |
|---|---|---|
| 3 — Fonte de dados | `openrouter-models.json` | Google Sheets com colunas |
| 4 — Eixos e teses | Funções `classify_tier` e `classify_modality` | Prompt que classifica no Sheets, com colunas novas |
| 5 — Anatomia e assets | Dicionário `BUILD` no código | Prompt-mestre dos 8 slides + sessão única com IA de imagem para gerar capa, ícone do tier, moldura |
| 6 — Captura de prints | Script com Playwright headless | Extensão do Chrome "Full Page Screen Capture" ou print manual de 4 URLs por item |
| 7 — Renderização | `gerar_carrossel.py` com Playwright | Script Python escrito pela IA, rodado no Google Colab (sem instalar nada) |
| 8 — Publicação | `publicar.py` que chama Expx Flow | Agendamento manual no Instagram ou ferramenta gratuita (Buffer, Later) |

A lógica de cinco estágios, o `stable_pick` por hash do id, o loop `k` e a checagem de estouro continuam sendo explicados. O que muda é o instrumento: em vez de o leitor digitar Python, ele copia um prompt para a IA escrever o Python para ele, cola no Google Colab (rodando no navegador) e aperta play.

---

## 3. Sistema visual

| Item | Definição |
|---|---|
| Paleta primária | Verde EXPX `#16A34A` para texto, `#15803D` para borda/seta em fundo claro (contraste 4,5:1 verificado sobre creme `#F5F1E9`). Texto do corpo `#1B1714` sobre creme, `#F1EBE1` sobre preto `#141210`. Múrceo `#6B6358` (claro) / `#A69D8F` (escuro). |
| Cor de destaque secundária | Laranja Academia `#E85D00` para texto, `#C64A00` para texto em fundos claros, para exemplos em código e em destaque de aviso. |
| Tipografia | Chakra Petch (títulos das pranchas) + JetBrains Mono (kickers, labels, números) + Inter (corpo do miolo), sempre com fallback de sistema na `font-family`. |
| Formato | A5 (1050 × 1485 viewBox nas pranchas; PDF final 420 × 595 pt). |
| Regra de capa | Capa escura, miolo branco. Exceção deliberada à regra de fundo do ecossistema: leitura impressa manda branco. Capa usa fundo escuro `#141210`, título em verde EXPX `#16A34A`, subtítulo em laranja `#E85D00`, kicker mono JetBrains Mono. |
| Exceção de marca de terceiros | Nenhuma. O objeto do livro (a série de carrosséis sobre OpenRouter) não é produto de terceiro com marca forte. OpenRouter é citado como fonte de dados pública, sem endosso. |

---

## 4. Tabela de figuras

| Arquivo | Capítulo | O que mostra |
|---|---|---|
| `00-capa.svg` | Abertura | Capa escura, título "Carrosséis Infinitos com Qualquer IA", subtítulo em destaque, kicker Academia do Código. |
| `01-jeito1-vs-jeito2.svg` | 1 | Dois caminhos lado a lado: chamada por peça (gasto em linha reta) versus construção do gerador (gasto único, depois zero). |
| `02-os-cinco-estagios.svg` | 2 | Fluxograma horizontal em U dos cinco estágios: catálogo, gerador de copy, prints, renderizador, publicador. |
| `03-catalogo-sheets.svg` | 3 | Tela de Google Sheets com colunas-exemplo do catálogo, com setas indicando quais colunas viram eixos. |
| `04-eixos-e-teses.svg` | 4 | Matriz tier × modalidade com células, uma tese por faixa de tier em destaque. |
| `05-anatomia-8-slides.svg` | 5 | Pilha de 8 cartões numerados com a função de cada slide (gancho, o_que_e, pratica, o_que_vender, como_cobrar, openrouter, prova, cta). |
| `06-pipeline-prints.svg` | 6 | Cadeia de URLs alternativas para captura de prints, com checagem HTTP. |
| `07-loop-k.svg` | 7 | Loop de ajuste do slide no Canva / Sheets, com casos de estourar e crescer. |
| `08-esteira-publicacao.svg` | 8 | Da pasta de saída ao agendamento e ao DM no Instagram. |
| `09-checklist-replicacao.svg` | 10 | Lista numerada das 10 etapas para replicar em outra série, com caixa de destaque verde para "sem gastar token aqui". |

---

## 5. Sumário capítulo a capítulo

Cada capítulo segue a mesma anatomia: **conceito** (linguagem acessível), **material necessário**, **passo a passo numerado**, **prompt para colar na IA**, **o que conferir** e **o que muda amanhã de manhã**.

| # | Título | Consequência empresarial |
|---|---|---|
| 0 | Abertura: como ler este livro e a conta dos tokens | O leitor sai sabendo quanto vai gastar de token para fazer a primeira série (a conta cabe em uma tarde). |
| 1 | A armadilha do token na peça | O leitor reconhece a falsa vitória de pedir IA para escrever cada carrossel individualmente. |
| 2 | A fábrica em cinco estágios | O leitor enxerga a esteira como cinco caixas que conversam por catálogo e template, e não como "um prompt mágico". |
| 3 | A fonte de dados: o catálogo é o motor | O leitor entende que sem catálogo com atributos que mudem a copy, não há lote, e sai com o Sheets montado. |
| 4 | Eixos, teses e pools de frases | O leitor aprende a classificar os itens em 2 a 3 eixos, escrever uma tese por combinação e gerar 8 a 10 variações por slide. |
| 5 | Anatomia dos 8 slides como contrato | O leitor entende por que fixar a anatomia evita regerar tudo quando muda uma regra. |
| 6 | Prova visual: 4 prints por carrossel | O leitor sai com a rotina de coletar prints em escala, sem confiar na memória. |
| 7 | Renderizar sem surpresas: copy vira imagem | O leitor entende como o template detecta que algo estourou e como corrigir o prompt antes de gerar o lote. |
| 8 | Publicação e DM na mesma chamada | O leitor entende como o bloco de automação fecha a esteira: a peça de topo aponta para o próximo degrau. |
| 9 | Erros que a série cometeu | O leitor sai com a lista dos sete defeitos que chegaram ao PNG e economiza o pagamento da próxima série. |
| 10 | Replicar para qualquer série + checklist | O leitor tem o roteiro de 10 passos para abrir a próxima série e o checklist que barra publicação errada. |

---

## 6. Estrutura de produção

```
carrosseis-infinitos/
├── SUMARIO.md                       (este arquivo)
├── manuscrito/
│   ├── 00-abertura.md
│   ├── 01-a-armadilha-do-token-na-peca.md
│   ├── 02-a-fabrica-em-cinco-estagios.md
│   ├── 03-a-fonte-de-dados.md
│   ├── 04-eixos-teses-e-pools.md
│   ├── 05-anatomia-dos-8-slides.md
│   ├── 06-prova-visual.md
│   ├── 07-renderizar-sem-surpresas.md
│   ├── 08-publicacao-e-dm.md
│   ├── 09-erros-que-a-serie-cometeu.md
│   ├── 10-replicar-para-qualquer-serie.md
│   └── 99-checklist-final.md
├── figuras/
│   ├── 00-capa.svg
│   ├── 01-jeito1-vs-jeito2.svg
│   ├── 02-os-cinco-estagios.svg
│   ├── 03-catalogo-sheets.svg
│   ├── 04-eixos-e-teses.svg
│   ├── 05-anatomia-8-slides.svg
│   ├── 06-pipeline-prints.svg
│   ├── 07-loop-k.svg
│   ├── 08-esteira-publicacao.svg
│   └── 09-checklist-replicacao.svg
└── scripts/
    ├── build-html.py                (gera livro.html)
    ├── book.css                     (estilo A5)
    ├── check-manuscrito.py          (largura de código, travessão, artefatos)
    ├── check-svg-geo.py             (R1/R2/R3 das pranchas)
    └── print-pdf.py                 (sobe servidor, mede DOM, imprime PDF)
```

| Métrica | Alvo | Status |
|---|---|---|
| Palavras por capítulo (isca) | 1.200 a 1.600 | a confirmar |
| Bloco de código (caixa de prompt) | máximo 60 caracteres por linha | a verificar |
| Total manuscrito | 13.000 a 17.000 palavras | a confirmar |
| Figuras | 10 pranchas A5 + capa | 10 SVGs |
| Verificadores | 0 falhas em manuscrito, R1/R2/R3 zerados | a rodar no fim |

---

## Decisões registradas (para auditoria)

1. **Framework espinha dorsal:** Direcionamento antes da Velocidade (a Falsa Vitória da IA), área `ia`. Decidido por congruência com a tese: o erro do jeito 1 é acelerar a produção peça a peça (velocidade sem direção), o acerto do jeito 2 é gastar tokens no direcionamento (construção dos prompts mestres e do catálogo) antes de acelerar a produção.
2. **Título final:** "Carrosséis Infinitos com Qualquer IA — Praticamente Sem Gastar Tokens". Subtítulo registrado no topo deste sumário.
3. **CTA:** download do template de prompt inicial + checklist final. Link real a cadastrar antes da publicação; a lacuna vira pergunta, nunca invenção.
4. **Extensão:** isca técnica com passo a passo (10 capítulos, 25 a 40 páginas).
5. **100% sem código.** Tradução honesta dos capítulos técnicos para prompts copy-paste, registrada na seção 2.
6. **Exceção de marca de terceiros:** não aplicável. O OpenRouter é citado como fonte de dados pública, não como produto endossado.
