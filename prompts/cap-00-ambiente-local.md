# Prompt 00: Prepare o ambiente local

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Estou usando você no Claude Code ou no OpenCode,
na pasta local da minha fábrica de carrosséis.
Sou leigo. Implemente no computador; não entregue
apenas instruções ou um bloco de código no chat.

1. Identifique sistema operacional, pasta atual,
   permissões disponíveis e ambiente de execução.
   Informe se está no Windows, macOS, Linux ou WSL.
2. Verifique Python, sua versão e o executável usado.
   Se faltar Python, consulte a instalação oficial
   adequada ao sistema e tente instalá-lo com as
   permissões disponíveis. Se precisar de uma ação
   minha, diga exatamente qual e aguarde a conclusão.
   Não declare a instalação concluída sem conferir.
3. Crie um ambiente virtual .venv neste projeto.
   Use o Python desse ambiente nas próximas etapas.
4. Crie as pastas 01-catalogo, 02-copy, 03-prints,
   04-pngs/assets, 05-publicados, scripts e logs.
5. Crie scripts/verificar_ambiente.py e execute-o.
   Ele deve gravar e ler um arquivo de teste local,
   informar a versão do Python e a pasta usada.
   Não faça chamadas a modelos de IA nesse teste.
6. Salve AMBIENTE.md com o que realmente verificou:
   sistema, versão, executável, pastas e pendências.
   Se falhar, corrija e repita o teste quando possível.

No fim, mostre os arquivos criados, o comando que
executou, a saída obtida e o caminho de AMBIENTE.md.
Se você não tiver ferramentas para editar ou executar,
explique como abrir uma sessão local com essas funções.
Não simule execução nem peça para eu montar o script.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 00.
- Seção do livro: Prompt para colar no agente: preparar o ambiente local.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
