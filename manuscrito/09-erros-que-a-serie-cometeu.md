# Capítulo 9: Erros que a série cometeu (e que a sua não vai repetir)

**Tempo de leitura:** 14 min
**O que você sai sabendo:** os sete defeitos específicos que chegaram ao PNG da série OpenRouter, com a causa raiz, o efeito visível, e a correção no prompt-mestre para a sua série não repetir.
**Token gasto neste capítulo:** zero na leitura; uma sessão curta de IA para validar suas primeiras peças contra esta lista.

## Conceito

Cada linha desta tabela nasceu de um PNG errado. Cada PNG errado custou horas de revisão e ajuste. Vale a pena ler antes de começar, porque a próxima série não precisa pagar o que esta já pagou para aprender.

Os erros estão em ordem de impacto visual (do mais óbvio ao mais sutil). Para cada erro, a tabela traz:

- **O erro** (o que foi feito de errado).
- **O efeito** (como aparece no PNG).
- **A correção** (onde mexer no prompt-mestre ou no template).

## Os sete erros

### Erro 1: Um exemplo só de cena para modelos de visão

**Erro.** O prompt-mestre do slide 3 (prática) tinha uma única cena por modalidade: `foto da nota fiscal` para visão, `trecho de código` para código, `página de chat` para texto.

**Efeito.** 254 dos 418 carrosséis diziam "foto da nota fiscal" no slide 3. O feed ficou visualmente igual peça após peça, e o leitor percebeu a repetição no terceiro post.

**Correção.** Pool de dez cenas por modalidade, cobrindo setores diferentes: nota fiscal, print de erro, currículo em PDF, canteiro de obra, contrato, planta baixa, boleto, exame médico, etiqueta de estoque, manual técnico. Cada item recebe uma cena pelo hash do id, sem sorteio.

**Onde mexer.** No prompt do capítulo 4 (prompt 2, slide 3), exigir pool mínimo de 8 a 10 variações por combinação de eixos, e validar visualmente que não são paráfrases.

### Erro 2: Mancha de luz posicionada com `bottom` negativo

**Erro.** O asset visual "mancha de luz" do template escuro foi posicionado com `bottom: -50px` (estilosa, "vazando" para fora do slide).

**Efeito.** O slide estourava 100px sem depender do fator `k` (o loop de ajuste não pegava porque o estouro era do asset, não do texto). Os 209 slides escuros saíram com a mancha cortada no rodapé.

**Correção.** Posicionar assets absolutos sempre com `top` (referência ao topo do slide), nunca com `bottom` negativo. Se o efeito visual exigir que o asset "vaze", controlar o overflow com `overflow: hidden` no container do slide, e medir a altura do container antes de salvar.

**Onde mexer.** No template CSS do prompt do capítulo 7, escrever: "Todos os assets posicionados absolutamente devem usar `top`, nunca `bottom` negativo. Use `overflow: hidden` no container do slide."

### Erro 3: Página do OpenRouter sem o sufixo `:free`

**Erro.** A URL da página de preço do OpenRouter era construída sem o sufixo `:free` quando o tier era `free`. Resultado: a URL caía na página do modelo pago equivalente.

**Efeito.** O print do slide 6 (preço) mostrava o preço pago de um modelo que a copy dizia ser gratuito. Contradição visível, perda de credibilidade.

**Correção.** A cadeia de URLs do capítulo 6 precisa ter uma regra explícita por tier: para `free`, sufixo `:free`; para `barato`, sem sufixo; etc. Validar antes de capturar, com uma chamada HEAD que confere o conteúdo da página (não só o status 200).

**Onde mexer.** No prompt do capítulo 6, escrever a cadeia de URLs por tier, e incluir no script a validação do conteúdo: "Se o tier é free, a página precisa ter a string 'free' no HTML; caso contrário, pula para a próxima URL da cadeia."

### Erro 4: Card de preço promocional fora de pico

**Erro.** O print do slide 6 (preço) capturava o card de preço promocional que o OpenRouter mostrava em horário de pico. Fora do horário, o card mostrava o preço cheio.

**Efeito.** Para os posts agendados fora do horário de pico, o print contradizia a copy ("custo de centavos por milhão de tokens") com o preço cheio.

**Correção.** Empilhar cabeçalho com a tabela de providers no print, em vez de capturar o card isolado. Assim, o print mostra a tabela de preços completa, que é estável.

**Onde mexer.** No template do slide 6 (capítulo 5), pedir que o print seja sempre a tabela de preços, não o card individual.

### Erro 5: Contexto de 1.048.576 dividido por mil

**Erro.** O número de tokens de contexto (1.048.576) era formatado como "1049k tokens" (divisão por 1.000).

**Efeito.** O leitor familiar com o número real percebia que o "k" estava errado. Parecia descuido de quem não entende o produto.

**Correção.** Formatar contexto como múltiplo de 1.048.576 (que é 2^20, a unidade binária), não de 1.000 (unidade decimal). 1.048.576 vira "1M tokens"; 131.072 vira "128k tokens".

**Onde mexer.** No prompt do capítulo 4, especificar a regra de formatação de números com unidades binárias. E adicionar no checklist final (capítulo 99) a conferência manual de 3 números por peça.

### Erro 6: Catálogo de prints não atualizado após a captura em lote

**Erro.** O catálogo `prints-catalog.json` dizia que 3 itens estavam com prints completos, mas a pasta `saida/` tinha os 1.672 prints.

**Efeito.** O renderizador (capítulo 7) confiava no catálogo e renderizava 3 peças sem os prints, mesmo com os arquivos no disco. As 3 peças saíram sem prova visual.

**Correção.** O catálogo de prints deve ser regenerado ao fim de cada captura em lote (ou apagado, deixando o renderizador ler diretamente da pasta). A fonte da verdade é a pasta, não o catálogo.

**Onde mexer.** No prompt do capítulo 6, escrever: "O catálogo de prints é gerado pela própria captura, no fim do script. Não atualize manualmente. O renderizador lê da pasta."

### Erro 7: Cor de texto escurecida sobre fundo escuro nos pills

**Erro.** Os pills (caixas pequenas com palavras-chave, usadas no slide 8 como destaque do CTA) tinham o texto em tom escuro para ter contraste com o fundo claro do pill. No tema escuro, o pill continuava claro, mas o texto também, e o pill ficava ilegível.

**Efeito.** Os 209 slides escuros tinham o CTA ilegível. O leitor passava o olho pelo slide 8 sem entender o que tinha que fazer.

**Correção.** A cor de texto dentro do pill deve ser a cor de acento pura (`#16A34A` no template Academia), não uma variação escurecida. A regra da série OpenRouter: "Use o acento puro como cor de texto em qualquer lugar onde o pill precisa ser legível."

**Onde mexer.** No template CSS do prompt do capítulo 7, escrever: "Pills com classe `.pill` devem usar `color: var(--acc)` (acento puro), nunca uma variação escurecida do acento."

## Como usar esta lista na sua série

Aplique os 7 erros como checklist de validação das suas primeiras 5 peças geradas (não das 418, e só das 5 primeiras). O fluxo é:

1. Gere os 3 itens-piloto do capítulo 7.
2. Para cada um dos 24 PNGs (3 itens × 8 slides), passe os olhos pela tabela de erros acima.
3. Algum dos 7 defeitos aparece na sua peça? Se sim, anote qual e onde.
4. Cole a lista dos defeitos encontrados no prompt abaixo.
5. A IA ajusta o prompt-mestre ou o template para eliminar a classe de erro (não o item específico, e a classe inteira).
6. Regere os 3 itens-piloto. Repita até nenhum dos 7 defeitos aparecer.

## Material necessário

- Os 24 PNGs dos 3 itens-piloto (gerados no capítulo 7).
- Acesso ao ChatGPT, Claude ou Gemini.

## Passo a passo

1. Abra os 24 PNGs no visualizador de imagens.
2. Para cada slide, passe pela tabela acima.
3. Anote, em uma frase por defeito: "Erro X aparece no slide Y do item Z, no formato [descrição]."
4. Abra o ChatGPT.
5. Cole o prompt abaixo com a lista preenchida.
6. A IA vai ajustar o prompt-mestre para eliminar a classe de erro.
7. Regere os 3 itens-piloto e repita até os 7 defeitos não aparecerem.

## Prompt para colar na IA

```
Você é meu engenheiro de qualidade de carrosséis.

Gerei 3 itens-piloto da minha série (24 PNGs no total). Ao
conferir os PNGs contra os 7 defeitos conhecidos da série
"Carrosséis Infinitos com Qualquer IA", encontrei:

  Erro [N] - [nome do erro]: aparece no slide [N] do item
  [N], no formato [descrição breve].
  Erro [N] - [nome do erro]: ...
  (copiar e colar aqui o que você anotou)

Os 7 defeitos conhecidos são:
  1. Repetição de cena no slide 3 (pool < 8)
  2. Asset posicionado com bottom negativo
  3. Print de preço não bate com o tier
  4. Card promocional fora de pico
  5. Formatação de número binário errado
  6. Catálogo de prints desatualizado
  7. Pill de CTA ilegível no tema escuro

Para cada defeito encontrado:
  - Identifique a causa raiz (qual parte do template, do
    prompt-mestre ou do script).
  - Reescreva APENAS a parte com defeito (não o template
    inteiro, não o prompt inteiro). Mudança mínima, máxima
    eficácia.
  - Me dê o trecho de código ou prompt antes/depois.

Termine com a lista de mudanças que você fez e por que
essas mudanças eliminam a CLASSE de erro (não só o item
específico).
```

## O que muda amanhã de manhã

Você vai abrir a pasta `04-pngs/` e ver os 3 itens-piloto regenerados, sem nenhum dos 7 defeitos. Amanhã, quando gerar o lote inteiro, esses 7 defeitos estão eliminados por construção (não por sorte). A próxima série que você abrir não paga por estes defeitos de novo, e cada defeito novo que aparecer vira uma linha nova nesta tabela, e a tabela cresce com a sua experiência, não com a série alheia.
