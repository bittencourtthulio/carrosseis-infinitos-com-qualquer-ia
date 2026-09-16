# Prompt 08: Automação em massa

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Implemente o pacote de publicação em Python local.
Leia 05-publicados/REGRAS.md e a amostra aprovada,
02-copy/carrosseis.json e logs/renderizacao.json.

Crie scripts/preparar_publicacao.py e execute-o.
Reutilize textos e regras; não chame modelos de IA
para escrever mensagens item por item.
Selecione somente itens com imagens válidas.
Grave o pacote em 05-publicados/pacote/,
com PNGs ou referências locais, legenda e destino.
Crie um manifesto com estado e arquivos de cada item.
Uma retomada não deve duplicar o que já foi preparado.

Se houver ferramenta de publicação já conectada,
confira sua documentação e implemente o adaptador
compatível. Registre o ID retornado pela ferramenta.
Teste com uma peça antes de publicar o lote.
Se a integração estiver ausente, entregue o pacote
local e um guia dos passos de conexão ainda necessários.

Execute a validação dos arquivos e links do pacote.
Mostre quantos itens estão prontos, bloqueados,
agendados ou publicados, conforme evidência real.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 08.
- Seção do livro: Prompt para colar no agente: implementar a preparação em lote.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
