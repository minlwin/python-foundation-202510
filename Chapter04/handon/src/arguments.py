def greet(name = "student", age = 18):
    print(f"I am {name} and {age} years old")

if __name__ == "__main__":
    greet("Aung Aung", 20)
    greet(age = 20, name = "Aung Aung")

    greet()
    greet("Nilar")
    greet(age=30)