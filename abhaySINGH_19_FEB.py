#Calendar Module
import calendar

print(calendar.weekheader(3))
print()
#show weekheader as MON TUE WED THU FRI SAT SUN

print(calendar.month(2020, 2, 3))
#to show specific year and month and all the dates in it like here i print FEB 2020

print(calendar.calendar(2020, 3))
#to show the entire calender of any perticuler year

day_of_the_week = calendar.weekday(1947, 8, 15)
print(day_of_the_week)
#to show the weekday on perticuler day from any year

is_leap = calendar.isleap(2020)
print(is_leap)
print(calendar.isleap(2021))
#to check whether it is a leap year or not

how_many_leap_days = calendar.leapdays(2020,2021)
print(how_many_leap_days)
#to find our leap days between two years

password = "Abhay123"
if password == "Abhay123":
    print("paasword is correct")
else:
    print("incorrect password")
#simple if else statement

username = "abhay123"
password = 12345
if username == "abhay123" and password == 12345:
    print("login")
else:
    print("username or password is incorrect")
#use of and in if else statement

def marks(args):
    pass


marks = int(marks)
marks = input("marks? ")
if marks >= 60:
    print("first division")
elif marks >= 45:
    print("second division")
else:
    print("Third division")












