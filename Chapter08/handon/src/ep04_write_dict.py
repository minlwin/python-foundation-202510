import csv

if __name__ == '__main__':
    with open("./files/ep04.txt", "+a") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name"], quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerow({"id" : 1, "name" : "Mike"})