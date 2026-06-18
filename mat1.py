import matplotlib.pyplot as mlp 

import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
mlp.title("Graph")
mlp.xlabel("X")
mlp.ylabel("Y")
mlp.plot(x,y, marker="o", linestyle="dashed")
mlp.show()

# lb=["Sawdah","Juveriya","C","D","E"]
# exp=[0,0,0,0.1,0]
# mlp.pie(y, labels=lb, explode=exp)
# mlp.legend()
# mlp.show()