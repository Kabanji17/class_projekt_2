import datetime
from tests.conftest import task
from src.task import Task



def test_task_init(task):
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"


def test_task_create():
    task = Task("Купить билеты", "Купить билеты на самолет")
    task.name = "Купить билеты"
    task.description = "Купить билеты на самолет"
    task.status = "Ожидает старта"
    task.created_at = datetime.datetime.now().date().strftime("%d.%m.%Y")

def test_task_update(capsys, task):
    task.created_at = "29.07.2024"
    message = capsys.readouterr()
    assert message.out.strip() == "Нельзя изменить дату создания на дату из прошлого"

    task.created_at = datetime.datetime.now().date().strftime("%d.%m.%Y")
    assert task.created_at == datetime.datetime.now().date().strftime("%d.%m.%Y")