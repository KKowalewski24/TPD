from random import expovariate


class Task:
    def __init__(self, start_time, handling_time):
        self.start_time = start_time
        self.handling_time = handling_time
        self.end_time = None
        self.consumed_time = 0
        self.priority = 0

    def handle(self, current_time, spent_time):
        self.consumed_time += spent_time
        if self.consumed_time >= self.handling_time:
            self.end_time = current_time

    def update_priority(self, current_time, coef):
        self.priority = (current_time - self.start_time) * coef



def generate_tasks(mean_break_time, mean_handling_time, number_of_tasks):
    tasks = [] 
    last_start_time = 0.0
    for i in range(number_of_tasks):
        start_time = last_start_time + expovariate(1.0 / mean_break_time)
        handling_time = expovariate(1.0 / mean_handling_time)
        tasks.append(Task(start_time, handling_time))
        last_start_time = start_time
    return tasks


# parameters
alpha = 1
beta = 1
mean_break_time = 3
mean_handling_time = 5

# lists of tasks
tasks = generate_tasks(mean_break_time, mean_handling_time, int(input("Number of tasks:")))
waiting_tasks = []
handled_tasks = []
done_tasks = []

# main loop (1 loop equals 1 second)
time = 0
DELTA = 1
while tasks[-1].end_time is None:
    time += DELTA

    # add new tasks to 'waiting'
    waiting_tasks += [task for task in tasks if task.start_time >= time]

    # update priorities
    for task in waiting_tasks:
        task.update_priority(time, alpha)
    for task in handled_tasks:
        task.update_priority(time, beta)

    # move tasks from 'waiting' to 'handled'
    min_handled_priority = min((task.priority for task in handled_tasks), default=0)
    handled_tasks += [task for task in waiting_tasks if task.priority >= min_handled_priority]
    waiting_tasks = [task for task in waiting_tasks if task.priority < min_handled_priority]

    # handle tasks (round robin)
    for task in handled_tasks:
        task.handle(time, DELTA / len(handled_tasks))

    # move tasks from 'handled' to 'done'
    done_tasks += [task for task in handled_tasks if task.end_time is not None]
    handled_tasks = [task for task in handled_tasks if task.end_time is None]

    print("{}: {}/{}".format(time, len(done_tasks), len(tasks)))
