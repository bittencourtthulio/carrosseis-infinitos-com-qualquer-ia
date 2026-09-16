# Prompt 04: Pools de variações

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Você é meu agente local no Claude Code ou OpenCode.
Leia o catálogo, seu esquema e 02-copy/teses.md.
Crie os arquivos e execute o gerador; não entregue
somente uma resposta de texto nesta conversa.

A série tem a anatomia fixa de 8 slides:
  1. gancho (dor concreta que termina no nome do item)
  2. o_que_e (define e desarma a objeção técnica)
  3. pratica (cena de uso por modalidade)
  4. o_que_vender (bullets que viram linha de proposta)
  5. como_cobrar (monetização que fecha a conta do gancho)
  6. [NOME_PRODUTO] (preço real e link)
  7. benchmark (número real com leitura por faixa)
  8. cta (promessa do tier + chamada para ação)

Use a tabela de teses salva no passo anterior.

Para CADA combinação de eixos e para CADA slide (exceto o
slide 6, que tem preço fixo), gere um POOL de 8 a 10
variações.

Cada variação deve:
  - Caber em até [N, ex: 100] caracteres.
  - Conter 1 a 3 "trechos de destaque" (palavras ou
    expressões
    curtas que viram negrito no post).
  - Ser semanticamente diferente das outras variações
    do pool
    (não ser paráfrase).
  - No slide 1 (gancho),
    terminar no NOME do item (placeholder
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

Salve os pools em 02-copy/pools.json com versão.
Crie scripts/gerar_copy.py para ler o catálogo,
classificar os itens e selecionar variações por
hash estável do ID, sem chamar modelo de IA.
Use as fontes para preencher os campos factuais.
Não transforme preço alto em prova de qualidade.
Não prometa capacidade que os dados não comprovam.

Execute uma amostra de até três itens.
Salve 02-copy/carrosseis.json com oito slides por item,
função, texto, destaques, provas exigidas e legenda.
Documente o contrato em 02-copy/CONTRATO.md.
Repita a execução e confira o determinismo da saída.
Mostre os arquivos criados e as verificações feitas.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 04.
- Seção do livro: Prompt 2 para colar na IA (pools de variações).
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
