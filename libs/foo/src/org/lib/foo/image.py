from pathlib import Path

from PIL import Image


def load_image(path: Path) -> Image.Image:
    image = Image.open(path)
    return image


def save_image(image: Image.Image, path: Path) -> None:
    image.save(path)
