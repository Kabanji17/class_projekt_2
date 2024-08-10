import pytest

from src.task import Task
from src.user import User
from src.task_iterator import TaskIterator
from src.periodic_task import PeriodicTask
from src.dedline_task import DeadlineTask


@pytest.fixture
def first_user():
    return User(
        username="Usr123",
        email="Vova.Putin@email.com",
        first_name="Vladimir",
        last_name="Putin",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", created_at="31.07.2024"),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="31.07.2024"),
        ],
    )


@pytest.fixture
def second_user():
    return User(
        username="Usr1234",
        email="Dima.Medvedev@email.com",
        first_name="Dmitriy",
        last_name="Medvedev",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", created_at="31.07.2024"),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="31.07.2024"),
            Task("Купить укроп", "Купить укроп для салата", created_at="31.07.2024"),
        ],
    )


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2022")


@pytest.fixture
def task_with_runtime1():
    return Task("Купить помидоры", "Купить помидоры для салата", created_at="20.04.2022", run_time=60)


@pytest.fixture
def task_with_runtime2():
    return Task("Купить перец", "Купить перец для салата", created_at="20.04.2022", run_time=70)


@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)


@pytest.fixture
def task_periodic_1():
    return PeriodicTask("Купить водку", "Купить спиртное на праздник", "09.08.2024", "10.08.2024", run_time=60)


@pytest.fixture
def task_periodic_2():
    return PeriodicTask("Купить виски", "Купить спиртное на праздник", "09.08.2024", "10.08.2024", run_time=90)


@pytest.fixture
def task_deadline_1():
    return DeadlineTask("Купить пиво", "Купить спиртное на праздник", "11.08.2024", run_time=60)


@pytest.fixture
def task_deadline_2():
    return DeadlineTask("Купить шампанское", "Купить спиртное на праздник", "12.08.2024", run_time=90)