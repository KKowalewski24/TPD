from typing import Dict, List

import pandas as pd


# Returns Dict of matrix order number and list of indexes of rows in matrix for critical path
def find_critical_paths(matrices: Dict[int, pd.DataFrame]) -> Dict[int, List[int]]:
    _insert_earliest_and_latest_times(matrices)
    _insert_total_time_left(matrices)

    critical_paths: Dict[int, List[int]] = {}
    for matrix in matrices:
        df: pd.DataFrame = matrices[matrix]
        # Add indexes in which total time left is equals to 0
        critical_paths[matrix] = df.index[df.iloc[:, 11] == 0].tolist()

    return critical_paths


def _insert_earliest_and_latest_times(matrices: Dict[int, pd.DataFrame]) -> None:
    # TODO
    for matrix in matrices:
        matrices[matrix]["t_0_i"] = 1
        matrices[matrix]["t_1_i"] = 1
        matrices[matrix]["t_0_j"] = 1
        matrices[matrix]["t_1_j"] = 1


def _insert_total_time_left(matrices: Dict[int, pd.DataFrame]) -> None:
    for matrix in matrices:
        matrices[matrix]["Z_c"] = matrices[matrix].iloc[:, [5, 7, 10]].apply(
            _calculate_total_time_left, axis=1
        )


def _calculate_total_time_left(row_data: List[float]) -> float:
    if len(row_data) != 3:
        raise Exception("Length of array must be equal 3 - formula requires 3 params")

    return row_data[2] - row_data[1] - row_data[0]
