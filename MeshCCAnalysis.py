import pandas as pdb
import numpy as np
from pandas import *
import scipy.io as spio
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
from math import exp, factorial, pow,log
from decimal import Decimal
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
    selectstmt = selectstmt + " a.id = b.id_tblNEURONSPIKE and b.distance < 1   and a.CrossValidation  =1  "
    selectstmt = selectstmt + " and b.id_tblLOCATIONDATA = d.id    and    a.TimeSpike >= 5285 and a.TimeSpike<=7353 "
    selectstmt = selectstmt + " and d.mesh =  " + str(meshID) + "  + 1 "
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


    return varTimeSpikeDiff, summ,npsum


def getTotalTimeByRatInMesh(meshID):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()
    selectstmt = ""
    selectstmt = " SELECT "
    selectstmt = selectstmt + " d.id, d.AnimalName, d.time_at_location, a.TimeSpike, d.x_axis, d.y_axis, d.mesh, a.CrossValidation  "
    selectstmt = selectstmt + " from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP "
    selectstmt = selectstmt + " b, NueroSCi.tblLOCATIONDATAI d "
    selectstmt = selectstmt + " where "
    selectstmt = selectstmt + " a.id = b.id_tblNEURONSPIKE and b.distance < 1    "
    selectstmt = selectstmt + " and b.id_tblLOCATIONDATA = d.id    and    a.TimeSpike >= 5285 and a.TimeSpike<=7353   and d.x_axis !=0 and  d.y_axis !=0  "
    selectstmt = selectstmt + " and d.mesh =  " + str(meshID) + "  + 1 "
    selectstmt = selectstmt + " order by  "
    selectstmt = selectstmt + "   4 asc "
    curr.execute(selectstmt)
    data = curr.fetchall()
    varTimeSpike = []
    varTimeSpikeDiff = []
    k=0
    summ=0.00
    for row in data :
        varTimeSpike.append(float(row[2]))
        if k== 0 :
            varTimeSpikeDiff.append(float("0.00"))
        else:
            if abs((float(varTimeSpike[k])- float(varTimeSpike[k-1]))) < 6.00 :
                varTimeSpikeDiff.append(float(varTimeSpike[k])- float(varTimeSpike[k-1]))
                summ=summ + float(varTimeSpike[k])- float(varTimeSpike[k-1])

        k=k+1
    npsum= np.sum(varTimeSpikeDiff)

    curr.close()
    conn.close()


    return varTimeSpikeDiff, summ,npsum

def getSpikeCountInMesh(meshID,TotalTimeInMesh):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()

    selectstmt = "   "
    selectstmt = selectstmt + "  select X.NeuronID, (SELECT   count(*) +1  from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id      "
    selectstmt = selectstmt + "  and d.x_axis !=0.00      "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    selectstmt = selectstmt + "  and d.mesh=  " +str(meshID) +"  + 1  "
    selectstmt = selectstmt + "  and a.NeuronID=X.NeuronID)  SpikeCount   "
    selectstmt = selectstmt + "  FROM  "

    selectstmt = selectstmt + "  (SELECT  distinct  a.NeuronID as NeuronID from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id    and d.x_axis != 0.00      "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    selectstmt = selectstmt + "  group by a.NeuronID   order by 1 asc )   X  "

    curr.execute(selectstmt)
    data = curr.fetchall()
    varNueronID = []
    varNeuronSpikeCount = []
    varFiringRateOfNeuronsinMesh = []




    for row in data :
        varNueronID.append(row[0])
        varNeuronSpikeCount.append(row[1])
        # 1000 is to convert the time into second from milliseconds

        x = 0.00
        if TotalTimeInMesh[meshID]==0.00:
            x=0.00
        if TotalTimeInMesh[meshID] > 0.00:
            x=float(row[1])/float(TotalTimeInMesh[meshID])

        varFiringRateOfNeuronsinMesh.append(x)


    curr.close()
    conn.close()

    #print varNeuronSpikeCount

    return meshID, varNueronID,varNeuronSpikeCount,varFiringRateOfNeuronsinMesh
pairnmesh =[]
corrcoef =[]
N=400
M=400
varMesh=0
#get total time in mesh
Mesh =[]
TotalTimeInMesh=[]
Dt_btweenMeshes=[]
indexarr=[]
l=0
for j in range(0,N):
    xx, a, b=getTotalTimeByRatInMesh(j)
    Mesh.append(j)
    TotalTimeInMesh.append(a)

totTime=np.sum(TotalTimeInMesh)
print totTime



count=0

con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

animalname ="I"
# purge the table
insertstmt ="DELETE from  NueroSCi.tbCorrCoefMesh  where  AnimalName='"+animalname+"' "
commitstmt ="commit "

try:
    cur.execute(insertstmt)
    cur.execute(commitstmt)


except mysql.connector.ProgrammingError:
    print "The following query failed:"
    print insertstmt + " " + commitstmt






for  k in  range(0 , 400 ):
    meshIDk, varNueronIDk, varNeuronSpikeCountk, varFiringRateOfNeuronsinMeshk = getSpikeCountInMesh(k,TotalTimeInMesh)
    for j in  range(k+1 , 400 ):

        PairMesh = str(k) +":"+ str(j)
        meshIDj, varNueronIDj, varNeuronSpikeCountj, varFiringRateOfNeuronsinMeshj=getSpikeCountInMesh(j,TotalTimeInMesh)

        a, b = np.corrcoef(varFiringRateOfNeuronsinMeshk, varFiringRateOfNeuronsinMeshj)[0]


        insertstmt = (
            "INSERT INTO NueroSCi.tbCorrCoefMesh(IDROW,IDCOL, CORRCOEF, AnimalName) VALUES('%s','%s', '%s', '%s')" % (
                str(k), str(j), str(b),animalname ))

        try:
            cur.execute(insertstmt)
            cur.execute(commitstmt)


        except mysql.connector.ProgrammingError:
            print "The following query failed:"
            print insertstmt

        count=count+1
        print count



#df = DataFrame({'Pairnmesh':pairnmesh, 'CorrCoef': corrcoef})

#df.sort_values('CorrCoef', axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')

#print "Sorted Pairwise Correlation"
#print df

