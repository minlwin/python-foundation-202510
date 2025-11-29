from abc import ABC, abstractmethod

class Operation(ABC):

    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name

    def execute(self):
        print(f"{self.id}. {self.name}")
        print("------------------------")
        self.do_business()
        print("------------------------\n")

    @abstractmethod
    def do_business(self):
        pass

class ShowAllTasks(Operation):
    def __init__(self) -> None:
        super().__init__(1, "Show All Task")

    def do_business(self):
        return
    
class CreateTask(Operation):
    def __init__(self) -> None:
        super().__init__(2, "Create Task")

    def do_business(self):
        return