# Prompt 05: Anatomia dos slides

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Você é meu agente local e diretor de arte desta série.
Leia PROJETO.md e 02-copy/CONTRATO.md.
Crie TEMPLATE.md nesta pasta com a entrega abaixo.
Crie também 04-pngs/assets/BRIEFINGS.md.
Não deixe o resultado somente nesta conversa.

Minha série tem a tese [TESE GERAL, ex: "Cada LLM é uma
ferramenta de receita diferente para software house"] e o
público-alvo [PÚBLICO, ex: donos de software house].

Os 2 eixos de classificação dos itens são:
  Eixo 1: [NOME] (valores: [LISTA])
  Eixo 2: [NOME] (valores: [LISTA])

Aqui está a tabela de teses por combinação:
  Leia 02-copy/teses.md, salvo no capítulo anterior.

Me dê a anatomia fixa dos 8 slides para esta série:

  Slide 1 - gancho:
    Função: ...
    O que carrega: ...
    Tom: ...
    Layout visual sugerido: ...
    Exemplo de copy real para o item "[ITEM EXEMPLO]" na
    combinação (VALOR_1, VALOR_A):
      "..."
      Destaques: [...]

  Slide 2 - o_que_e:
    ... (mesmo formato)

  ... (até slide 8 - cta)

Para cada slide, justifique em 1 frase por que essa função
existe na anatomia. Se algum slide parece redundante com
outro, aponte e sugira a fusão.

Termine com:
  - Lista dos assets visuais que precisam ser gerados para
    esta série (capa, ícones, molduras etc.).
  - Briefing de 1 parágrafo para cada asset, pronto para eu
    colar na IA de imagem.

Registre em TEMPLATE.md os limites de texto,
tamanhos mínimos de fonte e áreas reservadas às imagens.
Confira os arquivos já disponíveis em 04-pngs/assets.
Se houver uma ferramenta de imagem conectada, use-a
para produzir uma amostra e salve o arquivo real.
Se não houver, indique o briefing que devo levar
à IA de imagem e onde salvar o resultado aprovado.
Não trate um briefing escrito como imagem já gerada.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 05.
- Seção do livro: Prompt para colar na IA (anatomia dos 8 slides).
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
