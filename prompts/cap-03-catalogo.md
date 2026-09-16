# Prompt — Capítulo 3 · A fonte de dados (catálogo)

**Quando usar:** quando você tem o tema da série mas ainda não decidiu quais colunas vão na planilha catálogo, ou quais atributos viram eixos de classificação.

**Onde é citado no livro:** capítulo 3, seção "Prompt para colar na IA".

---

## O prompt

Cole este bloco no ChatGPT, Claude ou Gemini. Preencha os colchetes e inclua 10 linhas reais do seu catálogo (copie e cole do Google Sheets como tabela).

```
Você é meu arquiteto de catálogo para uma série de carrosséis.

Minha série é sobre [TEMA]. O catálogo que estou montando tem
[N, ex: 200] itens. Abaixo segue uma amostra de 10 linhas
reais do catálogo, no formato de tabela:

| id | nome | [SUAS COLUNAS] |
| 1  | ...  | ...            |
| 2  | ...  | ...            |
| ...                        |

Quero produzir carrosséis sobre [TEMA] no formato do livro
"Carrosséis Infinitos com Qualquer IA" (anatomia fixa de 8
slides, copy por peça gerada a partir de eixos de
classificação).

Para esse catálogo:

1. Quais colunas são ÚTEIS para gerar copy diferente para cada
   item (atributos que mudam a copy)? Liste e explique em 1
   frase cada.

2. Quais colunas são apenas metadados para o renderizador (cor
   de destaque, URL de logo) e não afetam a copy? Liste e
   explique.

3. Sugira 2 eixos de classificação para a copy:
     - Eixo 1: nome, valores possíveis (3 a 6), com base nas
       colunas do meu catálogo.
     - Eixo 2: nome, valores possíveis (3 a 6), com base nas
       colunas do meu catálogo.
   Para cada eixo, justifique em 1 frase por que esses valores
   geram copy diferente.

4. Alguma coluna importante está faltando no meu catálogo para
   sustentar esses eixos? Sugira até 3 colunas novas.

5. Alguma coluna existe mas não serve para nada? Sugira
   remover.

Termine com a estrutura final da planilha (nome e tipo de cada
coluna), pronta para eu aplicar.
```

## Exemplo preenchido

```
Minha série é sobre ferramentas de IA para programadores. O
catálogo tem 200 itens. Amostra:

| id | nome | categoria | preco_mes | tem_api | url_oficial |
| 1  | Cursor | editor | 20 | sim | https://cursor.sh |
| 2  | Copilot | editor | 10 | sim | https://github.com/copilot |
| 3  | v0 | gerador | 20 | sim | https://v0.dev |
| 4  | Cody | chat | 0 | sim | https://sourcegraph.com/cody |
| 5  | Continue | editor | 0 | sim | https://continue.dev |
| 6  | Aider | chat | 0 | sim | https://aider.chat |
| 7  | Devin | agente | 500 | sim | https://devin.ai |
| 8  | Phind | chat | 0 | sim | https://phind.com |
| 9  | Codeium | editor | 0 | sim | https://codeium.com |
| 10 | Tabnine | editor | 12 | sim | https://tabnine.com |
```

## Variações

**Se você ainda não tem linhas:** adicione "Me dê 10 linhas de exemplo para o tema [TEMA], inventadas mas realistas. Use-as como base para a análise."

**Se você já tem mais de 100 linhas:** adicione "Analise apenas as primeiras 30 linhas; eu vou validar que o padrão se mantém nas outras."

## O que conferir depois

- Os 2 eixos sugeridos têm entre 3 e 6 valores cada?
- A IA sugeriu colunas novas que você consegue obter?
- A estrutura final cabe no Google Sheets sem fórmulas complicadas?

## Saída esperada

A IA devolve (a) lista de colunas úteis vs metadados, (b) dois eixos com 3 a 6 valores cada, (c) sugestões de colunas novas, (d) estrutura final da planilha.
