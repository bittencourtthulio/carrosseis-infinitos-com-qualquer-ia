# Prompt 02: A fábrica em cinco estágios

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Implemente a estrutura da minha fábrica nesta pasta.
Use Claude Code ou OpenCode para criar os arquivos.
Não devolva apenas uma sugestão de organização.

Tema: [TEMA]
Público: [PÚBLICO]
Objetivo do conteúdo: [OBJETIVO]
Dados que já tenho: [ARQUIVO OU FONTE]

Leia AMBIENTE.md e DECISAO.md, se existirem.
Crie PROJETO.md com objetivo, entradas, saídas
e critério de conclusão de cada uma das etapas:
catálogo, texto, provas, imagens e publicação.

Prepare as pastas 01-catalogo, 02-copy, 03-prints,
04-pngs/assets, 05-publicados, scripts e logs.
Adote CSV local para o catálogo e JSON para os textos.
Registre os nomes de arquivo que cada etapa vai ler.
Não transforme os programas em clientes de API de IA.
A produção deverá usar regras e arquivos locais.

Crie um README.md para leigo, explicando onde olhar
depois de cada etapa. Liste dados que ainda faltam.
Não preencha fatos reais com exemplos inventados.
Se precisar exemplificar a estrutura, identifique
os dados como fictícios e separe-os do catálogo real.

Confira no disco os diretórios e documentos criados.
Termine com os caminhos e a próxima ação concreta.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 02.
- Seção do livro: Prompt para colar no agente.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
