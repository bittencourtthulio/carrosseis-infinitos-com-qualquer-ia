# Prompt 06: Captura de prints

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Implemente a captura de provas neste projeto local.
Leia AMBIENTE.md, PROJETO.md, 02-copy/CONTRATO.md
e 02-copy/carrosseis.json.
Use o Python da .venv. Crie e execute os arquivos;
não entregue somente código nesta conversa.

Crie scripts/capturar_prints.py para localizar as
provas exigidas e salvar em 03-prints/[id]/.
Use URLs registradas nos dados e alternativas
que sustentem a mesma afirmação do slide.
Se faltar uma fonte, registre a pendência.
Não invente preço, benchmark ou tela de produto.

Instale as dependências no ambiente do projeto.
Use navegador automatizado para capturar a página.
Não confunda HTTP 200 com prova correta.
Trate login, página de erro e bloqueios como pendências.
Se HEAD falhar, não descarte sem conferir a navegação.
Não substitua uma prova por uma imagem gerada por IA.

Crie 03-prints/inventario.json com ID, slide,
URL, data, caminho e estado de cada captura.
Mantenha o histórico ao revalidar uma fonte.
Não apague uma prova antiga por um erro transitório.

Execute até três itens representativos.
Verifique se os arquivos abrem e têm conteúdo útil.
Monte uma galeria local com fonte e finalidade.
Se ocorrer erro técnico, corrija e execute novamente.
Prepare seleção por IDs, lote e retomada.
Mostre o comando executado, os arquivos gravados
e quais provas precisam da minha conferência.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 06.
- Seção do livro: Prompt para colar no agente.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
