import pytest
from tests.conftest import first_user, second_user, task
from src.user import User
from src.task import Task


def test_user_init(first_user, second_user):
    assert first_user.username == "Usr123"
    assert first_user.email == "Vova.Putin@email.com"
    assert len(first_user.task_in_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 5
    assert second_user.all_tasks_count == 5


def test_user_task_list_property(first_user):
    assert first_user.task_list == ('Купить огурцы. Статус выполнения: Ожидает старта. Дата создания: 31.07.2024.\n'
                                    'Купить помидоры. Статус выполнения: Ожидает старта. Дата создания: 31.07.2024.\n')


def test_user_task_list_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3