from calendar import month
from datetime import date, datetime
from os import sep
from re import DOTALL

dt1 = datetime(year=2022, month=2, day=3)
# dt2 = datetime(year=2022, month=1, day=3, hour=3, minute=23)
# dt3 = datetime(2018, 3, 5)
# dt4 = datetime(2018, 3, 5, 10, 28)

print(dt1)
# print(dt2)
# print(dt3)
# print(dt4)
print()


print(dt1.day)
print(dt1.month)
print(dt1.year)
print()

print("now method")
cdt = dt1.now()        # current date and time
print(cdt)
print(cdt.day, cdt.month, cdt.year, sep="-")
print()

print("today method")
today = dt1.today()
print(today)