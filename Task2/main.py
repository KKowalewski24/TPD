import subprocess
import sys
from argparse import ArgumentParser, Namespace
from typing import List

import numpy as np

from module.linear_programming_solution import get_linear_solution
from module.matrix_reducer import reduce_rows_cols_in_matrix
from module.saddle_point_solution import has_saddle_point, is_fair_play_game, \
    max_min_by_rows, min_max_by_columns
from module.test_matrix_param import test_different_matrix_param
from module.util import substitute_letter_and_convert_to_numeric

"""
Sample usage:
    Only substitution chosen value:
        python main.py -f data/matrix_from_task.txt -s 5
    Testing value to substitute:
        python main.py -f data/matrix_from_task.txt --test -b -20 -e 21 -w 4
    Check available params:
        python main.py -h
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    matrix: np.ndarray = np.loadtxt(args.filename, dtype=str)
    print("Matrix before substitution")
    print(matrix)

    if not args.test:
        process_calculations(matrix, args.substitute)
    else:
        test_different_matrix_param(matrix, args.begin, args.end, args.win)

    display_finish()


# DEF ------------------------------------------------------------------------ #
def process_calculations(matrix: np.ndarray, substitute_value: float) -> None:
    substituted_matrix = substitute_letter_and_convert_to_numeric(
        matrix, substitute_value
    )

    print("Matrix after substitution")
    print(substituted_matrix)

    player_a_strategy, player_a_game_value = max_min_by_rows(substituted_matrix)
    player_b_strategy, player_b_game_value = min_max_by_columns(substituted_matrix)

    if has_saddle_point(player_a_game_value, player_b_game_value):
        print_result_saddle_point(
            ["A", "B"], [player_a_strategy, player_b_strategy],
            player_a_game_value, is_saddle_point=True,
            is_fair_play=is_fair_play_game(player_a_game_value, player_b_game_value)
        )
        return

    reduced_matrix: np.ndarray = reduce_rows_cols_in_matrix(substituted_matrix)

    print("Matrix after row and column reduction")
    print(reduced_matrix)

    player_a_value, player_b_value, game_value = get_linear_solution(reduced_matrix)
    print_result_linear_solution(["A", "B"], [player_a_value, player_b_value], game_value)


def print_result_saddle_point(player_ids: List[str], strategy_numbers: List[int],
                              game_value: int, is_saddle_point: bool = False,
                              is_fair_play: bool = False) -> None:
    if len(player_ids) != len(strategy_numbers) or len(player_ids) != 2:
        raise Exception("Lists must have equal length and length must be equals 2!!!")

    if is_saddle_point:
        print("\nGame Has Saddle Point !!!")
    if is_fair_play:
        print("Game is fair play ==> V==0")

    print("Game Value: " + str(game_value))

    for index in range(len(player_ids)):
        print("Player " + player_ids[index]
              + ", Strategy order number: " + str(strategy_numbers[index] + 1))


def print_result_linear_solution(player_ids: List[str], player_values: List[List[float]],
                                 game_value: float) -> None:
    if len(player_ids) != len(player_values) or len(player_ids) != 2:
        raise Exception("Lists must have equal length and length must be equals 2!!!")

    print("Game Value: " + str(game_value))

    for i in range(len(player_ids)):
        print("Player " + player_ids[i], end=": ")
        for j in range(len(player_values[i])):
            print(str(player_values[i][j]), end=", ")
        print()


def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()
    # TODO ADD SUBCOMMANDS
    arg_parser.add_argument(
        "-f", "--filename", required=True, type=str, help="Filename of matrix"
    )
    arg_parser.add_argument(
        "-s", "--substitute", type=float,
        help="Value to substitute letters in chosen matrix"
    )
    arg_parser.add_argument(
        "--test", default=False, action="store_true",
        help="Test different params marked as letter in passed matrix"
    )
    arg_parser.add_argument(
        "-b", "--begin", type=int, help="Begin of substituted values"
    )
    arg_parser.add_argument(
        "-e", "--end", type=int, help="End of substituted values"
    )
    arg_parser.add_argument(
        "-w", "--win", type=int, help="Average win value"
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
