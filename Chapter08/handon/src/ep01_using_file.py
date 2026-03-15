import sys

def generate_id():
    try:
        with open('files/user_id.txt', "r+") as file:
            temp = file.read()
            if temp is not None:
                value = int(temp)
                value += 1
                file.seek(0)
                file.write(str(value))
                file.truncate()
                return value
    except FileNotFoundError:
        with open('files/user_id.txt', "x") as file:
            value = 1
            file.write(str(value))
            return value

def show_title(title):
    print(f"{'':-^30}")
    print(f"{title:<30}")
    print(f"{'':-<30}\n")

def create_user():
    show_title("Create User")
    name = input(f"{'Enter Name':<12}: ")
    phone = input(f"{'Enter Phone':<12}: ")
    email = input(f"{'Enter Email':<12}: ")
    user_id = generate_id()

    try:
        with open("files/users.txt", "+a") as file:
            file.write(f"{user_id},{name},{phone},{email}\n")
    except FileNotFoundError:
        with open("files/users.txt", "x") as file:
            file.write(f"{user_id},{name},{phone},{email}\n")

    print(f"\n{name} is created with id {user_id}.\n")

def show_all_users():
    show_title("Show All Users")
    try:
        with open("files/users.txt", "r") as file:
            print(f"{'ID':<3}{'Name':<20}{'Phone':<14}{'Email':<30}")
            print(f"{'':-<67}")
            for line in file:
                array = line.strip().split(",")
                print(f"{array[0]:<3}{array[1]:<20}{array[2]:<14}{array[3]:<30}")
    except FileNotFoundError:
        print(f"Error : There is no users. Please Add New User.")

    print()

if __name__ == '__main__':
    while True:
        show_title("Select Operation")
        print("1. Create User")
        print("2. Show All Users\n")

        operation = input("Operation ID : ")
        
        match operation:
            case "1":
                create_user()
                continue
            case "2":
                show_all_users()
                continue
        break

    show_title("Thank you")
