l1 = ["a","b","c","d","e","f","g"]
l1.remove("g")
print(l1)

n = l1.pop(4)
print(n)
print(l1)

l1.clear()
print(l1)

l2 = [1,2,3,4]
del l2
#print(l2)

#print(l1.index('a'))

l3 = ["a","b","c","d","e","c","g"]
print(l3.index("c"))
print(l3.index("c", 3))
#for second repeat letter
print(l3.count("c"))
#to find out index position

#print(len(l3))
#l3.reverse()
#print(l3)

l3 = ["a","b","d","c","e","c","g"]
l3.sort()
print(l3)

l3.sort(reverse=True)
print(l3)

# l4 =[1,2,3,4,5,5,6,7,8]
# l3=l4
# print(l3)
# print(l4)

l4 = l3.copy()
#shallow copy
l3[1] = 5
print(l3)

s1 = set(l3)
print(s1)

s1 ={1,2,3,4,1,2,4,5}
print(s1)
#we can't do indexing in sets

l1 = [1,2,3,4,5,6]
l2 = [6,7,8,9,10]
print(l1+l2)
print(l1*4)
#l1*l2 we cant multiply two lists or divide

print(l1*int(1.5))










