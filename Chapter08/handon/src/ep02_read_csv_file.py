import csv

if __name__ == '__main__':
    with open('./files/users.txt', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)