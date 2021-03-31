from typing import Tuple

import numpy as np
from pulp import LpVariable, LpProblem, LpMinimize, LpMaximize


def get_linear_solution(matrix: np.ndarray) -> None:
    scaled_matrix, scale_value = scale_matrix(matrix)


def scale_matrix(matrix: np.ndarray) -> Tuple[np.ndarray, float]:
    min_value_in_matrix = matrix.min()
    if min_value_in_matrix <= 0:
        matrix = matrix + abs(min_value_in_matrix)

    return matrix, abs(min_value_in_matrix)
