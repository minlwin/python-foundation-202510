import pytest 
import src.operations

def test_show_all_notasks(capsys : pytest.CaptureFixture[str]):
    src.operations.tasks = {}
    src.operations.show_all()
    sysout = capsys.readouterr()
    assert sysout.out == "Task List\n------------------------\nThere is no tasks\n------------------------\n"

def test_show_all_hastask(capsys : pytest.CaptureFixture[str]):
    src.operations.tasks = {1 : "Hello Task"}
    src.operations.show_all()
    sysout = capsys.readouterr()
    assert sysout.out == "Task List\n------------------------\n1. Hello Task\n------------------------\n"
