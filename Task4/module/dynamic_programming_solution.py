from typing import Dict, List, Tuple

import pandas as pd


def find_optimal_strategy(process_table: pd.DataFrame) -> Tuple[List[str], float]:
    graph = _build_graph(process_table)
    stages = _get_stages_number(process_table)

    for stage in reversed(stages):
        for node in reversed(graph):
            if graph[node]["stage"] == stage:
                before_items = graph[node]["before"]
                after_items = _get_dict_when_no_neighbours(graph[node]["after"], node)
                for after in after_items:
                    print(after, end=" ")
                    print(after_items[after])

    return [""], 1


# Returns passed dict if it is not empty, otherwise it returns new dict with
# node_number and ZERO value of loss
def _get_dict_when_no_neighbours(neighbours: Dict[int, float],
                                 node_number: int) -> Dict[int, float]:
    if bool(neighbours):
        return neighbours
    return {node_number: 0}


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
