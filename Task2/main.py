import subprocess
import sys
from argparse import ArgumentParser, Namespace
from typing import List, Tuple

import numpy as np

from module.functions import has_saddle_point, is_fair_play_game, max_min_by_rows, \
    min_max_by_columns, substitute_letter_and_convert_to_numeric
from module.matrix_reducer import reduce_rows_cols_in_matrix
from module.test_matrix_param import test_different_matrix_param

"""
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    matrix: np.ndarray = np.loadtxt(args.filename, dtype=str)
    print("matrix before substitution")
    print(matrix)

    if not args.param:
        process_calculations(matrix, args.substitute)
    else:
        test_different_matrix_param(matrix, -15, 16, 4)

    display_finish()


# DEF ------------------------------------------------------------------------ #
def process_calculations(matrix: np.ndarray, substitute_value: int) -> None:
    substituted_matrix = substitute_letter_and_convert_to_numeric(
        matrix, substitute_value
    )

    player_a: Tuple[int, int] = max_min_by_rows(substituted_matrix)
    player_b: Tuple[int, int] = min_max_by_columns(substituted_matrix)

    if has_saddle_point(player_a[1], player_b[1]):
        print_result_saddle_point(
            ["A", "B"], [player_a[0], player_b[0]],
            is_fair_play_game(player_a[1], player_b[1])
        )
        return

    # TODO ADD NEXT STEPS
    reduced_matrix: np.ndarray = reduce_rows_cols_in_matrix(substituted_matrix)


def print_result_saddle_point(player_ids: List[str], strategy_numbers: List[int],
                              is_fair_play: bool) -> None:
    if len(player_ids) != len(strategy_numbers) or len(player_ids) != 2:
        raise Exception("Lists must have equal length and length must be equals 2!!!")

    print("\nGame Has Saddle Point !!!")
    if is_fair_play:
        print("Game is fair play ==> V==0")

    for index in range(len(player_ids)):
        print("Player " + player_ids[index]
              + ", Strategy order number: " + str(strategy_numbers[index] + 1))


def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()
    # todo add grouping args
    arg_parser.add_argument(
        '-f', '--filename', required=True, type=str, help="Filename of matrix"
    )
    arg_parser.add_argument(
        "-s", "--substitute", required=True, type=int,
        help="Value to substitute letter in chosen matrix"
    )
    arg_parser.add_argument(
        "-p", "--param", default=False, action="store_true",
        help="Test different params marked as letter in passed matrix"
    )

    return arg_parser.parse_args()


# UTIL ----------------------------------------------------------------------- #
def check_types_check_style() -> None:
    subprocess.call(["mypy", "."])
    subprocess.call(["flake8", "."])


def check_if_exists_in_args(arg: str) -> bool:
    return arg in sys.argv


def display_finish() -> None:
    print("------------------------------------------------------------------------")
    print("FINISHED")
    print("------------------------------------------------------------------------")


# __MAIN__ ------------------------------------------------------------------- #
if __name__ == "__main__":
    if check_if_exists_in_args("-t"):
        check_types_check_style()
    else:
        main()
