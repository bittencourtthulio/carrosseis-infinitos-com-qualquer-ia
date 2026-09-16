# Prompt — Capítulo 9 · Validação contra os 7 defeitos conhecidos

**Quando usar:** depois de gerar os 3 itens-piloto do capítulo 7, para conferir que nenhum dos 7 defeitos conhecidos aparece antes de gerar o lote.

**Onde é citado no livro:** capítulo 9, seção "Prompt para colar na IA".

---

## O prompt

```
Você é meu engenheiro de qualidade de carrosséis.

Gerei 3 itens-piloto da minha série (24 PNGs no total). Ao
conferir os PNGs contra os 7 defeitos conhecidos da série
"Carrosséis Infinitos com Qualquer IA", encontrei:

  Erro [N] - [nome do erro]: aparece no slide [N] do item
  [N], no formato [descrição breve].
  Erro [N] - [nome do erro]: ...
  (copiar e colar aqui o que você anotou)

Os 7 defeitos conhecidos são:
  1. Repetição de cena no slide 3 (pool < 8)
  2. Asset posicionado com bottom negativo
  3. Print de preço não bate com o tier
  4. Card promocional fora de pico
  5. Formatação de número binário errado
  6. Catálogo de prints desatualizado
  7. Pill de CTA ilegível no tema escuro

Para cada defeito encontrado:
  - Identifique a causa raiz (qual parte do template, do
    prompt-mestre ou do script).
  - Reescreva APENAS a parte com defeito (não o template
    inteiro, não o prompt inteiro). Mudança mínima, máxima
    eficácia.
  - Me dê o trecho de código ou prompt antes/depois.

Termine com a lista de mudanças que você fez e por que
essas mudanças eliminam a CLASSE de erro (não só o item
específico).
```

## Os 7 defeitos conhecidos (resumo)

| # | Defeito | Causa raiz | Correção |
|---|---|---|---|
| 1 | Slide 3 repete cena (ex.: "foto da nota fiscal") | Pool < 8 variações por modalidade | Mínimo 8 variações no prompt do cap 4 |
| 2 | Slide estoura 100px sem ajustar | Asset posicionado com `bottom: -50px` | Posicionar com `top`, usar `overflow: hidden` |
| 3 | Print do slide 6 mostra preço pago | Cadeia de URL não usa `:free` para tier free | Validar conteúdo (não só status 200) no script de captura |
| 4 | Card promocional fora de pico | Captura de card isolado em vez de tabela | Empilhar cabeçalho com tabela de preços |
| 5 | "1049k tokens" (deveria ser "1M") | Divisão por 1000 em vez de 1048576 | Formatar múltiplos de 2^20 |
| 6 | Catálogo diz que tem print, pasta não tem | Catálogo não foi regenerado após captura | Regenerar catálogo no fim da captura |
| 7 | CTA ilegível no tema escuro | Texto do pill usa variação escurecida | Usar acento puro no CSS |

## Como aplicar este prompt

1. Abra os 24 PNGs (3 itens × 8 slides) no visualizador.
2. Para cada slide, passe pela tabela acima. Anote os defeitos em uma frase por linha.
3. Cole a lista de defeitos encontrados no prompt.
4. A IA ajusta o template / prompt-mestre / script.
5. Regere os 3 itens-piloto.
6. Repita até nenhum defeito aparecer.
7. Quando os 7 defeitos não aparecerem nos 3 itens-piloto, gere o lote.

## Variação: validar a série inteira, não só os 3 itens-piloto

Se você já gerou o lote e quer validar todos os 418 itens:

```
Adicione ao prompt:
"Em vez de validar 3 itens, valide os [N] itens da série
(que estão na pasta 04-pngs/). Para cada defeito encontrado
em qualquer item, me dê a lista de itens afetados, a
correção, e o item-piloto a ser regenerado.
```

Atenção: esse modo demora mais (a IA precisa ler o PNG de cada item), mas pega defeitos que aparecem só em combinações específicas.

## O que conferir depois

- A IA identificou a causa raiz de cada defeito?
- A IA reescreveu apenas a parte com defeito (não o template inteiro)?
- A correção elimina a CLASSE de erro (não só o item específico)?
- Depois da correção, os 3 itens-piloto regenerados não têm nenhum dos 7 defeitos?

## Saída esperada

Lista de mudanças (com diff antes/depois) que eliminam a classe de erro. Aplique, regenere, repita até os 7 defeitos não aparecerem.
