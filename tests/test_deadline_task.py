from datetime import datetime

import pytest


def test_deadline_task_init(task_deadline_1):
    assert task_deadline_1.name == "Купить пиво"
    assert task_deadline_1.description == "Купить спиртное на праздник"
    assert task_deadline_1.status == "Ожидает старта"
    assert task_deadline_1.created_at == datetime.now().date().strftime("%d.%m.%Y")
    assert task_deadline_1.deadline == "11.08.2024"


def test_deadline_task_add(task_deadline_1, task_deadline_2):
    assert task_deadline_1 + task_deadline_2 == 150


def test_deadline_task_add_invalid(task_deadline_1, task_deadline_2):
    with pytest.raises(TypeError):
        result = task_deadline_1 + 1
        result = task_deadline_2 + 2
