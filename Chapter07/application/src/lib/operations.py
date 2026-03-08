from abc import ABC, abstractmethod
from src.lib.accounts import Account

class OperationBase(ABC):
    counter = 0

    def __init__(self, name:str, account:Account):
        super().__init__()
        self.id = OperationBase.generateId()
        self.name = name
        self.account = account

    def show_menu(self):
        print(f"{self.id}. {self.name}")

    def execute(self):
        print("--------------------------")
        print(f"{self.id}. {self.name}")
        print()
        self.operate()
        print()

    @abstractmethod
    def operate(self):
        pass

    @classmethod
    def generateId(cls):
        cls.counter += 1
        return str(cls.counter)
    
class BalanceCheckOperation(OperationBase):

    def __init__(self, account):
        super().__init__("Check Balance", account)

    def operate(self):
        print(f"Your balance is {self.account.get_balance()}")
    
class DepositOperation(OperationBase):

    def __init__(self, account):
        super().__init__("Deposit", account)

    def operate(self):
        amount = input("Enter Amount : ")
        balance = self.account.deposit(amount)
        print(f"Your balance is {self.account.get_balance()}")
    
class WithdrawOperation(OperationBase):

    def __init__(self, account):
        super().__init__("Withdraw", account)

    def operate(self):
        amount = input("Enter Amount : ")
        balance = self.account.withdraw(amount)
        print(f"Your balance is {self.account.get_balance()}")
