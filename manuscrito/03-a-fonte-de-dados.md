# Capítulo 3: A fonte de dados: o catálogo é o motor

**Tempo de leitura:** 14 min
**O que você sai sabendo:** como decidir quais atributos do seu catálogo viram eixos de classificação da copy, e como transformar uma lista de itens em uma planilha estruturada que alimenta a fábrica inteira.
**Token gasto neste capítulo:** zero na leitura; uma sessão curta de design com a IA quando você aplicar.

## Conceito

Sem catálogo com atributos que mudem a copy, não há lote. Este capítulo é sobre a decisão que vem antes de qualquer prompt-mestre: **o que entra na planilha**.

A tentação é começar pela copy. "Vou pedir para a IA escrever o carrossel de cada item." Mas se você fizer isso, vai descobrir (em geral na peça número cinco) que a copy precisa de informação que você não tem. "Qual é o preço deste item? Ah, não coloquei. Qual é a categoria? Também não." E volta para o catálogo.

A ordem certa é o contrário: catálogo primeiro, copy depois. O catálogo é o motor. A copy é o carro. Você não pinta o carro antes de comprar o motor.

## O que é um "atributo que muda a copy"

Um atributo muda a copy quando, ao mudar o valor do atributo, a copy gerada para o item muda de forma perceptível. Exemplos:

| Atributo | Item A | Item B | A copy muda? |
|---|---|---|---|
| Preço por token | $0.0001 | $0.01 | Sim, a copy do slide "como cobrar" muda. |
| Modalidade | texto | imagem | Sim, a copy do slide "prática" muda. |
| Cor do provider | verde | laranja | Sim, o destaque visual muda. |
| URL do site oficial | site1.com | site2.com | Não, a copy fica igual (o print muda, não a copy). |
| Nome do item | "Alpha" | "Beta" | Não (a copy cita o nome em todos os slides, mas a estrutura não muda). |

A última coluna é o teste. Se a copy fica igual quando o atributo muda, o atributo não precisa estar no catálogo (ou precisa, mas como metadado de impressão, não como eixo de copy).

## Como decidir os eixos de classificação

Eixos são os atributos que viram categorias. A série OpenRouter usou dois eixos:

- **Eixo preço** (4 valores: free, barato, médio, caro)
- **Eixo modalidade** (6 valores: texto, código, visão, vídeo, imagem, áudio)

Dois eixos com 4 e 6 valores dão 24 combinações possíveis. Cada combinação recebeu uma tese em uma frase, e cada slide de cada combinação recebeu um pool de frases.

Para a sua série, comece com **dois eixos de 3 a 6 valores cada**. Mais que isso, a tabela de teses explode. Menos que isso, a copy perde variação.

Para decidir quais eixos, faça a si mesmo três perguntas:

1. **"Se dois itens diferem apenas neste atributo, a copy deles tem que ser diferente?"** Se sim, é um eixo.
2. **"Esse atributo tem pelo menos três valores distintos no meu catálogo?"** Se tem só dois (sim/não, presente/ausente), vira um filtro, não um eixo.
3. **"Eu consigo explicar a tese para cada combinação sem repetir a mesma frase?"** Se em alguma combinação você não sabe o que dizer, ou o eixo é irrelevante ou o catálogo precisa de mais atributos.

## O catálogo mínimo viável

A estrutura da planilha, com uma linha por item e uma coluna por atributo:

| Coluna | Tipo | Exemplo | Obrigatória? |
|---|---|---|---|
| `id` | número | 1 | sim |
| `nome` | texto | "Alpha 3.5 Vision" | sim |
| `categoria_1` | texto | "barato" | sim (eixo 1) |
| `categoria_2` | texto | "visão" | sim (eixo 2) |
| `preco_prompt` | texto | "0.0001" | depende do produto |
| `preco_completion` | texto | "0.0002" | depende do produto |
| `url_oficial` | texto | "https://..." | sim |
| `descricao_curta` | texto (até 280 caracteres) | "Modelo de visão..." | sim |
| `destaque_visual` | hex cor | "#16A34A" | opcional |
| `logomarca` | URL de imagem | "https://..." | opcional |

As colunas `categoria_1` e `categoria_2` são os eixos. As outras colunas são atributos que a copy consome (citados em algum slide) ou metadados para o renderizador.

## Material necessário

- Conta gratuita ou paga em ChatGPT, Claude ou Gemini.
- Acesso a Google Sheets (uma planilha em branco).

## Passo a passo

1. Crie uma planilha nova em Google Sheets, com o nome `catalogo-[sua-serie]`.
2. Crie as colunas da tabela acima (ou ajuste os nomes para o seu domínio).
3. Preencha 10 linhas com itens reais (ou candidatos a itens) da sua série.
4. Abra o ChatGPT.
5. Cole o prompt abaixo, incluindo as 10 linhas da planilha (copie e cole como tabela no chat).
6. Leia a resposta. A IA vai sugerir os eixos e apontar colunas que estão faltando ou sobrando.
7. Copie a resposta para `fabrica-carrosseis/cap03`.
8. Ajuste as colunas da planilha conforme a sugestão da IA.

## Prompt para colar na IA

```
Você é meu arquiteto de catálogo para uma série de
    carrosséis.

Minha série é sobre [TEMA]. O catálogo que estou montando
    tem
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

1. Quais colunas são ÚTEIS para gerar copy diferente
    para cada
   item (atributos que mudam a copy)? Liste e explique em 1
   frase cada.

2. Quais colunas são apenas metadados para o renderizador
    (cor
   de destaque, URL de logo) e não afetam a copy? Liste e
   explique.

3. Sugira 2 eixos de classificação para a copy:
     - Eixo 1: nome, valores possíveis (3 a 6), com base nas
       colunas do meu catálogo.
     - Eixo 2: nome, valores possíveis (3 a 6), com base nas
       colunas do meu catálogo.
   Para cada eixo, 
    justifique em 1 frase por que esses valores
   geram copy diferente.

4. Alguma coluna importante está faltando no meu catálogo
    para
   sustentar esses eixos? Sugira até 3 colunas novas.

5. Alguma coluna existe mas não serve para nada? Sugira
   remover.

Termine com a estrutura final da planilha (nome e 
    tipo de cada
coluna), pronta para eu aplicar.
```



**QR code do prompt:**

![QR code do prompt cap-03-catalogo](../figuras/qr_box/cap-03-catalogo.svg)

[Abrir no GitHub](https://github.com/bittencourtthulio/carrosseis-infinitos-com-qualquer-ia/blob/main/prompts/cap-03-catalogo.md)

(O prompt completo, com instruções de uso e variações para Claude e Gemini, está em `prompts/cap-03-catalogo.md` no repositório público.)

## O que conferir

- Os dois eixos sugeridos pela IA têm entre 3 e 6 valores cada? Se um eixo ficou com 2 valores (sim/não), peça outro: "Me dê um eixo diferente, com pelo menos 3 valores."
- A IA apontou colunas novas para incluir? Confirme se você tem esses dados ou consegue obtê-los. Se não consegue (por exemplo, "preço promocional fora de pico" é dado privado de um marketplace), troque por outro atributo que você tem.
- A estrutura final da planilha cabe no Sheets sem fórmula complicada? Se a IA sugerir colunas com fórmulas encadeadas, peça para simplificar: "A coluna X pode ser texto puro, sem fórmula? Quem vai preencher é humano."

## O que muda amanhã de manhã

Você vai abrir a planilha `catalogo-[sua-serie]` e preencher todas as linhas, não só as 10. Se o catálogo é grande (mais de 50 itens), divida em dois dias: hoje os primeiros 25, amanhã os outros 25. Não peça para a IA gerar os dados do catálogo: a IA não conhece seu domínio, e os dados inventados vão para a copy, e a copy inventada vai para o post, e o leitor percebe. Catálogo é trabalho humano, copy é trabalho do sistema.

## QR codes dos prompts deste capitulo

Aponte a camera do celular para cada QR code ou clique no link para abrir o arquivo `.md` completo no GitHub. O arquivo contem o prompt destacado, variacoes para Claude e Gemini, exemplos preenchidos e o checklist de validacao.

### Prompt 03 - A fonte de dados

![QR code do Prompt 03 - A fonte de dados](../figuras/qr_box/cap-03-catalogo.svg)

[Abrir no GitHub](https://github.com/bittencourtthulio/carrosseis-infinitos-com-qualquer-ia/blob/main/prompts/cap-03-catalogo.md)  
Arquivo: `prompts/cap-03-catalogo.md` no repositorio publico.

