import string
from typing import Dict, List, Union

import numpy as np
import pandas as pd


def read_csv_matrices(filenames: List[str]) -> Dict[str, pd.DataFrame]:
    matrices: Dict[str, pd.DataFrame] = {}
    for index in range(len(filenames)):
        matrices[_get_character_by_index(index)] = pd.read_csv(filenames[index])

    return matrices


# TODO PROBABLY DELETE THIS
def read_matrices(filenames: List[str]) -> Dict[str, np.ndarray]:
    matrices: Dict[str, np.ndarray] = {}
    for index in range(len(filenames)):
        matrices[_get_character_by_index(index)] = np.loadtxt(filenames[index])

    return matrices


def print_matrices(matrices: Union[Dict[str, np.ndarray], Dict[str, pd.DataFrame]]) -> None:
    print("\nMatrices from files")
    for matrix in matrices:
        print("\n" + matrix)
        print(matrices[matrix])


def _get_character_by_index(index: int) -> str:
    return string.ascii_uppercase[index % len(string.ascii_uppercase)]
