import numpy as np

a0 = np.array(45)
print(a0.ndim)
print(a0)

# a1 = np.array([1,2,3,4,5])
# print(a1.ndim)
# print(a1[3])

# a2 = np.array([[1,2,3],[4,5,6]])
# print(a2.ndim)
# print(a2[0][2])

# a3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(a3.ndim)
# print(a3[0][1][2])

a4 = np.array([[[[1,2,3],[4,5,6]]],[[[7,8,9],[10,11,12]]]])
print(a.4ndim)
print(a4[0][0][1][2])

print(a1.dtype)

c = a1.copy()
print(c)
c[2] = 10
print(c)
print(a1)

print(c.base)

z = a1[1:4].view()
print(z)

z[1] = 89
print(z)
print(a1)

print(z.base)

x = a1 + a1
print(x)

print(a1)