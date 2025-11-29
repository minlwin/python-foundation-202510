from typing import Protocol

class BankingModule(Protocol):
    def transfer(self, fromAccount:str, toAccount:str, amount:int) -> None:
        ...

class Bank:

    def __init__(self, banking:BankingModule) -> None:
        self.banking = banking

    def transfer(self, fromAccount:str, toAccount:str, amount:int):
        print("Checking Transaction")
        self.banking.transfer(fromAccount, toAccount, amount)
        print("Transaction End")

class OfflineBanking():
    def transfer(self, fromAccount: str, toAccount: str, amount: int) -> None:
        print(f"{amount} is transfer from {fromAccount} to {toAccount} via offline banking")

class OnlineBanking():
    def transfer(self, fromAccount: str, toAccount: str, amount: int) -> None:
        print(f"{amount} is transfer from {fromAccount} to {toAccount} via online banking")
        

if __name__ == "__main__":
    myBank = Bank(OnlineBanking())
    myBank.transfer("Account A", "Account B", 1000)