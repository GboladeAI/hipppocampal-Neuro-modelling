
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
sql=sql+"  and c.mesh=b.mesh   "
sql=sql+"  and a.AnimalName='I'   "
sql=sql+"  order by 1 asc   "
cur.execute("  Select * from bprm_accuracy     ")
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
st=0
for row in data :
    st=st+row[2]
    Timepoints1.append(row[3])
    n_1_points.append( row[4])
    n_2_points.append( row[5])
    n_3_points.append( row[6])
    n_4_points.append( row[7])
    n_5_points.append( row[8])
    n_6_points.append( row[9])
    n_7_points.append( row[10])
    n_8_points.append( row[11])
    n_9_points.append( row[12])
    n_10_points.append( row[13])
    n_11_points.append( row[14])
    n_12_points.append( row[15])
    n_13_points.append( row[16])
    n_14_points.append( row[17])
    n_15_points.append( row[18])
    n_16_points.append( row[19])
    n_17_points.append( row[20])
    n_18_points.append( row[21])
    n_19_points.append( row[22])
    n_20_points.append( row[23])
    n_21_points.append( row[24])
    n_22_points.append( row[25])
    n_23_points.append( row[26])
    n_24_points.append( row[27])
    n_25_points.append( row[28])
    n_26_points.append( row[29])
    n_27_points.append( row[30])
    n_28_points.append( row[31])
    n_29_points.append( row[32])
    n_30_points.append( row[33])
    n_31_points.append( row[34])
    n_32_points.append( row[35])
    n_33_points.append( row[36])
    n_34_points.append( row[37])
    n_35_points.append( row[38])
    n_36_points.append( row[39])
    averagevelocity.append(row[41])
)




fig=p.figure()

# plot3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array
plt.plot(Timepoints1,n_1_points, 'blue')



red_patch = mpatches.Patch(color='b', label='BPRM(Independent)')
green_patch = mpatches.Patch(color='g', label='BPRM(Dependent)')
plt.legend(handles=[red_patch,green_patch])

plt.title("Accuracy of BPRM(Independent and Dependent) for Animal Ibsen")
plt.xlabel("Time Bin (ms)")
plt.ylabel("Accuracy")
#fig.add_axes(ax)
p.show()
