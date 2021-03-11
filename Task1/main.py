import subprocess
import sys

import numpy as np

from module.decision_criteria.criteria import max_max_criteria
from module.decision_criteria.criteria import maxi_min_criteria
from module.decision_criteria.criteria import mini_max_criteria

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
    display_finish()


# DEF ------------------------------------------------------------------------ #

# UTIL ----------------------------------------------------------------------- #
def check_types_check_style() -> None:
    subprocess.call(["mypy", "."])
    subprocess.call(["flake8", "."])


def check_if_args_exists(arg: str) -> bool:
    return arg in sys.argv


def display_finish() -> None:
    print("------------------------------------------------------------------------")
    print("FINISHED")
    print("------------------------------------------------------------------------")


# __MAIN__ ------------------------------------------------------------------- #
if __name__ == "__main__":
    if check_if_args_exists("-t"):
        check_types_check_style()

    main()
