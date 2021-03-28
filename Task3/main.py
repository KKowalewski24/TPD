import subprocess
import sys
from argparse import ArgumentParser, Namespace

"""
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    display_finish()


# DEF ------------------------------------------------------------------------ #
def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()

    general = arg_parser.add_argument_group("general")

    general.add_argument(
        '-f', '--filename', required=True, type=str, help="Filename of matrix"
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
