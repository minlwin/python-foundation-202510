def say_hello(name):
    return f"Hello {name}"

def add(digit1, digit2):
    print(f"Digit 1 is {digit1}")
    return digit1 + digit2
    print(f"Digit 2 is {digit2}")

if __name__ == "__main__":
    result = say_hello("JDC")
    print(result)

    addResult = add(10, 20)
    print(addResult)
