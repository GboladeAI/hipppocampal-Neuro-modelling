
import pandas as pdb
import numpy as np
import scipy.io as spio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='Gbolade', api_key='0nDAuNGs3qrAqbnopw6t')

from matplotlib import cm
import sys
import pylab as p

import mysql.connector
mmesh=7
con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

ssql = "   SELECT  distinct  a.NeuronID as NeuronID from NueroSCi.tblNeuronspikeI a,   "
ssql = ssql + "       NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
ssql = ssql + "         where a.id = b.id_tblNEURONSPIKE        "
ssql = ssql + "         and b.distance < 1    and b.id_tblLOCATIONDATA=d.id    and d.x_axis != 0.00     "
ssql = ssql + "           and d.y_axis !=0.00      "
#ssql = ssql + "          and a.CrossValidation=1       "
ssql = ssql + "            group by a.NeuronID   order by 1 asc   "
#list of Nuerons
cur.execute(ssql)
data = cur.fetchall()
varNueronID = []
my_xticks = []
for row in data:
    varNueronID.append(row[0])
    my_xticks.append(str(row[0]))



ssql="  SELECT AnimalName, mesh,    "
ssql=ssql + "    TimeInMesh,     "
ssql=ssql + "        n_1,     "
ssql=ssql + "        n_2,     "
ssql=ssql + "        n_3,     "
ssql=ssql + "        n_4,     "
ssql=ssql + "       n_5,     "
ssql=ssql + "       n_6,     "
ssql=ssql + "          n_7,     "
ssql=ssql + "          n_8,     "
ssql=ssql + "          n_9,     "
ssql=ssql + "          n_10,     "
ssql=ssql + "          n_11,     "
ssql=ssql + "          n_12,     "
ssql=ssql + "          n_13,     "
ssql=ssql + "          n_14,     "
ssql=ssql + "          n_15,     "
ssql=ssql + "          n_16,     "
ssql=ssql + "         n_17,     "
ssql=ssql + "          n_18,     "
ssql=ssql + "          n_19,     "
ssql=ssql + "          n_20,     "
ssql=ssql + "          n_21,     "
ssql=ssql + "          n_22,     "
ssql=ssql + "          n_23,     "
ssql=ssql + "          n_24,     "
ssql=ssql + "          n_25,     "
ssql=ssql + "          n_26,     "
ssql=ssql + "          n_27,     "
ssql=ssql + "          n_28,     "
ssql=ssql + "          n_29,     "
ssql=ssql + "          n_30,     "
ssql=ssql + "          n_31,     "
ssql=ssql + "          n_32,     "
ssql=ssql + "          n_33,     "
ssql=ssql + "          n_34,     "
ssql=ssql + "          n_35,     "
ssql=ssql + "          n_36     "
ssql=ssql + "      FROM NueroSCi.tblTrainNueronSpikeCount     "
ssql=ssql + "      where mesh =      "+str(mmesh) +  "   "
cur.execute(  ssql     )
# fetch all of the rows from the query
data = cur.fetchall ()
xpoints = []
ypoints = []
varColor = []
MyData = []
MyTime = []

# print the rows
index=0
for row in data:
    TimeiNMesh = row[2]
    if TimeiNMesh >0.000:
        for nFields in range(3, 39):
            xpoints.append(varNueronID[index] )
            index=index+1
            ypoints.append(float(row[nFields])/float(TimeiNMesh))


fig=p.figure()

# plot3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array


width=0.5

plt.xticks(xpoints, my_xticks)
plt.bar(xpoints,ypoints, width, color="blue")
plt.xlabel('Neurons')
plt.ylabel('Firing Rate (Hertz)')
plt.title(" Firing Rate Nuerons In Mesh : "+ str(mmesh))
#fig.add_axes(ax)
plt.show()
