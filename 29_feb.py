a = 10
print(id(a))
a = a+5
print(id(a))
print(a)

a = "HELLO"
print(id(a))
a = a + " WORLD"
print(id(a))
print(a)

a = 10
a = 15
print(a)
#latest value printed

x = 2.1 + 1.1
y = 3.2
if x == y:
    print("true")
else:
    print("false")

x = "hello "
y = "hello"
if x == y:
    print("true")
else:
    print("false")

x = 10
print(bin(x))
print(oct(x))
print(hex(x))
#convert any num to binary or octadecimal or hexadecimal

x = 125.56
print(int(x))
print(complex(x))
#to convert any num into integar or float or complex numbers

print(type(x))
print(isinstance(x, float))

x = 25.6
if isinstance(x, int):
    print("x is a integar")
elif isinstance(x, float):
    print("x is a float")
else:
    print("x is a complex")

x = 45.7
if type(x) == int:
    print("integar")
elif type(x) == float:
    print("float")
else:
    print("complex")







