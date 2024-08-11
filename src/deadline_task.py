from src.task import Task


class DeadlineTask(Task):

    def __init__(self, name, description, deadline, status="Ожидает старта", created_at=None, run_time=0):
        super().__init__(name, description, status, created_at, run_time)
        self.deadline = deadline

    def __add__(self, other):
        if isinstance(other, DeadlineTask):
            return self.run_time + other.run_time

        raise TypeError
