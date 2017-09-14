
import pandas as pdb
import numpy as np
import scipy.io as spio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
import pylab as p

import mysql.connector

con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

cur.execute("  SELECT * FROM NueroSCi.vw_bprmaccuracy     ")
# fetch all of the rows from the query
data = cur.fetchall ()
xpoints = []
BPRMIndependent = []
BPRMDependent = []
varColor = []
MyData = []
MyTime = []
# print the rows
for row in data :
    xpoints.append( float(row[0]))
    BPRMIndependent.append( float(row[1]))
    BPRMDependent.append( float(row[2]))


fig=p.figure()

# plot3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array


red_patch = mpatches.Patch(color='b', label='BPRM(Independent)')
green_patch = mpatches.Patch(color='g', label='BPRM(Dependent)')
plt.legend(handles=[red_patch,green_patch])


plt.plot(xpoints,BPRMIndependent, color='b')
plt.plot(xpoints,BPRMDependent, color='g')
#plt.Axes.set_xlabel('Dt seconds')
#plt.Axes.set_ylabel('Accuracy')
plt.title("Accuracy of BPRM for Animal Ibsen")
plt.xlabel("Time Bin (ms)")
plt.ylabel("Accuracy")
#fig.add_axes(ax)
p.show()
