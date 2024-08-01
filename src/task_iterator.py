from src.task import Task
from src.user import User


class TaskIterator():

    def __init__(self, user_obj):
        self.user = user_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.user.task_in_list):
            task = self.user.task_in_list[self.index]
            self.index += 1
            return task
        else:
            raise StopIteration

if __name__ == "__main__":
    task_1 = Task("Купить огурцы", "Купить огурцы для салата")
    usr_1 = User("Oleg123", "Oleg.Olegov@email.com", "Oleg", "Olegov", [task_1])
    task_2 = Task("Купить лук", "Купить лук для салата")
    usr_1.task_list = task_2

    iterator = TaskIterator(usr_1)

    for task in iterator:
        print(task)
    print()
    for task in iterator:
        print(task)