import subprocess
import sys
from argparse import ArgumentParser, Namespace

import numpy as np
from typing import Tuple, List

from module.functions import min_max_by_columns, max_min_by_rows, has_saddle_point, \
    is_fair_play_game

"""
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    # TODO FIX ISSUE WITH READING 'A' FROM MATRIX
    chosen_matrix: np.ndarray = np.loadtxt(args.filename)
    print("chosen_matrix")
    print(chosen_matrix)

    process_calculations(chosen_matrix)

    display_finish()


# DEF ------------------------------------------------------------------------ #
def process_calculations(matrix: np.ndarray) -> None:
    player_a: Tuple[int, int] = max_min_by_rows(matrix)
    player_b: Tuple[int, int] = min_max_by_columns(matrix)
    if has_saddle_point(player_a[1], player_b[1]):
        print_result_saddle_point(
            ["A", "B"], [player_a[0], player_b[0]],
            is_fair_play_game(player_a[1], player_b[1])
        )
        return

    # TODO ADD NEXT STEPS


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
    arg_parser.add_argument('-f', '--filename', required=True, type=str)

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
