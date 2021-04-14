from typing import Dict, List

import pandas as pd


def read_csv_matrices(filenames: List[str]) -> Dict[int, pd.DataFrame]:
    matrices: Dict[int, pd.DataFrame] = {}
    for index in range(len(filenames)):
        matrices[index + 1] = pd.read_csv(filenames[index])

    return matrices
