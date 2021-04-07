import subprocess
import sys
from argparse import ArgumentParser, Namespace
from typing import List

import numpy as np

from module.linear_programming_solution import get_linear_solution
from module.matrix_reducer import reduce_rows_cols_in_matrix
from module.saddle_point_solution import has_saddle_point, is_fair_play_game, \
    max_min_by_rows, min_max_by_columns

"""
Sample usage:
    python main.py -f data/matrix_from_task.txt
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    matrix: np.ndarray = np.loadtxt(args.filename)
    print("Matrix")
    print(matrix)
    process_calculations(matrix)

    display_finish()


# DEF ------------------------------------------------------------------------ #
def process_calculations(matrix: np.ndarray) -> None:
    player_a_strategy, player_a_game_value = max_min_by_rows(matrix)
    player_b_strategy, player_b_game_value = min_max_by_columns(matrix)

    if has_saddle_point(player_a_game_value, player_b_game_value):
        print_result_saddle_point(
            ["A", "B"], [player_a_strategy, player_b_strategy],
            player_a_game_value, True,
            is_fair_play_game(player_a_game_value, player_b_game_value)
        )
        return

    reduced_matrix: np.ndarray = reduce_rows_cols_in_matrix(matrix)

    print("Matrix after row and column reduction")
    print(reduced_matrix)

    player_a_value, player_b_value, game_value = get_linear_solution(reduced_matrix)
    print_result_linear_solution(["A", "B"], [player_a_value, player_b_value], game_value)


def print_result_saddle_point(player_ids: List[str], strategy_numbers: List[int],
                              game_value: int, is_saddle_point: bool,
                              is_fair_play: bool) -> None:
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
    arg_parser.add_argument(
        "-f", "--filename", required=True, type=str, help="Filename of matrix"
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
