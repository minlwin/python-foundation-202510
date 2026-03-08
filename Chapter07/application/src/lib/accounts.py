from collections import namedtuple

class Account:
    def __init__(self, id:str, name: str, pin: str):
        self._id = id
        self._pin = pin
        self._balance = 0
        self.name = name

    def check_pin(self, pin : str):
        return self._pin == pin
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += self._check_amount(amount)
        return self._balance

    def withdraw(self, amount):
        withdraw_amount = self._check_amount(amount)

        if withdraw_amount > self._balance:
            raise AccountError(f"You can't withdraw {amount} from your balance {self._balance}.")

        self._balance -= withdraw_amount
        return self._balance
    
    @staticmethod
    def _check_amount(amount):

        if amount == None:
            raise AccountError("Amount must not be none.")

        try:
            value = int(amount)

            if value == 0:
                raise AccountError("Amount must not be Zero.")
            
            if value < 0:
                raise AccountError("Amount must not be Minus Value.")

            return value
        except ValueError:
            raise AccountError("Amount must be valid integer.")


AccountInput = namedtuple('AccountInput', ["id", "name", "pin"])

class AccountError(Exception):
    def __init__(self, message):
        self.message = message

class AccountManager:
    def __init__(self, accounts : list[AccountInput]):
        self._storage = {input.id : Account(*input) for input in accounts}

    def login(self, id: str, pin : str):
        if id == None or id == '':
            raise AccountError("Please enter Account ID.")
        
        if pin == None or pin == '':
            raise AccountError("Please enter PIN.")
        
        account = self._storage.get(id)
        
        if account == None:
            raise AccountError("Please check your ID.")
        
        if not account.check_pin(pin):
            raise AccountError("Please check your PIN.")
        
        return account

