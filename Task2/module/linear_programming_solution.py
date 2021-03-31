from typing import Tuple

import numpy as np
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum


def get_linear_solution(matrix: np.ndarray) -> None:
    scaled_matrix, scale_value = scale_matrix(matrix)
    rows_number = scaled_matrix.shape[0]
    cols_number = scaled_matrix.shape[1]

    variable_x = [LpVariable("X" + str(index + 1), 0) for index in range(rows_number)]
    problem_a = LpProblem("A", LpMinimize)
    problem_a += lpSum(variable_x)

    for i in range(cols_number):
        problem_a += lpSum(
            [variable_x[j] * scaled_matrix[j, i] for j in range(len(scaled_matrix[:, i]))]
        ) >= 1

    problem_a.solve()

    # variable_y = LpVariable("Y", lowBound=0)
    # problem_b = LpProblem("B", LpMaximize)
    # problem_b += lpSum(variable_y)
    #
    # for index in range(rows_number):
    #     problem_b += lpSum([variable_y * item for item in scaled_matrix[index]]) <= 1
    #
    # problem_b.solve()

    for variable in problem_a.variables():
        print(variable)
        print(variable.varValue)

    game_value = 1 / sum([var.varValue for var in problem_a.variables()])
    reverted_game_value = revert_scaling_game_value(game_value, scale_value)


def scale_matrix(matrix: np.ndarray) -> Tuple[np.ndarray, float]:
    min_value_in_matrix = matrix.min()
    if min_value_in_matrix <= 0:
        matrix = matrix + abs(min_value_in_matrix)

    return matrix, min_value_in_matrix


def revert_scaling_game_value(game_value: float, scale_value: float) -> float:
    if scale_value <= 0:
        game_value = game_value - abs(scale_value)
    return game_value
