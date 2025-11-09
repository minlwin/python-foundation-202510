def using_args(*args):
    print(args)

def using_keyword_args(**kwargs):
    print(kwargs)

if __name__ == "__main__":
    using_args(1, 2, 3)
    using_keyword_args(name = "Thidar", age = 20)