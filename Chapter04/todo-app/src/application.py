from src.utils import show_message, get_operation_id
from src.operations import show_all, create_task, delete_tasks, find_tasks

def main():
    
    show_message("TODO Application")

    while True:
        operation_id = get_operation_id()
        
        match operation_id:
            case "1":
               show_all()
            case "2":
                create_task()
            case "3":
                find_tasks()
            case "4":
                delete_tasks()
            case _:
                break

    show_message("Thank You")

if __name__ == "__main__":
    main()
