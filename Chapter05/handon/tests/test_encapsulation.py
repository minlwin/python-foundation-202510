from src.encapsulation import User

def test_encapsulation():
    user = User("Aung Aung", 20)
    user._age = -10
    user._name = ""