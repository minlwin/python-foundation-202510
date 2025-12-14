from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    unit_price: int

class ProductManager:
    _instance:ProductManager | None = None

    def __new__(cls) -> ProductManager:
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        self._products:dict[int, Product] = {
            1 : Product(1, "Coke", 1500),
            2 : Product(2, "Pepsi", 1000),
            3 : Product(3, "Nest Cafe", 2500),
            4 : Product(4, "Pucci Cake", 1500),
            5 : Product(5, "Potato Chips", 2000),
            6 : Product(6, "Fish Chips", 2500),
        }

    def get_all(self) -> list[Product]:
        return list(self._products.values())
    
    def find_by_id(self, id: int) -> Product | None:
        return self._products.get(id)
