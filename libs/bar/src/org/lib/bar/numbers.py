import json

import numpy as np

from org.lib.bar.utils import ASSETS_PATH


def get_fibonacci() -> np.ndarray:
    fibonacci_json_path = ASSETS_PATH / "fibonacci.json"
    with open(fibonacci_json_path) as f:
        fibonacci = json.load(f)
    np_fibonacci = np.array(fibonacci)
    return np_fibonacci


def get_primes() -> np.ndarray:
    primes_json_path = ASSETS_PATH / "primes.json"
    with open(primes_json_path) as f:
        primes = json.load(f)
    np_primes = np.array(primes)
    return np_primes
