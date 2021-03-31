import string

import numpy as np


# Function substitutes all letter from 'A' to 'Z' not only 'A' letter
def substitute_letter_and_convert_to_numeric(matrix: np.ndarray,
                                             substitute_value: float) -> np.ndarray:
    matrix = np.char.upper(matrix)

    for character in string.ascii_uppercase:
        if np.isin(matrix, character).any():
            matrix = np.char.replace(matrix, character, str(substitute_value))

    return matrix.astype(np.float32)
