from src.task import Task
from src.periodic_task import PeriodicTask
from src.deadline_task import DeadlineTask


def test_print_mixin(capsys):
    Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2022")
    message = capsys.readouterr()
    assert message.out.strip() == 'Task(Купить огурцы, Купить огурцы для салата, Ожидает старта, 20.04.2022)'

    PeriodicTask("Купить водку", "Купить спиртное на праздник", "09.08.2024", "10.08.2024", run_time=60)
    message = capsys.readouterr()
    assert message.out.strip() == "PeriodicTask(Купить водку, Купить спиртное на праздник, Ожидает старта, 11.08.2024)"

    DeadlineTask("Купить пиво", "Купить спиртное на праздник", "11.08.2024", run_time=60)
    message = capsys.readouterr()
    assert message.out.strip() == "DeadlineTask(Купить пиво, Купить спиртное на праздник, Ожидает старта, 11.08.2024)"