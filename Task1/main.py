import subprocess
import sys
from argparse import ArgumentParser, Namespace

import numpy as np

from module.criteria import bayes_laplace_criteria, hurwicz_criteria, max_max_criteria, \
    maxi_min_criteria, savage_criteria

"""
Sample usage:
    python main.py -f data/task_matrix.txt --hurwicz 0.5 -p 0.25 0.25 0.25 0.25
    python main.py -f data/exam_matrix1.txt --hurwicz 0.5 -p 0.1 0.3 0.2 0.2 0.2
"""


# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    chosen_matrix: np.ndarray = np.loadtxt(args.filename)
    print("Chosen Matrix")
    print(chosen_matrix)

    display_result(
        maxi_min_criteria(chosen_matrix),
        "Walda - Minimaks użyteczności - maksymalizuje najmniejszą możliwą użyteczność"
    )
    display_result(
        max_max_criteria(chosen_matrix),
        "Max Max - kryterium optymistyczne"
    )
    display_result(
        hurwicz_criteria(chosen_matrix, args.hurwicz),
        "Hurwicz"
    )
    display_result(
        bayes_laplace_criteria(chosen_matrix, args.probabilities),
        "Bayes Laplace"
    )
    display_result(
        savage_criteria(chosen_matrix),
        "Savage"
    )

    display_finish()


# DEF ------------------------------------------------------------------------ #
def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "-f", "--filename", required=True, type=str, help="Filename of matrix"
    )
    arg_parser.add_argument(
        "--hurwicz", required=True, type=float, help="Coefficient of Hurwicz criterion"
    )
    arg_parser.add_argument(
        "-p", "--probabilities", required=True, type=float, action="store", nargs="*",
        help="List of probabilities"
    )
    return arg_parser.parse_args()


def display_result(decision_number: int, criteria_name: str) -> None:
    print(criteria_name)
    print("\t\tDecyzja numer: " + str(decision_number + 1))


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
