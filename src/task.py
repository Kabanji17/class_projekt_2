import datetime
from src.base_task import BaseTask
from src.print_mixin import PrintMixin


class Task(BaseTask, PrintMixin):
    name: str
    description: str
    status: str
    created_at: str
    run_time: int

    def __init__(self, name, description, status="Ожидает старта", created_at=None, run_time=0):
        self.name = name
        self.description = description
        self.status = status
        self.__created_at = created_at if created_at else datetime.date.today().strftime("%d.%m.%Y")
        self.run_time = run_time
        super().__init__()

    def __str__(self):
        return f"{self.name}, Статус выполнения: {self.status}, Дата создания: {self.created_at}"

    def __add__(self, other):
        if isinstance(other, Task):
            return self.run_time + other.run_time

        raise TypeError

    @classmethod
    def new_task(cls, name, description, status="Ожидает старта", created_at=None):
        return cls(name, description, status, created_at)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, new_data: str):
        if datetime.datetime.strptime(new_data, "%d.%m.%Y").date() < datetime.datetime.now().date():
            print("Нельзя изменить дату создания на дату из прошлого")
            return
        self.__created_at = new_data


if __name__ == "__main__":
    task_1 = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)
    print(task_1.name, task_1.description, task_1.status, task_1.created_at)

    task_2 = Task.new_task("Купить билеты", "Купить билеты на самолет")
    print(task_2.name, task_2.description, task_2.status, task_2.created_at)
    task_2.created_at = "29.07.2024"

    print(task_1 + task_2)