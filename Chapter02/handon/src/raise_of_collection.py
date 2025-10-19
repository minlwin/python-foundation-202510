if __name__ == "__main__":
    my_fav = set()

    while True:
        result = input("Your fav foods : ")

        if "Nothing" == result:
            break

        my_fav.add(result)

    print(f"Your fav are {", ".join(my_fav)}")