def show_value_and_type(value:str):
    print(f"Value is {value}")
    print(f"Type is  {type(value).__name__}")

if __name__ == '__main__':
    name:str = "Python"
    show_value_and_type(name)

    name = name * 3
    show_value_and_type(name)
