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

    if args.time:
        variant_number, probability = calculate_probability_and_variant(matrices, args.time)
        print_result_for_term(probability, variant_number)
    elif args.probability:
        completion_times = calculate_completion_time(matrices, args.probability)
        print_result_for_probability(completion_times)
    else:
        raise Exception("time or probability must be passed !!!")

    display_finish()


# DEF ------------------------------------------------------------------------ #
def print_matrices(matrices: Union[Dict[int, np.ndarray], Dict[int, pd.DataFrame]]) -> None:
    for matrix in matrices:
        print("Matrix order number: " + str(matrix + 1))
        print(str(matrices[matrix]) + "\n")


def print_result_for_term(probability: float, variant_number: int) -> None:
    print("Probability:" + str(round(probability, 4)))
    print("More probable variant: " + str(variant_number + 1))


def print_result_for_probability(completion_times: Dict[int, float]) -> None:
    for completion_time in completion_times:
        print(
            "Project order number: " + str(completion_time + 1)
            + ", Completion time: " + str(round(completion_times[completion_time], 4))
        )


def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()

    arg_parser.add_argument(
        "-f", "--filenames", required=True, type=str, action="store", nargs="*",
        help="List of filenames of matrices"
    )
    arg_parser.add_argument(
        "-dt", "--time", type=float, help="Value of directive time"
    )
    arg_parser.add_argument(
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
