# Prompt — Capítulo 8 (1/2) · Bloco de automação para os 3 primeiros itens

**Quando usar:** depois de gerar os PNGs do capítulo 7, para montar o bloco `automation` da planilha (palavra-chave, DM, link, public reply).

**Onde é citado no livro:** capítulo 8, seção "Prompt para colar na IA".

---

## O prompt

```
Você é meu arquiteto de automação de marketing.

Minha série de [N] carrosséis está pronta. Cada peça tem um
slide 8 (CTA) que termina com a frase:
  "[FRASE DO CTA, ex: 'Comenta LLM gratuito que eu te mando
  o comparativo no direct']"

A escada da minha série é:
  - Degrau 0: peça do carrossel (sem custo)
  - Degrau 1: comentário com palavra-chave
  - Degrau 2: DM com [MATERIAL GRATUITO, ex: 'PDF comparativo
    dos modelos']
  - Degrau 3: convite para [PRÓXIMO PASSO, ex: 'aula
    experimental de 30 minutos']
  - Degrau 4: oferta de [PRODUTO PRINCIPAL, ex: 'mentoria
    em grupo']

O material gratuito do degrau 2 está em [LINK].
O convite para o degrau 3 é enviado em sequência, 2 dias
depois, por outra automação (não neste livro).

A copy dos 3 primeiros itens da minha série é:

  Item 1 - [NOME]:
    Slide 1 (gancho): "[COPY]"
    Slide 8 (cta): "[COPY]"
  Item 2 - [NOME]:
    Slide 1 (gancho): "[COPY]"
    Slide 8 (cta): "[COPY]"
  Item 3 - [NOME]:
    Slide 1 (gancho): "[COPY]"
    Slide 8 (cta): "[COPY]"

Para cada um desses 3 itens, me dê o bloco de automation
pronto, no formato:

  item [N]:
    keywords: [LISTA DE 1 A 3 PALAVRAS-CHAVE]
    mensagem: "[TEXTO DO DM, com {{nome}} onde entra o nome do
      leitor, e com link {{link}} onde entra o link do
      material]"
    link: "[LINK DO MATERIAL GRATUITO]"
    public_reply_enabled: true
    public_reply_text: "[TEXTO DA RESPOSTA PÚBLICA]"

Justifique em 1 frase cada escolha (por que essa palavra-
chave, por que essa mensagem, por que esse public reply).
```

## Regras para validar a resposta

- **Palavra-chave:** 1 a 2 palavras, alinhada com a categoria do item e com a copy do slide 1.
- **Mensagem do DM:** até 280 caracteres, com `{{nome}}` e `{{link}}`.
- **Link:** o mesmo para todos os itens da série (a menos que você queira diferenciar por tier).
- **Public reply:** uma das frases curtas ("Te chamei no direct!", "Material na sua DM :)", "Confere o direct").

## O que conferir depois

- A palavra-chave tem no máximo 2 palavras?
- A mensagem do DM cabe em 280 caracteres?
- O `{{nome}}` está dentro da mensagem?
- O public reply está habilitado em todos os 3 itens?
- O link é o mesmo para todos os 3 itens (ou você justificou a diferença)?

## Saída esperada

Bloco `automation` pronto para os 3 primeiros itens, com justificativa. Depois de validar, aplique aos outros 415 itens usando o segundo prompt (`cap-08-automacao-massa.md`).
