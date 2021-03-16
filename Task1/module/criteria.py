from typing import List

import numpy as np


# Minimaks użyteczności - maksymalizuje najmniejszą możliwą użyteczność
def maxi_min_criteria(matrix: np.ndarray, debug_mode: bool = False) -> int:
    min_rows = matrix.min(axis=1)
    if debug_mode:
        print("min_rows")
        print(min_rows)
    return int(min_rows.argmax())


# Max Max - kryterium optymistyczne
def max_max_criteria(matrix: np.ndarray, debug_mode: bool = False) -> int:
    max_rows = matrix.max(axis=1)
    if debug_mode:
        print("max_rows")
        print(max_rows)
    return int(max_rows.argmax())


# Hurwicz
def hurwicz_criteria(matrix: np.ndarray, factor: float,
                     debug_mode: bool = False) -> int:
    if factor > 1:
        raise Exception("factor cannot be greater than 1!")

    factor_complement: float = 1 - factor
    min_rows = matrix.min(axis=1)
    max_rows = matrix.max(axis=1)

    if debug_mode:
        print("min_rows")
        print(min_rows)
        print("max_rows")
        print(max_rows)

    min_rows = min_rows * factor
    max_rows = max_rows * factor_complement

    if debug_mode:
        print("min_rows after multiplication by the factor")
        print(min_rows)
        print("max_rows after multiplication by the factor")
        print(max_rows)

    summed_rows = min_rows + max_rows

    if debug_mode:
        print("summed_rows")
        print(summed_rows)

    return int(summed_rows.argmax())


# Bayes Laplace
def bayes_laplace_criteria(matrix: np.ndarray, probabilities: List[float],
                           debug_mode: bool = False) -> int:
    columns_number: int = matrix.shape[1]
    if columns_number != len(probabilities):
        raise Exception(
            "Number of probabilities must equal to number of column in matrix")

    columns_multiplied_summed = np.sum(matrix * probabilities, axis=1)

    if debug_mode:
        print(columns_multiplied_summed)
    return int(columns_multiplied_summed.argmax())


# Savage - jest błąd w wykładzie - strona 39 - [zbożę 4, normalne] - powinno byc 5 a nie 3
def savage_criteria(matrix: np.ndarray, debug_mode: bool = False) -> int:

    relative_losses_matrix = (matrix.max(axis=0) - matrix)
    max_relative_losses_matrix = relative_losses_matrix.max(axis=1)

    if debug_mode:
        print(relative_losses_matrix)
        print(max_relative_losses_matrix)

    return int(max_relative_losses_matrix.argmin())
