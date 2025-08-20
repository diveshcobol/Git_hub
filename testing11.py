import re
from datetime import datetime

def is_valid_ddmmyyyy(date_str: str) -> bool:
    """
    Check if the given string matches ddmmyyyy format and is a valid date.
    """
    # Must be exactly 8 digits
    if not re.fullmatch(r"\d{8}", date_str):
        return False
    
    # Extract day, month, year
    day = int(date_str[0:2])
    month = int(date_str[2:4])
    year = int(date_str[4:8])

    try:
        datetime(year, month, day)  # Validate actual date
        return True
    except ValueError:
        return False


# 🔹 Example tests
test_dates = ["01012025", "31122024", "31022025", "abcd2025"]

for d in test_dates:
    print(f"{d}: {is_valid_ddmmyyyy(d)}")
