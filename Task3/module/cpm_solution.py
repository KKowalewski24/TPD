from typing import List

import pandas as pd


def find_critical_paths(matrix: pd.DataFrame) -> List[int]:
    # represent graph as dictionary
    graph = {}
    for index, row in matrix.iterrows():
        i, j, time = (int(row['Activity-I']), int(row['Activity-J']),
                      float(row['time']))
        if i not in graph:
            graph[i] = {'t0': None, 't1': None, 'before': {}, 'after': {}}
        if j not in graph:
            graph[j] = {'t0': None, 't1': None, 'before': {}, 'after': {}}
        graph[i]['after'][j] = time
        graph[j]['before'][i] = time

    # calculate t0 and t1 (assume that nodes are numbered correctly)
    nodes_numbers = sorted(graph)
    graph[nodes_numbers[0]]['t0'] = 0
    for j in nodes_numbers[1:]:
        graph[j]['t0'] = max(
            [graph[i]['t0'] + t for i, t in graph[j]['before'].items()])

    nodes_numbers = list(reversed(nodes_numbers))
    graph[nodes_numbers[0]]['t1'] = graph[nodes_numbers[0]]['t0']
    for i in nodes_numbers[1:]:
        graph[i]['t1'] = min(
            [graph[j]['t1'] - t for j, t in graph[i]['after'].items()])

    # calculate total reserve
    for i in graph:
        graph[i]['total_reserve'] = {
            j: graph[j]['t1'] - graph[i]['t0'] - t
            for j, t in graph[i]['after'].items()
        }

    # calculate critical path
    critical_path = []
    for i in sorted(graph):
        for j in graph[i]['total_reserve']:
            if graph[i]['total_reserve'][j] == 0 and (
                    len(critical_path) == 0 or critical_path[-1][1] == i):
                critical_path.append((i, j))

    return critical_path


if __name__ == '__main__':
    df = pd.DataFrame.from_dict({
        'Activity-I': [1, 1, 2, 2, 3, 4, 4, 5],
        'Activity-J': [2, 3, 4, 5, 5, 5, 6, 6],
        'time': [5, 7, 6, 8, 3, 4, 2, 5]
    })
    print(find_critical_paths(df))
