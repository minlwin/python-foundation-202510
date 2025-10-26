ACTIONS = {
    1 : "Show Students",
    2 : "Find One",
    3 : "Create Student"
}

if __name__ == "__main__":
    print("=======================")
    print("Welcome")
    print("=======================")
    print()

    while True:
        for id in ACTIONS.keys():
            print(f"{id} : {ACTIONS.get(id)}")
        
        print()

        response = input("Please select action id : ")
        action_id = int(response)

        if action_id not in [1, 2, 3]:
            print("Invalid Action ID")
            break
        
        print(f"You select {action_id} : {ACTIONS.get(action_id)}")
        print()
