id = 0
tasks:dict[int, str] = {}

def operation(name:str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(name)
            print("------------------------")  
            func(*args, **kwargs)
            print("------------------------")  
        return wrapper
    return decorator

@operation("Task List")
def show_all():
    if len(tasks) > 0:
        for key in tasks.keys():
            print(f"{key}. {tasks.get(key)}") 
    else:
        print("There is no tasks")

@operation("Create Task")
def create_task():
    global id
    task_name = input("Task Name : ")
    tasks[id := id + 1] = task_name
    print(f"Your task is created at id : {id}")  

@operation("Find Tasks")
def find_tasks():
    keyword = input("Search Keyword : ")
    found = False
    for id in tasks.keys():
        task = tasks[id]
        if keyword.lower() in task.lower():
            print(f"{id}. {task}")
            found = True
    if not found:
        print("There is no result")

@operation("Delete Task")
def delete_tasks():
    task_id = input("Task ID : ")
    task = tasks.get(int(task_id)) 

    if task == None:
        print(f"There is no task with id {task_id}")
    else:
        del tasks[int(task_id)]
        print("Your task is deleted")
