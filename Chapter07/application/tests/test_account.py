import pytest
from src.lib.accounts import Account, AccountError

@pytest.fixture
def account():
    return Account(id="A001", name="Thidar", pin="1234")

@pytest.mark.parametrize("pin,expected", [
    pytest.param("1234", True, id="Success Test"),
    pytest.param("1235", False, id="Failure Test"),
    pytest.param("", False, id="Blank String Test"),
    pytest.param(None, False, id="None Test"),
    pytest.param(10, False, id="Other Types Test"),
])
def test_check_pin(account, pin, expected):
    assert account.check_pin(pin) == expected


def test_get_balance(account):
    assert account.get_balance() == 0

@pytest.fixture
def deposit_account(request):
    id, name, pin, amount = request.param
    account = Account(id, name, pin)
    account._balance = amount
    return account

@pytest.mark.parametrize("deposit_account,amount,expected",[
    pytest.param(("001", "Mike", "001", 1000), 1000, 2000, id="Test 1"),
    pytest.param(("001", "Mike", "001", 1001), 1001, 2002, id="Test 2"),
    pytest.param(("001", "Mike", "001", 1002), "1002", 2004, id="Test 3")
], indirect=["deposit_account"])
def test_deposit_success(deposit_account, amount, expected):
    assert deposit_account.deposit(amount) == expected

@pytest.mark.parametrize("amount,expected", [
    pytest.param(0, "Amount must not be Zero.", id="ZERO Failure"),
    pytest.param("0", "Amount must not be Zero.", id="ZERO String Failure"),
    pytest.param(-1, "Amount must not be Minus Value.", id="Minus Failure"),
    pytest.param("-1", "Amount must not be Minus Value.", id="Minus String Failure"),
    pytest.param("", "Amount must be valid integer.", id="String Failure"),
    pytest.param(None, "Amount must not be none.", id="None Failure"),
])
def test_deposit_fails(account, amount, expected):
    with pytest.raises(AccountError) as info:
        account.deposit(amount)
    assert info.value.message == expected


@pytest.fixture(params=[
    pytest.param(("A001", "Mike", "A001", 500_000), id="500,000 Account"),
    pytest.param(("A001", "Mike", "A001", 1_000_000), id="1,000,000 Account"),
])
def withdraw_account(request):
    id, name, pin, amount = request.param
    account = Account(id, name, pin)
    account._balance = amount
    return account

@pytest.mark.parametrize("amount", [
    pytest.param(50_000, id="Integer Value"), 
    pytest.param("100", id="String Value")
])
def test_withdraw_success(withdraw_account, amount):
    balance = withdraw_account.get_balance()
    assert withdraw_account.withdraw(amount) == balance - int(amount)

@pytest.mark.parametrize("amount,expected", [
    pytest.param(0, "Amount must not be Zero.", id="ZERO Failure"),
    pytest.param("0", "Amount must not be Zero.", id="ZERO String Failure"),
    pytest.param(-1, "Amount must not be Minus Value.", id="Minus Failure"),
    pytest.param("-1", "Amount must not be Minus Value.", id="Minus String Failure"),
    pytest.param("", "Amount must be valid integer.", id="String Failure"),
    pytest.param(None, "Amount must not be none.", id="None Failure"),
])
def test_withdraw_failures(account, amount, expected):
    with pytest.raises(AccountError) as exec_info:
        account.withdraw(amount)
    assert exec_info.value.message == expected


@pytest.fixture
def insufficient_account(account)->Account:
    account._balance = 100_000
    return account

@pytest.mark.parametrize("amount", [
    pytest.param(100001, id="Integer Value"), 
    pytest.param("100001", id="String Value")
])
def test_withdraw_insufficient_error(insufficient_account, amount):
    with pytest.raises(AccountError) as exec_info:
        insufficient_account.withdraw(amount)
    assert exec_info.value.message == f"You can't withdraw {amount} from your balance {insufficient_account.get_balance()}."