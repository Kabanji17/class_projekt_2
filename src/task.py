import datetime


class Task:
    name: str
    description: str
    status: str
    created_at: str

    def __init__(self, name, description, status="Ожидает старта", created_at=None):
        self.name = name
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.date.today().strftime("%d.%m.%Y")


if __name__ == "__main__":
    task_1 = Task("Купить огурцы", "Купить огурцы для салата")
    print(task_1.name, task_1.description, task_1.status, task_1.created_at)