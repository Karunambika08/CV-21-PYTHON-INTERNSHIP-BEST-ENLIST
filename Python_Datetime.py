Date and Time in Python¶
1. Write a Python program to convert a string to datetime
In [1]:
import datetime
In [2]:
def convert(date_time):
    format = '%b %d %Y %I:%M%p' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str
In [4]:
date_time = 'Mar 24 2021 03:24PM'
print(convert(date_time))
2021-03-24 15:24:00
2. Write a Python program to subtract five days (last working day) from current date
In [5]:
from datetime import date, timedelta
delta = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date  is :',delta)
Current Date : 2021-07-09
5 days before Current Date  is : 2021-07-04
3. Write a Python program to convert the date to datetime using a function
In [7]:
from datetime import datetime
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))
2021-07-09 00:00:00
4. Write a Python program to print next 7 days (week) starting from today
In [10]:
import datetime
base = datetime.datetime.today()
for x in range(0, 7):
    print(base + datetime.timedelta(days=x))
2021-07-09 18:36:42.005611
2021-07-10 18:36:42.005611
2021-07-11 18:36:42.005611
2021-07-12 18:36:42.005611
2021-07-13 18:36:42.005611
2021-07-14 18:36:42.005611
2021-07-15 18:36:42.005611
