from typing import Dict, List

import pandas as pd


def prepare_matrices(matrices: Dict[int, pd.DataFrame]) -> Dict[int, pd.DataFrame]:
    for i in range(len(matrices)):
        matrices[i]['time'] = matrices[i].iloc[:, 1:4].apply(_calculate_time, axis=1)
        matrices[i]['variance'] = matrices[i].iloc[:, [1, 3]].apply(_calculate_variance, axis=1)

    return matrices


def _calculate_time(row_data: List[float]) -> float:
    if len(row_data) != 3:
        raise Exception("Length of array must be equal 3 - formula requires 3 params")

    return (row_data[0] + 4 * row_data[1] + row_data[2]) / 6


def _calculate_variance(row_data: List[float]) -> float:
    if len(row_data) != 2:
        raise Exception("Length of array must be equal 2 - formula requires 2 params")

    return ((row_data[1] - row_data[0]) / 6) ** 2
