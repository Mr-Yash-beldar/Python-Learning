import re

def is_valid_date(date):
    pattern = r'^\d{4}-\d{2}-\d{2}'

    if re.match(pattern, date):
        return True
    else:
        return False

date = input("Enter a date (YYYY-MM-DD): ")

if is_valid_date(date):
    print(f"{date} is a valid date.")
else:
    print(f"{date} is not a valid date. Please use the YYYY-MM-DD format.")
