from typing import Any, List, Union

import numpy as np

from module.Record import Record


# Minimaks użyteczności - maksymalizuje najmniejszą możliwą użyteczność
def maxi_min_criteria(matrix: np.ndarray, debug_mode: bool = False) -> Record:
    min_rows: Union[np.number, np.ndarray] = matrix.min(axis=1)
    if debug_mode:
        print("min_rows")
        print(min_rows)
    return Record(int(min_rows.argmax()), float(min_rows.max()))


# Max Max - kryterium optymistyczne
def max_max_criteria(matrix: np.ndarray, debug_mode: bool = False) -> Record:
    max_rows: Union[np.number, np.ndarray] = matrix.max(axis=1)
    if debug_mode:
        print("max_rows")
        print(max_rows)
    return Record(int(max_rows.argmax()), float(max_rows.max()))


# Hurwicz
def hurwicz_criteria(matrix: np.ndarray, factor: float,
                     debug_mode: bool = False) -> Record:
    if factor > 1:
        raise Exception("factor cannot be greater than 1!")

    factor_complement: float = 1 - factor
    min_rows: Union[np.number, np.ndarray] = matrix.min(axis=1)
    max_rows: Union[np.number, np.ndarray] = matrix.max(axis=1)

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

    summed_rows: Union[np.number[Any], np.ndarray] = np.array(
        [min_rows, max_rows]
    ).sum(axis=0)

    if debug_mode:
        print("summed_rows")
        print(summed_rows)

    return Record(int(summed_rows.argmax()), float(summed_rows.max()))


# Bayes Laplace
def bayes_laplace_criteria(matrix: np.ndarray, probabilities: List[float],
                           debug_mode: bool = False) -> Record:
    columns_number: int = matrix.shape[1]
    if columns_number != len(probabilities):
        raise Exception(
            "Number of probabilities must equal to number of column in matrix")

    columns_multiplied_summed: Union[np.number[Any], np.ndarray] = np.array(
        matrix * probabilities
    ).sum(axis=1)

    if debug_mode:
        print(columns_multiplied_summed)

    return Record(
        int(columns_multiplied_summed.argmax()),
        float(columns_multiplied_summed.max())
    )


# Savage - jest błąd w wykładzie - strona 39 - [zbożę 4, normalne] - powinno byc 5 a nie 3
def savage_criteria(matrix: np.ndarray, debug_mode: bool = False) -> Record:
    matrix_transposed: List[Any] = matrix.transpose().tolist()
    max_column_values: Union[np.number, np.ndarray] = matrix.max(axis=0)

    if debug_mode:
        print(matrix_transposed)
        print(max_column_values)

    relative_losses_matrix: List[Any] = []
    for row_index in range(len(matrix_transposed)):
        relative_losses_matrix.append([])
        for item_index in range(len(matrix_transposed[row_index])):
            relative_losses_matrix[row_index].append(abs(
                matrix_transposed[row_index][item_index] - max_column_values[row_index]
            ))

    max_relative_losses_matrix: Union[np.number, np.ndarray] = np.array(
        relative_losses_matrix
    ).max(axis=0)

    if debug_mode:
        print(relative_losses_matrix)
        print(max_relative_losses_matrix)

    return Record(
        int(max_relative_losses_matrix.argmin()),
        float(max_relative_losses_matrix.min())
    )
