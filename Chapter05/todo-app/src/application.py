from src.operation import Operation

class Application:
    def __init__(self, name:str, operations:list[Operation]) -> None:
        self.name = name
        self.operations = operations

    @staticmethod
    def show_message(message:str):
        pass

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
