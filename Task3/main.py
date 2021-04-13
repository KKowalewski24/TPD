import subprocess
import sys
from argparse import ArgumentParser, Namespace
from typing import Dict

import pandas as pd

from module.reader import print_matrices, read_csv_matrices

"""
python main.py -f data/A_variant_matrix_from_task.txt data/B_variant_matrix_from_task.txt -dt 48
python main.py -f data/A_variant_matrix_from_task.csv data/B_variant_matrix_from_task.csv -dt 48
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    matrices: Dict[int, pd.DataFrame] = read_csv_matrices(args.filenames)
    print_matrices(matrices)
    display_finish()


# DEF ------------------------------------------------------------------------ #
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
        "-pr", "--probability", type=float, help="Value of directive term"
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
