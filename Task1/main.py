import subprocess
import sys

import numpy as np

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
    display_finish()


# DEF ------------------------------------------------------------------------ #

# UTIL ----------------------------------------------------------------------- #
def check_types_check_style() -> None:
    subprocess.call(["mypy", "."])
    subprocess.call(["flake8", "."])


def compile_to_pyc() -> None:
    subprocess.call(["python", "-m", "compileall", "."])


def display_finish() -> None:
    print("------------------------------------------------------------------------")
    print("FINISHED")
    print("------------------------------------------------------------------------")


# __MAIN__ ------------------------------------------------------------------- #
if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "typing" or sys.argv[1] == "-t"):
        check_types_check_style()
    elif len(sys.argv) == 2 and (sys.argv[1] == "build" or sys.argv[1] == "-b"):
        compile_to_pyc()
    else:
        check_types_check_style()
        main()
