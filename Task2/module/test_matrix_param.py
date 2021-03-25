from typing import List, Tuple

import numpy as np

from module.functions import has_saddle_point, max_min_by_rows, min_max_by_columns
from module.matrix_reducer import reduce_rows_cols_in_matrix


def test_different_matrix_param(primary_matrix: np.ndarray, range_begin: int,
                                range_end: int, average_win: int) -> None:
    display_params(test_saddle_point(primary_matrix, range_begin, range_end))
    display_params(test_mixed_strategies(primary_matrix, range_begin, range_end))
    # TODO ADD USAGE OF check_if_has_average_win


def test_saddle_point(primary_matrix: np.ndarray,
                      range_begin: int, range_end: int) -> List[int]:
    param_values_for_saddle_point: List[int] = []

    for index in range(range_begin, range_end):
        # TODO ADD REPLACING 'A' WITH INDEX VALUE
        player_a: Tuple[int, int] = max_min_by_rows(primary_matrix)
        player_b: Tuple[int, int] = min_max_by_columns(primary_matrix)

        if has_saddle_point(player_a[1], player_b[1]):
            param_values_for_saddle_point.append(index)

    return param_values_for_saddle_point


def test_mixed_strategies(primary_matrix: np.ndarray,
                          range_begin: int, range_end: int) -> List[int]:
    param_values_for_mixed_strategies: List[int] = []

    for index in range(range_begin, range_end):
        reduced_matrix: np.ndarray = reduce_rows_cols_in_matrix(primary_matrix)
        # TODO ADD REPLACING 'A' WITH INDEX VALUE
        # TODO ADD NEXT STEPS

    return param_values_for_mixed_strategies


# '-' near value means opposite value
# Checking opposite value is required because this is game with zero sum
def check_if_has_average_win(player_a_value: int, player_b_value: int,
                             average_win: int) -> bool:
    if (player_a_value == average_win and player_b_value == - average_win) \
            or (player_b_value == average_win and player_a_value == -average_win):
        return True
    return False


def display_params(params: List[int]) -> None:
    for param in params:
        print(param)
