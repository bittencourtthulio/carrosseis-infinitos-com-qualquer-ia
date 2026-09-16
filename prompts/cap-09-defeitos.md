# Prompt 09: Validação dos defeitos

Material do livro **Carrosséis Infinitos com Qualquer IA: Praticamente Sem Gastar Tokens**.

## Onde usar

Cole este prompt em: Claude Code ou OpenCode, na pasta local da fábrica. Substitua os campos entre colchetes por seus dados.
A sessão precisa ter ferramentas para editar arquivos e executar comandos. Um chat comum sem acesso à máquina não consegue cumprir a etapa local.

## Prompt completo

```
Você é meu engenheiro de qualidade de carrosséis.
Atue como agente local no Claude Code ou OpenCode.
Leia os arquivos, faça as correções e execute os scripts.
Não peça para eu aplicar trechos de código manualmente.

Gerei 3 itens-piloto da minha série (24 PNGs no total). Ao
conferir os PNGs contra os 7 defeitos conhecidos da série
"Carrosséis Infinitos com Qualquer IA", encontrei:

  Erro [N] - [nome do erro]: aparece no slide [N] do item
  [N], no formato [descrição breve].
  Erro [N] - [nome do erro]: ...
  (copiar e colar aqui o que você anotou)

Os 7 defeitos conhecidos são:
  1. Repetição de cena no slide 3 (pool < 8)
  2. Asset posicionado com bottom negativo
  3. Print de preço não bate com o tier
  4. Card promocional fora de pico
  5. Formatação de número binário errado
  6. Catálogo de prints desatualizado
  7. Pill de CTA ilegível no tema escuro

Para cada defeito encontrado:
  - Identifique a causa raiz (qual parte do template, do
    prompt-mestre ou do script).
  - Reescreva APENAS a parte com defeito (não o template
    inteiro, não o prompt inteiro). Mudança mínima, máxima
    eficácia.
  - Edite os arquivos locais responsáveis pelo defeito.
  - Execute novamente os itens afetados na .venv.
  - Confira as imagens e registre o teste realizado.

Termine com a lista de mudanças que você fez e por que
essas mudanças eliminam a CLASSE de erro (não só o item
específico).
Salve logs/correcoes.md e abra a galeria atualizada.
Se não conseguir executar, informe o bloqueio real.
Não substitua prova de execução por código sugerido.
```

## Como conferir a entrega

Confira os arquivos na pasta e o relatório da execução. Código escrito na conversa, sem arquivo criado e sem teste, não comprova a implementação.

A preparação e as correções com o agente usam o modelo escolhido. O lote determinístico deve rodar em Python sem chamadas a modelos. Usar o iniciador local evita abrir uma nova conversa apenas para repetir o lote.

## Origem

- Capítulo: 09.
- Seção do livro: Prompt para colar na IA.
- Revisão: execução local com Claude Code ou OpenCode.

Todos os direitos reservados a Thulio Bittencourt. Repositório sem licença aberta.
