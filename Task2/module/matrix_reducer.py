import numpy as np


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
