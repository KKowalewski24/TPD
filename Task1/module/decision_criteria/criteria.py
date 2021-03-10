from typing import Union

import numpy as np

from module.Record import Record


# Max Min - Wald
def maxi_min_criteria(matrix: np.ndarray) -> Record:
    sub_result: Union[np.number, np.ndarray] = matrix.min(axis=1)
    return Record(sub_result.argmax().__int__(), sub_result.max().__float__())


# Mini Max
def mini_max_criteria() -> None:
    pass


# Max Max
def max_max_criteria() -> None:
    pass


# Hurwicz
def hurwicz_criteria() -> None:
    pass


# Bayes Laplace
def bayes_laplace_criteria() -> None:
    pass


# Savege
def savage_criteria() -> None:
    pass
