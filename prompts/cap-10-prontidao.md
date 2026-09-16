# Prompt 10: Auditoria de prontidão

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Estou na pasta local da fábrica já construída.
Uso Claude Code ou OpenCode com ferramentas de execução.
Prepare a próxima série sem refazer o que já funciona.

Tema: [TEMA]
Público: [PÚBLICO]
Objetivo: [OBJETIVO]
Fonte dos novos dados: [ARQUIVO OU URL]

Leia AMBIENTE.md, PROJETO.md, TEMPLATE.md
e COMO-GERAR.md. Inspecione scripts e arquivos.
Crie NOVA-SERIE.md com o que será reutilizado,
o que precisa mudar e quais dados ainda faltam.
Preserve a série anterior em uma versão identificada.

Prepare os diretórios e a importação da nova fonte.
Execute a validação do catálogo e registre pendências.
Atualize o contrato e as regras que eu aprovar.
Não gere fatos, preços ou provas ausentes.

Rode uma amostra com os programas locais existentes.
Se faltar uma decisão editorial, pergunte objetivamente.
Se houver erro técnico, corrija e execute de novo.
Abra a galeria da amostra e mostre os caminhos reais.
Registre em logs/nova-serie.json os testes executados.
Não chame modelos de IA dentro dos geradores do lote.
Informe a condição que falta para liberar a produção.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 10.
- Seção do livro: Prompt para colar no agente: preparar a próxima série.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
