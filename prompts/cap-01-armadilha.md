# Prompt 01: A armadilha do token na peça

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Você é meu agente local no Claude Code ou OpenCode.
Trabalhe na pasta aberta e leia AMBIENTE.md.
Minha série é sobre [TEMA], para [PÚBLICO].
Eu uso (ou estou prestes a usar) IA para escrever cada
    carrossel
individualmente, peça por peça.

Me explique,
    com UMA analogia de leigo, por que pedir para a IA
escrever cada carrossel individualmente é mais caro
    em token,
mais lento em revisão e
    menos consistente em marca do que gastar
uma sessão maior de tokens para construir o sistema
    que escreve
os carrosséis.

Use linguagem de quem nunca programou. Máximo de 1 página.
Crie DECISAO.md com a explicação e as perguntas abaixo.
Registre o que ainda depende da minha resposta.
Não invente contagens de tokens ou economia garantida.
Mostre o caminho do arquivo realmente criado.
Termine com 3 perguntas para eu identificar se estou
    cometendo
esse erro na minha série atual:

  1. Estou reescrevendo o prompt a cada peça, ou tenho um
     prompt-mestre?
  2. Quando preciso corrigir uma regra de copy,
    eu regenero a
     peça errada ou corrijo o prompt e regenero o lote?
  3. O token que eu já gastei até hoje seria suficiente para
     ter construído o sistema completo?
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 01.
- Seção do livro: Prompt para colar na IA.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
