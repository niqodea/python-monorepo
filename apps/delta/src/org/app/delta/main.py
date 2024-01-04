import numpy as np

from org.lib.bar import get_primes
from org.lib.foo import load_image

from org.app.delta.utils import ASSETS_PATH


def main() -> None:
    for image_path in ASSETS_PATH.iterdir():
        image = load_image(image_path)

        np_image = np.array(image)

        mean_intensity = int(np_image.mean())

        print(f"Mean intensity of {image_path.name} is {mean_intensity}")

        for prime in get_primes():
            if mean_intensity % prime == 0:
                print(f"Mean intensity {mean_intensity} is divisible by {prime}")
            else:
                print(f"Mean intensity {mean_intensity} is not divisible by {prime}")


if __name__ == "__main__":
    main()
