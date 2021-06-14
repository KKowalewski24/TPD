import argparse
import subprocess
import sys
from random import expovariate

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDRegressor

from module.Task import Task

"""
python main.py -e 1000 1 1 10 5 -e 1000 2 1 10 5 -e 1000 4 1 10 5 -e 1000 8 1 10 5 -e 1000 0 0 10 5
python main.py -e 1000 1 1 6 5 -e 1000 2 1 6 5 -e 1000 4 1 6 5 -e 1000 8 1 6 5 -e 1000 0 0 6 5
python main.py -e 1000 1 1 2 5 -e 1000 2 1 2 5 -e 1000 4 1 2 5 -e 1000 8 1 2 5 -e 1000 0 0 2 5
"""


# MAIN ----------------------------------------------------------------------- #
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", action="append", nargs=5,
        metavar=["n_tasks", "alpha", "beta", "mean_break_time", "mean_handling_time"],
        type=int, required=True
    )
    args = parser.parse_args()

    results = []
    min_handling_time = 100000000
    max_handling_time = 0
    for n_tasks, alpha, beta, mean_break_time, mean_handling_time in args.e:
        done_tasks = make_simulation(n_tasks, alpha, beta, mean_break_time, mean_handling_time)
        handling_times = np.array([task.handling_time for task in done_tasks])
        waiting_times = np.array(
            [task.end_time - task.start_time - task.handling_time for task in done_tasks]
        )

        regressor = SGDRegressor()
        regressor.fit(np.reshape(handling_times, (-1, 1)), waiting_times)
        results.append((regressor, "a={}, b={}".format(alpha, beta)))

        if min_handling_time > min(handling_times):
            min_handling_time = min(handling_times)

        if max_handling_time < max(handling_times):
            max_handling_time = max(handling_times)

    for regressor, label in results:
        plt.plot(
            [min_handling_time, max_handling_time],
            regressor.predict(np.reshape([min_handling_time, max_handling_time], (-1, 1))),
            label=label
        )

    plt.legend()
    plt.show()

    display_finish()


# DEF ------------------------------------------------------------------------ #
def generate_tasks(mean_break_time, mean_handling_time, number_of_tasks):
    tasks = set()
    last_start_time = 0.0
    for i in range(number_of_tasks):
        start_time = last_start_time + expovariate(1.0 / mean_break_time)
        handling_time = expovariate(1.0 / mean_handling_time)
        tasks.add(Task(start_time, handling_time))
        last_start_time = start_time
    return tasks


def make_simulation(number_of_tasks, alpha, beta, mean_break_time, mean_handling_time):
    print("\n\n--------START---------")
    # lists of tasks
    tasks = generate_tasks(mean_break_time, mean_handling_time, number_of_tasks)
    waiting_tasks = set()
    handled_tasks = set()
    done_tasks = set()

    # main loop (1 loop equals 1 second)
    time = 0
    DELTA = 1
    while len(done_tasks) != number_of_tasks:
        time += DELTA

        # move tasks from 'tasks' to 'waiting'
        waiting_tasks |= {task for task in tasks if task.start_time <= time}
        tasks -= waiting_tasks

        # update priorities
        for task in waiting_tasks:
            task.update_priority(time, alpha)
        for task in handled_tasks:
            task.update_priority(time, beta)

        # move tasks from 'waiting' to 'handled'
        min_handled_priority = min((task.priority for task in handled_tasks), default=0)
        handled_tasks |= {task for task in waiting_tasks if task.priority >= min_handled_priority}
        waiting_tasks -= handled_tasks

        # handle tasks (round robin)
        for task in handled_tasks:
            task.handle(time, DELTA / len(handled_tasks))

        # move tasks from 'handled' to 'done'
        done_tasks |= {task for task in handled_tasks if task.end_time is not None}
        handled_tasks -= done_tasks

        print("{}: {}/{}".format(time, len(done_tasks), number_of_tasks))

    return done_tasks


# UTIL ----------------------------------------------------------------------- #
def check_types_check_style() -> None:
    subprocess.call(["mypy", "."])
    subprocess.call(["flake8", "."])


def compile_to_pyc() -> None:
    subprocess.call(["python", "-m", "compileall", "."])


def check_if_exists_in_args(arg: str) -> bool:
    return arg in sys.argv


def display_finish() -> None:
    print("------------------------------------------------------------------------")
    print("FINISHED")
    print("------------------------------------------------------------------------")


# __MAIN__ ------------------------------------------------------------------- #
if __name__ == "__main__":
    if check_if_exists_in_args("-t"):
        check_types_check_style()
    elif check_if_exists_in_args("-b"):
        compile_to_pyc()
    else:
        main()
