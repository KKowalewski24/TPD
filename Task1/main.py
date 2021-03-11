import subprocess
import sys

import numpy as np

from module.Record import Record
from module.decision_criteria.criteria import hurwicz_criteria, max_max_criteria, \
    maxi_min_criteria, mini_max_criteria

"""
"""

# VAR ------------------------------------------------------------------------ #
matrix_from_task: np.ndarray = np.array([
    [0.5, 0.6, 0.4, 0.5],
    [0.1, 0.7, 0.4, 0.7],
    [0.8, 0.2, 0.5, 0.5],
    [0.1, 0.8, 0.5, 0.7],
])

lecture_matrix: np.ndarray = np.array([
    [24, 28, 36],
    [31, 30, 28],
    [28, 24, 29],
    [27, 29, 33],
    [31, 30, 29],
])


# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    chosen_matrix: np.ndarray = lecture_matrix
    # todo add argv choose
    display_result(maxi_min_criteria(chosen_matrix))
    display_result(mini_max_criteria(chosen_matrix))
    display_result(max_max_criteria(chosen_matrix))
    display_result(hurwicz_criteria(chosen_matrix, 0.25))

    display_finish()


# DEF ------------------------------------------------------------------------ #
def display_result(record: Record) -> None:
    print("Decyzja numer: " + str(record.row_number + 1))


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

    main()
