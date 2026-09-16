# Prompt — Capítulo 5 (1/2) · Anatomia dos 8 slides

**Quando usar:** depois de validar as teses e pools, para fixar a anatomia dos 8 slides (a função de cada um, o que carrega, o tom e o exemplo de copy).

**Onde é citado no livro:** capítulo 5, seção "Prompt para colar na IA (anatomia dos 8 slides)".

---

## O prompt

```
Você é meu diretor de arte de uma série de carrosséis.

Minha série tem a tese [TESE GERAL, ex: "Cada LLM é uma
ferramenta de receita diferente para software house"] e o
público-alvo [PÚBLICO, ex: donos de software house].

Os 2 eixos de classificação dos itens são:
  Eixo 1: [NOME] (valores: [LISTA])
  Eixo 2: [NOME] (valores: [LISTA])

Aqui está a tabela de teses por combinação:
  [COLE A TABELA DO PROMPT 1 DO CAPÍTULO 4]

Me dê a anatomia fixa dos 8 slides para esta série:

  Slide 1 - gancho:
    Função: ...
    O que carrega: ...
    Tom: ...
    Layout visual sugerido: ...
    Exemplo de copy real para o item "[ITEM EXEMPLO]" na
    combinação (VALOR_1, VALOR_A):
      "..."
      Destaques: [...]

  Slide 2 - o_que_e:
    ... (mesmo formato)

  ... (até slide 8 - cta)

Para cada slide, justifique em 1 frase por que essa função
existe na anatomia. Se algum slide parece redundante com
outro, aponte e sugira a fusão.

Termine com:
  - Lista dos assets visuais que precisam ser gerados para
    esta série (capa, ícones, molduras etc.).
  - Briefing de 1 parágrafo para cada asset, pronto para eu
    colar na IA de imagem.
```

## O que conferir depois

- Os 8 slides cobrem gancho, definição, prática, venda, monetização, link, prova e CTA?
- O exemplo de copy de cada slide cita o item de exemplo e bate com a tese da combinação?
- Algum slide parece redundante com outro? Peça fusão.
- A lista de assets visuais tem capa, ícones, moldura e detalhe de marca?

## Saída esperada

A IA devolve a anatomia detalhada dos 8 slides (função, conteúdo, tom, layout, exemplo de copy) e a lista de assets visuais com briefing para cada um. Salve como `fabrica-carrosseis/cap05-anatomia.md`.
