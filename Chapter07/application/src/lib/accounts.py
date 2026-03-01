from collections import namedtuple

class Account:
    def __init__(self, id:str, name: str, pin: str):
        self._id = id
        self._pin = pin
        self._balance = 0
        self.name = name

    def checkPin(self, pin : str):
        return self._pin == pin
    
    def getBalance(self):
        return self._balance
    
    def deposit(self, amount: int):
        self._balance += amount
        return self._balance

AccountInput = namedtuple('AccountInput', ["id", "name", "pin"])

class AccountError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class AccountManager:
    def __init__(self, accounts : list[AccountInput]):
        self._storage = {input.id : Account(**input) for input in accounts}

    def login(self, id: str, pin : str):
        account = self._storage.get(id)
        
        if account == None:
            raise AccountError("Invalid account id.")
        
        if not account.checkPin(pin):
            raise AccountError("Invalid PIN Number")
        
        return account

