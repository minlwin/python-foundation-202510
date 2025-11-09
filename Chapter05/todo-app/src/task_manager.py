class Task:
    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name

class TaskManager:

    def __init__(self) -> None:
        self._id = 0
        self._tasks:dict[int, Task] = {}

    def get_all_tasks(self):
        return self._tasks
    
    def add_task(self, task:str):
        id = self._id + 1
        self._id = id
        self._tasks[id] = Task(id, task)
        return id

    def search(self, keyword:str):
        result:list[Task] = []
        for task in self._tasks.values():
            if keyword.lower() in task.name.lower():
                result.append(task)
        return result
    
    def delete(self, id:int):
        del self._tasks[id]