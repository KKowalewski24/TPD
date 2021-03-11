from typing import Any, Union

import numpy as np

from module.Record import Record


# Minimaks użyteczności - maksymalizuje najmniejszą możliwą użyteczność
def maxi_min_criteria(matrix: np.ndarray) -> Record:
    min_rows: Union[np.number, np.ndarray] = matrix.min(axis=1)
    print("min_rows")
    print(min_rows)
    return Record(int(min_rows.argmax()), float(min_rows.max()))


# Minimaks zawodu - minimaluzuje największy możliwy zawód
def mini_max_criteria(matrix: np.ndarray) -> Record:
    max_rows: Union[np.number, np.ndarray] = matrix.max(axis=1)
    print("max_rows")
    print(max_rows)
    return Record(int(max_rows.argmin()), float(max_rows.min()))


# Max Max - kryterium optymistyczne
def max_max_criteria(matrix: np.ndarray) -> Record:
    max_rows: Union[np.number, np.ndarray] = matrix.max(axis=1)
    print("max_rows")
    print(max_rows)
    return Record(int(max_rows.argmax()), float(max_rows.max()))


# Hurwicz
def hurwicz_criteria(matrix: np.ndarray, factor: float) -> Record:
    if factor > 1:
        raise Exception("factor cannot be greater than 1!")

    factor_complement: float = 1 - factor
    min_rows: Union[np.number, np.ndarray] = matrix.min(axis=1)
    max_rows: Union[np.number, np.ndarray] = matrix.max(axis=1)

    min_rows = min_rows * factor
    max_rows = max_rows * factor_complement

    summed_rows: Union[np.number[Any], np.ndarray] = np.array(
        [min_rows, max_rows]
    ).sum(axis=0)

    return Record(int(summed_rows.argmax()), float(summed_rows.max()))


# Bayes Laplace
def bayes_laplace_criteria(matrix: np.ndarray) -> Record:
    return Record(1, 1)


# Savege
def savage_criteria(matrix: np.ndarray) -> Record:
    return Record(1, 1)
