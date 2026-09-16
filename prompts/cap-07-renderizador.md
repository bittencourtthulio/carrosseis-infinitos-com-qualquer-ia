# Prompt 07: Renderizador em lote

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Trabalhe na pasta local desta fábrica de carrosséis.
Sou leigo e uso Claude Code ou OpenCode.
Crie os arquivos, execute e confira o resultado.
Não entregue somente código para eu copiar.

Leia AMBIENTE.md, PROJETO.md, TEMPLATE.md,
02-copy/carrosseis.json, 04-pngs/assets e 03-prints.
Identifique o que existe antes de alterar arquivos.
Se faltar uma entrada, informe a pendência concreta.

1. Verifique o Python local e o ambiente .venv.
   Instale nele as dependências necessárias.
   Prepare o navegador usado pelo renderizador.
   Registre as versões e os comandos que executou.
2. Crie scripts/gerar_carrossel.py funcional.
   Leia o JSON local e monte HTML/CSS por slide.
   Use os assets já aprovados; não gere imagens por IA.
   Grave PNGs de 1080 por 1350 pixels em
   04-pngs/[id-do-item]/slide_1.png até slide_8.png.
   Salve a legenda de cada item na mesma pasta.
3. O programa não pode chamar modelos de linguagem
   nem APIs de geração de imagem durante o lote.
   O texto vem do JSON e as imagens vêm dos arquivos.
4. Meça os elementos no navegador antes do PNG.
   Detecte texto cortado, estouro e imagem ausente.
   Ajuste o layout dentro dos limites de TEMPLATE.md.
   Não esconda erros reduzindo a fonte indefinidamente.
   Confirme o carregamento das fontes usadas.
   Use contraste adequado para texto e controles.
5. Implemente --itens para selecionar alguns IDs,
   --lote para gerar todos e --retomar para continuar.
   Retomada deve conferir se dados ou assets mudaram.
   Crie logs/renderizacao.json com estado por slide.
   Registre falhas; não classifique saída inválida
   como pronta para publicação.
6. Execute primeiro até três itens representativos.
   Se houver três itens, confira os 24 PNGs esperados.
   Teste dimensões, abertura dos arquivos e alertas.
   Se falhar, leia o erro, corrija e execute de novo.
   Abra uma galeria HTML local para minha revisão.
7. Crie um iniciador para meu sistema operacional
   que execute o Python de .venv na pasta correta.
   Ele deve permitir amostra, lote e retomada,
   mostrar progresso e guardar o log.
   Teste o comando que esse iniciador vai executar.
   Nenhuma dessas opções deve chamar um modelo de IA.
8. Salve COMO-GERAR.md com o nome do iniciador,
   onde estão os PNGs e como retomar após uma falha.

Mostre os caminhos dos arquivos criados, o comando
executado, a saída real e o resumo da amostra.
Não afirme que executou algo que só escreveu.
Se uma permissão bloquear a ação, explique o passo
necessário para eu liberar e retome a execução.
O lote completo vem depois da revisão da amostra.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 07.
- Seção do livro: Prompt para colar no agente: criar e executar o renderizador local.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
