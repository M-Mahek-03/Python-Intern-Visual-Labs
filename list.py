friends = [5, 1, 7, 9, 3]
print(type(friends))
print(friends)
#print(friends[10])
'''
for f in friends:
    print(f)
'''

friends.append(20)
friends.remove(7)
print(friends)
print(friends.pop())
#print(friends.pop())
#print(friends.pop())
#print(friends.pop())
#print(friends.pop())
print(friends.count(5))
#print(friends.count(1))
#print(friends.count(9))
#print(friends.count(3))
#print(friends.count(20))
friends.insert(1,100)
print(friends)
vl = friends.copy()
friends.clear()
print(vl)
 #del friends
print(friends)

if 5 in vl:
    print("five is present")
    
if 120 not in vl:
    print("120 not is present")






