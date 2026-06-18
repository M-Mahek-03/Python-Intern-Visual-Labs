t = ("Mahek", 10, ["C", "C++", "Java"])
print(type(t))

#ghumna
for i in t[2]:
    print(i)

t[2][0] = "Aamina"
print(t[2])

u = (t, "Mahek", 3, True)
print(u)

print(u[0])
u[0][2][2] = "Mehrin"
print(u) 
