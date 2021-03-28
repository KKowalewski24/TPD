import string
from typing import Dict, List

import numpy as np


def read_matrices(filenames: List[str]) -> Dict[str, np.ndarray]:
    matrices: Dict[str, np.ndarray] = {}
    for index in range(len(filenames)):
        matrices[get_character_by_index(index)] = np.loadtxt(filenames[index])

    return matrices


def get_character_by_index(index: int) -> str:
    return string.ascii_uppercase[index % len(string.ascii_uppercase)]


def print_matrices(matrices: Dict[str, np.ndarray]) -> None:
    print("\nMatrices from files")
    for matrix in matrices:
        print("\n" + matrix)
        print(matrices[matrix])
