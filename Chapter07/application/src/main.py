from src.lib.accounts import AccountInput, AccountManager
from src.lib.operations import OperationBase, BalanceCheckOperation, DepositOperation, WithdrawOperation

class Application:
    def __init__(self, accounts : list[AccountInput]) -> None:
        self._account_manager = AccountManager(accounts)

    def launch(self):
        _show_message("Welcome to ATM")
        
        self._login_operation()

        while True:
            operation = self._get_operation()
            if operation == None:
                break;
            operation.execute()

        _show_message("Thank You")

    
    def _get_operation(self)->OperationBase:
        print("--------------------------")
        print("Operations")
        for operation in self._operations.values():
            operation.show_menu()
        print()

        menu_id = input("Enter ID : ")
        return self._operations.get(menu_id, None)


    def _login_operation(self):
        account_id = input("Enter ID  : ")
        password = input("Enter PIN : ")
        account = self._account_manager.login(account_id, password)
        self._operations = {ope.id : ope for ope in [
            BalanceCheckOperation(account),
            DepositOperation(account),
            WithdrawOperation(account)
        ]}        
        print()
        

def _show_message(message):
    print("==============================")
    print(message)
    print("==============================")
    print()

if __name__ == "__main__":
    application = Application([
        AccountInput("1001", "Min Lwin", "1234"),
        AccountInput("1002", "Thidar", "1234"),
        AccountInput("1003", "Nilar", "1234"),
    ])
    application.launch()