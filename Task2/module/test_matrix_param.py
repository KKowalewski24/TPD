from typing import List, Tuple

import numpy as np

from module.matrix_reducer import reduce_rows_cols_in_matrix
from module.saddle_point_solution import has_saddle_point, max_min_by_rows, \
    min_max_by_columns
from module.util import substitute_letter_and_convert_to_numeric


def test_different_matrix_param(matrix: np.ndarray, range_begin: int, range_end: int,
                                average_win_value: int) -> None:
    display_params(
        "Saddle Point",
        test_saddle_point(matrix, range_begin, range_end)
    )
    display_params(
        "Mixed Strategy",
        test_mixed_strategies(matrix, range_begin, range_end)
    )
    display_params(
        "Average win for v=" + str(average_win_value),
        test_average_win_value(matrix, range_begin, range_end, average_win_value)
    )


def test_saddle_point(matrix: np.ndarray, range_begin: int, range_end: int) -> List[int]:
    param_values_for_saddle_point: List[int] = []

    for index in range(range_begin, range_end):
        substituted_matrix = substitute_letter_and_convert_to_numeric(matrix, index)
        player_a: Tuple[int, int] = max_min_by_rows(substituted_matrix)
        player_b: Tuple[int, int] = min_max_by_columns(substituted_matrix)

        if has_saddle_point(player_a[1], player_b[1]):
            param_values_for_saddle_point.append(index)

    return param_values_for_saddle_point


def test_mixed_strategies(matrix: np.ndarray, range_begin: int,
                          range_end: int) -> List[int]:
    param_values_for_mixed_strategies: List[int] = []

    for index in range(range_begin, range_end):
        substituted_matrix = substitute_letter_and_convert_to_numeric(matrix, index)
        reduced_matrix: np.ndarray = reduce_rows_cols_in_matrix(substituted_matrix)
        # TODO ADD NEXT STEPS

    return param_values_for_mixed_strategies


def test_average_win_value(matrix: np.ndarray, range_begin: int, range_end: int,
                           average_win_value: int) -> List[int]:
    param_values_for_average_win: List[int] = []

    for index in range(range_begin, range_end):
        substituted_matrix = substitute_letter_and_convert_to_numeric(matrix, index)
        reduced_matrix: np.ndarray = reduce_rows_cols_in_matrix(substituted_matrix)
        # TODO ADD NEXT STEPS
        # TODO ADD CALL check_if_has_average_win

    return param_values_for_average_win


# '-' near value means opposite value
# Checking opposite value is required because this is game with zero sum
def check_if_has_average_win(player_a_value: int, player_b_value: int,
                             average_win: int) -> bool:
    if (player_a_value == average_win and player_b_value == - average_win) \
            or (player_b_value == average_win and player_a_value == -average_win):
        return True
    return False


def display_params(strategy_type: str, params: List[int]) -> None:
    print(strategy_type)
    for param in params:
        print("\tParameter A: " + str(param))