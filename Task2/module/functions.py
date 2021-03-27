import string
from typing import Tuple

import numpy as np


def max_min_by_rows(matrix: np.ndarray) -> Tuple[int, int]:
    min_rows = matrix.min(axis=1)
    return int(min_rows.argmax()), int(min_rows.max())


def min_max_by_columns(matrix: np.ndarray) -> Tuple[int, int]:
    max_cols = matrix.max(axis=0)
    return int(max_cols.argmin()), int(max_cols.min())


def has_saddle_point(first_value: int, second_value: int) -> bool:
    if first_value == second_value:
        return True
    return False


def is_fair_play_game(first_value: int, second_value: int) -> bool:
    if first_value == 0 and second_value == 0:
        return True
    return False


# Function substitutes all letter from 'A' to 'Z' not only 'A' letter
def substitute_letter_and_convert_to_numeric(matrix: np.ndarray,
                                             substitute_value: int) -> np.ndarray:
    matrix = np.char.upper(matrix)

    for character in string.ascii_uppercase:
        if np.isin(matrix, character).any():
            matrix = np.char.replace(matrix, character, str(substitute_value))

    return matrix.astype(np.float32)
