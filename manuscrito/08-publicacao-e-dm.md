# Capítulo 8 — Publicação e DM na mesma chamada

**Tempo de leitura:** 13 min
**O que você sai sabendo:** como montar o bloco de automação que faz a peça de topo do carrossel apontar para o próximo degrau (palavra-chave de comentário + DM com link), e como agendar a série no Instagram sem chamar modelo de IA.
**Token gasto neste capítulo:** zero na leitura; uma sessão curta com a IA para montar o bloco de automação quando você aplicar.

## Conceito

O carrossel não termina quando o último slide é postado. Termina quando o leitor entra na esteira de relacionamento (comenta, recebe DM, baixa material, vira lead). É aqui que a peça de topo vira peça de funil.

A série OpenRouter chamava esse passo de "automação". Para cada item da série, a planilha `02-copy` tinha um bloco `automation` com:

| Campo | O que é | Exemplo |
|---|---|---|
| `keywords` | Lista de palavras-chave que o leitor comenta para ativar a automação | `["LLM", "modelo"]` |
| `mensagem` | Mensagem de DM enviada para quem comentou | `"Oi {{nome}}! Aqui está o material gratuito sobre como escolher LLM para software house: ..."` |
| `link` | Link enviado na DM | `"https://expx.com.br/material"` |
| `public_reply_enabled` | Se a automação responde também em comentário público | `true` |
| `public_reply_text` | Texto da resposta pública | `"Te chamei no direct!"` |

A peça de topo do carrossel (slide 8, CTA) cita a palavra-chave. O leitor comenta. A automação detecta o comentário e dispara o DM. O carrossel é peça de topo, e o CTA leva ao próximo degrau, não ao mais caro.

## Por que o CTA aponta para o próximo degrau

A tentação é colocar o CTA direto na oferta mais cara ("Compre o curso de R$ 5.000"). Em uma série que ainda não gerou confiança, o leitor pula. Em uma série que gerou confiança passo a passo, o leitor entra no próximo degrau.

A escada clássica da série OpenRouter era:

```
degrau 0: peça do carrossel (peça de topo, sem custo)
degrau 1: comentário com palavra-chave → DM com material gratuito
degrau 2: lead qualificado → convite para aula experimental
degrau 3: aluno da aula → oferta do produto principal
```

Cada peça do carrossel alimenta o degrau 1. Os leitores que chegam no DM recebem material gratuito (degrau 2). Os que abrem o material recebem convite para a aula (degrau 3). Os que comparecem à aula recebem a oferta (degrau 4).

A peça do carrossel não precisa carregar o CTA da oferta. Ela precisa carregar o CTA do próximo degrau.

## A escolha da palavra-chave

A palavra-chave do comentário é o gatilho da automação. Ela tem que ser:

- **Curta o bastante para o leitor digitar sem pensar.** Duas palavras, no máximo.
- **Específica o bastante para não disparar por engano.** Evite palavras que aparecem em comentários não relacionados.
- **Alinhada com o conteúdo do carrossel.** Se a peça fala de "modelo de IA gratuito", a palavra-chave tem que ser "LLM gratuito", não "IA" (genérico demais).

A série OpenRouter usava a própria categoria do item como palavra-chave: `LLM gratuito`, `LLM barato`, `modelo de visão`, `modelo de código`. Quem comenta "LLM gratuito" em uma peça sobre um modelo free, recebe DM sobre o material de modelos free.

Para a sua série, a palavra-chave segue a mesma lógica: a categoria do item, em duas palavras, alinhada com o gancho da peça.

## O public reply (resposta pública em comentário)

A resposta pública serve para dois propósitos:

1. **Sinalizar para outros leitores que o comentário foi atendido.** Quem vê o comentário original e a resposta automática entende que "comentar funciona".
2. **Aumentar a contagem de comentários visível no post.** O Instagram valoriza posts com muitos comentários no alcance.

A frase do public reply é curta e não revela que é automática: `"Te chamei no direct!"`, `"Material na sua DM :)"`, `"Confere o direct"`. Evite "Obrigado por comentar!" — soa robótico.

A regra da série OpenRouter era manter o public reply habilitado em todos os itens, exceto quando o post pudesse receber comentário ofensivo em volume (assunto polêmico). Para a sua série, comece com habilitado em todos e desligue se o volume de comentários ofensivos aparecer.

## Material necessário

- Conta gratuita ou paga em ChatGPT, Claude ou Gemini.
- Acesso à planilha `02-copy` do capítulo 4.
- Conta no Instagram Business (para usar a API de automação ou ferramentas de terceiros).
- Conta no ManyChat, na ferramenta de automação nativa do Instagram, ou no Buffer / Later / Meta Business Suite para agendamento.

## Passo a passo

1. Defina a escada de degraus da sua série (do degrau 0 ao último).
2. Defina o material gratuito que vai no DM (degrau 2).
3. Defina a mensagem de DM e o link (degrau 2).
4. Defina a palavra-chave do comentário (degrau 1).
5. Defina o texto do public reply.
6. Abra o ChatGPT.
7. Cole o prompt abaixo, com a tabela de campos preenchida para os 3 primeiros itens da sua série.
8. Leia a resposta. Para cada item, confira se a palavra-chave, a mensagem, o link e o public reply estão alinhados com o conteúdo da peça.
9. Copie a resposta para `fabrica-carrosseis/cap08`.
10. Aplique o bloco de automação aos outros 415 itens (a IA pode fazer isso em massa, no prompt seguinte).

## Prompt para colar na IA

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

Repita o processo em sequência para os próximos 5 itens da
série (itens 4 a 8), lendo da planilha
[URL_DA_PLANILHA].
```

## Prompt para colar na IA (em massa, para os 415 itens restantes)

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

(Os dois prompts completos, com exemplos preenchidos para o nicho de [TEMA], estão em `prompts/cap-08-automacao.md` e `prompts/cap-08-automacao-massa.md` no repositório público.)

## O que conferir

- A palavra-chave tem no máximo 2 palavras? Se a IA sugerir 3 ou 4, peça para reduzir.
- A mensagem do DM cabe em 280 caracteres? Se passar, peça para cortar. O Instagram limita DMs a 1000 caracteres, mas o leitor não lê mais que 280.
- O `{{nome}}` está dentro da mensagem? Se não estiver, a IA não vai personalizar o DM.
- O public reply está habilitado em todos os itens? Se algum estiver com `false`, peça para justificar.
- O link do material é o mesmo para todos os itens? Se você quiser link diferente por categoria (ex.: modelo free recebe link A, modelo caro recebe link B), peça para a IA diferenciar por tier.

## O que muda amanhã de manhã

Você vai abrir a planilha `02-copy` e conferir que cada linha tem o bloco `automation` preenchido. Amanhã, quando configurar a ferramenta de automação (ManyChat, ferramenta nativa do Instagram, ou script Python que chama a API), você aponta a ferramenta para a planilha e ela lê o bloco. Cada comentário com a palavra-chave dispara o DM com a mensagem personalizada. Você não precisa revisar item por item: a copy já foi revisada na planilha, e a automação é determinística.
