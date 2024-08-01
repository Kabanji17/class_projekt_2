from src.task import Task


class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

    def __str__(self):
        return f"{self.last_name} {self.first_name}, Email: {self.email}, Всего задач в списке: {len(self.__task_list)}"

    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{str(task)}\n"
        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        self.__task_list.append(task)
        User.all_tasks_count += 1

    @property
    def task_in_list(self):
        return self.__task_list


if __name__ == "__main__":
    task_1 = Task("Купить огурцы", "Купить огурцы для салата")
    usr_1 = User("Oleg123", "Oleg.Olegov@email.com", "Oleg", "Olegov", [task_1])

    print(usr_1.task_list)
    print(User.all_tasks_count)

    task_2 = Task("Купить лук", "Купить лук для салата")
    usr_1.task_list = task_2

    print(usr_1.task_list)
    print(User.all_tasks_count)

    print(usr_1)