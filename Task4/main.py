import subprocess
import sys
from argparse import ArgumentParser, Namespace
from typing import List

import pandas as pd

from module.dynamic_programming_solution import find_optimal_strategy

"""
Sample usage:
    python main.py -f data/process_table_from_task.csv
"""


# VAR ------------------------------------------------------------------------ #

# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    args = prepare_args()
    process_table: pd.DataFrame = pd.read_csv(args.filename)
    print("process_table")
    print(process_table, end="\n\n")
    best_decisions, min_losses = find_optimal_strategy(process_table)
    display_result(best_decisions, min_losses)

    display_finish()


# DEF ------------------------------------------------------------------------ #
def display_result(best_decisions: List[str], min_losses: float) -> None:
    print("Minimal losses value: " + str(min_losses))
    for best_decision in best_decisions:
        print("Best decisions: ")
        print(best_decision, end=",")
    print()


def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "-f", "--filename", required=True, type=str, help="Filename of process table"
    )

    return arg_parser.parse_args()


# UTIL ----------------------------------------------------------------------- #
def check_types_check_style() -> None:
    subprocess.call(["mypy", "."])
    subprocess.call(["flake8", "."])


def compile_to_pyc() -> None:
    subprocess.call(["python", "-m", "compileall", "."])


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
    elif check_if_exists_in_args("-b"):
        compile_to_pyc()
    else:
        main()
