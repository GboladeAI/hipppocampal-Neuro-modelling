
import pandas as pdb
import numpy as np
import scipy.io as spio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import cm
import sys
import pylab as p

import mysql.connector

con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()
sql="  select c.ID,a.mesh,a.TimeInMesh , a.n_1/a.TimeInMesh,a.n_2/a.TimeInMesh,    "
sql=sql+"  a.n_3/a.TimeInMesh,a.n_4/a.TimeInMesh,a.n_5/a.TimeInMesh ,a.n_6/a.TimeInMesh,a.n_7/a.TimeInMesh,  "
sql=sql+"  a.n_8/a.TimeInMesh,a.n_9/a.TimeInMesh,a.n_10/a.TimeInMesh , a.n_11/a.TimeInMesh,a.n_12/a.TimeInMesh,  "
sql=sql+"  a.n_13/a.TimeInMesh,a.n_14/a.TimeInMesh,a.n_15/a.TimeInMesh ,a.n_16/a.TimeInMesh,a.n_17/a.TimeInMesh, "
sql=sql+"  a.n_18/a.TimeInMesh,a.n_19/a.TimeInMesh,a.n_20/a.TimeInMesh , a.n_21/a.TimeInMesh,a.n_22/a.TimeInMesh,  "
sql=sql+"  a.n_23/a.TimeInMesh,a.n_24/a.TimeInMesh,a.n_25/a.TimeInMesh,a.n_26/a.TimeInMesh ,a.n_27/a.TimeInMesh,   "
sql=sql+"  a.n_28/a.TimeInMesh,a.n_29/a.TimeInMesh,a.n_30/a.TimeInMesh , a.n_31/a.TimeInMesh,a.n_32/a.TimeInMesh,  "
sql=sql+"  a.n_33/a.TimeInMesh,a.n_34/a.TimeInMesh,a.n_35/a.TimeInMesh,a.n_36/a.TimeInMesh,  "
sql=sql+"  b.Distance_covered, b.Distance_covered/a.TimeinMesh  as Average_Velocity    "

sql=sql+"  from   "
sql=sql+"  NueroSCi.tblNueronSpikeCount a ,  NueroSCi.Distance_Covered1 b ,  "
sql=sql+"  NueroSCI.tblMapMeshOrder c   "
sql=sql+"  where a.timeInmesh>0.00    "
sql=sql+"  and a.mesh=b.mesh   "
#sql=sql+"  and a.TimeInMesh>5.00   "
sql=sql+"  and c.mesh=b.mesh   "
sql=sql+"  and a.AnimalName='I'   "

sql=sql+"  order by 1 asc   "
cur.execute(sql)
# fetch all of the rows from the query
data = cur.fetchall ()
Timepoints1 = []
averagevelocity=[]
n_1_points = []
n_2_points = []
n_3_points = []
n_4_points = []
n_5_points = []
n_6_points = []
n_7_points = []
n_8_points = []
n_9_points = []
n_10_points = []
n_11_points = []
n_12_points = []
n_13_points = []
n_14_points = []
n_15_points = []
n_16_points = []
n_17_points = []
n_18_points = []
n_19_points = []
n_20_points = []
n_21_points = []
n_22_points = []
n_23_points = []
n_24_points = []
n_25_points = []
n_26_points = []
n_27_points = []
n_28_points = []
n_29_points = []
n_30_points = []
n_31_points = []
n_32_points = []
n_33_points = []
n_34_points = []
n_35_points = []
n_36_points = []


varColor = []
MyData = []
MyTime = []
# print the rows
ALL=[]
st=0
for row in data :
    st=st+row[2]
    print st
    Timepoints1.append(st)
    n_1_points.append( row[3])
    n_2_points.append( row[4])
    n_3_points.append( row[5])
    n_4_points.append( row[6])
    n_5_points.append( row[7])
    n_6_points.append( row[8])
    n_7_points.append( row[9])
    n_8_points.append( row[10])
    n_9_points.append( row[11])
    n_10_points.append( row[12])
    n_11_points.append( row[13])
    n_12_points.append( row[14])
    n_13_points.append( row[15])
    n_14_points.append( row[16])
    n_15_points.append( row[17])
    n_16_points.append( row[18])
    n_17_points.append( row[19])
    n_18_points.append( row[20])
    n_19_points.append( row[21])
    n_20_points.append( row[22])
    n_21_points.append( row[23])
    n_22_points.append( row[24])
    n_23_points.append( row[25])
    n_24_points.append( row[26])
    n_25_points.append( row[27])
    n_26_points.append( row[28])
    n_27_points.append( row[29])
    n_28_points.append( row[30])
    n_29_points.append( row[31])
    n_30_points.append( row[32])
    n_31_points.append( row[33])
    n_32_points.append( row[34])
    n_33_points.append( row[35])
    n_34_points.append( row[36])
    n_35_points.append( row[37])
    n_36_points.append( row[38])
    averagevelocity.append(row[40])

ALL.append(n_1_points)
ALL.append(n_2_points)
ALL.append(n_3_points)
ALL.append(n_4_points)
ALL.append(n_5_points)
ALL.append(n_6_points)
ALL.append(n_7_points)
ALL.append(n_8_points)
ALL.append(n_9_points)
ALL.append(n_10_points)
ALL.append(n_11_points)
ALL.append(n_12_points)
ALL.append(n_13_points)
ALL.append(n_14_points)
ALL.append(n_15_points)
ALL.append(n_16_points)
ALL.append(n_17_points)
ALL.append(n_18_points)
ALL.append(n_19_points)
ALL.append(n_20_points)
ALL.append(n_21_points)
ALL.append(n_22_points)
ALL.append(n_23_points)
ALL.append(n_24_points)
ALL.append(n_25_points)
ALL.append(n_26_points)
ALL.append(n_27_points)
ALL.append(n_28_points)
ALL.append(n_29_points)
ALL.append(n_30_points)
ALL.append(n_31_points)
ALL.append(n_32_points)
ALL.append(n_33_points)
ALL.append(n_34_points)
ALL.append(n_35_points)
ALL.append(n_36_points)




fig=p.figure()

# Compute Rows required
nX=6
nY=6
Tot = nX * nY
Rows = Tot // nY
Rows += Tot % nY

# Create a Position index

Position = range(1,int(Tot + 1))

# Create main figure

fig = plt.figure(1)
index=0

xticllabel = [0.0, 500.00, 1000.00, 1500.00, 2000.00]
yticllabel = [0.0, 20.00, 40.00, 60.00, 80.00]
for k in range(int(Tot)):
  # add every single subplot to the figure with a for loop

  ax = fig.add_subplot(Rows,nY,Position[k])

  ax = fig.add_subplot(Rows, nY, Position[k])
  ax.set_axis_bgcolor('white')

  ax.plot(Timepoints1, ALL[index], color='g')  # Or whatever you want in the subplot
  ax.set_title("Neuron-" + str(int(k + 1)), fontsize=5)
  ax.set_yticklabels(yticllabel,fontsize=3)
  ax.set_xticklabels(xticllabel,fontsize=3)
  ax.axis('on')
  index=index+1



#int(Tot)
#plt.suptitle("Location of Rat (Ibsen) divided into smaller meshes  of ("+str(float(X/nX))+" X " +str(float(Y/nY))+ "       )")
plt.suptitle("Nueron Firing Rates(Hertz) versus Time (s) for Rat (Ibsen)")


plt.show()


