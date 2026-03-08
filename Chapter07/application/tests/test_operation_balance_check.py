import pytest

from src.lib.accounts import Account
from src.lib.operations import BalanceCheckOperation

@pytest.fixture
def operation():
    account = Account("1001", "A001", "1001")
    account._balance = 100_000
    return BalanceCheckOperation(account)

def test_operation(operation, capsys):
    operation.operate()
    captcured = capsys.readouterr()
    assert captcured.out == "Your balance is 100000\n"