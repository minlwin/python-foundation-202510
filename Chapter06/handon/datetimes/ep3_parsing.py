import datetime as dt

if __name__ == "__main__":
    dateString = "2026/01/11 00:00"
    dateObject = dt.datetime.strptime(dateString, "%Y/%m/%d %H:%M")

    print(dateObject)