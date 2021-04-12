from typing import Dict, List, Union

import numpy as np
import pandas as pd


def read_csv_matrices(filenames: List[str]) -> Dict[int, pd.DataFrame]:
    matrices: Dict[int, pd.DataFrame] = {}
    for index in range(len(filenames)):
        matrices[index] = pd.read_csv(filenames[index])

    return matrices


# TODO PROBABLY DELETE THIS
def read_matrices(filenames: List[str]) -> Dict[int, np.ndarray]:
    matrices: Dict[int, np.ndarray] = {}
    for index in range(len(filenames)):
        matrices[index] = np.loadtxt(filenames[index])

    return matrices


def print_matrices(matrices: Union[Dict[int, np.ndarray], Dict[int, pd.DataFrame]]) -> None:
    print("\nMatrices from files")
    for matrix in matrices:
        print("\n" + str(matrix))
        print(matrices[matrix])
