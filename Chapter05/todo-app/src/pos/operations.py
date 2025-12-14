from src.application import Operation

class SaleHistory(Operation):
    def __init__(self, id = 1) -> None:
        super().__init__(id, "Sale History")

    def do_business(self):
        pass

class CreateSale(Operation):
    def __init__(self, id = 2) -> None:
        super().__init__(id, "Create Sale")

    def do_business(self):
        pass


class FindSale(Operation):
    def __init__(self, id = 3) -> None:
        super().__init__(id, "Find Sale By Id")    

    def do_business(self):
        pass
