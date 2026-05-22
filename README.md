# YOLO Object Detection DIO

Projeto de detecção de objetos com YOLOv8, criado para entrega na DIO. A proposta é demonstrar um fluxo funcional de visão computacional usando Google Colab, modelo pré-treinado, inferência em imagem e documentação do caminho para transfer learning com classes customizadas.

O projeto não afirma que um modelo foi treinado do zero. Ele usa YOLOv8 pré-treinado para a demonstração prática e explica como preparar uma base anotada para treinar novas classes.

## Objetivo

Construir um projeto completo e organizado para:

- executar detecção de objetos com YOLOv8;
- usar um modelo pré-treinado da biblioteca Ultralytics;
- salvar uma imagem final com bounding boxes;
- documentar como criar uma base de dados anotada;
- explicar como aplicar transfer learning com pelo menos duas classes detectáveis.

As classes usadas como referência no projeto incluem `person`, `car`, `dog` e `bicycle`, que fazem parte do COCO Dataset e já são reconhecidas pelo modelo pré-treinado.

## O que é YOLO

YOLO significa You Only Look Once. É uma família de modelos de visão computacional usada para detectar objetos em imagens e vídeos.

A ideia principal é analisar a imagem em uma única passagem pela rede neural e retornar, ao mesmo tempo:

- quais objetos aparecem na imagem;
- onde eles estão;
- qual a confiança da predição.

Neste projeto foi usado o YOLOv8, por ser simples de instalar, bem documentado e fácil de executar no Google Colab.

## Classificação, detecção e segmentação

Classificação responde qual é o principal objeto ou categoria de uma imagem. Por exemplo: "esta imagem contém um cachorro".

Detecção de objetos identifica vários objetos e informa a posição de cada um por meio de caixas delimitadoras. Por exemplo: "há uma pessoa à esquerda, um carro ao fundo e uma bicicleta no centro".

Segmentação vai além da caixa. Ela marca os pixels que pertencem a cada objeto, criando uma máscara mais precisa.

Este projeto trabalha com detecção de objetos.

## O que é bounding box

Bounding box é a caixa desenhada ao redor de um objeto detectado. Ela indica a localização aproximada do objeto dentro da imagem.

Em uma saída típica de YOLO, cada bounding box vem acompanhada de:

- nome da classe;
- confiança da detecção;
- coordenadas da caixa.

## O que é Labelme

Labelme é uma ferramenta usada para rotular imagens. Com ela, é possível desenhar caixas ou polígonos ao redor dos objetos e salvar as anotações.

Essas anotações podem ser convertidas para o formato YOLO e usadas no treinamento de um modelo customizado.

## O que é COCO Dataset

COCO é uma base pública muito usada em visão computacional. Ela contém imagens anotadas com várias classes do mundo real, como pessoas, carros, cachorros e bicicletas.

O modelo `yolov8n.pt` usado neste projeto já foi treinado com classes do COCO. Por isso ele consegue detectar vários objetos sem a necessidade de treinamento adicional.

## Como funciona transfer learning

Transfer learning é o reaproveitamento de um modelo já treinado em uma grande base de dados para resolver um novo problema.

Em vez de começar do zero, usamos pesos pré-treinados como ponto de partida. Depois, treinamos o modelo com uma base menor e específica, por exemplo:

- `dog`
- `bicycle`

Esse processo costuma reduzir o tempo de treinamento e melhorar os resultados quando a base customizada não é muito grande.

## Estrutura do projeto

```text
yolo-object-detection-dio/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── yolo_object_detection_colab.ipynb
├── src/
│   └── detect.py
├── images/
│   ├── input/
│   ├── output/
│   └── README.md
├── dataset/
│   └── README.md
└── docs/
    └── entrega_dio.md
```

## Como executar no Google Colab

1. Abra o arquivo `notebooks/yolo_object_detection_colab.ipynb` no Google Colab.
2. Execute as células em ordem.
3. O notebook instala o Ultralytics, carrega o modelo `yolov8n.pt`, baixa uma imagem de exemplo e executa a inferência.
4. A imagem final com bounding boxes é salva em:

```text
images/output/yolo_result.jpg
```

O notebook também mostra o resultado visual dentro do próprio Colab.

## Como executar localmente

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Coloque uma imagem em:

```text
images/input/
```

Execute:

```bash
python src/detect.py
```

O resultado será salvo em:

```text
images/output/
```

## Resultados esperados

Ao executar o notebook ou o script local, o modelo deve gerar uma imagem com caixas ao redor dos objetos detectados.

Exemplo de arquivo esperado:

```text
images/output/yolo_result.jpg
```

ou, no script local:

```text
images/output/nome_da_imagem_detected.jpg
```

## Prints e imagens de resultado

Para gerar prints para a entrega:

1. execute todas as células do notebook no Colab;
2. abra a imagem gerada em `images/output/yolo_result.jpg`;
3. tire um print da célula de visualização do resultado;
4. opcionalmente, salve também um print da execução mostrando o caminho do arquivo gerado.

Como o resultado depende da imagem usada e da confiança do modelo, este repositório não inventa métricas ou resultados fixos.

## Dataset customizado

Para treinar com classes próprias, a base precisa estar no formato YOLO:

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

O arquivo `data.yaml` informa onde estão as imagens e quais são as classes.

Exemplo:

```yaml
path: /content/yolo-object-detection-dio/dataset
train: images/train
val: images/val

names:
  0: dog
  1: bicycle
```

Com a base pronta, o treinamento por transfer learning pode ser iniciado com:

```bash
yolo detect train model=yolov8n.pt data=dataset/data.yaml epochs=30 imgsz=640
```

## Aprendizados

Este projeto reforça conceitos importantes de visão computacional:

- diferença entre classificação, detecção e segmentação;
- uso de modelos YOLO pré-treinados;
- inferência em imagens;
- interpretação de bounding boxes;
- organização de datasets para detecção;
- ideia prática de transfer learning.

## Melhorias futuras

- adicionar uma base própria com duas classes reais;
- treinar o modelo no Colab com `data.yaml`;
- comparar métricas como precision, recall e mAP;
- testar diferentes versões do YOLOv8;
- incluir inferência em vídeo.

## Conclusão

O projeto demonstra um fluxo funcional de detecção de objetos com YOLOv8 e documenta o caminho para criação de uma base anotada e treinamento por transfer learning.

Ele está pronto para ser executado no Google Colab, permite teste local com imagens próprias e mantém a documentação clara sobre o que foi implementado.

## Comandos git

```bash
git init
git add .
git commit -m "feat: add yolo object detection project"
git branch -M main
git remote add origin https://github.com/fezleep/yolo-object-detection-dio.git
git push -u origin main
```
