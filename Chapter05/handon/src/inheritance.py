from typing import Any, Self

class Vehicle:
    def __new__(cls, name:str) -> Self:
        print("Vehicle is instantiated.")
        return super().__new__(cls)
    
    def __init__(self, name:str) -> None:
        self._name = name
        print(f"Vehicle is initialized with {name}")
    
    def start(self):
        print(f"{self._name} is started.")

    def stop(self):
        print(f"{self._name} is stopped.")

class Car(Vehicle):

    def __new__(cls) -> Self:
        print("Car is instantiated.")
        return super().__new__(cls, "Car")

    def __init__(self) -> None:
        super().__init__("Car")
        print("Car is initialized")
    
    def drive(self):
        print(f"{self._name} is driving.")

    def start(self):
        print("Woo Woo")

if __name__ == "__main__":
    car = Car()
    car.start()
    car.drive()
    car.stop()