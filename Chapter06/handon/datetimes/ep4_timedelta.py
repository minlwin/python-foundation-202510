import datetime as dt

if __name__ == "__main__":
    ten_days = dt.timedelta(days=10)
    two_week = dt.timedelta(weeks=2)

    today = dt.date.today()
    next_month = dt.date(year=today.year, month=today.month + 1, day=today.day)

    print(f"Today is {today}")
    print(f"Next Month is {next_month}")

    one_month = next_month - today

    print(f"Next Month - Today is {one_month}")

    print(f"{ten_days} + {two_week} = {ten_days + two_week}")

    print(f"{today} + {one_month} = {today + one_month}")