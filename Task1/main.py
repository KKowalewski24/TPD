import subprocess
import sys

import numpy as np

from module.decision_criteria.criteria import hurwicz_criteria, max_max_criteria, \
    maxi_min_criteria, mini_max_criteria

"""
"""

# VAR ------------------------------------------------------------------------ #
base_matrix: np.ndarray = np.array([
    [0.5, 0.6, 0.4, 0.5],
    [0.1, 0.7, 0.4, 0.7],
    [0.8, 0.2, 0.5, 0.5],
    [0.1, 0.8, 0.5, 0.7],
])


# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    print(maxi_min_criteria(base_matrix))
    print(mini_max_criteria(base_matrix))
    print(max_max_criteria(base_matrix))
    print(hurwicz_criteria(base_matrix, 0.25))
    display_finish()


# DEF ------------------------------------------------------------------------ #

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
