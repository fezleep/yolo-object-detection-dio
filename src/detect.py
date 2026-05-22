from pathlib import Path

from ultralytics import YOLO


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = PROJECT_ROOT / "images" / "input"
OUTPUT_DIR = PROJECT_ROOT / "images" / "output"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def find_first_image() -> Path | None:
    images = sorted(
        path for path in INPUT_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )
    return images[0] if images else None


def main() -> None:
    print("Iniciando detecção com YOLOv8...")

    if not INPUT_DIR.exists():
        print(f"Pasta de entrada não encontrada: {INPUT_DIR}")
        return

    image_path = find_first_image()
    if image_path is None:
        print("Nenhuma imagem encontrada em images/input.")
        print("Adicione uma imagem .jpg, .jpeg, .png, .bmp ou .webp e execute novamente.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"{image_path.stem}_detected{image_path.suffix}"

    print(f"Imagem de entrada: {image_path}")
    print("Carregando modelo pré-treinado yolov8n.pt...")
    model = YOLO("yolov8n.pt")

    print("Executando inferência...")
    results = model.predict(
        source=str(image_path),
        conf=0.25,
        save=False,
        verbose=False,
    )

    annotated_image = results[0].plot()

    import cv2

    cv2.imwrite(str(output_path), annotated_image)

    boxes_count = len(results[0].boxes)
    print(f"Objetos detectados: {boxes_count}")
    print(f"Resultado salvo em: {output_path}")


if __name__ == "__main__":
    main()
