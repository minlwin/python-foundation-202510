import datetime as dt

if __name__ == "__main__":
    # Create Current Date Times
    today = dt.date.today()
    print(today)

    today2 = dt.datetime.today()
    print(today2)

    now = dt.datetime.now()
    print(now)

    time1 = dt.time()
    print(time1)

    print(now.time())
    
    # Create Specific Date Times with Constructor
    print(dt.date(day=28, year=1975, month=1))
    print(dt.datetime(year=2026, month=3, day=10, hour=10))
    print(dt.time(hour=10))
