from dataclasses import dataclass
from src.pos.products import Product

@dataclass
class SaleItem:
    product: Product
    quantity: int

    def total(self) -> int:
        return self.quantity * self.product.unit_price
    
    def with_product(self, prodct: Product) -> SaleItem:
        return SaleItem(prodct, self.quantity)
    
    def with_quantity(self, quantity: int) -> SaleItem:
        return SaleItem(self.product, quantity)

@dataclass
class Sale:
    id: int
    items: tuple[SaleItem, ...]
    tax: int

    def sub_total(self) -> int:
        return Sale.sum(self.items)
    
    def all_total(self) -> int:
        return self.sub_total() + self.tax
    
    def total_count(self) -> int:
        count = 0
        for item in self.items:
            count += item.quantity
        
        return count

    @staticmethod
    def sum(items: tuple[SaleItem, ...]) -> int:
        amount = 0
        for item in items:
            amount += item.total()
        return amount
    


class SaleManager:
    _instance: SaleManager | None = None

    def __new__(cls) -> SaleManager:
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._id = 0
        self._tax_rate = 5
        self._sales : dict[int, Sale] = {}

    def create(self, items: tuple[SaleItem, ...]) -> Sale:
        self._id = self._id + 1
        sub_total = Sale.sum(items)
        tax = sub_total // 100 * self._tax_rate
        sale = Sale(id=self._id, items=items, tax=tax)
        self._sales[self._id] = sale
        return sale
    
    def get_all(self) -> tuple[Sale, ...]:
        return tuple(self._sales.values())
    
    def find_by_id(self, id: int) -> Sale | None: 
        return self._sales.get(id)
        