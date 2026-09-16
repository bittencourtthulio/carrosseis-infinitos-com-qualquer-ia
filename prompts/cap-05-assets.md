# Prompt — Capítulo 5 (2/2) · Briefing para IA de imagem (assets do template)

**Quando usar:** depois de validar a anatomia do capítulo 5, para gerar os assets visuais do template (capa, ícones de tier, moldura, detalhe de marca). É a sessão ÚNICA de geração visual pesada da série.

**Onde é citado no livro:** capítulo 5, seção "Prompt para colar na IA de imagem (capa da série)".

---

## Por que esta sessão é única

Os assets gerados aqui viram o rosto da série inteira. A capa aparece 1 vez, mas os ícones de tier aparecem em 418 slides (1 vez por peça). A moldura aparece em 4 slides por peça, em todas as peças. Por isso a qualidade precisa ser alta: você vai conviver com estes assets por semanas.

Esta é a única vez que você gasta tokens de imagem em volume. A geração em lote (capítulo 7) usa Python puro, sem chamar modelo de imagem. A próxima série, se mantiver a paleta da marca, reaproveita os mesmos assets.

---

## Prompt 1 — Capa da série

Cole o briefing que o prompt anterior gerou para a capa, e acrescente no final:

```
[COLE O BRIEFING QUE O PROMPT ANTERIOR GEROU PARA A CAPA]

Acrescente no final do meu prompt:
  - Formato 1080x1350 (proporção 4:5 do Instagram).
  - Estilo visual: [ESTILO, ex: minimalista, com tipografia
    geométrica, paleta verde EXPX #16A34A + creme #F5F1E9].
  - Sem texto corrido na imagem (o texto vai ser inserido
    depois pelo template).
  - Sem fotos de pessoas, sem logotipos de empresas reais,
    sem cara de banco de imagem.
  - Resultado final: alto contraste, legível em miniatura no
    feed, com espaço livre no centro para o título ser
    sobreposto.
```

## Prompt 2 — Ícone do tier

```
Ícone pequeno, [NOME DO TIER, ex: "free"], 256x256, fundo
transparente, alto contraste. Representar o conceito de
[CONCEITO, ex: "zero custo / margem integral"]. Estilo
[ESTILO, ex: geométrico minimalista]. Pode ser um glifo, um
símbolo ou uma forma abstrata. Sem texto, sem foto, sem
rebuscamento. Resultado: PNG com fundo transparente, pronto
para sobrepor no template.
```

Gere 4 ícones (um por valor do eixo preço: free, barato, médio, caro).

## Prompt 3 — Moldura do print

```
Moldura para captura de tela, 1:1 ou 4:5, transparente nas
bordas. Estilo [ESTILO]. Apenas os elementos visuais que
fazem parecer "isto é um print de tela": um traço, um canto
dobrado, uma sombra suave. Sem texto, sem cor de marca
(produtora), sem preenchimento no centro (o print vem
depois). Resultado: PNG com fundo transparente, pronto para
ficar atrás do print real.
```

## Prompt 4 — Detalhe de marca (opcional)

```
[LOGO ou SÍMBOLO] em [ESTILO, ex: traço fino monocromático],
256x64, fundo transparente, [COR]. Pode ser o logo da marca
ou um símbolo simples. Resultado: PNG com fundo transparente,
pronto para ir no rodapé dos slides.
```

---

## Como escolher entre as IAs de imagem

| IA | Quando usar |
|---|---|
| Midjourney | Padrão-ouro de qualidade visual. Vale a assinatura mensal para a sessão de assets. |
| DALL-E 3 (OpenAI) | Se você já tem assinatura ChatGPT Plus. Mais rápido, qualidade boa, menor controle. |
| Imagen 3 (Google) | Se você já tem Google One AI Premium. Excelente para textos curtos na imagem (não usar aqui, é template sem texto). |
| Ideogram | Boa opção gratuita com qualidade decente. Use se orçamento for zero. |
| Leonardo AI | Boa opção gratuita com qualidade decente e mais controle de estilo. |

Recomendo Midjourney ou DALL-E para esta sessão. A diferença entre gratuita e paga aparece na capa do feed, onde o leitor decide em 200 milissegundos se vai parar ou continuar rolando.

---

## O que conferir depois

- A capa ficou legível em miniatura (200x300 pixels)? Abra o feed e veja.
- Os ícones de tier têm fundo transparente? Se vierem com fundo branco quadrado, remova no Photopea.
- Os 4 ícones têm o mesmo estilo visual entre si? Se o "free" parece desenhado por uma pessoa e o "caro" por outra, peça para refazer.
- A moldura é só moldura (sem conteúdo no centro)?
- O detalhe de marca está em PNG transparente, na resolução correta?

## Saída esperada

7 arquivos PNG (1 capa, 4 ícones, 1 moldura, 1 detalhe de marca) na pasta `04-pngs/assets/`, com nomes claros.
