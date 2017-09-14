
import pandas as pdb
import numpy as np
import math
import scipy.io as spio
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
import pylab as p
#import matplotlib.axes3d as p3
import mpl_toolkits.mplot3d.axes3d as p3
import mysql.connector

con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

cur.execute("SELECT mesh, Distance_covered, TimeinMesh,Distance_covered/TimeinMesh  as Average_Velocity FROM NueroSCi.Distance_Covered1  "
            "where Distance_Covered>0.00 and TimeinMesh >0.00   ")
# fetch all of the rows from the query
data = cur.fetchall ()
Mesh = []
MyDist = []
Time=[]
avVelocity=[]
CumulativeTime=[]
st=0.00
# print the rows
for row in data :
    st=st+ float(row[2])
    Mesh.append( row[0])
    MyDist.append(row[1])
    Time.append(row[2])
    avVelocity.append(row[3])
    CumulativeTime.append(st)



cur.close()
con.close()

plt.plot(CumulativeTime,avVelocity,color='b')
plt.xlabel('Time Spent in the Mesh (s)')
plt.ylabel('Velocity in cm/s')
plt.suptitle(" Velocity Time Graph of the Rat Ibsen in the Maze")
#fig.add_axes(ax)
p.show()


plt.bar(Mesh,avVelocity, color='b')
plt.xlabel('Meshes')
plt.ylabel('Velocity in cm/s')
plt.suptitle(" Velocity In Mesh Graph of the Rat Ibsen in the Maze")
#fig.add_axes(ax)
p.show()


plt.bar(Mesh,MyDist,color='b')
plt.xlabel('Mesh')
plt.ylabel('Euclidean Distance Covered (cm)')
plt.suptitle(" Euclidean Distance Covered In Mesh Graph of  Rat Ibsen in the Maze")
#fig.add_axes(ax)
p.show()



#print Mesh, MyDist
