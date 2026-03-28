import csv

def generate_id():
    with open('files/user_id.txt', "w+") as file:
        value = 0
        temp = file.read()
        if temp is not None:
            if temp is not "":
                value = int(temp)
            value += 1
            
            file.seek(0)
            file.write(str(value))
            file.truncate()

        return value

def show_title(title):
    print(f"{'':-^30}")
    print(f"{title:<30}")
    print(f"{'':-<30}\n")

def create_user():
    user = {}
    user['id'] = generate_id()

    show_title("Create User")
    user['name'] = input(f"{'Enter Name':<15}: ")
    user['phone'] = input(f"{'Enter Phone':<15}: ")
    user['email'] = input(f"{'Enter Email':<15}: ")
    user['address'] = input(f"{'Enter Address':<15}: ")

    with open("files/users.txt", "a+") as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'name', 'phone', 'email', 'address'], quoting=csv.QUOTE_ALL)

        if not file.read(1):
            writer.writeheader()

        writer.writerow(user)

    print(f"\n{user['name']} is created with id {user['id']}.\n")

def show_all_users():
    show_title("Show All Users")
    try:
        with open("files/users.txt", "r") as file:
            print(f"{'ID':<3}{'Name':<20}{'Phone':<14}{'Email':<30}{'Address':<40}")
            print(f"{'':-<107}")
            reader = csv.DictReader(file)
            for user in reader:
                print(f"{user['id']:<3}{user['name']:<20}{user['phone']:<14}{user['email']:<30}{user['address']:<40}")
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
