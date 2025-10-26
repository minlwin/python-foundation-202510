def do_job():
    done = 0
    while done < 5:
        done += 1
        result = input("Please enter something : ")

        if result == "E":
            print("Will Continue")
            continue

        if result == "":
            break

        print(f"Your message is {result}")
    else:
        print("Finish successfully")

if __name__ == '__main__':
    do_job()