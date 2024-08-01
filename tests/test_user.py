import pytest

from src.task import Task
from src.user import User
from tests.conftest import first_user, second_user, task


def test_user_init(first_user, second_user):
    assert first_user.username == "Usr123"
    assert first_user.email == "Vova.Putin@email.com"
    assert len(first_user.task_in_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 5
    assert second_user.all_tasks_count == 5


def test_user_task_list_property(first_user):
    assert first_user.task_list == (
        "Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 31.07.2024\n"
        "Купить помидоры, Статус выполнения: Ожидает старта, Дата создания: 31.07.2024\n"
    )


def test_user_task_list_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3


def test_user_str(first_user, second_user):
    assert str(first_user) == "Putin Vladimir, Email: Vova.Putin@email.com, Всего задач в списке: 2"
    assert str(second_user) == "Medvedev Dmitriy, Email: Dima.Medvedev@email.com, Всего задач в списке: 3"

def test_task_iterator(task_iterator):
    iter(task_iterator)
    assert task_iterator.index == 0
    assert next(task_iterator).name == "Купить огурцы"
    assert next(task_iterator).name == "Купить помидоры"
    assert next(task_iterator).name == "Купить укроп"

    with pytest.raises(StopIteration):
        next(task_iterator)
