#generate code to calculate the difference between the dates from datetime import datetime
from datetime import datetime

def calculate_date_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    return abs((date2 - date1).days)

date1 = "2026-07-01"
date2 = "2026-08-11"

result = calculate_date_difference(date1, date2)
print(result)
