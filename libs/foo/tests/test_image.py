from pathlib import Path

import pytest
from PIL import Image, ImageChops

from org.lib.foo.image import load_image, save_image


@pytest.fixture
def image():
    image_ = Image.new("RGB", (100, 100), color="red")
    return image_


def test_load_image(image: Image.Image, tmp_path: Path) -> None:
    path = tmp_path / "test_image.png"
    image.save(path)

    loaded_image = load_image(path)

    difference = ImageChops.difference(loaded_image, image)
    assert (
        difference.getbbox() is None
    ), "The loaded image differs from the original image"


def test_save_image(image: Image.Image, tmp_path: Path):
    path = tmp_path / "test_image.png"

    save_image(image, path)

    saved_image = Image.open(path)
    difference = ImageChops.difference(saved_image, image)
    assert (
        difference.getbbox() is None
    ), "The saved image differs from the original image"
