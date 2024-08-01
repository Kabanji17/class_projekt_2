import json
import os

from src.task import Task
from src.user import User


def read_json(file_path: str) -> dict:
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict):
    users = []
    for user in data:
        tasks = []
        for task in user["task_list"]:
            tasks.append(Task(**task))
        user["task_list"] = tasks
        users.append(User(**user))
    return users


if __name__ == "__main__":
    raw_data = read_json("../data/data.json")
    users_data = create_objects_from_json(raw_data)
    print(users_data[0].username)
