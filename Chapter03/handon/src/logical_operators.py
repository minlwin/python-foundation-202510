def yes() -> bool:
    print("Yes")
    return True

def no() -> bool:
    print("No")
    return False

if __name__ == '__main__':
    print(f"yes() or yes() is {yes() or yes()}")
    no()