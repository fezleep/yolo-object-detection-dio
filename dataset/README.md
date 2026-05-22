# Dataset

Esta pasta documenta como organizar uma base de dados para treinar ou ajustar um modelo YOLO com classes próprias.

Neste projeto, a inferência usa um modelo YOLOv8 pré-treinado. O treinamento customizado não é executado aqui como resultado final pronto, porque isso exigiria uma base rotulada real. O caminho para fazer transfer learning está documentado no notebook e neste arquivo.

## Como seria uma base rotulada

Uma base para detecção de objetos precisa ter:

- imagens dos objetos que serão detectados;
- anotações indicando a posição de cada objeto;
- uma lista de classes, como `dog` e `bicycle`;
- separação entre treino e validação.

Em detecção, a anotação normalmente é uma bounding box, ou seja, uma caixa que envolve o objeto na imagem.

## Como usar Labelme

O Labelme é uma ferramenta para rotular imagens manualmente.

Fluxo básico:

1. abrir uma imagem no Labelme;
2. desenhar uma caixa ou polígono ao redor do objeto;
3. informar o nome da classe;
4. salvar a anotação;
5. converter as anotações para o formato esperado pelo YOLO, quando necessário.

O Labelme costuma salvar anotações em JSON. Para treinar YOLO, é comum converter essas anotações para `.txt` no formato YOLO.

## Como usar COCO

COCO é um dataset público muito usado em visão computacional. Ele possui imagens anotadas para tarefas como detecção, segmentação e captioning.

O YOLOv8 pré-treinado usado neste projeto já conhece classes do COCO, como:

- `person`
- `car`
- `dog`
- `bicycle`

Por isso ele consegue detectar esses objetos sem treinamento adicional.

## Estrutura esperada para YOLO

Um dataset customizado no formato YOLO pode ser organizado assim:

```text
dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
└── data.yaml
```

Cada imagem deve ter um arquivo `.txt` correspondente na pasta `labels`.

Exemplo:

```text
dataset/images/train/foto_001.jpg
dataset/labels/train/foto_001.txt
```

## Exemplo de anotação YOLO

Uma linha de anotação YOLO segue este formato:

```text
classe x_centro y_centro largura altura
```

Os valores de posição e tamanho são normalizados entre 0 e 1.

Exemplo:

```text
0 0.512 0.438 0.210 0.340
```

## Exemplo de `data.yaml`

```yaml
path: /content/yolo-object-detection-dio/dataset
train: images/train
val: images/val

names:
  0: dog
  1: bicycle
```

Com essa estrutura, o YOLOv8 consegue localizar as imagens, ler os labels e aplicar transfer learning a partir de um modelo pré-treinado.
