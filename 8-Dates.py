# Dates
import datetime

now_time = datetime.datetime.now()
print("Time Now : ", now_time)

# separate time print
print()
print("1. Year : ", now_time.year)
print("2. Month : ", now_time.month)
print("3. Date : ", now_time.day)
print("4. Hour : ", now_time.hour)
print("5. Minute : ", now_time.minute)
print("6. Second : ", now_time.second)
print("7. Microsecond : ", now_time.microsecond)

# The strftime() Method
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
print("8. Day : ", now_time.strftime("%U"))

# Data objects create - create a date: year, month, day.(hour, minute, second, microsecond, tzone)
print()
# datetime() class requires three parameters
x = datetime.datetime(2026, 5, 1, 10)
print(x)
