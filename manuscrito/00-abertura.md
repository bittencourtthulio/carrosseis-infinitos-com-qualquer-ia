# Abertura: como ler este livro e a conta dos tokens

**Tempo de leitura:** 8 min
**O que você sai sabendo:** quanto de token esta primeira série vai gastar de verdade, e em quantas sessões.
**Token gasto neste capítulo:** zero.

Este não é um livro sobre "como pedir um carrossel para a IA". É um livro sobre como gastar tokens uma vez e, depois disso, fazer a IA escrever um sistema que produz carrosséis para você sem chamar modelo de linguagem de novo.

A diferença parece pequena, e é a diferença entre o livro dar certo e o livro virar mais um pdf de prompt.

## Para quem é este livro

Este livro é para você que:

- posta (ou quer postar) carrosséis no Instagram, LinkedIn ou TikTok para vender produto, serviço ou ideia;
- já tentou usar IA para escrever a copy de cada peça e descobriu que o custo sobe em linha reta, a consistência cai, e cada correção obriga regerar tudo;
- não é programador, não quer instalar Python, não vai rodar terminal, e mas sabe copiar e colar texto no ChatGPT, Claude ou Gemini;
- quer entender a conta por trás do "praticamente sem gastar tokens" antes de prometer isso para si mesmo.

Se você já é dev e prefere ler código, o material original da série (técnico, em Python) está citado no capítulo 10 como referência opcional. Este livro é a tradução para leigo, e a tradução é honesta sobre o que mudou.

## Como ler

Você tem duas formas.

**Leitura corrida, do capítulo 1 ao 10.** Funciona se você nunca produziu carrossel em série e quer entender o método inteiro antes de tocar. Reserve umas duas horas e tenha o ChatGPT (ou o assistente que você usa) aberto em outra aba. Cada capítulo tem um **prompt para colar na IA** em uma caixa destacada, e o livro é mais útil se você for colando conforme lê.

**Leitura por bloco, na ordem do seu projeto.** Cada capítulo é independente o bastante para você pular para o que precisa:

| Se você está agora em... | Comece pelo capítulo... |
|---|---|
| "Quero entender se vale a pena antes de começar" | 1 |
| "Já entendi, quero montar a esteira" | 2 |
| "Já tenho a esteira, falta o catálogo" | 3 |
| "Tenho o catálogo, falta a copy" | 4 e 5 |
| "Tenho a copy, falta a imagem" | 7 |
| "Já postei, quero fazer a próxima série" | 10 |

O capítulo 9 (erros que a série cometeu) vale a leitura em qualquer momento, porque cada erro é dinheiro que a próxima série não precisa mais pagar.

## A conta dos tokens: o que "praticamente sem gastar" quer dizer

O título promete "praticamente sem gastar tokens". Isso é promessa, e promessa sem conta é marketing. Aqui vai a conta da série original, com os números contados nos arquivos:

| Etapa da primeira série | O que é | Token gasto |
|---|---|---|
| Sessão de design com IA de texto (um dia) | Você e a IA escrevem os prompts mestres, o template dos 8 slides, as regras de classificação do catálogo, a tabela de teses por eixo, e o roteiro dos assets visuais. | algumas horas de conversa |
| Sessão única de geração visual com IA de imagem (algumas horas) | Você usa Midjourney, DALL-E, Imagen ou similar para gerar os assets do template: capa, ícone do tier, moldura, detalhe de marca. Esse é o investimento pesado, e acontece uma vez. | várias gerações de imagem, conta única |
| Sessão de ajuste por amostra (meio dia) | Você gera três peças com os assets prontos, vê onde a copy falha, ajusta o prompt mestre, repete até as três passarem. | algumas horas de conversa |
| Sessão de guia (uma hora) | Você pede à IA para escrever o runbook da série: comandos, leitura do log, checklist, problemas conhecidos. | uma conversa curta |
| Produção das 418 peças | Você cola o script Python que a IA escreveu para você no Google Colab e aperta play. O script lê a planilha do Sheets, usa os assets gerados pela IA de imagem, e gera os 3.344 PNGs sozinho. | zero token de modelo |
| Captura dos 1.672 prints | Extensão do Chrome ou ferramenta gratuita baixa os prints de cada item, com cadeia de URLs alternativas. | zero token de modelo |
| Publicação agendada | Buffer, Later, ou Instagram direto. Sem chamar modelo. | zero token de modelo |
| Manutenção depois (correções, abertura da próxima série) | Uma sessão curta de IA por correção relevante, ou uma sessão para abrir série nova. Reaproveita os assets visuais da primeira série se mantiver a marca. | algumas horas por correção relevante |

Total: **três a quatro sessões de IA na primeira série**, mais sessões curtas conforme você precisa corrigir ou abrir série nova. Em troca: uma série de centenas de carrosséis, mais a próxima série, e a seguinte.

A palavra "praticamente" do título reconhece dois investimentos: a sessão de design (texto) e a sessão única de geração visual (imagem). "Sem gastar" seria mentira. "Gastando poucos" é o que a tese prova. A geração visual pesada acontece **uma vez** porque os assets viram parte do template: toda peça da série (e da próxima série, se você mantiver a marca) usa os mesmos assets. A geração em lote, depois disso, é Python rodando no Colab, e Python não cobra por peça.

## O que você precisa ter aberto antes de começar

- Conta gratuita ou paga em ChatGPT, Claude ou Gemini (qualquer uma serve; o livro mostra exemplos no ChatGPT por ser o mais popular, mas a estrutura é a mesma nos outros).
- Conta em uma IA de imagem de ponta (Midjourney, DALL-E, Imagen, Ideogram ou similar) para a sessão única de geração dos assets do template (capítulo 5).
- Uma conta Google com acesso a Sheets, Slides e Colab (todos gratuitos).
- Uma conta Canva gratuita, se você for pelo caminho alternativo de renderização sem código (capítulo 7 explica os três caminhos).
- Uma pasta no Google Drive ou no seu computador para guardar os prompts mestres que a IA vai escrever para você. Cada capítulo deste livro aponta para o prompt principal em uma caixa destacada. Copie e cole no Drive no final de cada capítulo.

Você não precisa instalar programa. Você não precisa comprar ferramenta. Você não precisa saber programar, e o Python que roda a fábrica em lote é escrito pela IA e executado no Google Colab, que funciona dentro do navegador.

## O que muda amanhã de manhã

Se você só tiver 30 minutos hoje, faça isto:

1. Abra o capítulo 1 e leia até o primeiro prompt.
2. Cole o prompt no ChatGPT, Claude ou Gemini.
3. Leia a resposta da IA. Mesmo que você não vá usar hoje, a resposta já fixa o conceito.
4. Guarde a resposta numa pasta do Drive chamada `fabrica-carrosseis`.

Amanhã, quando voltar, a pasta já tem a primeira peça do sistema. A construção começa amanhã, e o resto do livro é ampliação do que você acabou de guardar.
