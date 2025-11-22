class Vehicle:
    def __new__(cls, name:str) -> Vehicle:
        print(f"Constructing Vehicle with {name}")
        return super().__new__(cls)

    def __init__(self, name:str) -> None:
        self._name = name
        print(f"Initializing Vehicle with {name}")

    def start(self):
        print(f"{self._name} is starting.")

    def stop(self):
        print(f"{self._name} is stopped.")

if __name__ == '__main__':
    v = Vehicle("Boat")
    print(v.__dict__)