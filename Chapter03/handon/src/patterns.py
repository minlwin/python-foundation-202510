def show(data) :
    match data:
        case n if type(data).__name__ == 'int' and n >= 0:
            print("Positive Number")
        case n if type(data).__name__ == 'int' and n < 0:
            print("Negative Number")
        case [1, 2, 3]:
            print("Sequence with 1, 2, 3")
        case [1, *rest]:
            print("Sequence Start with 1")
        case {"name" : name, "age" : age}:
            print(f"Hello {name} you are {age} years old.")
        case _:
            print("Other Patterns")

if __name__ == "__main__":
    show(10)
    show(-10)
    show([1, 2, 3])
    show([1, 2 , 3, 4, 5])
    show({"name" : "Aung Aung", "age" : 20})