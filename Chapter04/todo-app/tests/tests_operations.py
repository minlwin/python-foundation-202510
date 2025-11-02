import pytest 
from src.operations import show_all, tasks

def test_show_all(capsys : pytest.CaptureFixture[str]):
    global tasks 
    tasks = {}
    show_all()
    sysout = capsys.readouterr()
    assert sysout.out == "Task List\n------------------------\nThere is no tasks\n------------------------\n"
