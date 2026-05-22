# Texto para entrega da DIO

## Descrição curta

Projeto de detecção de objetos com YOLOv8, usando Google Colab, modelo pré-treinado da Ultralytics e documentação do fluxo para criação de base de dados e transfer learning com classes customizadas.

## O que foi implementado

Foi criado um projeto organizado para executar inferência com YOLOv8 em uma imagem de exemplo, gerar bounding boxes e salvar o resultado visual.

Também foi incluído um notebook completo para Google Colab, com explicações sobre YOLO, dataset anotado, transfer learning e comandos comentados para treinamento customizado no formato YOLO.

Além disso, o projeto possui um script local em Python para detectar objetos em imagens colocadas na pasta `images/input` e salvar os resultados em `images/output`.

## Tecnologias usadas

- Python
- Google Colab
- YOLOv8
- Ultralytics
- OpenCV
- Matplotlib

## Como o projeto atende ao desafio

O projeto atende ao desafio porque apresenta o fluxo principal de uma solução de detecção de objetos:

- organização da base de imagens;
- explicação sobre rotulagem;
- uso de classes detectáveis;
- carregamento de modelo YOLO pré-treinado;
- execução de inferência;
- geração de imagem final com bounding boxes;
- documentação do processo de transfer learning.

As classes usadas como referência incluem objetos do COCO Dataset, como `person`, `car`, `dog` e `bicycle`.

## Observação sobre treinamento

Neste projeto, a demonstração prática usa um modelo YOLOv8 pré-treinado. O modelo não foi treinado do zero e não são apresentados resultados falsos de treinamento.

O notebook documenta o caminho para transfer learning com uma base customizada no formato YOLO, usando pelo menos duas classes, como `dog` e `bicycle`. Para executar esse treinamento, é necessário preparar uma base real com imagens e labels correspondentes.
