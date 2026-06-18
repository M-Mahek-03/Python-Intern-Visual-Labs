#understanding tuple
t = (1, 2, 3)
print(t, type(t))
print(t[2])

#t[2] = 30
t = (4, 5, 6)
print(t, type(t))
u = (t, 4)
print(u)
print(u[0][0])
v = ([1,2,3],[4,5,6])
print(v[0])
v[0][0] = "Mahek"
print(v[0])
v[0] = ["a","b","c"]