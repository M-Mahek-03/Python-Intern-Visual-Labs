import matplotlib.pyplot as mlp 
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

mlp.subplot(1,2,1)
mlp.plot(x, y, marker="*")

x1 = np.array([11,12,13,14,15])
y1 = np.array([16,17,18,19,20])

mlp.subplot(1,2,2)
mlp.plot(x1, y1, marker="o")

mlp.show()
