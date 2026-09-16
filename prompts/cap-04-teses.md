# Prompt 04: Teses por combinação

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Você é meu agente local e redator-chefe desta série.
Leia PROJETO.md, 01-catalogo/catalogo.csv
e 01-catalogo/ESQUEMA.md antes de escrever.
Salve a entrega em 02-copy/teses.md.

Minha série tem estes dois eixos de classificação:

  Eixo 1 (nome: [NOME,
    ex: TIER_DE_PRECO]): valores possíveis
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
  - prometer uma coisa concreta para o leitor (não
    ser genérica);
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

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 04.
- Seção do livro: Prompt 1 para colar na IA (teses por combinação).
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
