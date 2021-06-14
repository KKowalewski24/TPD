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
