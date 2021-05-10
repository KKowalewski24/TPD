from typing import Dict, List, Tuple

import pandas as pd


def find_optimal_strategy(process_table: pd.DataFrame) -> Tuple[List[int], float]:
    graph = _build_graph(process_table)

    for node in reversed(graph):
        if len(graph[node]["after"]) > 0:
            graph[node]["min_losses"] = min(
                [graph[node]["after"][after] + graph[after]["min_losses"]
                 for after in graph[node]["after"]]
            )
        else:
            graph[node]["min_losses"] = 0

    return [], graph[1]["min_losses"]


def _build_graph(process_table: pd.DataFrame) -> Dict:
    graph = {}
    for index, row in process_table.iterrows():
        initial_state, end_state, losses = (
            int(row["initial_state"]), int(row["end_state"]), float(row["losses"])
        )

        if initial_state not in graph:
            graph[initial_state] = {"before": {}, "after": {}}
        if end_state not in graph:
            graph[end_state] = {"before": {}, "after": {}}

        graph[initial_state]["after"][end_state] = losses
        graph[end_state]["before"][initial_state] = losses

    return graph
