from typing import List

import pandas as pd


def read_csv_matrices(filenames: List[str]) -> List[pd.DataFrame]:
    matrices: List[pd.DataFrame] = []
    for filename in filenames:
        matrices.append(pd.read_csv(filename))

    return matrices
