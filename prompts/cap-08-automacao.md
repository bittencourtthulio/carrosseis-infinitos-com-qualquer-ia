# Prompt 08: Bloco de automação

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Trabalhe nos arquivos locais desta fábrica.
Leia PROJETO.md e 02-copy/carrosseis.json.
Minha chamada para ação é: [AÇÃO DO LEITOR]
O destino real é: [LINK]
A ferramenta de publicação é: [NOME OU NÃO DEFINIDA]

Crie 05-publicados/REGRAS.md com o próximo passo,
a legenda-base e, se aplicável, a regra de comentário
e a mensagem de DM. Use campos de personalização
somente quando a ferramenta escolhida os suportar.

Crie uma amostra em 05-publicados/amostra.json
para até três itens, reutilizando os textos aprovados.
Confira alinhamento com o último slide e o destino.
Não invente URL, credencial ou recurso da ferramenta.

Separe claramente: arquivos preparados, integração
conectada, teste realizado e publicação confirmada.
Se faltar acesso, mostre a ação que depende de mim.
Não diga que enviou uma DM só porque salvou o JSON.
Mostre os arquivos criados e a amostra para revisão.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 08.
- Seção do livro: Prompt para colar no agente: preparar as regras.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
