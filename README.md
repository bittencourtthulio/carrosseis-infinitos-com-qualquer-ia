# Carrosséis Infinitos com Qualquer IA

## Prompts para construir a fábrica no seu computador

Use **Claude Code ou OpenCode** com a pasta local do projeto aberta.
O agente cria arquivos, prepara Python e dependências, executa a amostra
e corrige erros. Os prompts não pedem apenas código para copiar.

Comece pela preparação do ambiente. O OpenCode pode usar o provedor e o
modelo que você escolher, desde que a combinação suporte ferramentas de
edição e execução. No Claude Code, use os modelos disponíveis na ferramenta.

| Capítulo | Prompt |
|---|---|
| 00 | [Prepare o ambiente local](prompts/cap-00-ambiente-local.md) |
| 01 | [A armadilha do token na peça](prompts/cap-01-armadilha.md) |
| 02 | [A fábrica em cinco estágios](prompts/cap-02-cinco-estagios.md) |
| 03 | [Estruture o catálogo](prompts/cap-03-catalogo.md) |
| 04 | [Teses por combinação](prompts/cap-04-teses.md) |
| 04 | [Pools de variações](prompts/cap-04-pools.md) |
| 05 | [Anatomia dos slides](prompts/cap-05-anatomia.md) |
| 05 | [Assets visuais](prompts/cap-05-assets.md) |
| 06 | [Captura de prints](prompts/cap-06-prints.md) |
| 07 | [Renderizador em lote](prompts/cap-07-renderizador.md) |
| 08 | [Bloco de automação](prompts/cap-08-automacao.md) |
| 08 | [Automação em massa](prompts/cap-08-automacao-massa.md) |
| 09 | [Validação dos defeitos](prompts/cap-09-defeitos.md) |
| 10 | [Auditoria de prontidão](prompts/cap-10-prontidao.md) |

## A conta dos tokens

A IA participa da construção e das correções. As imagens do template são
geradas e aprovadas na preparação. Depois, o Python reutiliza dados e assets
sem chamar modelos na produção em lote. Pedir ao agente para iniciar o lote
ainda usa uma interação; o iniciador local criado pelo agente evita isso.

## Como usar

1. Abra o primeiro arquivo de prompt.
2. Copie o bloco de texto e preencha os campos entre colchetes.
3. Cole no agente com a pasta da fábrica aberta.
4. Confira os arquivos e o resultado real de execução.
5. Siga os capítulos na ordem, reaproveitando o projeto.

O prompt de imagem pode ser usado numa ferramenta de imagem separada
quando o agente não tiver uma ferramenta desse tipo conectada.

## Licença

Todos os direitos reservados a Thulio Bittencourt. Sem licença aberta.
