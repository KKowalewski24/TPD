from typing import Tuple

import numpy as np
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum


def get_linear_solution(matrix: np.ndarray) -> None:
    scaled_matrix, scale_value = scale_matrix(matrix)

    variable_x = LpVariable("X", lowBound=0)
    problem_a = LpProblem("A", LpMinimize)
    problem_a += lpSum(variable_x)

    variable_y = LpVariable("Y", lowBound=0)
    problem_b = LpProblem("B", LpMaximize)
    problem_b += lpSum(variable_y)

    # TODO CHANGE FOR REAL VALUE
    game_value = 1
    revert_scaling_game_value(game_value, scale_value)


def scale_matrix(matrix: np.ndarray) -> Tuple[np.ndarray, float]:
    min_value_in_matrix = matrix.min()
    if min_value_in_matrix <= 0:
        matrix = matrix + abs(min_value_in_matrix)

    return matrix, min_value_in_matrix


def revert_scaling_game_value(game_value: float, scale_value: float) -> float:
    if scale_value <= 0:
        game_value = game_value - abs(scale_value)
    return game_value
