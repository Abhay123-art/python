my_tuple= tuple([1,2,3])
print(id(my_tuple))
print(my_tuple)

print(my_tuple.index(1))

print(my_tuple[0:2])
my_tuple = (4,5,6)
print(my_tuple)
print(id(my_tuple))

t = (1,2,[4,5,6],7,8)
t[2][1]= 9
print(t)
t[2].append(9)
print(t)

l1 = [1,2,3,(4,5,6),7]
l1[3] = (1,2,3)
print(l1)

a = "hello"
b = " world"
print(a+b)
print("hello"+" world")

str1 = "i love bhopal"
print(str1.upper())
print(str1.lower())
print(str1.isupper())
print(str1.capitalize())
print(str1.split())
print(len(str1))
print(str1.count("o"))
print(str1.isalpha())
print(str1.isalnum())
print(str1.isnumeric())
print(str1.strip())
#removes empty spaces LSTRIP AND RSTRIP iis also there

print(str1.startswith("i"))
print(str1.endswith("l"))
print(str1[7:13])
print(str1[7:13].upper())
print(str1.find("bhopal"))

while True:
    n = int(input("n = "))
    if 0 < n <= 5:
        print("hi")
    elif 6<n<=10:
        print("hey")
    elif 11<n<=15:
        print("hello")
    else:
        print("bye")
        break
j = 0
while j<10:
    n = int(input("n = "))
    if 0 < n <= 5:
        print("hi")
    elif 6<n<=10:
        print("hey")
    elif 11<n<=15:
        print("hello")
    else:
        print("bye")
    j = j+1

n = 5
while n>0:
    print("lather")
    print("rinse")
    n = n-1
print("dry off")

n = 0
while n>0:
    print("lather")
    print("rinse")
    n=n+1
print("dry off")

while True:
    line = input(" input ")
    if line.lower =="done":
        break
    print(line)
print("done")





