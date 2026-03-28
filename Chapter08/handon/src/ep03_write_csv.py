import csv

if __name__ == '__main__':
    with open('./files/ep03.txt', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_STRINGS, quotechar="'")
        writer.writerows([
            [1, "Java Basic", "Language Foundation,OOP,Essential API"],
            [2, "Python", "Foundation,OOP,Data Structure"]
        ])