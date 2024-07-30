import pytest
from tests.conftest import task



def test_task_init(task):
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "20.04.2022"