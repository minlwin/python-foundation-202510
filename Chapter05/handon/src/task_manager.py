class Task:
    _id = 0

    def __init__(self, id:int, name:str) -> None:
        self._id = id
        self._name = name

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    @classmethod
    def create(cls, name:str):
        cls._id += 1
        return Task(cls._id, name)
    
    def __str__(self) -> str:
        return f"Task[id:{self._id}, name:{self._name}]"
    
class TaskManager:
    _instance : TaskManager | None = None

    def __init__(self) -> None:
        self._repository:dict[int, Task] = {}

    def create(self, name:str):
        task = Task.create(name)
        self._repository[task.get_id()] = task
        return task
    
    def find_all(self):
        return list(self._repository.values())
    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = TaskManager()

        return cls._instance