#Mehriiiin Code.
import numpy as np

output = np.ones([5,5])
print(output)

b = np.zeros([3,3])

b[1, 1] = 9
print(b)
output[1:4, 1:4] = b
print(output)