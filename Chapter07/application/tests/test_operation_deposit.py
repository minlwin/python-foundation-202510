import pytest
from src.lib.accounts import Account, AccountError
from src.lib.operations import DepositOperation

@pytest.fixture
def operation():
    account = Account("A001", "A001", "A001")
    return DepositOperation(account)

def test_deposit_success(operation, capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "10000")
    operation.operate()
    captured = capsys.readouterr()
    assert captured.out == "Your balance is 10000\n"

@pytest.mark.parametrize("amount,message", [
    pytest.param("", "Amount must be valid integer.", id="Blanck Amount Test"),
    pytest.param("0", "Amount must not be Zero.", id="Zero Amount Test"),
    pytest.param("-1", "Amount must not be Minus Value.", id="Minus Amount Test"),
])
def test_deposit_failures(operation, monkeypatch, amount, message):
    with pytest.raises(AccountError) as info:
        monkeypatch.setattr("builtins.input", lambda _: amount)
        operation.operate()
    assert info.value.message == message