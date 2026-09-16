# Prompt — Capítulo 10 · Auditoria de prontidão da próxima série

**Quando usar:** quando você quiser abrir uma nova série (tema diferente) e quiser saber se está pronto para rodar o playbook antes de começar.

**Onde é citado no livro:** capítulo 10, seção "Passo a passo (aplicar o playbook à próxima série)".

---

## O prompt

```
Você é meu auditor de prontidão de série.

Estou planejando minha próxima série de carrosséis. Antes de
rodar o playbook, quero saber se estou pronto.

Minha próxima série:
  - Tema: [TEMA]
  - Público: [PÚBLICO]
  - Produto que estou vendendo: [PRODUTO]
  - Volume estimado: [N, ex: 100] carrosséis
  - Volume de posts por semana: [N, ex: 5]

Aqui está o que já tenho:
  - Catálogo: [SIM/NÃO] (se sim, [N] linhas, com as colunas
    [LISTA])
  - Eixos definidos: [SIM/NÃO] (se sim, [EIXO 1] com [LISTA]
    e [EIXO 2] com [LISTA])
  - Tabela de teses: [SIM/NÃO] (se sim, quantas combinações)
  - Pools de variações: [SIM/NÃO] (se sim, quantas variações
    por slide na média)
  - Anatomia dos 8 slides: [SIM/NÃO]
  - Assets visuais: [SIM/NÃO] (capa nova, ícones de tier,
    moldura)
  - Prints capturados: [SIM/NÃO]
  - Renderizador testado em 3 amostras: [SIM/NÃO]
  - Automação de DM configurada: [SIM/NÃO]

Me faça 10 perguntas para eu saber se estou pronto para rodar
o playbook. Não responda por mim. Apenas pergunte.

Depois que eu responder, me dê um relatório de prontidão
com: (a) o que está pronto, (b) o que está faltando, (c)
qual o próximo passo imediato.
```

## Variação: para uma série que reaproveita a fábrica anterior

Se você está abrindo uma série 2 sobre tema diferente mas mantendo a marca visual (paleta, fontes, ícones de tier), adicione:

```
Da série anterior [NOME_DA_SERIE], vou reaproveitar:
  - Paleta visual
  - Fontes (Chakra Petch, JetBrains Mono, Inter)
  - Ícones de tier
  - Detalhe de marca
Vou gerar:
  - Capa nova
  - Moldura nova (se o estilo mudou)
```

## O que conferir depois

- A IA fez 10 perguntas (não respondeu por você)?
- As perguntas cobrem catálogo, eixos, teses, pools, anatomia, assets, prints, renderizador, automação?
- Quando você respondeu, a IA devolveu "pronto para gerar o lote" ou pediu mais informação?

## Saída esperada

A IA devolve um relatório de prontidão com 3 listas (o que está pronto, o que está faltando, próximo passo). Se algo está faltando, siga o playbook do capítulo 10 (passos 1 a 10) para preencher.
