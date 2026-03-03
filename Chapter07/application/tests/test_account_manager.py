import pytest
from src.lib.accounts import AccountManager, AccountInput, AccountError

INPUTS = [
    AccountInput(id="A001", name="User1", pin="user1"),
    AccountInput(id="A002", name="User2", pin="user2"),
    AccountInput(id="A003", name="User3", pin="user3"),
]

@pytest.fixture
def manager()->AccountManager:
    return AccountManager(INPUTS)

@pytest.mark.parametrize("id,name,pin", [ input for input in INPUTS ])
def test_login_success(manager, id, name, pin):
    account = manager.login(id=id, pin=pin)
    assert account.name == name


@pytest.mark.parametrize("id,pin,expected", [
    pytest.param(None, "aaa", "Please enter Account ID.", id="None ID Test"),
    pytest.param("", "aaa", "Please enter Account ID.", id="Blank ID Test"),
    pytest.param("a001", "aaa", "Please check your ID.", id="Invalid ID Test"),
    pytest.param("A001", None, "Please enter PIN.", id="None PIN Test"),
    pytest.param("A002", "", "Please enter PIN.", id="Blank PIN Test"),
    pytest.param("A003", "User3", "Please check your PIN.", id="Invalid PIN Test"),
])
def test_login_failure(manager, id, pin, expected):
    with pytest.raises(AccountError) as info:
        manager.login(id, pin)
    assert info.value.message == expected