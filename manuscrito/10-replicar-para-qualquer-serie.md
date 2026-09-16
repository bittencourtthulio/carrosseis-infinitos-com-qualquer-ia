# Capítulo 10: Replicar para qualquer série + checklist final

**Tempo de leitura:** 16 min
**O que você sai sabendo:** os 10 passos para abrir a próxima série de carrosséis em cima da fábrica que você acabou de montar, e o checklist que barra publicação errada.
**Token gasto neste capítulo:** zero na leitura; uma sessão curta de IA quando você aplicar o playbook à próxima série.

## Conceito

O que você montou nos capítulos 1 a 9 não é uma série de carrosséis. É uma **fábrica** de séries de carrosséis. Trocar a fonte de dados e os pools produz a próxima série com o mesmo renderizador, o mesmo publicador e o mesmo checklist. O ativo que você leva adiante não são os 418 posts: é o gerador.

Este capítulo fecha o livro com duas peças:

1. **O playbook de 10 passos** para abrir a próxima série. Sequência numerada, em ordem de execução.
2. **O checklist de publicação** que barra post com defeito. Lista de verificação que você roda antes de cada post agendado.

## O playbook de 10 passos

### 1. Escolha a fonte

Um catálogo com atributos que mudem a copy. Para a série OpenRouter, foi o dump da API de modelos. Para a sua próxima série, pode ser:

- **Repositórios do GitHub** com colunas de estrelas, linguagem, licença, último commit, número de contribuidores.
- **Ferramentas de um marketplace** com preço, categoria, número de usuários, link da demo.
- **Funcionalidades de um produto** com módulo, persona-alvo, complexidade de implantação, retorno esperado.
- **Cases de cliente** com porte, segmento, problema, solução, métrica de resultado.
- **Cidades, regiões, eventos, livros, perfumes**, e qualquer coisa que vire linha de catálogo com atributos comparáveis.

Regra: o catálogo precisa ter pelo menos 30 linhas e pelo menos 4 colunas com valores comparáveis.

### 2. Defina os eixos

Dois eixos com 3 a 6 valores cada. Cada combinação recebe uma tese em uma frase. Escreva as teses antes dos pools.

A pergunta que decide o eixo 1: "se dois itens diferem apenas neste atributo, a copy deles tem que ser diferente?" Se sim, é eixo 1.

A pergunta que decide o eixo 2: "qual é o atributo que mais varia entre os itens do meu catálogo?" Geralmente é eixo 2.

### 3. Desenhe o contrato

Campos do item, anatomia dos 8 slides com função nomeada (capítulo 5), lista `negrito`, campo `print` descritivo, campo `template` alternando claro/escuro, bloco `automation` (capítulo 8).

O contrato é a planilha `02-copy` da nova série. As colunas são as mesmas; o que muda é o conteúdo.

### 4. Peça o gerador de copy (sessão de design com IA de texto)

Use o prompt do capítulo 4 (teses + pools) com o tema da nova série. A IA vai gerar:

- A tabela de teses por combinação (uma frase por combinação).
- Os pools de 8 a 10 variações por slide em cada combinação.
- A regra de `stable_pick` por hash do id (a IA inclui na explicação, mesmo que a implementação esteja no script Python do passo 5).
- A regra de conexão entre o gancho (slide 1, termina em `{{NOME}}`) e o slide 2 (abre com "Esse é o `{{NOME}}`").

Valide 5 combinações antes de aprovar todas. Se 5 passam, as outras 19 costumam passar.

### 5. Peça o renderizador (sessão de design com IA de texto)

Use o prompt do capítulo 7 (renderizador) com os campos específicos da nova série (URL da nova planilha, lista de novos assets). A IA vai gerar:

- O script Python que lê a nova planilha via gspread.
- O template HTML/CSS com os 8 slides, com tema claro/escuro, com a cor de destaque ajustada por contraste.
- O loop `k` com ambos os caminhos (encolher e crescer).
- A checagem de fonte carregada antes de gerar.
- O log com `k` por slide.

### 6. Gere os assets visuais (sessão única com IA de imagem)

Use o prompt do capítulo 5 (briefings para IA de imagem). Gere a capa nova da série, mantenha os ícones de tier se a paleta da marca for a mesma, gere moldura nova se o estilo visual mudou.

Lembre: a sessão de imagem é **única por série**. A próxima série reaproveita o que puder.

### 7. Gere 3 amostras e revise

Pegue 3 itens do novo catálogo: um claro, um escuro, um com provider de cor difícil. Gere os 24 PNGs. Passe os olhos pelos 7 defeitos do capítulo 9. Ajuste o que precisar. Repita até os 3 passarem sem erro.

### 8. Capture os prints

Use o prompt do capítulo 6 com a nova cadeia de URLs (que muda conforme o domínio). Rode o script no Colab. Confira que cada print bate com o slide em que vai aparecer.

### 9. Gere o lote

Rode o script de renderização sem o filtro de itens. Filtre o log por `k < 0.85` ou por aviso de 14 rodadas. Revise só esses.

### 10. Publique pelo JSON (ou planilha)

Use o publicador do capítulo 8, lendo o bloco `automation` da nova planilha. Agende a série. Monitore as primeiras peças em volume baixo para confirmar que a automação de DM está disparando certo. Suba o volume.

## O checklist de publicação

Antes de postar cada peça (ou antes de liberar o lote inteiro), passe por este checklist. Uma resposta "não" barra a publicação.

**Copy**

- [ ] O gancho (slide 1) termina no nome do item (`{{NOME}}`)?
- [ ] O slide 2 abre com "Esse é o `{{NOME}}`"?
- [ ] Os pools têm 8 a 10 variações por slide, e a variação escolhida para este item é semanticamente diferente das outras?
- [ ] Nenhuma variação contém travessão ou meia-risca?
- [ ] Nenhuma variação promete resultado sem fonte ("você vai vender 10x mais")?
- [ ] Todos os números citados têm fonte (preço por milhão, contexto, benchmark)?

**Visual**

- [ ] O print do slide 2 (o_que_e) bate com o que o slide diz?
- [ ] O print do slide 3 (pratica) bate com a cena da copy?
- [ ] O print do slide 6 (preço) bate com o tier do item (free mostra `:free`, caro mostra preço cheio)?
- [ ] O print do slide 7 (benchmark) tem o número legível e a fonte está visível?
- [ ] A cor de destaque do item tem contraste mínimo de 3:1 com o fundo (não some no tema escuro)?
- [ ] O pill do CTA (slide 8) tem texto legível (acento puro, não variação escurecida)?
- [ ] Nenhum asset está posicionado com `bottom` negativo fora do container?
- [ ] A fonte do template carregou (não saiu com fallback)?

**Automação**

- [ ] O bloco `automation` está preenchido (keywords, mensagem, link, public reply)?
- [ ] A palavra-chave tem 1 a 2 palavras, alinhada com o conteúdo do slide 8?
- [ ] A mensagem do DM tem `{{nome}}` e `{{link}}`?
- [ ] O link do material está vivo (HEAD 200)?

**Log**

- [ ] O slide não está marcado como "estourou 14 rodadas"?
- [ ] O `k` final está acima de 0.85?
- [ ] Não há aviso de "fonte não carregou" no log?

Se algum item falhar, corrija antes de postar. Se tudo passar, agende.

## Material necessário

- Conta gratuita ou paga em ChatGPT, Claude ou Gemini.
- A fábrica montada nos capítulos 1 a 9 (catálogo, copy, prints, renderizador, publicador).
- O catálogo da próxima série.

## Passo a passo (aplicar o playbook à próxima série)

1. Defina a próxima série em uma frase: "Vou produzir [N] carrosséis sobre [TEMA] para [PÚBLICO] vender [PRODUTO]."
2. Abra o ChatGPT.
3. Cole o prompt abaixo. Não responda por você mesmo: responda com dados reais da próxima série.
4. A IA vai devolver um relatório de prontidão com as 10 perguntas respondidas (ou com pedido de informação onde faltar).
5. Para cada pergunta que você não consegue responder, volte ao passo correspondente do playbook e preencha.
6. Repita até a IA devolver "pronto para gerar o lote".
7. Siga os passos 6 a 10 do playbook.

## Prompt para colar na IA

```
Você é meu auditor de prontidão de série.

Estou planejando minha próxima série de carrosséis. Antes de
rodar o playbook, quero saber se estou pronto.

Minha próxima série:
  - Tema: [TEMA]
  - Público: [PÚBLICO]
  - Produto que estou vendendo: [PRODUTO]
  - Volume estimado: [N, ex: 100] carrosséis
  - Volume de posts por semana: [N, ex: 5]

Aqui está o que já tenho:
  - Catálogo: [SIM/NÃO] (se sim, [N] linhas, com as colunas
    [LISTA])
  - Eixos definidos: [SIM/NÃO] (se sim, [EIXO 1] com [LISTA]
    e [EIXO 2] com [LISTA])
  - Tabela de teses: [SIM/NÃO] (se sim, quantas combinações)
  - Pools de variações: [SIM/NÃO] (se sim, quantas variações
    por slide na média)
  - Anatomia dos 8 slides: [SIM/NÃO]
  - Assets visuais: [SIM/NÃO] (capa nova, ícones de tier,
    moldura)
  - Prints capturados: [SIM/NÃO]
  - Renderizador testado em 3 amostras: [SIM/NÃO]
  - Automação de DM configurada: [SIM/NÃO]

Me faça 10 perguntas para eu saber se estou pronto
    para rodar
o playbook. Não responda por mim. Apenas pergunte.

Depois que eu responder, me dê um relatório de prontidão
com: (a) o que está pronto, (b) o que está faltando, (c)
qual o próximo passo imediato.
```

## O que muda amanhã de manhã

Você vai abrir o Google Drive e criar a pasta `fabrica-carrosseis/serie-02-[tema]`. Vai copiar a estrutura de pastas da série 01 (catálogo, copy, prints, pngs, publicados) para a nova pasta. Vai manter os assets visuais que servem para a nova série (ícones de tier, detalhe de marca) e gerar capa nova. Vai abrir a planilha `02-copy` da série 01 como template, duplicar para a série 02, e apagar os dados. Vai estar pronto para a próxima sessão de design com a IA. Em uma tarde, a série 02 está em pé. Em uma semana, está no ar.

## O CTA do livro

Você chegou no fim. O que você tem agora é uma fábrica, não uma série. A fábrica roda com três ingredientes:

1. Um catálogo com atributos que mudem a copy.
2. Sessões curtas de IA (texto e imagem) para manter o sistema.
3. O playbook dos 10 passos acima.

O CTA deste livro é duplo:

- **Pegue os prompts.** Todos os prompts destacados neste livro estão no repositório público, em arquivos `.md` individuais, um por capítulo. Cada capítulo aponta o nome do arquivo (ex.: `prompts/cap-04-teses.md`). Copie, adapte, use.
- **Rode o checklist.** Antes de postar a próxima peça, passe o checklist. Uma resposta "não" barra. Em uma série bem desenhada, o checklist passa em segundos. Em uma série mal desenhada, ele pega o defeito antes do leitor.

Obrigado por ler até aqui. Agora vá construir.

## QR codes dos prompts deste capitulo

Aponte a camera do celular para cada QR code ou clique no link para abrir o arquivo `.md` completo no GitHub. O arquivo contem o prompt destacado, variacoes para Claude e Gemini, exemplos preenchidos e o checklist de validacao.

### Prompt 04 (1/2) - Teses por combinacao

![QR code do Prompt 04 (1/2) - Teses por combinacao](../figuras/qr_box/cap-04-teses.svg)

[Abrir no GitHub](https://github.com/bittencourtthulio/carrosseis-infinitos-com-qualquer-ia/blob/main/prompts/cap-04-teses.md)  
Arquivo: `prompts/cap-04-teses.md` no repositorio publico.

