from src.application import Operation
from src.pos.products import ProductManager
from src.pos.sales import SaleItem, SaleManager, Sale

class SaleHistory(Operation):
    def __init__(self, id = 1) -> None:
        super().__init__(id, "Sale History")

    def do_business(self):
        sales = SaleManager().get_all()

        if len(sales) == 0:
            print("There is no sale history.")
            return

        print(f"{'':-<44}")
        print(f"{'ID':<4}{'Items':>10}{'Sub Total':>10}{'Tax':>10}{'All Total':>10}")
        print(f"{'':-<44}")
        for sale in sales:
            print(f"{sale.id:<4}{sale.total_count():>10}{sale.sub_total():>10}{sale.tax:>10}{sale.all_total():>10}")
        print(f"{'':-<44}\n")


class CreateSale(Operation):
    def __init__(self, id = 2) -> None:
        super().__init__(id, "Create Sale")
        self._items:list[SaleItem] = []

    def do_business(self):
        self._items = []

        # Show Products
        CreateSale._show_products()

        # Add To Cart
        while True:
            item = CreateSale._get_sale_item()

            if item == None:
                break

            self._items.append(item)
            print(f"Add {item.quantity} {item.product.name}s to cart.\n")

        # Check Out
        print("\nThank you")
        sale = SaleManager().create(tuple(self._items))
        show_details(sale)

    @staticmethod
    def _show_products():
        products = ProductManager().get_all()
        print(f"{'':-<25}")
        print(f"{'ID':<3}{'Name':<16}{'Price':>6}")
        print(f"{'':-<25}")
        for p in products:
            print(f"{p.id:<3}{p.name:<16}{p.unit_price:>6}")
        print(f"{'':-<25}")


    @staticmethod
    def _get_sale_item():
        selected_id = input("Enter Product ID : ")
        selected_product = ProductManager().find_by_id(int(selected_id))

        if selected_product == None:
            return None
        
        quantity = input("Enter Quantity : ")
        return SaleItem(selected_product, int(quantity))

class FindSale(Operation):
    def __init__(self, id = 3) -> None:
        super().__init__(id, "Find Sale By Id")    

    def do_business(self):
        id = input("Enter Sale ID : ")
        sale = SaleManager().find_by_id(int(id))

        if sale == None:
            print(f"There is no sale history for id no {id}.")
            return
        
        show_details(sale)

def show_details(sale: Sale) : 
    print(f"{'':-<40}")
    print(f"{'No':<4}{'Name':<16}{'Price':>6}{'Qty':>4}{'Total':>10}")
    print(f"{'':-<40}")
    for index, item in enumerate(sale.items):
        print(f"{index + 1:<4}{item.product.name:<16}{item.product.unit_price:>6}{item.quantity:>4}{item.total():>10}")
    print(f"{'':-<40}")
    print(f"{"Sub Total":<10}{sale.sub_total():>30}")
    print(f"{"Tax":<10}{sale.tax:>30}")
    print(f"{"All Total":<10}{sale.all_total():>30}")
    print(f"{'':-<40}")
