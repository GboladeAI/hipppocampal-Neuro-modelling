from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


import pandas as pd
import numpy  as np
from collections import *



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[1,2,3,4,5,6,7,8,9,10]
y =[5,6,2,3,13,4,1,2,4,8]
z =[2,3,3,3,5,7,9,11,9,10]



ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()




Se_data = pd.Series(Counter(np.random.randint(0,10,100)))
plt.axis('Off')
with plt.style.context("seaborn-whitegrid"):
    fig, ax = plt.subplots()
    Se_data.plot(kind="barh", ax=ax, title="No Border")
    plt.show()
with plt.style.context("seaborn-white"):
    fig, ax = plt.subplots()
    Se_data.plot(kind="barh", ax=ax, title="With Border")

    plt.show()