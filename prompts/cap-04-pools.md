# Prompt — Capítulo 4 (2/2) · Pools de variações

**Quando usar:** depois de validar as teses por combinação, para gerar 8 a 10 variações por slide em cada combinação.

**Onde é citado no livro:** capítulo 4, seção "Prompt 2 para colar na IA (pools de variações)".

---

## O prompt

```
Você é meu redator de copy para uma série de carrosséis.

A série tem a anatomia fixa de 8 slides:
  1. gancho (dor concreta que termina no nome do item)
  2. o_que_e (define e desarma a objeção técnica)
  3. pratica (cena de uso por modalidade)
  4. o_que_vender (bullets que viram linha de proposta)
  5. como_cobrar (monetização que fecha a conta do gancho)
  6. [NOME_PRODUTO] (preço real e link)
  7. benchmark (número real com leitura por faixa)
  8. cta (promessa do tier + chamada para ação)

Aqui está a tabela de teses por combinação:

  [COLE A TABELA DO PROMPT 1]

Para CADA combinação de eixos e para CADA slide (exceto o
slide 6, que tem preço fixo), gere um POOL de 8 a 10
variações.

Cada variação deve:
  - Caber em até [N, ex: 100] caracteres.
  - Conter 1 a 3 "trechos de destaque" (palavras ou expressões
    curtas que viram negrito no post).
  - Ser semanticamente diferente das outras variações do pool
    (não ser paráfrase).
  - No slide 1 (gancho), terminar no NOME do item (placeholder
    {{NOME}}). No slide 2 (o_que_e), abrir com "Esse é o
    {{NOME}}".
  - Usar vocabulário alinhado ao público e ao tom.

Formato de saída:

  Combinação: (VALOR_1, VALOR_A)
    Slide 1 - gancho:
      variação 1: texto | destaque: [...]
      variação 2: texto | destaque: [...]
      ... (8 a 10 variações)
    Slide 2 - o_que_e:
      ... (mesmo formato)
    ... até slide 8

  Combinação: (VALOR_1, VALOR_B)
    ...
```

## Regra de ouro

Se a IA devolver menos de 8 variações por slide, peça:
"Preciso de no mínimo 8 variações por slide. Varie os argumentos, não só as palavras. Se você sente que já repetiu, inverta a estrutura da frase."

Se a IA devolver paráfrases ("X é bom" / "X é ótimo" / "X é excelente"), peça:
"Reescreva essas variações. Cada uma precisa ter um argumento diferente. Se duas variações só trocam uma palavra, considere-as a mesma."

## O que conferir depois

- Pools têm 8 a 10 variações por slide (exceto slide 6)?
- Slide 1 (gancho) sempre termina em `{{NOME}}`?
- Slide 2 (o_que_e) sempre abre com "Esse é o `{{NOME}}`"?
- Cada variação tem 1 a 3 trechos de destaque (não a frase inteira)?
- Variações são semanticamente diferentes (não paráfrases)?

## Saída esperada

Para cada combinação de eixos, 8 listas numeradas (uma por slide, exceto slide 6), cada lista com 8 a 10 entradas no formato "texto | destaque: [...]".
