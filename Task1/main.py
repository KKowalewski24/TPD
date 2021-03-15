import subprocess
import sys
import os

import numpy as np
from typing import List

from module.Record import Record
from module.criteria import hurwicz_criteria, max_max_criteria, \
    maxi_min_criteria, savage_criteria, bayes_laplace_criteria
from module.util import is_convertible_to_float, is_array_convertible_to_int


# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    chosen_matrix: np.ndarray = np.loadtxt(get_filename())
    print("chosen_matrix")
    print(chosen_matrix)

    hurwicz_factor: float = get_factor()
    probabilities: List[float] = get_probabilities()
    print()

    display_result(
        maxi_min_criteria(chosen_matrix),
        "Minimaks użyteczności - maksymalizuje najmniejszą możliwą użyteczność"
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
        bayes_laplace_criteria(chosen_matrix, probabilities),
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


def get_probabilities() -> List[float]:
    value: str = ""
    has_only_integers: bool = False
    while not has_only_integers:
        value = input(
            "Podaj kolejne dzielniki ułamków zwykłych prawdopodobieństw rozdzielone spacjami: "
        )
        has_only_integers = is_array_convertible_to_int(value.split())

    return [1 / int(item) for item in value.split()]


def get_filename() -> str:
    filename: str = ""
    while not os.path.isfile(filename):
        filename = input("Podaj nazwę pliku txt z macierzą użyteczności: ")
    return filename


def display_result(record: Record, criteria_name: str) -> None:
    print(criteria_name)
    print("\t\tDecyzja numer: " + str(record.row_number + 1))


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
