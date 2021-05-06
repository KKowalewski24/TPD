from typing import Dict, List, Tuple

import pandas as pd


def find_optimal_strategy(process_table: pd.DataFrame) -> Tuple[List[str], float]:
    graph = _build_graph(process_table)

    stages = _get_stages_number(process_table)
    for stage in reversed(stages):
        for node in graph:
            if graph[node]["stage"] == stage:
                print(node, end=" ")
                print(graph[node])

    return [""], 1


def _build_graph(process_table: pd.DataFrame) -> Dict:
    graph = {}
    for index, row in process_table.iterrows():
        stage, initial_state, end_state, losses = (
            int(row["stage"]), int(row["initial_state"]),
            int(row["end_state"]), float(row["losses"])
        )

        if initial_state not in graph:
            graph[initial_state] = {"before": {}, "after": {}, "stage": stage}
        if end_state not in graph:
            graph[end_state] = {"before": {}, "after": {}, "stage": stage}

        graph[initial_state]["after"][end_state] = losses
        graph[end_state]["before"][initial_state] = losses

    return graph


def _get_stages_number(process_table: pd.DataFrame) -> List[int]:
    return process_table["stage"].unique()
