import math
shape = str(input("shape - "))
r = int(input("r - "))
if shape == "circle":
    print(math.pi*r**2)
elif shape == "sphere":
    print(4*math.pi*r**2)
elif shape == "perimeter":
    print(2*math.pi*r)
else:
    print("none")
#to find area of a perticuler shape

length = int(input("l - "))
breadth = int(input("b - "))
if length == breadth:
    print("square")
else:
    print("rectangle")
#to check whether it is a square or not

value1 = int(input("v1 - "))
value2 = int(input("v2 - "))
if value1>value2:
    print("value1")
elif value1<value2:
    print("value2")
else:
    print("equal")
#to find out greater value

ONEunit = 100
quantity = int(input("quantity - "))
discount = (quantity*ONEunit)*10/100
cost = (quantity*ONEunit)
if quantity*ONEunit>10:
    print("cost is",cost - discount)
else:
    print("discount is",discount)
'''
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''

Salary = int(input("Salary - "))
Year_of_service = int(input("Year of service - "))
if Year_of_service>5:
    print("bonus is",.05*Salary)
else:
    print("no bonus")
'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
'''

abhay_age= int(input("abhay's age - "))
shubham_age = int(input("shubham's age - "))
som_age = int(input("som's age - "))
if abhay_age>shubham_age and som_age:
    print("oldest one is abhay")
elif abhay_age<shubham_age and som_age:
    print("youngest one is abhay")
elif shubham_age>abhay_age and som_age:
    print("oldest one is shubham")
elif shubham_age<abhay_age and som_age:
    print("youngest one is shubham")
elif som_age>abhay_age and shubham_age:
    print("oldest one is shubham")
elif som_age<abhay_age and shubham_age:
    print("youngest one is som")
else:
    print("all are equal")
'''
Take input of age of 3 people by user and determine oldest and youngest among them
'''








