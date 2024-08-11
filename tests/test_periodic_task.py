from datetime import datetime

import pytest


def test_periodic_task_init(task_periodic_1):
    assert task_periodic_1.name == "Купить водку"
    assert task_periodic_1.description == "Купить спиртное на праздник"
    assert task_periodic_1.status == "Ожидает старта"
    assert task_periodic_1.created_at == datetime.now().date().strftime("%d.%m.%Y")
    assert task_periodic_1.start_date == "09.08.2024"
    assert task_periodic_1.end_date == "10.08.2024"
    assert task_periodic_1.frequency == "Ежедневная"


def test_periodic_task_add(task_periodic_1, task_periodic_2):
    assert task_periodic_1 + task_periodic_2 == 150


def test_periodic_task_add_invalid(task_periodic_1, task_periodic_2):
    with pytest.raises(TypeError):
        result = task_periodic_1 + 1
        result = task_periodic_2 + 2
