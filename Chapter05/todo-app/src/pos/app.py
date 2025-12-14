from src.application import Application
from src.pos.operations import SaleHistory, CreateSale, FindSale

if __name__ == "__main__":
    Application(name="POS Application", operations=[
        SaleHistory(),
        CreateSale(),
        FindSale()
    ]).start()