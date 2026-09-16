# Prompt — Capítulo 8 (2/2) · Bloco de automação em massa

**Quando usar:** depois de validar o bloco de automação dos 3 primeiros itens, para gerar o bloco dos outros 415 itens automaticamente.

**Onde é citado no livro:** capítulo 8, seção "Prompt para colar na IA (em massa, para os 415 itens restantes)".

---

## O prompt

```
Você é meu arquiteto de automação de marketing.

Para CADA item da planilha
[URL_DA_PLANILHA_COM_COPY_DOS_415_ITENS_RESTANTES], gere o
bloco de automation seguindo as mesmas regras que você
acabou de aplicar aos 3 primeiros itens:

  - keywords: 1 a 3 palavras curtas, alinhadas com a
    categoria do item e com a copy do slide 1.
  - mensagem: até 280 caracteres, com {{nome}} e {{link}}.
  - link: o mesmo para todos os itens
    ([LINK_DO_MATERIAL]).
  - public_reply_enabled: true.
  - public_reply_text: uma das 3 frases curtas que você
    sugeriu antes (varie entre os itens).

Formato de saída: um JSON com [N] entradas, cada uma com os
campos acima. Salve em um Google Sheets novo, na aba
"automation".
```

## Como validar a saída em massa

1. Abra a planilha nova que a IA preencheu.
2. Confira 10 itens aleatórios: a palavra-chave está alinhada com a copy? A mensagem tem `{{nome}}` e `{{link}}`? O link é o mesmo para todos?
3. Filtre a coluna `keywords` por itens com mais de 2 palavras. Se houver, peça para a IA reduzir.
4. Filtre a coluna `mensagem` por itens com mais de 280 caracteres. Se houver, peça para a IA cortar.
5. Filtre a coluna `public_reply_text` por itens com frases diferentes das 3 sugeridas. Se houver, peça para uniformizar.

## Variação: se você quiser diferenciar o link por tier

Adicione ao prompt:

```
Para itens de tier "free" e "barato", use o link
[LINK_DO_MATERIAL_FREE].
Para itens de tier "medio" e "caro", use o link
[LINK_DO_MATERIAL_PRO].
```

## Variação: se você quiser desabilitar o public reply em alguns itens

Adicione ao prompt:

```
Para itens cujo tema (coluna [COLUNA_DE_TEMA]) contém a
palavra "[PALAVRA_POLÊMICA, ex: 'concorrência']", desabilite
o public_reply_enabled (false) para evitar acúmulo de
comentários negativos no post.
```

## O que conferir depois

- A IA gerou bloco para todos os 415 itens?
- A palavra-chave tem no máximo 2 palavras em todos os itens?
- A mensagem do DM cabe em 280 caracteres em todos os itens?
- O `{{nome}}` está dentro da mensagem em todos os itens?
- O link é o mesmo (ou a diferenciação foi justificada)?

## Saída esperada

JSON ou planilha com 415 entradas, cada uma com `keywords`, `mensagem`, `link`, `public_reply_enabled`, `public_reply_text`. Salve como nova aba `automation` na planilha `02-copy`.
