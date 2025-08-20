from datetime import datetime, timedelta

def january_dates_ddmmyyyy(year: int):
    """
    Print all dates in January of the given year in ddmmyyyy format.
    """
    start_date = datetime(year, 1, 1)   # 1st Jan
    end_date = datetime(year, 2, 1)     # 1st Feb (stop before this)

    current = start_date
    while current < end_date:
        print(current.strftime("%d%m%Y"))  # ddmmyyyy
        current += timedelta(days=1)


# 🔹 Example: Show Jan 2025
january_dates_ddmmyyyy(2025)

