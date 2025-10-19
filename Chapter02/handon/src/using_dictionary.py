if __name__ == '__main__':
    dictionary = {}

    print("""
=========================
Dictionary          
=========================
""")

    while True:
        question = input("You > ")

        if question == 'Exit':
            break

        answer = dictionary.get(question)

        if answer != None:
            print(f"Bot > {answer}\n")
        else: 
            print("Bot > I've no idea, please teach me.")
            result = input("You > ")

            if result == 'Exit':
                break

            dictionary[question] = result
            print("Bot > Thank you for your kindness.\n")


    print("""
=========================
Thank You          
=========================   
""")
