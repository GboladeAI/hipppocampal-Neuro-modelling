
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
sql=sql+"  and a.TimeInMesh>5.00   "
sql=sql+"  and c.mesh=b.mesh   "
sql=sql+"  and a.AnimalName='I'   "
sql = sql + "  and ( a.n_1    "
sql = sql + "  +   a.n_2   "
sql = sql + " + a.n_3  "
sql = sql + " + a.n_4   "
sql = sql + "+ a.n_5  "
sql = sql + "+ a.n_6 "
sql = sql + "+ a.n_7 "
sql = sql + "+ a.n_8 "
sql = sql + "+ a.n_9 "
sql = sql + "+ a.n_10 "
sql = sql + "+ a.n_11 "
sql = sql + "+ a.n_12 "
sql = sql + "+ a.n_13 "
sql = sql + "+ a.n_14 "
sql = sql + "+ a.n_15 "
sql = sql + "+ a.n_16 "
sql = sql + "+ a.n_17 "
sql = sql + "+ a.n_18 "
sql = sql + "+ a.n_19 "
sql = sql + "+ a.n_20 "
sql = sql + "+ a.n_21 "
sql = sql + "+ a.n_22 "
sql = sql + "+ a.n_23 "
sql = sql + "+ a.n_24 "
sql = sql + "+ a.n_25 "
sql = sql + "+ a.n_26 "
sql = sql + "+ a.n_27 "
sql = sql + "+ a.n_28 "
sql = sql + "+ a.n_29 "
sql = sql + "+ a.n_30 "
sql = sql + "+ a.n_31 "
sql = sql + "+ a.n_32 "
sql = sql + "+ a.n_33 "
sql = sql + "+ a.n_34 "
sql = sql + "+ a.n_35 "
sql = sql + "+ a.n_36 ) > 0  "
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
st=0
for row in data :
    st=st+row[2]
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





fig=p.figure()

# plot3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array
plt.scatter(Timepoints1,n_1_points, marker='o',color= 'b')
plt.scatter(Timepoints1,n_2_points,marker='o', color=  'g')
plt.scatter(Timepoints1,n_3_points,marker='o', color=  'r')
plt.scatter(Timepoints1,n_4_points,marker='o', color= 'purple')
plt.scatter(Timepoints1,n_5_points,marker='o', color=  'coral')
plt.scatter(Timepoints1,n_6_points,marker='o', color= 'brown')
plt.scatter(Timepoints1,n_7_points,marker='o', color= 'orange')
plt.scatter(Timepoints1,n_8_points,marker='o', color=  'black')
plt.scatter(Timepoints1,n_9_points,marker='o',color=  'indigo')
plt.scatter(Timepoints1,n_10_points,marker='o', color= 'violet')

plt.scatter(Timepoints1,n_11_points, marker='o',color= 'tan')
plt.scatter(Timepoints1,n_12_points,marker='o', color=  'darksalmon')
plt.scatter(Timepoints1,n_13_points,marker='o', color=  'sienna')
plt.scatter(Timepoints1,n_14_points,marker='o', color= 'maroon')
plt.scatter(Timepoints1,n_15_points,marker='o', color=  'lightseagreen')
plt.scatter(Timepoints1,n_16_points,marker='o', color= 'navy')
plt.scatter(Timepoints1,n_17_points,marker='o', color= 'mediumpurple')
plt.scatter(Timepoints1,n_18_points,marker='o', color=  'plum')
plt.scatter(Timepoints1,n_19_points,marker='o',color=  'c')
plt.scatter(Timepoints1,n_20_points,marker='o', color= 'fuchsia')


patch1 = mpatches.Patch(color='b', label='Neuron  1')
patch2 = mpatches.Patch(color='g', label='Neuron  2')
patch3 = mpatches.Patch(color='r', label='Neuron  3')
patch4 = mpatches.Patch(color='purple', label='Neuron  4')
patch5 = mpatches.Patch(color='gray', label='Neuron  5')
patch6 = mpatches.Patch(color='brown', label='Neuron  6')
patch7 = mpatches.Patch(color='orange', label='Neuron  7')
patch8 = mpatches.Patch(color='black', label='Neuron  8')
patch9 = mpatches.Patch(color='indigo', label='Neuron  9')
patch10 = mpatches.Patch(color='violet', label='Neuron 10')
patch11 = mpatches.Patch(color='tan', label='Neuron  11')
patch12 = mpatches.Patch(color='darksalmon', label='Neuron  12')
patch13 = mpatches.Patch(color='sienna', label='Neuron  13')
patch14 = mpatches.Patch(color='maroon', label='Neuron  14')
patch15 = mpatches.Patch(color='lightseagreen', label='Neuron  15')
patch16 = mpatches.Patch(color='navy', label='Neuron  16')
patch17 = mpatches.Patch(color='mediumpurple', label='Neuron  17')
patch18 = mpatches.Patch(color='plum', label='Neuron  18')
patch19 = mpatches.Patch(color='c', label='Neuron  19')
patch20 = mpatches.Patch(color='fuchsia', label='Neuron 20')

plt.legend(handles=[patch1,patch2,patch3,patch4,patch5,patch6,patch7,patch8,patch9,patch10,
                    patch11, patch12, patch13, patch14, patch15, patch16, patch17, patch18, patch19, patch20])

plt.title("Firing Rates of Nueron IDs(1,2,3....20) for Animal Ibsen  while running")
plt.xlabel("Time (ms)")
plt.ylabel("Firing Rate (Hertz)")
#fig.add_axes(ax)
p.show()
