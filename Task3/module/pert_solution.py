from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy.stats import norm

from module.cpm_solution import find_critical_path


# Returns order number of more probable variant and probability value
def calculate_probability_and_variant(matrices: Dict[int, pd.DataFrame],
                                      expected_time: float) -> Tuple[int, float]:
    times_and_stds: Dict[int, Tuple[float, float]] = _calculate_times_and_stds(matrices)
    probabilities: Dict[int, float] = {}

    for time_and_std in times_and_stds:
        time: float = times_and_stds[time_and_std][0]
        std: float = times_and_stds[time_and_std][1]
        if std == 0:
            print("Std cannot be ZERO - Dividing by ZERO is forbidden")
            continue

        probabilities[time_and_std] = norm.cdf((expected_time - time) / std)

    max_probability_key: int = max(probabilities, key=probabilities.get)
    return max_probability_key, probabilities[max_probability_key]


# Returns order number of matrix and time value for each
def calculate_completion_time(matrices: Dict[int, pd.DataFrame],
                              expected_probability: float) -> Dict[int, float]:
    print(norm.ppf(0.99))
    return {-5: -0.5}


# Returns Dict of matrix order number and tuple of summed time and standard deviation
def _calculate_times_and_stds(matrices: Dict[int, pd.DataFrame]) -> Dict[int, Tuple[float, float]]:
    prepared_matrices: Dict[int, pd.DataFrame] = _prepare_matrices(matrices)
    critical_paths: Dict[int, List[int]] = find_critical_path(prepared_matrices)
    times_and_stds: Dict[int, Tuple[float, float]] = {}

    # Iterate over matrices order number
    for critical_path in critical_paths:
        # Get times for critical path and sum them
        time_sum: float = prepared_matrices[critical_path].iloc[:, 4][
            critical_paths[critical_path]].sum()
        # Get variance for critical path, sum them and calculate sqrt
        std: float = np.sqrt(
            prepared_matrices[critical_path].iloc[:, 5][critical_paths[critical_path]].sum()
        )
        times_and_stds[critical_path] = (time_sum, std)

    return times_and_stds


# Returns original DataFrame with added two columns
def _prepare_matrices(matrices: Dict[int, pd.DataFrame]) -> Dict[int, pd.DataFrame]:
    for i in range(len(matrices)):
        matrices[i]['time'] = matrices[i].iloc[:, 1:4].apply(_calculate_time_for_rows, axis=1)
        matrices[i]['variance'] = matrices[i].iloc[:, [1, 3]].apply(
            _calculate_variance_for_rows, axis=1
        )

    return matrices


def _calculate_time_for_rows(row_data: List[float]) -> float:
    if len(row_data) != 3:
        raise Exception("Length of array must be equal 3 - formula requires 3 params")

    return (row_data[0] + 4 * row_data[1] + row_data[2]) / 6


def _calculate_variance_for_rows(row_data: List[float]) -> float:
    if len(row_data) != 2:
        raise Exception("Length of array must be equal 2 - formula requires 2 params")

    return ((row_data[1] - row_data[0]) / 6) ** 2
