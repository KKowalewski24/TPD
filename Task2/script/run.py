import os
import pathlib
import subprocess
import sys

"""
"""

# VAR ------------------------------------------------------------------------ #
FILENAME = "matrix_from_task.txt"


# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    go_to_parent_directory()
    subprocess.call(["python", "main.py", "-f", FILENAME])

    display_finish()


# DEF ------------------------------------------------------------------------ #

# UTIL ----------------------------------------------------------------------- #
def go_to_parent_directory() -> None:
    os.chdir(pathlib.Path(os.getcwd()).parent)


def check_types() -> None:
    subprocess.call(["mypy", "."])


def check_if_exists_in_args(arg: str) -> bool:
    return arg in sys.argv


def display_finish() -> None:
    print("------------------------------------------------------------------------")
    print("FINISHED")
    print("------------------------------------------------------------------------")


# __MAIN__ ------------------------------------------------------------------- #
if __name__ == "__main__":
    if check_if_exists_in_args("-t"):
        check_types()
    else:
        main()
