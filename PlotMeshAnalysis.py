
import pandas as pdb
import numpy as np
import scipy.io as spio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
import pylab as p

import mysql.connector

con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

cur.execute(" SELECT * FROM NueroSCi.meshanalysis     ")
# fetch all of the rows from the query
data = cur.fetchall ()
xpoints = []
ypoints = []
varColor = []
MyData = []
MyTime = []
# print the rows
for row in data :
    xpoints.append( float(row[0]))
    ypoints.append( float(row[1]))


fig=p.figure()

# plot3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array
#marker='o', linestyle='--', color='r'
plt.plot(xpoints,ypoints, marker='o', linestyle='--', color='g',markerfacecolor='darkgreen')

#plt.Axes.set_xlabel('Dt seconds')
#plt.Axes.set_ylabel('Accuracy')
plt.suptitle("Variation of Grid Size  and Proportion of NonEmpty Meshes ")
plt.xlabel("Number of Meshes in Maze")
plt.ylabel("Proportion of NonEmpty Meshes")
#plt.legend("Proportion of NonEmpty Meshes =  (NonEmpty meshes in maze)/(Total Number of meshes in Maze)")
#fig.add_axes(ax)
p.show()
