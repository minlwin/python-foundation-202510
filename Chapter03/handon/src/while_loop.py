def show(message:str, count:int):
    done = 0
    while done < count:
        done += 1
        print(f"{done} : {message}")

if __name__ == '__main__':
    show("Hello Python", 3)