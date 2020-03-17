l1 = ["a", "b", "c", "d"]
l2 = ["d", "e", "f", "g"]
s1 = set(l1)
s2 = set(l2)
print(s1)
print(s2)

s1.add("h")
print(s1)
s1.update(s2)
print(s1)

s1.update(["h","u","j"],{"k","l","m"})
print(s1)

s1.discard("l")
print(s1)

s1.remove("k")
print(s1)

n = s1.pop()
print(n)
print(s1.pop())
print(s1.pop())

s1.clear()
print(s1)

del s1
#print(s1)

s3 = {"a", "b", "c", "d","g"}
s4 = {"d", "e", "f", "g","k"}
print(s3|s4)
#union
print(s3&s4)
#intersection
print(s3-s4)
#diffrence
print(s3^s4)
#symetrical_difference

print(s3.intersection(s4))
print(s3.union(s4))
print(s3.difference(s4))
print(s3.symmetric_difference(s4))

#DICTIONARY
my_dict = {}
my_dict = {"1","one","2","two"}
print(my_dict)

my_dict = dict([("name","abhay"),("age",24)])
print(my_dict)
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.get("salary", 10000))
print(my_dict.get("salary"))
print(my_dict)
#has to give a dafault value otherwise get output of none

my_dict["salary"] = 10000
print(my_dict)
#to add a new content in our dictionary
print(my_dict.get("salary"))

my_dict["name"] = "abh"
print(my_dict)

my_dict["name"] = my_dict["name"]+ "ay rajput"
print(my_dict)

my_dict["age"] += 5
print(my_dict)
#n = my_dict.pop()
#print(n)
print(my_dict.pop("name"))
print(my_dict.popitem())

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

dict1 = {"name": "abhay","age":24}
dict2 = {"occupation":"student"}
dict1.update(dict2)
print(dict1)

for z in dict1.keys():
    print(dict1[z])
#itteration in dictionary





