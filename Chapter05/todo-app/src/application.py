from abc import abstractmethod, ABC

_MESSAGE_FMT = """
================================
{}
================================
"""

class Application:
    def __init__(self, name:str, operations:list[Operation]) -> None:
        self.name = name
        self.operations = operations

    @staticmethod
    def show_message(message:str):
        print(_MESSAGE_FMT.format(message))

    def get_operation(self):
        print("Select Operation")
        for operation in self.operations:
            print(f"{operation.id}. {operation.name}")

        selected_id = input("\nSelected ID : ")

        for operation in self.operations:
            if operation.id == int(selected_id):
                return operation

    def start(self):
        Application.show_message(self.name)

        while True:
            operation = self.get_operation()
            if operation == None:
                break
            operation.execute()
        
        Application.show_message("Thank You")

class Operation(ABC):

    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name

    def execute(self):
        print(f"{self.id}. {self.name}")
        self.do_business()
        print("\n")

    @abstractmethod
    def do_business(self):
        pass