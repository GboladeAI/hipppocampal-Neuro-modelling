
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

def getTotalTimeByRatInMesh(meshID):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()
    selectstmt = ""

    selectstmt = " SELECT "
    selectstmt = selectstmt + " d.id, d.AnimalName, d.time_at_location, a.TimeSpike, d.x_axis, d.y_axis, d.mesh, a.CrossValidation  "
    selectstmt = selectstmt + " from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP "
    selectstmt = selectstmt + " b, NueroSCi.tblLOCATIONDATAI d "
    selectstmt = selectstmt + " where "
    selectstmt = selectstmt + " a.id = b.id_tblNEURONSPIKE and b.distance < 1     "
    selectstmt = selectstmt + " and b.id_tblLOCATIONDATA = d.id    and    a.TimeSpike >= 5285 and a.TimeSpike<=7353 "
    selectstmt = selectstmt + " and d.mesh = "+str(meshID)+ " "
    selectstmt = selectstmt + " order by  "
    selectstmt = selectstmt + "   4 asc "
    #print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()
    varTimeSpike = []
    varTimeSpikeDiff = []
    k=0
    summ=0.00

    for row in data :
        mymeshID=row[6]
        varTimeSpike.append(float(row[2]))
        if k== 0 :
            varTimeSpikeDiff.append(float("0.00"))
        else:
            if abs((float(varTimeSpike[k])- float(varTimeSpike[k-1]))) < 6.00 :
                varTimeSpikeDiff.append(float(varTimeSpike[k])- float(varTimeSpike[k-1]))
                summ=summ + float(varTimeSpike[k])- float(varTimeSpike[k-1])

        k=k+1

    #print varTimeSpikeDiff
    npsum= np.sum(varTimeSpikeDiff)

    curr.close()
    conn.close()


    return summ


def getDistanceCoveredPerMEsh(vmesh):
    con = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
    cur = con.cursor()
    ssql = "  select d.mesh, a.BrainRegion, a.NeuronID, d.x_axis,  d.y_axis,a.TimeSpike,d.time_at_location    "
    ssql = ssql + "   ,b.distance,count(a.NeuronID)   "
    ssql = ssql + "   from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d   "
    ssql = ssql + "   where a.id = b.id_tblNEURONSPIKE and b.distance < 1 and b.id_tblLOCATIONDATA=d.id    "
    ssql = ssql + "   and d.x_axis !=0.00 and d.y_axis !=0.00 and a.AnimalName='I' and a.BrainRegion='hc'   "
    ssql = ssql + "   and d.mesh = " + str(vmesh) + "       "
    ssql = ssql + "   group by d.mesh,a.BrainRegion, a.NeuronID ,d.x_axis,  d.y_axis,a.TimeSpike,d.time_at_location ,b.distance   "
    ssql = ssql + "   order by 1 asc, 6 asc, 7 desc  "
    cur.execute(ssql)
    # fetch all of the rows from the query
    data = cur.fetchall()

    Distance =[]
    k=0
    #print "=============================="
    #print "Mesh****"+ str(vmesh)
    #print "______________________________"
    for row in data:
        if k==0:
            #Distance.append(0.00)
            pre_xaxis = row[3]
            pre_yaxis = row[4]
            pre_time = row[5]

        current_xaxis=row[3]
        current_yaxis=row[4]
        current_time=row[5]
        # take care of the spurion animal step
        if current_time - pre_time <6.00:
            dist =math.pow(((current_xaxis-pre_xaxis)**2 + (current_yaxis-pre_yaxis)**2), 0.5)
            #print dist
            Distance.append(dist)

        pre_xaxis = row[3]
        pre_yaxis = row[4]
        pre_time = row[5]

        k=k+1




    con.close()
    cur.close()

    return  np.sum(Distance)
con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

cur.execute("SELECT mesh FROM NueroSCi.Distance_Covered1  ")
# fetch all of the rows from the query
data = cur.fetchall ()
Mesh = []
MyDist = []

# print the rows
for row in data :
    varmesh=row[0]
    Mesh.append( varmesh)
    ddist= getDistanceCoveredPerMEsh(varmesh)
    timeInMesh = getTotalTimeByRatInMesh(varmesh)
    MyDist.append( ddist)
    print varmesh, ddist,timeInMesh
    con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    cur=con.cursor()
    cur.execute(" update  NueroSCi.Distance_Covered1 set distance_covered=" + str(ddist) +" , TimeInMesh ="+str(timeInMesh)+" where  mesh ="+str(varmesh)+" ")
    cur.execute("commit")
    cur.close()
    con.close()





#print Mesh, MyDist
