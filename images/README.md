# Pasta de imagens

Esta pasta separa as imagens usadas para teste e os resultados gerados pelo modelo.

## `input/`

Coloque aqui as imagens que você quer testar localmente com o script `src/detect.py`.

Exemplo:

```text
images/input/minha_imagem.jpg
```

Formatos comuns como `.jpg`, `.jpeg` e `.png` funcionam bem.

## `output/`

O script salva nesta pasta as imagens processadas com as bounding boxes desenhadas.

Exemplo:

```text
images/output/minha_imagem_detected.jpg
```

No Google Colab, o notebook também salva o resultado final dentro de `images/output`.
