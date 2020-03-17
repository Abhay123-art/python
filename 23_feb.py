#SYNTAX RULES IN PYTHON

x=2; y=5
print(x+y)

'''
this is a multiline comment
called as DOC STRAY
'''

x= 333+\
    444+\
    557
print(x)

#python define block of codes as tab or spaces

x = "Hello"
y = "hello"
if x==y:
#we can also use x is y:
    print("true")
else:
    print("false")

#variable name should start from underscore "_" or "alphabets" like 1ab = 5 is wrong variable name should be start from
#except first chracter can be alphanumeric (a-z,A-Z,0-9 or underscore"_")
#identifier name or variable name must not be a keyword
a0b =5
print(a0b)

print(11/4)

#a = input("enter name - ")
#b = int(input("enter age - "))
#print("name and age - ", a," , ",24)

a = 34
b = 23
if a and b:
     print("both are true")
else:
     print("both are false")

a1= int(input("a - "))
b1= int(input("b - "))
j= a1 >> b1

print("binary right shift", j)

'''
LOGICAL OPERATERS
(a and b) Returns True if both a and b are True
(a or b) Returns True if either or both are True
(Not a) Returns True if a is False, True otherwise
'''
#BITWISE OPERATERS
#Binary AND(a&b) OR(a|b) XOR(a^b) NOT(~a,~v) LEFT SHIFT (a<<) RIGHT SHIFT(a>>b)


a = 10
a = a+5
print(a+a)





















