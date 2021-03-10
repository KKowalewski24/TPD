from typing import Union

import numpy as np

from module.Record import Record


# Max Min - Wald
def maxi_min_criteria(matrix: np.ndarray) -> Record:
    min_rows: Union[np.number, np.ndarray] = matrix.min(axis=1)
    print("min_rows")
    print(min_rows)
    return Record(int(min_rows.argmax()), float(min_rows.max()))


# Mini Max
def mini_max_criteria(matrix: np.ndarray) -> Record:
    max_rows: Union[np.number, np.ndarray] = matrix.max(axis=1)
    print("max_rows")
    print(max_rows)
    return Record(int(max_rows.argmin()), float(max_rows.min()))


# Max Max
def max_max_criteria(matrix: np.ndarray) -> Record:
    max_rows: Union[np.number, np.ndarray] = matrix.max(axis=1)
    print("max_rows")
    print(max_rows)
    return Record(int(max_rows.argmax()), float(max_rows.max()))


# Hurwicz
def hurwicz_criteria() -> None:
    pass


# Bayes Laplace
def bayes_laplace_criteria() -> None:
    pass


# Savege
def savage_criteria() -> None:
    pass
