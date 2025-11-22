class User:
    def __init__(self, name:str, age:int) -> None:
        self._name = name
        self._age = age

    def greet(self) -> str:
        return f"Hello! I am {self._name} and {self._age} years old!"
    
class Container:
    def __init__(self) -> None:
        self._storage:list[str] = []

    def add(self, item:str) -> None:
        self._storage.append(item)

    def get_all(self) -> list[str]:
        return list(self._storage)
    
    def size(self) -> int:
        return len(self._storage)
    
if __name__ == '__main__':
    c = Container()

    c.add("Hello")
    c.add("Python")
    print(f"Size is {c.size()}")

    all = c.get_all()
    all.clear()
    print(f"Size is {c.size()}")
