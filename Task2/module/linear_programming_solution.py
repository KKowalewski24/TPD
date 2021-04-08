import math
from typing import List, Tuple

import numpy as np
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

'''
In order to enable logging to console, remove PULP_CBC_CMD(msg=False) from solve function
'''


def get_linear_solution(matrix: np.ndarray) -> Tuple[List[float], List[float], float]:
    scaled_matrix, scale_value = scale_matrix(matrix)
    rows_number = scaled_matrix.shape[0]
    cols_number = scaled_matrix.shape[1]

    a_problem_variables = minimize_by_columns(scaled_matrix, rows_number, cols_number)
    b_problem_variables = maximize_by_rows(scaled_matrix, rows_number, cols_number)

    game_value = 1 / math.fsum(a_problem_variables)
    final_game_value = round(calculate_game_value(a_problem_variables, scale_value), 2)
    player_a = [round(var * game_value, 2) for var in a_problem_variables]
    player_b = [round(var * game_value, 2) for var in b_problem_variables]

    return player_a, player_b, final_game_value


def scale_matrix(matrix: np.ndarray) -> Tuple[np.ndarray, float]:
    min_value_in_matrix = float(matrix.min())
    if min_value_in_matrix <= 0:
        matrix = matrix + abs(min_value_in_matrix)

    return matrix, min_value_in_matrix


def minimize_by_columns(matrix: np.ndarray, rows_number: int,
                        cols_number: int) -> List[float]:
    problem = LpProblem("A", LpMinimize)
    variables = [LpVariable("X" + str(index + 1), 0) for index in range(rows_number)]
    problem += lpSum(variables)

    for i in range(cols_number):
        problem += lpSum(
            [variables[j] * matrix[j, i] for j in range(len(matrix[:, i]))]
        ) >= 1

    problem.solve(PULP_CBC_CMD(msg=False))

    return [var.varValue for var in problem.variables()]


def maximize_by_rows(matrix: np.ndarray, rows_number: int,
                     cols_number: int) -> List[float]:
    problem = LpProblem("B", LpMaximize)
    variables = [LpVariable("Y" + str(index + 1), 0) for index in range(cols_number)]
    problem += lpSum(variables)

    for i in range(rows_number):
        problem += lpSum(
            [variables[j] * matrix[i, j] for j in range(len(matrix[i]))]
        ) <= 1

    problem.solve(PULP_CBC_CMD(msg=False))

    return [var.varValue for var in problem.variables()]


def calculate_game_value(variables: List[float], scale_value: float) -> float:
    game_value = 1 / math.fsum(variables)
    if scale_value <= 0:
        game_value = game_value - abs(scale_value)

    return game_value
