import pytest

from src.task import Task
from src.user import User


@pytest.fixture
def first_user():
    return User(
        username="Usr123",
        email="Vova.Putin@email.com",
        first_name="Vladimir",
        last_name="Putin",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата")
        ]
    )

@pytest.fixture
def second_user():
    return User(
        username="Usr1234",
        email="Dima.Medvedev@email.com",
        first_name="Dmitriy",
        last_name="Medvedev",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
            Task("Купить укроп", "Купить укроп для салата")
        ]
    )



@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2022")
