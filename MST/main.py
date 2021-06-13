from argparse import ArgumentParser, Namespace

import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree


def main() -> None:
    args = prepare_args()
    graph_matrix: np.ndarray = np.loadtxt(args.filename)
    print("graph_matrix")
    print(graph_matrix, end="\n\n")

    tree = minimum_spanning_tree(graph_matrix)
    print(tree)


def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "-f", "--filename", required=True, type=str, help="Filename of matrix"
    )
    return arg_parser.parse_args()


if __name__ == "__main__":
    main()
