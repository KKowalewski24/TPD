from typing import Tuple

import numpy as np


def max_min_by_rows(matrix: np.ndarray) -> Tuple[int, int]:
    min_rows = matrix.min(axis=1)
    return int(min_rows.argmax()), int(min_rows.max())


def min_max_by_columns(matrix: np.ndarray) -> Tuple[int, int]:
    max_cols = matrix.max(axis=0)
    return int(max_cols.argmin()), int(max_cols.min())


def has_saddle_point(first_value: int, second_value: int) -> bool:
    if first_value == second_value:
        return True
    return False


def is_fair_play_game(first_value: int, second_value: int) -> bool:
    if first_value == 0 and second_value == 0:
        return True
    return False


def reduce_rows_cols_in_matrix(primary_matrix: np.ndarray) -> np.ndarray:
    rows_number = primary_matrix.shape[0]
    cols_number = primary_matrix.shape[1]

    reduced_matrix: np.ndarray = np.ndarray([])
    for i in range(rows_number):
        for j in range(rows_number):
            if i != j:
                if (primary_matrix[i] <= primary_matrix[j]).all() \
                        and has_smaller_item_in_row(primary_matrix[i], primary_matrix[j]):
                    print(primary_matrix[i])
                    print()

    for i in range(cols_number):
        for j in range(cols_number):
            if i != j:
                if (primary_matrix[:, i] >= primary_matrix[:, j]).all() \
                        and has_bigger_item_in_column(primary_matrix[i],
                                                      primary_matrix[j]):
                    print(primary_matrix[:, i])
                    print()

    return reduced_matrix


def has_smaller_item_in_row(row_to_check: np.ndarray, other_row: np.ndarray) -> bool:
    if len(row_to_check) != len(other_row):
        raise Exception("Lists must have equal length")

    return (row_to_check < other_row).any()


def has_bigger_item_in_column(column_to_check: np.ndarray,
                              other_column: np.ndarray) -> bool:
    if len(column_to_check) != len(other_column):
        raise Exception("Lists must have equal length")

    return (column_to_check < other_column).any()
