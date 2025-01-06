from datetime import date
print(type(date))

my_date = date(2000, 4, 15)
print(my_date)
print(my_date.day)
print(my_date.year)
print(my_date.month)
print(my_date.isocalendar())

from datetime import time
my_time = time(22, 30, 44)
print(my_time)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)

from datetime import datetime, timedelta
date_time = datetime(2025, 1, 5, 22, 36, 45)
print(date_time)
print(date_time.strftime("%d-%b-%Y %H:%M:%S"))

date_str = '10/12/2025'
converted_date = datetime.strptime(date_str, "%d/%m/%Y")
print(converted_date)

print(timedelta)
print(date_time + timedelta(days=100, minutes=120))