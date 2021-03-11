import subprocess
import sys

import numpy as np

from module.Record import Record
from module.criteria import hurwicz_criteria, max_max_criteria, \
    maxi_min_criteria, mini_max_criteria, savage_criteria, bayes_laplace_criteria

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
    [28, 34, 29],
    [27, 29, 33],
    [31, 30, 29],
])


# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    chosen_matrix: np.ndarray = lecture_matrix
    hurwicz_factor: float = get_factor()

    display_result(
        maxi_min_criteria(chosen_matrix),
        "Minimaks użyteczności - maksymalizuje najmniejszą możliwą użyteczność"
    )
    display_result(
        mini_max_criteria(chosen_matrix),
        "Minimaks zawodu - minimaluzuje największy możliwy zawód"
    )
    display_result(
        max_max_criteria(chosen_matrix),
        "Max Max - kryterium optymistyczne"
    )
    display_result(
        hurwicz_criteria(chosen_matrix, hurwicz_factor),
        "Hurwicz"
    )
    display_result(
        bayes_laplace_criteria(chosen_matrix),
        "Bayes Laplace"
    )
    display_result(
        savage_criteria(chosen_matrix),
        "Savage"
    )

    display_finish()


# DEF ------------------------------------------------------------------------ #
def get_factor() -> float:
    is_float: bool = False
    value: str = ""
    while not is_float:
        value = input("Podaj współczynnik do kryterium Hurwicza: ")
        is_float = is_convertible_to_float(value)

    return float(value)


def display_result(record: Record, criteria_name: str) -> None:
    print(criteria_name)
    print("\t\tDecyzja numer: " + str(record.row_number + 1))


def is_convertible_to_float(value: str):
    try:
        float(value)
        return True
    except ValueError:
        return False


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
