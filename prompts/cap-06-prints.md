# Prompt — Capítulo 6 · Captura de prints em escala

**Quando usar:** depois de validar o catálogo do capítulo 3, para escrever o script de captura que baixa os 4 prints de cada item.

**Onde é citado no livro:** capítulo 6, seção "Prompt para colar na IA".

---

## O prompt

```
Você é meu engenheiro de captura de imagens em escala.

Preciso capturar 4 prints por item para uma série de [N, ex:
418] carrosséis. Cada item tem 4 prints:

  tela.png (tela principal do produto ou serviço)
  funcionalidade.png (funcionalidade em uso)
  preco.png (página de preço oficial)
  benchmark.png (número ou prova social)

Minha planilha de catálogo está em
[URL_DO_GOOGLE_SHEETS] e tem as colunas [LISTA]. A coluna
[NOME_DA_COLUNA_DE_URL, ex: url_oficial] tem a URL principal
de cada item.

A cadeia de URLs alternativas para cada print é:
  Tela principal: [URL_PRINCIPAL] → [URL_ALTERNATIVA_1] →
  [URL_ALTERNATIVA_2]
  Funcionalidade: [URL_PRINCIPAL] → [URL_ALTERNATIVA_1]
  Preço: [URL_PRINCIPAL] → [URL_ALTERNATIVA_1]
  Benchmark: [URL_PRINCIPAL] → [URL_ALTERNATIVA_1]

Me escreva um script Python que:

  1. Lê a planilha do Google Sheets (use a biblioteca gspread
     ou similar).
  2. Para cada item, tenta cada URL da cadeia, na ordem, com
     uma chamada HEAD antes de abrir a página.
  3. Se a URL responde 200, abre a página em browser headless
     (use Playwright).
  4. Captura o conteúdo central, com margem de [N, ex: 100]
     pixels em cada lado.
  5. Salva em pasta local no formato:
     [ID_DO_ITEM]/[FUNCAO_DO_PRINT].png
     Exemplo: 001-alpha-3-5/tela.png
  6. Atualiza a planilha catálogo com o status de cada print
     (capturado / faltando / URL morta).

Termine com:
  - Lista de bibliotecas Python que o script usa.
  - Como rodar no Google Colab (sem instalar nada).
  - Como rodar o modo recheck (varredura que apaga prints
    cuja URL morreu).
```

## Como rodar no Google Colab

1. Abra `colab.research.google.com`.
2. Crie um notebook novo.
3. Cole o script na primeira célula.
4. Instale as bibliotecas na segunda célula:
   ```python
   !pip install gspread playwright pillow
   !playwright install chromium
   ```
5. Autorize o acesso ao Google Sheets na terceira célula:
   ```python
   from google.colab import auth
   auth.authenticate_user()
   ```
6. Rode o script na quarta célula.

## Modo recheck (semanal)

Adicione ao final do script:

```python
def recheck(planilha_url, pasta_raiz):
    """Apaga prints cuja URL morreu."""
    df = ler_planilha(planilha_url)
    for _, item in df.iterrows():
        for funcao in ['tela', 'funcionalidade', 'preco', 'benchmark']:
            url = item.get(f'url_{funcao}')
            if not url:
                continue
            if HEAD(url).status_code != 200:
                arquivo = f"{pasta_raiz}/{item['id']}/{funcao}.png"
                if os.path.exists(arquivo):
                    os.remove(arquivo)
                    print(f"Apagado: {arquivo}")
```

Rode semanalmente (sexta à noite, por exemplo).

## O que conferir depois

- O script tenta cada URL da cadeia antes de desistir?
- O script faz HEAD antes de abrir o browser (não desperdiça tempo)?
- O script salva no formato `[id]/[funcao].png`?
- O script atualiza a planilha catálogo com o status?
- O modo recheck está implementado?

## Saída esperada

Script Python funcional para Google Colab + lista de bibliotecas + instruções de recheck. Cole no Colab, rode, e a pasta `03-prints/` se preenche sozinha em minutos.
