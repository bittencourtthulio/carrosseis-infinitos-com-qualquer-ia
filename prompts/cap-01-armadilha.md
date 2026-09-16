# Prompt — Capítulo 1 · A armadilha do token na peça

**Quando usar:** quando você ainda não decidiu se vai pelo jeito 1 (IA gera cada peça) ou pelo jeito 2 (IA gera o sistema que gera as peças).

**Onde é citado no livro:** capítulo 1, seção "Prompt para colar na IA".

---

## O prompt

Cole este bloco no ChatGPT, Claude ou Gemini. Troque os colchetes pelos seus dados antes de colar.

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

## Variações

**Para Claude (Anthropic):** o prompt funciona como está. Se quiser instruir tom, adicione no início: "Responda em tom conversacional, sem jargão técnico, como se explicasse para um amigo empreendedor."

**Para Gemini (Google):** idem. Se a resposta vier muito longa, adicione no final: "Responda em no máximo 400 palavras. Use uma única analogia."

## O que conferir depois

- A analogia fez sentido? Se não, peça: "Me dê uma analogia diferente, ainda mais simples."
- As 3 perguntas finais caem na sua realidade? Se sim, você está no jeito 1 e este livro é para você.
- A resposta cabe em 1 página? Se passar, peça para resumir.

## Saída esperada

A IA devolve (a) uma analogia curta que explica a diferença entre os dois jeitos, (b) opcionalmente uma mini-conta de tokens, e (c) três perguntas de autodiagnóstico.

Guarde a resposta em `fabrica-carrosseis/cap01/` para consulta futura.
