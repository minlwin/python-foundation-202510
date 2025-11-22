class User:
    def __init__(self, name:str = "Anonymous", age: int = 20) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f"I am {self.name} and {self.age} years old.")

if __name__ == "__main__":
    user1 = User("Aung Aung", 20)
    user1.greet()

    user1.age = 21
    user1.greet()

    user2 = User(age = 25, name = "Thidar")
    user2.greet()


    