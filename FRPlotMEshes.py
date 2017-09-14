
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
ssql="  SELECT     "
ssql=ssql+ "  mesh,TimeInMesh       "
ssql=ssql+ "  ,     "
ssql=ssql+ "  (     "
ssql=ssql+ "  n_1     "
ssql=ssql+ "  +n_2     "
ssql=ssql+ "  +n_3     "
ssql=ssql+ "  +n_4     "
ssql=ssql+ "  +n_5     "
ssql=ssql+ "  +n_6     "
ssql=ssql+ "  +n_7     "
ssql=ssql+ "  +n_8     "
ssql=ssql+ "  +n_9     "
ssql=ssql+ "  +n_10     "
ssql=ssql+ "  +n_11     "
ssql=ssql+ "  +n_12     "
ssql=ssql+ "  +n_13     "
ssql=ssql+ "  +n_14     "
ssql=ssql+ "  +n_15     "
ssql=ssql+ "  +n_16     "
ssql=ssql+ "  +n_17     "
ssql=ssql+ "  +n_18     "
ssql=ssql+ "  +n_19     "
ssql=ssql+ "  +n_20     "
ssql=ssql+ "  +n_21     "
ssql=ssql+ "  +n_22     "
ssql=ssql+ "  +n_23     "
ssql=ssql+ "  +n_24     "
ssql=ssql+ "  +n_25     "
ssql=ssql+ "  +n_26     "
ssql=ssql+ "  +n_27     "
ssql=ssql+ "  +n_28     "
ssql=ssql+ "  +n_29     "
ssql=ssql+ "  +n_30     "
ssql=ssql+ "  +n_31     "
ssql=ssql+ "  +n_32     "
ssql=ssql+ "  +n_33     "
ssql=ssql+ "  +n_34     "
ssql=ssql+ "  +n_35     "
ssql=ssql+ "  +n_36     "
ssql=ssql+ "  )      "
ssql=ssql+ "  FROM NueroSCi.tblTrainNueronSpikeCount        "
ssql=ssql+ "  where TimeInmesh>5.00     "
ssql=ssql+ "  order by 3 desc     "
cur.execute(  ssql     )
# fetch all of the rows from the query
print ssql
data = cur.fetchall ()
xpoints = []
ypoints = []
varColor = []
MyData = []
MyTime = []
# print the rows
for row in data :
    xpoints.append( (row[0]))
    ypoints.append( float(row[2])/
                    float(row[1]))


fig=p.figure()

# plot3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array
plt.bar(xpoints,ypoints)
plt.xlabel('Meshes')
plt.ylabel('Firing Rate (Hertz)')
plt.title(" Estimated Cumulative Nueron Population Firing Rate Accross Meshes")
#fig.add_axes(ax)
p.show()
