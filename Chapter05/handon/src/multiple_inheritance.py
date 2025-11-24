class SuperOne:

    def __init__(self, name:str) -> None:
        self.name = name

    def one_method(self):
        print(f"One Method from Super One : {self.name}")

    def common_method(self):
        print("Common from Super One")

class SuperTwo:

    def __init__(self, value:int) -> None:
        self.value = value

    def two_method(self):
        print(f"Two Method from Super Two : {self.value}")

    def common_method(self):
        print("Common from Super Two")

class Child(SuperOne, SuperTwo):

    def __init__(self, name: str, value:int) -> None:
        self.name = name
        self.value = value

    def child_method(self):
        print("Method from Child Class")

if __name__ == "__main__":
    child = Child("Child Value", 100)
    child.child_method()
    child.one_method()
    child.two_method()
    child.common_method()
    print(child.name)
    print(child.value)