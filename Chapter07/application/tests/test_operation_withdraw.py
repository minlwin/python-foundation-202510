import pytest
from src.lib.accounts import Account, AccountError
from src.lib.operations import WithdrawOperation

@pytest.fixture
def operation(): 
    account = Account("A001", "A001", "A001")
    account._balance = 100_000
    return WithdrawOperation(account)

@pytest.mark.parametrize("amount", ["50000", "100000"])
def test_success(operation, capsys, monkeypatch, amount):
    monkeypatch.setattr("builtins.input", lambda _:amount)
    operation.operate()
    captured = capsys.readouterr()
    assert captured.out == f"Your balance is {100000 - int(amount)}\n"

@pytest.mark.parametrize("amount,message", [
    pytest.param("", "Amount must be valid integer.", id="Blanck Amount Test"),
    pytest.param("0", "Amount must not be Zero.", id="Zero Amount Test"),
    pytest.param("-1", "Amount must not be Minus Value.", id="Minus Amount Test"),
])
def test_failure_invalid(operation, monkeypatch, amount, message):
    with pytest.raises(AccountError) as info:
        monkeypatch.setattr("builtins.input", lambda _: amount)
        operation.operate()
    assert info.value.message == message    


def test_failure_insulficient(operation, monkeypatch):
    with pytest.raises(AccountError) as info:
        monkeypatch.setattr("builtins.input", lambda _: "100001")
        operation.operate()
    assert info.value.message == "You can't withdraw 100001 from your balance 100000."    
