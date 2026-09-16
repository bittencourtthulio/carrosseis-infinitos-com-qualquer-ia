# Capítulo 1 — A armadilha do token na peça

**Tempo de leitura:** 12 min
**O que você sai sabendo:** por que pedir IA para escrever cada carrossel é mais caro (em token, em consistência e em revisão) do que gastar tokens uma vez para escrever o sistema que escreve os carrosséis.
**Token gasto neste capítulo:** zero.

## Conceito

Existem dois jeitos de usar IA para produzir uma série de carrosséis.

**Jeito 1 — o modelo escreve cada peça.** Para cada item da série, você abre o ChatGPT, cola um prompt, recebe a copy, revisa, ajusta o prompt, gera de novo, copia para o Canva, ajusta o template, exporta o PNG, posta. Funciona bem para dez peças. Para quatrocentas, o custo em token cresce em linha reta, a consistência cai (o slide 1 fica num tom, o slide 80 fica em outro), e cada correção de copy obriga regerar tudo.

**Jeito 2 — o modelo escreve o sistema que escreve as peças.** Você gasta tokens uma vez, numa sessão longa de design com a IA, para construir o catálogo classificado, os prompts mestres por slide, o template visual e o script de geração em lote. Depois disso, gerar 418 carrosséis ou 4.180 custa o mesmo: zero em token de modelo, alguns minutos de CPU rodando o script que a IA escreveu.

Este livro é sobre o jeito 2. A diferença não é técnica, é econômica: no jeito 1 você paga por peça, no jeito 2 você paga pela fábrica uma vez e usa a fábrica de graça para sempre.

## Por que o jeito 1 parece certo no começo (e quebra no fim)

Quando você tem três peças para fazer, o jeito 1 é mais rápido. Você abre o ChatGPT, descreve a peça, ajusta, copia para o Canva, exporta. Em quinze minutos está pronto. Para três peças, gastar três vezes o tempo de prompt parece natural.

O que acontece quando você chega em vinte peças:

- A copy começa a divergir. Sem um prompt-mestre fixado, o modelo escreve a peça 17 com um tom, a peça 18 com outro, e o feed perde a cara da marca.
- As correções viram refação. Você percebe que o gancho do slide 1 está fraco. Volta nas 17 peças anteriores, regrava o gancho, perde meio dia.
- O token consumido não para de subir. Em ChatGPT Plus você tem um teto mensal; em API, a fatura cresce mês a mês.
- A revisão final vira um inferno. Antes de postar cada peça, você revê se a copy bate com o template, se a fonte carregou, se a cor de destaque está certa, se o CTA é o mesmo.

Quando você chega em cem peças, o jeito 1 já quebrou. Quando chega em quatrocentas, o jeito 1 não é uma decisão — é um pedido de desculpas para si mesmo.

## Por que o jeito 2 também parece caro (até você fazer a conta)

O jeito 2 tem um custo inicial alto: a sessão de design. Você vai gastar algumas horas em uma conversa longa com a IA para escrever os prompts mestres, o template visual, o catálogo classificado e o script de geração. É a parte chata do trabalho, e a tentação de pular para "gerar logo uma peça" é real.

A conta que mata essa tentação:

| Volume da série | Jeito 1 (token por peça) | Jeito 2 (token uma vez + script) |
|---|---|---|
| 10 peças | 10 prompts × 1.500 tokens = 15.000 tokens | 1 sessão de 20.000 tokens + script + 0 na produção |
| 50 peças | 75.000 tokens | 20.000 tokens + script + 0 na produção |
| 100 peças | 150.000 tokens | 20.000 tokens + script + 0 na produção |
| 500 peças | 750.000 tokens | 20.000 tokens + script + 0 na produção |

A conta ignora correções (no jeito 1, cada correção é uma regeração; no jeito 2, a correção é uma edição de uma linha no prompt-mestre que vale para a série inteira). Incluindo correções, a vantagem do jeito 2 só cresce.

A palavra "praticamente" do título reconhece a sessão de design. "Sem gastar" seria mentira. "Gastando poucos" é o que a tabela prova a partir de cinquenta peças.

## O que muda no jeito 2

Três coisas concretas, em ordem de impacto.

**1. A copy fica revisável em código, não em texto livre.** No jeito 2, cada peça da série é gerada por um prompt-mestre que mora em um arquivo (ou em uma planilha, no caminho sem código deste livro). Quando você percebe que o gancho do slide 1 precisa ser mais forte, você muda uma linha do prompt-mestre, regenera a série, e as quatrocentas peças saem com o gancho novo. No jeito 1, a mudança é refação manual.

**2. A identidade visual para de derivar.** No jeito 2, o template visual é gerado uma única vez pela IA de imagem (capítulo 5) e vive em uma pasta de assets. Toda peça da série usa os mesmos assets. No jeito 1, cada peça é montada no Canva na mão, e o "azul" da marca vira sete tons diferentes ao longo do feed.

**3. A geração vira determinística.** No jeito 2, cada item do catálogo recebe sempre a mesma copy (a escolha é por hash do id do item, igual a uma chave de gaveta: o mesmo item sempre abre a mesma gaveta). No jeito 1, o modelo pode (e costuma) gerar copy diferente a cada regeneração, o que torna a revisão impossível.

## Material necessário

- Conta gratuita ou paga em ChatGPT, Claude ou Gemini.
- Bloco de notas ou Google Docs para guardar a resposta da IA.

## Passo a passo

1. Abra o ChatGPT (ou o assistente que você usa).
2. Cole o prompt abaixo na conversa.
3. Leia a resposta. Mesmo que você não vá aplicar hoje, a analogia fixa o conceito.
4. Copie a resposta para uma pasta no Drive chamada `fabrica-carrosseis/cap01`.
5. Em uma frase, escreva no mesmo Docs: "Minha série atual, se eu for pelo jeito 1, vai me custar X tokens. Se eu for pelo jeito 2, vai me custar a sessão de design mais zero na produção. A partir de N peças, o jeito 2 ganha."

## Prompt para colar na IA

```
Você é meu consultor de IA aplicada a marketing de conteúdo.
Eu uso (ou estou prestes a usar) IA para escrever cada carrossel
individualmente, peça por peça.

Me explique, com UMA analogia de leigo, por que pedir para a IA
escrever cada carrossel individualmente é mais caro em token,
mais lento em revisão e menos consistente em marca do que gastar
uma sessão maior de tokens para construir o sistema que escreve
os carrosséis.

Use linguagem de quem nunca programou. Máximo de 1 página.
Termine com 3 perguntas para eu identificar se estou cometendo
esse erro na minha série atual:

  1. Estou reescrevendo o prompt a cada peça, ou tenho um
     prompt-mestre?
  2. Quando preciso corrigir uma regra de copy, eu regenero a
     peça errada ou corrijo o prompt e regenero o lote?
  3. O token que eu já gastei até hoje seria suficiente para
     ter construído o sistema completo?
```

(O prompt completo, com instruções de uso e variações para Claude e Gemini, está em `prompts/cap-01-armadilha.md` no repositório público.)

## O que conferir

- A IA respondeu em linguagem acessível (sem jargão técnico)? Se respondeu com termos como "fine-tuning" ou "embeddings", peça para simplificar: "Explique como se eu tivesse 16 anos e nunca tivesse usado IA."
- A analogia fez sentido para você? Se não fez, peça outra analogia no mesmo chat: "Me dê uma analogia diferente, ainda mais simples."
- As três perguntas finais caem na sua realidade? Se caem, você está no jeito 1 e este livro é para você.

## O que muda amanhã de manhã

Antes de dormir hoje, você vai decidir uma coisa: a sua série atual (a que você já começou ou está prestes a começar) vai pelo jeito 1 ou vai pelo jeito 2. A decisão cabe em uma frase e cabe em um papel colado no monitor. Se for jeito 2, você segue para o capítulo 2 amanhã. Se for jeito 1, você segue do mesmo jeito, mas agora sabe o preço que vai pagar.
