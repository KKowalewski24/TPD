import subprocess
import sys
import argparse
import numpy as np

"""
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    chosen_matrix: np.ndarray = np.loadtxt(args.filename, str)
    print("chosen_matrix")
    print(chosen_matrix)

    display_finish()


# DEF ------------------------------------------------------------------------ #
def prepare_args() -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f', '--filename', type=str)

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
