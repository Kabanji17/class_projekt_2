from src.task import Task


class PeriodicTask(Task):
    def __init__(self, name, description, start_date, end_date, status="Ожидает старта", created_at=None, run_time=0,
    frequency="Ежедневная"):
        super().__init__(name, description, status, created_at, run_time)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def __add__(self, other):
        if isinstance(other, PeriodicTask):
            return self.run_time + other.run_time

        raise TypeError



if __name__ == "__main__":
    per_task = PeriodicTask("Купить водку", "Купить спиртное на праздник", "09.08.2024", "10.08.2024", run_time=60)
    print(per_task.name)
    print(per_task.description)
    print(per_task.start_date)
    print(per_task.frequency)
    print(per_task.end_date)
    print(per_task.status)

    per_task_2 = PeriodicTask("Купить виски", "Купить спиртное на праздник", "09.08.2024", "10.08.2024", run_time=60)

    print(per_task + per_task_2)