# Prompt 03: Estruture o catálogo

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Prepare o catálogo real desta fábrica na pasta local.
Leia PROJETO.md e AMBIENTE.md.
Minha fonte está em: [ARQUIVO OU URL]

Leia a fonte e proponha as colunas necessárias.
Identifique dois eixos úteis para diferenciar a copy.
Explique a escolha com exemplos dos dados existentes.
Se uma informação não estiver na fonte, não a invente.
Marque-a como pendente e indique o que falta confirmar.

Crie 01-catalogo/catalogo.csv em UTF-8, com IDs
estáveis, fonte, data de coleta e status dos itens.
Guarde a entrada original sem sobrescrevê-la.
Crie 01-catalogo/ESQUEMA.md explicando as colunas.

Crie scripts/validar_catalogo.py e execute-o usando
o Python do projeto. Confira IDs duplicados,
campos obrigatórios vazios, valores inválidos
e categorias que não existem no esquema.
Dados ausentes não podem virar preço zero.

Salve logs/catalogo.json com contagens e pendências.
Mostre uma amostra para eu comparar com a fonte.
Corrija erros de importação e execute novamente.
Não exclua silenciosamente os itens problemáticos.
Mostre o que ficou pronto e o que ainda está bloqueado.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 03.
- Seção do livro: Prompt para colar no agente.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
