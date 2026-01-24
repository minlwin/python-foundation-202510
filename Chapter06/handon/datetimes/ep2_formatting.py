import datetime as dt

if __name__ == "__main__":
    value = dt.datetime(year=2026, month=1, day=1, hour=16, minute=0, second=0)

    # yyyy/MM/dd HH:mm:ss
    print(value.strftime("%Y/%m/%d %H:%M:%S"))

    # yyyy/M/d H:m:s
    print(f"{value.year}/{value.month}/{value.day} {value.hour}:{value.minute}:{value.second}")


