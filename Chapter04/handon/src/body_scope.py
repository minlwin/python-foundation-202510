print("Testing Body Scope of Python Function")

def print_hello():
    print("Hello Python")
    return
    print("After Hello Python")

if True:
    print("After Returning Hello Python")

print_hello()