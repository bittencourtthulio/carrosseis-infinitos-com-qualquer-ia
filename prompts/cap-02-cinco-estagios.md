# Prompt — Capítulo 2 · A fábrica em cinco estágios

**Quando usar:** quando você decidiu ir pelo jeito 2 e quer desenhar a esteira completa da sua série, do catálogo ao post agendado.

**Onde é citado no livro:** capítulo 2, seção "Prompt para colar na IA".

---

## O prompt

Cole este bloco no ChatGPT, Claude ou Gemini. Preencha os colchetes com seus dados.

```
Você é meu arquiteto de produção de conteúdo. Quero produzir
[N, ex: 100, 200, 500] carrosséis sobre [TEMA, ex: ferramentas
de IA para programadores] para vender [PRODUTO/SERVIÇO/IDEIA].

Me ajude a desenhar a esteira em 5 estágios, no mesmo padrão
que vou te explicar:

  Estágio 1: Fonte de dados. Entrada: [descreva o que você tem].
  Saída: planilha bruta. Ferramenta sugerida: Google Sheets.
  Estágio 2: Gerador de copy. Entrada: planilha do estágio 1.
  Saída: planilha de copy com 8 slides por item. Ferramenta:
  ChatGPT/Claude/Gemini + Sheets.
  Estágio 3: Captura de prints. Entrada: planilha do estágio 2.
  Saída: pasta de imagens. Ferramenta: extensão de Chrome ou
  script.
  Estágio 4: Renderizador. Entrada: planilha do estágio 2 e
  pasta de imagens. Saída: PNGs 1080x1350. Ferramenta: script
  Python no Google Colab OU Canva manual.
  Estágio 5: Publicador. Entrada: PNGs do estágio 4. Saída:
  posts agendados. Ferramenta: Buffer, Later ou Meta Business
  Suite.

Para CADA estágio, me dê:
  - Nome curto
  - Entrada (o que lê)
  - Saída (o que escreve)
  - Ferramenta sugerida (preferência por gratuita)
  - Quem faz (eu, a IA, ou um script que a IA vai escrever)

Termine com a lista do que eu preciso ter aberto antes de
começar (contas, planilhas, pastas).
```

## Exemplos preenchidos

### Exemplo 1: software house

- `[N]`: 200
- `[TEMA]`: modelos de IA para usar em código de produção
- `[PRODUTO/SERVIÇO/IDEIA]`: mentoria em grupo para líderes técnicos

### Exemplo 2: restaurante

- `[N]`: 60
- `[TEMA]`: pratos do cardápio de inverno
- `[PRODUTO/SERVIÇO/IDEIA]`: serviço de entrega no bairro

### Exemplo 3: agência de marketing

- `[N]`: 150
- `[TEMA]`: ferramentas de IA para equipes pequenas
- `[PRODUTO/SERVIÇO/IDEIA]`: assinatura mensal da agência

## Variações

**Para ferramentas que não conhece:** adicione "Só sugira ferramentas com versão gratuita ou que eu já tenha conta. Se precisar de uma ferramenta nova, explique o custo."

**Para séries muito pequenas (menos de 30 peças):** adicione "Como o volume é pequeno, me diga quais estágios eu posso fundir ou pular sem perder qualidade."

## O que conferir depois

- Os 5 estágios têm entradas e saídas concretas (arquivos nomeados)?
- As ferramentas sugeridas são gratuitas ou têm versão gratuita?
- O fluxo de arquivos cabe na sua pasta do Drive?

## Saída esperada

A IA devolve um diagrama em texto dos 5 estágios, com nome, entrada, saída, ferramenta sugerida e responsável por cada um. No final, uma checklist do que você precisa ter aberto antes de começar.
