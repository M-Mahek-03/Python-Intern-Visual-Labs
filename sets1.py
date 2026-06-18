s1={1,2,3,4,5}
s2={4,5,6,7,8}

print(s1)
print(s2)

for i in s1:
    print(i)

c=s2.difference(s1)
print(c)

c=s1.intersection(s2)
print(c)
#same print in both

c=s1.union(s2)
print(c)

c=s1.symmetric_difference(s2)
print(c)

s1.add(10)
print(c)

#s1.discard(4)
#print(s1)
