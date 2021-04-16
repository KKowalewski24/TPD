from typing import Dict, List

import pandas as pd


# Returns Dict of matrix order number and list of indexes of rows in matrix for critical path
def find_critical_path(matrices: Dict[int, pd.DataFrame]) -> Dict[int, List[int]]:
    # TODO
    return {0: [1, 2], 1: [3, 4]}
