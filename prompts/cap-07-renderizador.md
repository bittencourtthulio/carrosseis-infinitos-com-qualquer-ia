# Prompt — Capítulo 7 · Renderizador em lote (Python no Google Colab)

**Quando usar:** depois de ter a copy (capítulo 4), a anatomia (capítulo 5), os assets visuais (capítulo 5) e os prints (capítulo 6), para gerar os 3.344 PNGs (418 itens × 8 slides).

**Onde é citado no livro:** capítulo 7, seção "Prompt para colar na IA".

---

## O prompt

```
Você é meu engenheiro de geração de imagens em lote.

Preciso gerar [N, ex: 418] × 8 = [TOTAL, ex: 3344] PNGs no
formato 1080x1350 (proporção 4:5 do feed do Instagram). Cada
PNG é um slide de um carrossel.

Os 8 slides, por função, são:
  1. gancho
  2. o_que_e (com print)
  3. pratica (com print)
  4. o_que_vender (lista de bullets)
  5. como_cobrar
  6. link (com print do preço)
  7. benchmark (com print do número)
  8. cta (caixa de destaque)

A copy de cada item está na planilha
[URL_DO_GOOGLE_SHEETS_COM_A_COPY], com uma linha por item e
colunas nomeadas:
  - slide_1_texto, slide_1_destaques
  - slide_2_texto, slide_2_destaques, slide_2_print
  - ... (até slide 8)
  - template (claro ou escuro, alternando pelo id)
  - provider_color_hex (cor de destaque do item)

Os assets visuais estão na pasta `04-pngs/assets/`:
  - capa-serie.png (1080x1350)
  - icone-tier-free.png, icone-tier-barato.png,
    icone-tier-medio.png, icone-tier-caro.png
  - moldura-print.png
  - detalhe-marca.png

O template visual tem dois temas (claro e escuro), com
variáveis CSS equivalentes a:
  Claro:  --bg #F5F1E9, --txt #1B1714, --muted #6B6358,
          --acc #16A34A, --hl #15803D
  Escuro: --bg #141210, --txt #F1EBE1, --muted #A69D8F,
          --acc #16A34A, --hl #22C55E

Me escreva um script Python que:

  1. Lê a planilha de copy via gspread.
  2. Para cada item da série:
     a. Monta o HTML dos 8 slides, com base na função de cada
        slide e nos assets da pasta.
     b. Aplica o tema claro ou escuro conforme o campo
        `template` da planilha.
     c. Aplica a cor de destaque do item no campo --acc, com
        ajuste automático se o contraste com --bg for
        menor que 3:1 (clareia até 3:1, sem trocar o matiz).
     d. Abre o HTML no Chromium via Playwright em modo
        headless.
     e. Mede a altura real do slide com JavaScript injetado:
          const bad = [];
          if (slide.scrollHeight > 1350 + 1) bad.push('estourou');
          ... (outras checagens que você considerar)
     f. Se estourou, reduz fator k em 4% e remonta (até 14
        vezes).
     g. Se sobrou espaço (>80px), aumenta k em 4% (até 1.25).
     h. Salva screenshot do slide em PNG, no caminho
        `04-pngs/[ID_DO_ITEM]/slide_[N].png`.
  3. Loga cada slide com: id, função, k final, badges de
     estouro.
  4. Aborta com erro se a fonte não carregou
     (document.fonts.ready precisa resolver).
  5. Reutiliza o browser entre itens (não abre Chromium por
     peça).

Termine com:
  - Comando para rodar no Google Colab, célula por célula.
  - Como gerar apenas 3 itens-piloto (para teste).
  - Como ler o log e filtrar slides problemáticos.
```

## Estrutura típica do notebook no Colab

```python
# Célula 1: instalar dependências
!pip install gspread playwright pillow
!playwright install chromium

# Célula 2: autenticar
from google.colab import auth
auth.authenticate_user()

# Célula 3: montar a pasta de assets (copiar do Drive)
from google.colab import drive
drive.mount('/content/drive')
ASSETS = '/content/drive/MyDrive/fabrica-carrosseis/04-pngs/assets/'

# Célula 4: o script que a IA gerou (colar aqui)

# Célula 5: rodar 3 itens-piloto
!python main.py --itens 1,2,3

# Célula 6: rodar o lote inteiro (sem filtro)
!python main.py

# Célula 7: ler o log
!cat log_renderizacao.txt | grep -E "k<0.85|estourou|14 rodadas"
```

## Como ler o log

| Valor de `k` | Significado | Ação |
|---|---|---|
| 1.00 | coube sem ajuste | nenhuma |
| acima de 1.00 | sobrou espaço, texto cresceu | nenhuma |
| 0.85 a 0.96 | texto ou print grande, encolheu sozinho | nenhuma |
| abaixo de 0.85 | copy comprida ou print alto demais | encurtar copy ou recortar print |
| aviso de 14 rodadas | não coube nem encolhendo | encurtar copy |

Filtre por `k < 0.85` ou por aviso. Revise só esses. Em uma série bem desenhada, são menos de 50 slides para revisão humana.

## O que conferir depois

- O script lê a planilha via gspread (não manualmente)?
- O script monta HTML e renderiza com Playwright (não Pillow puro)?
- O loop `k` tem ambos os caminhos (encolher e crescer)?
- O script aborta se a fonte não carregou?
- O log tem `k` por slide?
- O modo "gerar apenas alguns itens" existe?

## Saída esperada

Script Python funcional para Google Colab + instruções de uso + leitura do log. Rode, espere o lote terminar, baixe os PNGs.
