print("Enter Marks")
Marks = int(input("Marks - "))
if Marks<25:
    print("F")
elif Marks>=25 and Marks<45:
    print("E")
elif Marks>=45 and Marks<50:
    print("D")
elif Marks>=50 and Marks<60:
    print("C")
elif Marks>=60 and Marks<80:
    print("B")
else:
    print("A")

'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
'''

print("Total number of classes held - 220")
total_classes = 220
classes_attended = int(input("classes attended - "))
attendence = classes_attended*100/total_classes
if attendence<75:
    print("student not allowed for exam")
else:
    print("student allowed for exam")

'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''

print("Total number of classes held - 220")
total_classes = 220
classes_attended = int(input("classes attended - "))
any_medical_cause = input("medical cause - ")
attendence = classes_attended*100/total_classes
if attendence >= 75:
    print("student is allowed for exam")
else:
    if attendence<75 and any_medical_cause == "yes":
        print("student is allowed for exam")
    else:
        print("student is not allowed for exam")
'''
Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has 
medical cause or not ( 'Y' or 'N' ) and print accordingly
'''

year = int(input("year - "))
if year%4 == 0:
    print("this is a leap year")
elif year%400*400 == 0:
    print("this century year is also laep year ")
else:
    print("this is not a leap year")

'''
Write a program to check if a year is leap year or not.
If a year is divisible by 4 then it is leap year but if the year is 
century year like 2000, 1900, 2100 then it must be divisible by 400.
'''

employee_age = int(input("age - "))
employee_sex = input("sex - ")
martial_status = input("martial status - ")
if employee_sex == "F":
    print("work is urban area")
elif employee_sex == "M" and employee_age>=20 and employee_age<=40:
    print("work in anywhere")
elif employee_sex == "M" and employee_age>40 and employee_age<=60:
    print("work is in urban area")
else:
    print("ERROR")

'''
Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of 
service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR"
'''

'''
A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895
'''

a = int(input("a = "))
rev = 0
while(a>0):
    c = a%10
    a = a//10
    rev = (rev*10)+c
print('reverse:', rev)

