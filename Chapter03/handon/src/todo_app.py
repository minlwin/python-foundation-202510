welcome = """
=====================
TODO Application
====================="""

thanks = """
=====================
Thank You
====================="""

operations = """
Select Operation
1. Show Tasks
2. Create Task
3. Find Tasks
4. Delete Task
"""

if __name__ == "__main__":
    print(welcome)
    
    id = 0
    tasks:dict[int, str] = {}

    while True:
        print(operations)
        operation_id = input("Select ID : ")
        print()

        match operation_id:
            case "1":
                print("Task List")
                print("------------------------")  
                if len(tasks) > 0:
                    for key in tasks.keys():
                        print(f"{key}. {tasks.get(key)}") 
                else:
                    print("There is no tasks")
                print("------------------------")   
            case "2":
                print("Create Task")
                print("------------------------")   
                task_name = input("Task Name : ")
                id += 1
                tasks[id] = task_name
                print(f"Your task is created at id : {id}")
                print("------------------------")   
            case "3":
                print("Find Task")
                print("------------------------") 
                keyword = input("Search Keyword : ")
                found = False
                for id in tasks.keys():
                    task = tasks[id]
                    if task.lower().startswith(keyword.lower()):
                        print(f"{id}. {task}")
                        found = True
                if not found:
                    print("There is no result")
                print("------------------------")   
            case "4":
                print("Delete Task")
                print("------------------------")  
                task_id = input("Task ID : ")
                task = tasks.get(int(task_id)) 

                if task == None:
                    print(f"There is no task with id {task_id}")
                else:
                    del tasks[int(task_id)]
                    print("Your task is deleted")
                print("------------------------") 
            case _:
                break      

    print(thanks)
