import pandas as pdb
import numpy as np
import pandas as pd
import scipy.io as spio

from matplotlib import cm
import sys
from math import exp, factorial, pow,log
from decimal import Decimal
import mysql.connector

def getTotalTimeByRatInMesh(meshID):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()
    selectstmt = ""
    meshID= meshID+1
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

def getSpikeCountInMesh(meshID,TimeInMesh):

    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()


    selectstmt = "   "
    selectstmt = selectstmt + "  select  X.NeuronID, (SELECT   count(*)  from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id      "
    selectstmt = selectstmt + "  and d.x_axis !=0.00      "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    #selectstmt = selectstmt + "  and a.CrossValidation=1      "
    selectstmt = selectstmt + "  and d.mesh=  " +str(meshID) +"    "
    selectstmt = selectstmt + "  and a.NeuronID=X.NeuronID)  SpikeCount   "
    selectstmt = selectstmt + "  FROM  "

    selectstmt = selectstmt + "  (SELECT  distinct  a.NeuronID as NeuronID from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id    and d.x_axis != 0.00      "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    #selectstmt = selectstmt + "  and a.CrossValidation=1      "
    selectstmt = selectstmt + "  group by a.NeuronID   order by 1 asc )   X  "

    #print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()

    #print data
    ssInsert = "    INSERT INTO NueroSCi.tblNueronSpikeCount (  "
    ssInsert = ssInsert + "   AnimalName,   mesh  "
    ssInsert = ssInsert + "  ,  TimeInMesh   ,  "
    ssInsert = ssInsert + " n_1,  "
    ssInsert = ssInsert + " n_2,  "
    ssInsert = ssInsert + " n_3,  "
    ssInsert = ssInsert + " n_4,  "
    ssInsert = ssInsert + " n_5,  "
    ssInsert = ssInsert + " n_6,  "
    ssInsert = ssInsert + " n_7,  "
    ssInsert = ssInsert + " n_8,  "
    ssInsert = ssInsert + " n_9,  "
    ssInsert = ssInsert + " n_10,  "
    ssInsert = ssInsert + " n_11,  "
    ssInsert = ssInsert + " n_12,  "
    ssInsert = ssInsert + " n_13,  "
    ssInsert = ssInsert + " n_14,  "
    ssInsert = ssInsert + " n_15,  "
    ssInsert = ssInsert + " n_16,  "
    ssInsert = ssInsert + " n_17,  "
    ssInsert = ssInsert + " n_18,  "
    ssInsert = ssInsert + " n_19,  "
    ssInsert = ssInsert + " n_20,  "
    ssInsert = ssInsert + " n_21,  "
    ssInsert = ssInsert + " n_22,  "
    ssInsert = ssInsert + " n_23,  "
    ssInsert = ssInsert + " n_24,  "
    ssInsert = ssInsert + " n_25,  "
    ssInsert = ssInsert + " n_26,  "
    ssInsert = ssInsert + " n_27,  "
    ssInsert = ssInsert + " n_28,  "
    ssInsert = ssInsert + " n_29,  "
    ssInsert = ssInsert + " n_30,  "
    ssInsert = ssInsert + " n_31,  "
    ssInsert = ssInsert + " n_32,  "
    ssInsert = ssInsert + " n_33,  "
    ssInsert = ssInsert + " n_34,  "
    ssInsert = ssInsert + " n_35,  "
    ssInsert = ssInsert + " n_36)  "
    ssInsert = ssInsert + " VALUES  "
    ssInsert = ssInsert + " ('I'  "
    ssInsert = ssInsert + " ,"+ str(meshID)+"   "
    ssInsert = ssInsert + " ,'" + str(TimeInMesh) + "'   "


    for row in data :
        vv=1
     

        ssInsert = ssInsert + " ," + str(row[1]) + "   "
    #close the bracket
    ssInsert = ssInsert + " )  "

    try:
        curr.execute(ssInsert)
        curr.execute("commit")
        print ("Mesh:::::" + str(meshID))
    except mysql.connector.ProgrammingError:
        print("The following query failed:")
        print (ssInsert)



    curr.close()
    conn.close()

    return


import datetime
print (datetime.datetime.now())


for i in range(1, 401):
    vMesh=i
    vTimeInMesh= getTotalTimeByRatInMesh(vMesh)
    getSpikeCountInMesh(vMesh,vTimeInMesh)


print (datetime.datetime.now())
