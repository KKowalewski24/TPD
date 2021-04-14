import subprocess
import sys
from argparse import ArgumentParser, Namespace
from typing import Dict, Union

import numpy as np
import pandas as pd

from module.pert_solution import calculate_completion_time, calculate_probability_and_variant
from module.reader import read_csv_matrices

"""
python main.py -f data/A_variant_matrix_from_task.csv data/B_variant_matrix_from_task.csv -dt 48
python main.py -f data/A_variant_matrix_from_task.csv data/B_variant_matrix_from_task.csv -pr 0.9
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    matrices: Dict[int, pd.DataFrame] = read_csv_matrices(args.filenames)
    print("Base matrices")
    print_matrices(matrices)

    if args.term:
        probability, variant_number = calculate_probability_and_variant(matrices, args.term)
        print_result_for_term(probability, variant_number)
    elif args.probability:
        # TODO
        print("args.probability")
        time = calculate_completion_time()
        print_result_for_probability(time)
    else:
        raise Exception("term or probability must be passed !!!")

    display_finish()


# DEF ------------------------------------------------------------------------ #
def print_matrices(matrices: Union[Dict[int, np.ndarray], Dict[int, pd.DataFrame]]) -> None:
    for matrix in matrices:
        print("Matrix order number: " + str(matrix + 1))
        print(str(matrices[matrix]) + "\n")


def print_result_for_term(probability: float, variant_number: int) -> None:
    print("Probability:" + str(probability))
    print("More probable variant: " + str(variant_number + 1))


def print_result_for_probability(time: float) -> None:
    print("Project completion time: " + str(time))


def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()

    general = arg_parser.add_argument_group("general")

    general.add_argument(
        "-f", "--filenames", required=True, type=str, action="store", nargs="*",
        help="List of filenames of matrices"
    )
    general.add_argument(
        "-dt", "--term", type=float, help="Value of directive term"
    )
    general.add_argument(
        "-pr", "--probability", type=float, help="Value of expected probability"
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
