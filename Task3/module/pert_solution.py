from typing import Callable, List, Tuple

import numpy as np
import pandas as pd
from scipy.stats import norm

from module.cpm_solution import find_critical_paths


def calculate_probability_and_variant(matrices: List[pd.DataFrame],
                                      expected_time: float) -> Tuple[int, float]:
    probabilities = _calculate_values_based_on_time_and_std(
        matrices, lambda time, std: norm.cdf((expected_time - time) / std)
    )
    max_probability = max(probabilities)
    max_probability_index = probabilities.index(max_probability)
    return max_probability_index, max_probability


def calculate_completion_time(matrices: List[pd.DataFrame],
                              expected_probability: float) -> List[float]:
    if expected_probability > 1:
        raise Exception("Probability cannot be greater than 1")

    return _calculate_values_based_on_time_and_std(
        matrices, lambda time, std: (norm.ppf(expected_probability) * std) + time
    )


def _calculate_values_based_on_time_and_std(
        matrices: List[pd.DataFrame],
        callback: Callable[[float, float], float]) -> List[float]:
    times_and_stds: List[Tuple[float, float]] = []
    for matrix in matrices:
        times_and_stds.append(_calculate_sum_time_and_std(matrix))

    values: List[float] = []
    for time_and_std in times_and_stds:
        time = time_and_std[0]
        std = time_and_std[1]
        if std == 0:
            print("Std cannot be ZERO - Dividing by ZERO is forbidden")
            continue

        values.append(callback(time, std))

    return values


def _calculate_sum_time_and_std(matrix: pd.DataFrame) -> Tuple[float, float]:
    _prepare_matrix(matrix)
    critical_path = [matrix[np.logical_and(matrix['Activity-I'] == i, matrix['Activity-J'] == j)]
            .iloc[0].name for i, j in find_critical_paths(matrix)]

    # Get times for critical path and sum them
    time_sum: float = matrix.iloc[:, 5][critical_path].sum()
    # Get variance for critical path, sum them and calculate sqrt
    std: float = np.sqrt(matrix.iloc[:, 6][critical_path].sum())

    return time_sum, std


def _prepare_matrix(matrix: pd.DataFrame) -> None:
    matrix['time'] = matrix.iloc[:, 2:5].apply(_calculate_time_for_rows, axis=1)
    matrix['variance'] = matrix.iloc[:, [2, 4]].apply(_calculate_variance_for_rows, axis=1)


def _calculate_time_for_rows(row_data: List[float]) -> float:
    if len(row_data) != 3:
        raise Exception("Length of array must be equal 3 - formula requires 3 params")

    return (row_data[0] + 4 * row_data[1] + row_data[2]) / 6


def _calculate_variance_for_rows(row_data: List[float]) -> float:
    if len(row_data) != 2:
        raise Exception("Length of array must be equal 2 - formula requires 2 params")

    return ((row_data[1] - row_data[0]) / 6) ** 2
