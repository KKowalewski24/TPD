from typing import Tuple

import numpy as np
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum


def get_linear_solution(matrix: np.ndarray) -> None:
    scaled_matrix, scale_value = scale_matrix(matrix)
    rows_number = scaled_matrix.shape[0]
    cols_number = scaled_matrix.shape[1]

    problem_a = LpProblem("A", LpMinimize)
    x_variables = [LpVariable("X" + str(index + 1), 0) for index in range(rows_number)]
    problem_a += lpSum(x_variables)

    for i in range(cols_number):
        problem_a += lpSum(
            [x_variables[j] * scaled_matrix[j, i] for j in
             range(len(scaled_matrix[:, i]))]
        ) >= 1

    problem_a.solve()

    problem_b = LpProblem("B", LpMaximize)
    y_variables = [LpVariable("Y" + str(index + 1), 0) for index in range(cols_number)]
    problem_b += lpSum(y_variables)

    for i in range(rows_number):
        problem_b += lpSum(
            [y_variables[j] * scaled_matrix[i, j] for j in range(len(scaled_matrix[i]))]
        ) <= 1

    problem_b.solve()

    for variable in problem_a.variables():
        print(variable, end=" = ")
        print(variable.varValue)

    for variable in problem_b.variables():
        print(variable, end=" = ")
        print(variable.varValue)

    game_value = 1 / sum([var.varValue for var in problem_a.variables()])
    reverted_game_value = revert_scaling_game_value(game_value, scale_value)


def scale_matrix(matrix: np.ndarray) -> Tuple[np.ndarray, float]:
    min_value_in_matrix = float(matrix.min())
    if min_value_in_matrix <= 0:
        matrix = matrix + abs(min_value_in_matrix)

    return matrix, min_value_in_matrix


def revert_scaling_game_value(game_value: float, scale_value: float) -> float:
    if scale_value <= 0:
        game_value = game_value - abs(scale_value)
    return game_value
