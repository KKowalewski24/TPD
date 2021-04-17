from typing import Dict, List

import pandas as pd


# Returns Dict of matrix order number and list of indexes of rows in matrix for critical path
def find_critical_paths(prepared_matrices: Dict[int, pd.DataFrame]) -> Dict[int, List[int]]:
    critical_paths: Dict[int, List[int]] = {}
    for matrix in prepared_matrices:
        critical_paths[matrix] = []

    return critical_paths
