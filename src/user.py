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
        self.task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0


if __name__ == "__main__":
    task_1 = Task("Купить огурцы", "Купить огурцы для салата")
    usr_1 = User("Oleg123", "Oleg.Olegov@email.com", "Oleg", "Olegov", [task_1])