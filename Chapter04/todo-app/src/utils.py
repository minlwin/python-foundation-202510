title = """
=====================
{}
====================="""

def show_message(message:str):
    print(title.format(message))

operations = """
Select Operation
1. Show Tasks
2. Create Task
3. Find Tasks
4. Delete Task
"""

def get_operation_id() -> str:
    print(operations)
    result = input("Selected ID : ")
    print()
    return result