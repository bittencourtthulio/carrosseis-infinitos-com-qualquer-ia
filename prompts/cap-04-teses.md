# Prompt — Capítulo 4 (1/2) · Teses por combinação

**Quando usar:** depois de definir os 2 eixos no capítulo 3, para escrever 1 tese em uma frase para cada combinação de eixos.

**Onde é citado no livro:** capítulo 4, seção "Prompt 1 para colar na IA (teses por combinação)".

---

## O prompt

```
Você é meu redator-chefe de uma série de carrosséis.

Minha série tem estes dois eixos de classificação:

  Eixo 1 (nome: [NOME, ex: TIER_DE_PRECO]): valores possíveis
  [VALOR_1, VALOR_2, VALOR_3, VALOR_4].
  Eixo 2 (nome: [NOME, ex: MODALIDADE]): valores possíveis
  [VALOR_A, VALOR_B, VALOR_C, VALOR_D, VALOR_E, VALOR_F].

O público-alvo da série é [DESCREVA, ex: donos de software
house que precisam decidir qual modelo de IA usar].
O tom de voz é [TOM, ex: direto, sem jargão, com vocabulário
de gestão de software house].
O produto/serviço que estou vendendo com a série é
[PRODUTO/SERVIÇO].

Para CADA combinação dos dois eixos, me dê UMA tese em UMA
frase. Cada tese deve:
  - prometer uma coisa concreta para o leitor (não ser genérica);
  - caber em no máximo 200 caracteres;
  - usar vocabulário alinhado ao público e ao tom;
  - ser diferente das teses das combinações vizinhas (não
    bastar trocar uma palavra).

Apresente o resultado como uma tabela:

| Combinação | Tese (1 frase, até 200 caracteres) |
| --- | --- |
| (VALOR_1, VALOR_A) | ... |
| ... | ... |
```

## Exemplo preenchido (eixo preço × eixo modalidade)

```
Eixo 1 (TIER_DE_PRECO): free, barato, medio, caro.
Eixo 2 (MODALIDADE): texto, codigo, visao, video, imagem, audio.

Público: donos de software house que precisam decidir qual
modelo de IA usar em produção.
Tom: direto, sem jargão, com vocabulário de gestão.
Produto: mentoria em grupo para líderes técnicos.

Para cada combinação, me dê uma tese em uma frase, até 200
caracteres, com argumento concreto.
```

## O que conferir depois

- As teses são realmente diferentes entre combinações vizinhas?
- A IA usou o tom e o público que você definiu?
- Alguma tese ficou genérica ("solução completa para seu negócio")? Peça para reescrever.

## Saída esperada

Tabela com 24 linhas (4 valores × 6 valores), cada uma com uma tese de até 200 caracteres. Salve no Drive como `fabrica-carrosseis/cap04-teses.md`.
