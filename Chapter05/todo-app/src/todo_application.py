from enum import Enum
from src.application import Operation, Application

class Status(Enum):
    Created = "0"
    Done = "1"
    Cancel = "2" 

class Task:
    _current_id = 0

    def __init__(self, name:str) -> None:
        self.__class__._current_id = self.__class__._current_id + 1
        self.id = self.__class__._current_id
        self.name = name
        self.status = Status.Created

class TaskManager:
    _instance:TaskManager | None = None
    
    def __new__(cls) -> TaskManager:
        if cls._instance == None:
            cls._instance = super().__new__(cls)

        return cls._instance
    
    def __init__(self) -> None:
        self._tasks:dict[int, Task] = {}

    def create_task(self, name:str)->Task:
        task = Task(name=name)
        self._tasks[task.id] = task
        return task
    
    def get_all(self)->list[Task]:
        return list(self._tasks.values())
    
    def find_by_id(self, id:int) -> Task | None:
        return self._tasks.get(id)
    
class TaskBaseOperation:
    def __init__(self) -> None:
        self._manager = TaskManager() 
    
class ShowAllTasks(TaskBaseOperation, Operation):
    def __init__(self, id = 1) -> None:
        super().__init__()
        self.id = id
        self.name = "Show All Task"

    def do_business(self):
        task_list = self._manager.get_all()
        if len(task_list) > 0:
            print(f"{'':-<46}")
            # Header
            print(f"{'ID':<4}{'NAME':<30}{'STATUS':<12}")
            print(f"{'':-<46}")
            # Data Rows
            for task in task_list:
                print(f"{task.id:<4}{task.name:<30}{task.status.name:<12}")
            print(f"{'':-<46}")
        else:
            print("There is no data.")
    
class CreateTask(TaskBaseOperation, Operation):
    def __init__(self, id = 2) -> None:
        super().__init__()
        self.id = id
        self.name = "Create Task"

    def do_business(self):
        # Get Task Name
        task_name = input("Enter Task Name : ")
        # Create Task
        task = self._manager.create_task(task_name)
        # Show Result
        print(f"{task.name} is created with id {task.id}.")

class UpdateStatus(TaskBaseOperation, Operation):
    def __init__(self, id = 3) -> None:
        super().__init__()
        self.id = id
        self.name = "Update Status"

    def do_business(self):
        # Get Task Id
        task_id = input("Enter Task ID : ")
        
        # Get Task form Task Manager
        task = self._manager.find_by_id(int(task_id))
        
        # If Not Found
        if task == None:
            print(f"There is no task with {task_id}")
            return
        
        # If Status is not updateble
        if task.status != Status.Created:
            print(f"{task.status.name} can't be update.")
            return
        
        # Else
        print("Select Status")
        print("1. Done")
        print("2. Cancel")
        selected_value = input("Status ID : ")
        task.status = Status(selected_value)
        print(f"{task.name} status is updated to {task.status.name}.")
    
if __name__ == "__main__":
    operations = [
        CreateTask(id=1),
        ShowAllTasks(id=2),
        UpdateStatus(id=3),
        # Update Name Operation
        # Delete Task Operation
    ]
    Application("TODO Application", operations).start()
