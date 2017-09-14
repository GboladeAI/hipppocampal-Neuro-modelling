import pandas as pdb
import numpy as np
import pandas as pd
import scipy.io as spio

from matplotlib import cm
import sys
from math import exp, factorial, pow,log
from decimal import Decimal
import mysql.connector
def getDependentProb(ProbA,ProbB):

    return (ProbA + ProbB) - (ProbA * ProbB )
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
    selectstmt = selectstmt + " a.id = b.id_tblNEURONSPIKE and b.distance < 1   and a.CrossValidation  =1  "
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


    return varTimeSpikeDiff, summ,meshID


def getTotalTimeByRatInMesh():
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()

    selectstmt = " SELECT TimeInMesh FROM NueroSCi.tblTrainNueronSpikeCount where AnimalName='I'  order by mesh asc "
    print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()
    varTimeAccrossGrid = []


    for row in data :
        vTimeinMesh=row[0]
        varTimeAccrossGrid.append(float(vTimeinMesh))

    npsum= np.sum(varTimeAccrossGrid)

    curr.close()
    conn.close()


    return npsum,varTimeAccrossGrid


def getSpikeCountInMesh1(meshID,TotalTimeInMesh):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()


    selectstmt = "   "
    selectstmt = selectstmt + "  select  X.NeuronID, (SELECT   count(*) +1  from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id      "
    selectstmt = selectstmt + "  and d.x_axis !=0.00      "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    selectstmt = selectstmt + "  and a.CrossValidation=1      "
    selectstmt = selectstmt + "  and d.mesh=  " +str(meshID) +"    "
    selectstmt = selectstmt + "  and a.NeuronID=X.NeuronID)  SpikeCount   "
    selectstmt = selectstmt + "  FROM  "

    selectstmt = selectstmt + "  (SELECT  distinct  a.NeuronID as NeuronID from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id    and d.x_axis != 0.00      "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    selectstmt = selectstmt + "  and a.CrossValidation=1      "
    selectstmt = selectstmt + "  group by a.NeuronID   order by 1 asc )   X  "

    #print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()
    varNueronID = []
    varNeuronSpikeCount = []
    varFiringRateOfNeuronsinMesh = []
    #print data

    for row in data :

        varNueronID.append(row[0])
        varNeuronSpikeCount.append(row[1])
        # 1000 is to convert the time into second from milliseconds

        x = 0.00
        if float(TotalTimeInMesh[meshID])==0.00:
            x=0.00
        if float(TotalTimeInMesh[meshID]) > 0.00:
            x=float(row[1])/(float(TotalTimeInMesh[meshID]))

        varFiringRateOfNeuronsinMesh.append(x)


    curr.close()
    conn.close()

    #print varNeuronSpikeCount

    return meshID, varNueronID,varNeuronSpikeCount,varFiringRateOfNeuronsinMesh




def getSpikeCountInMesh( meshID,TotalTimeInMesh):
    TimeiNMesh=0.000
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()



    ssql = "   SELECT  distinct  a.NeuronID as NeuronID from NueroSCi.tblNeuronspikeI a,   "
    ssql = ssql + "       NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    ssql = ssql + "         where a.id = b.id_tblNEURONSPIKE        "
    ssql = ssql + "         and b.distance < 1    and b.id_tblLOCATIONDATA=d.id    and d.x_axis != 0.00     "
    ssql = ssql + "           and d.y_axis !=0.00      "
    ssql = ssql + "          and a.CrossValidation=1       "
    ssql = ssql + "            group by a.NeuronID   order by 1 asc   "
    #list of Nuerons
    curr.execute(ssql)
    data = curr.fetchall()
    varNueronID = []
    for row in data:varNueronID.append(row[0])

    selectstmt = " SELECT * FROM NueroSCi.tblTrainNueronSpikeCount    where mesh =  " + str(meshID)
    curr.execute(selectstmt)
    data = curr.fetchall()
    varNeuronSpikeCount = []
    varFiringRateOfNeuronsinMesh =[]
    #print data
    for row in data:
        TimeiNMesh = row[2]
        for nFields in range(3,39) :
            varNeuronSpikeCount.append(row[nFields]+1)
            if float(row[2])==0.00:
                varFiringRateOfNeuronsinMesh.append(0.00)
            else:
                varFiringRateOfNeuronsinMesh.append((row[nFields]+1)/float(row[2]))


    curr.close()
    conn.close()

    #return meshID, varNueronID,varNeuronSpikeCount,TimeiNMesh
    return meshID, varNueronID, varNeuronSpikeCount, varFiringRateOfNeuronsinMesh





def getSpikeCountInMesh_Test(TimeAtLocation,TotalTimeInMesh, Dt,meshID):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()

    t1 = float(TimeAtLocation) - Dt
    t2 = float(TimeAtLocation) + Dt

    selectstmt = "   "
    selectstmt = selectstmt + "  select X.NeuronID,  /*FLOOR(0 + RAND() * 4),*/ (SELECT   count(*)  from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id      "
    #selectstmt = selectstmt + "  and d.x_axis !=0.00      "
    #selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    selectstmt = selectstmt + "  and d.time_at_location >= "+str(t1)+"   "
    selectstmt = selectstmt + "  and d.time_at_location <= " + str(t2) + "  "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    selectstmt = selectstmt + "  and a.CrossValidation=0      "
    #selectstmt = selectstmt + "  and d.mesh=  " +str(meshID) +"  "
    #selectstmt = selectstmt + " and d.mesh = "+ str(meshID) + " "

    selectstmt = selectstmt + "  and a.NeuronID=X.NeuronID)  SpikeCount  "
    selectstmt = selectstmt + "  FROM  "

    selectstmt = selectstmt + "  (SELECT  distinct  a.NeuronID as NeuronID from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id    and d.x_axis != 0.00      "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    selectstmt = selectstmt + "  and a.CrossValidation=0      "
    selectstmt = selectstmt + "  group by a.NeuronID  )   X order by 1 asc   "

    #print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()
    varNueronID = []
    varNeuronSpikeCount = []
    varFiringRateOfNeuronsinMesh = []
    #print data

    for row in data :

        varNueronID.append(row[0])
        varNeuronSpikeCount.append(row[1])
        # 1000 is to convert the time into second from milliseconds
        if float(TotalTimeInMesh[meshID])==0.00:
            x=0.00
        if float(TotalTimeInMesh[meshID]) > 0.00:
            x=float(row[1])/(float(TotalTimeInMesh[meshID]))

        varFiringRateOfNeuronsinMesh.append(x)


    curr.close()
    conn.close()

    #print varNeuronSpikeCount

    return meshID, varNueronID,varNeuronSpikeCount,varFiringRateOfNeuronsinMesh

def ProcessMesh(x_axis,y_axis,myDt, testDataID):

    vmyDt = str(int(myDt*10))
    totTime, TotalTimeInMesh = getTotalTimeByRatInMesh()

    #get the mesh id
    conn = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
    curr = conn.cursor()
    ssql = " SELECT mesh FROM NueroSCi.tblLOCATIONDATAI where x_axis = " + str(x_axis) + "  and  y_axis =" + str(y_axis) + "  limit 1 "
    ssqlTIME_AT_LOCATION = " SELECT time_at_location FROM NueroSCi.tblLOCATIONDATAI where x_axis = " + str(x_axis) + "  and  y_axis =" + str(y_axis) + "  limit 1 "
    curr.execute(ssql)
    data = curr.fetchall()
    for row in data: meshID = row[0]

    curr.execute(ssqlTIME_AT_LOCATION)
    data = curr.fetchall()
    for row in data: time_AT_Location = row[0]

    time_AT_LocationUPPER = float(time_AT_Location) + myDt
    time_AT_LocationLOWER = float(time_AT_Location) - myDt



    curr.close()
    conn.close()
    print (" The location x:" + str(x_axis) + " y:"+ str(y_axis) + "   Mesh:"+str(meshID))
    NumberOfMeshes=400

    Mesh =[]

    l=0



    P_MESH=0.0
    varP_MESH =[]
    varP_Neuronxy_In_MESH =[]

    varProbInMeshTest =[]

    XX=0.00
    sumxx=0.00
    columns = ['MESH','PROBABILITY']
    df = pd.DataFrame(index=Mesh,columns=columns)

    proPrior = []

    meshID, varNueronIDTEST, varNeuronSpikeCountTEST, varFiringRateOfNeuronsinMeshTEST = getSpikeCountInMesh_Test(time_AT_Location, TotalTimeInMesh, myDt,meshID)
    outValmeshID=meshID

    outMesh =[]
    for k in range(0,NumberOfMeshes-1):

        vaMeshID=k+1
        meshID, varNueronID, varNeuronSpikeCount, varFiringRateOfNeuronsinMesh = getSpikeCountInMesh(vaMeshID, TotalTimeInMesh)
        sumxx = 0.00

        sizeofarr = len(varNueronIDTEST)
        P_Neuronxy_In_MESH = 1.00
        P_MESH = TotalTimeInMesh[k] * pow(np.sum(TotalTimeInMesh), -1.00)
        proPrior.append(P_MESH)
        varPn = []
        for l in range(0, sizeofarr ):


            FIRINGRATE_train = varFiringRateOfNeuronsinMesh[l]

            SpikeCount_Test = varNeuronSpikeCountTEST[l]

            Pn=((FIRINGRATE_train * myDt) ** SpikeCount_Test) * (exp(-1.00 * FIRINGRATE_train * myDt) )/ factorial(SpikeCount_Test)
            varPn.append(Pn)

        # print NueronSPikeProbability
        p = 1.00
        p = getDependentProb(varPn[0], varPn[1])
        for l in range(2, sizeofarr):
            # print"******************************************"
            p = getDependentProb(p, varPn[l])
            P_Neuronxy_In_MESH = P_Neuronxy_In_MESH * (
                ((FIRINGRATE_train * myDt) ** SpikeCount_Test) * exp(-1.00 * FIRINGRATE_train * myDt)) / factorial(
                SpikeCount_Test)
            #TotalDependent Probability -  Independent Pro (Poison)
            p=p-P_Neuronxy_In_MESH

        XX = p * P_MESH
        sumxx = sumxx + XX
        varP_MESH.append(P_MESH)
        varP_Neuronxy_In_MESH.append(float(P_Neuronxy_In_MESH))
        varProbInMeshTest.append(float(XX))
        outMesh.append(k+1)



        print    str(int(k+1)) +" : " + str(XX) +":::::"+ str(TotalTimeInMesh[k]) + "::: " + str(p)






    s = pd.Series(varProbInMeshTest, index=outMesh)
    s.sort_values(axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')
    df = pd.DataFrame(s)
    prmesh= s[s == df[0].iloc[0]].index[0]
    maxprmesh = df[0].iloc[0]

    import matplotlib.pyplot as plt
    plt.bar(outMesh,varProbInMeshTest)
    plt.suptitle("BPRM(Dependent): Test Mesh:"+str(outValmeshID)+" , Dt: "+str(float(myDt))+"s  Predicted Prob.: "+str(maxprmesh) +" Mesh: "+str(prmesh))
    plt.xlabel("Mesh")
    plt.ylabel("Probabilty")

    plt.savefig("/Users/akingboladeshada/Desktop/Project_MSc/ProjectDATA_New/REPORT_BPRM_D_"+str(vmyDt)+"/Mesh"+str(outValmeshID)+"_"+str(testDataID)+"_prediction")
    #plt.savefig("/Users/akingboladeshada/Desktop/Project_MSc/ProjectDATA_New/Mesh"+str(outValmeshID)+"_"+str(testDataID)+"_prediction")
    plt.close()

    vprior=proPrior[int(str(outValmeshID))-1]
    vprobtestmesh =varProbInMeshTest[int(str(outValmeshID))-1]
    vtimeinTestMesh=TotalTimeInMesh[int(str(outValmeshID))-1]
    vtimeinPredMesh = TotalTimeInMesh[int(str(prmesh)) - 1]

    updatestmt = "  UPDATE NueroSCi.tblBPRM_Dt"+str(vmyDt)+"00    "
    updatestmt = updatestmt + "    SET              "

    updatestmt = updatestmt + "    PredictedMesh_BPRM_D =  " + str(prmesh) + " "
    updatestmt = updatestmt + "    WHERE id = " + str(testDataID) + " "
    print (updatestmt)

    conn = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
    curr = conn.cursor()
    print updatestmt
    try:
        curr.execute(updatestmt)
        curr.execute("commit")

        conn.close()
        curr.close()
    except mysql.connector.ProgrammingError:
        print( "The following query failed:")
        print (updatestmt)




    return


DT=0.1
vmyDt=str(int(DT*10))
conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
curr=conn.cursor()
arrID = []
arrXAXIS = []
arrYAXIS = []
selectstmt = "  "

selectstmt = selectstmt + " SELECT id,x_axis, y_axis FROM NueroSCi.tblBPRM_Dt"+vmyDt+"00 where  PredictedMesh is  null " \
                                                                                     "and PredictedMesh_BPRM_D is   null " \
                                                                                     " and id in (select id from lastTAb)  "
print selectstmt
curr.execute(selectstmt)
data = curr.fetchall()

k=0

# Get the total Time inMeshes and TimeArra accros the meshes.
TotalTimeInGrid, TotalTimeInMesh = getTotalTimeByRatInMesh()
for row in data :
    arrID.append(row[0])
    arrXAXIS.append(row[1])
    arrYAXIS.append(row[2])
    k=k+1


curr.close()
conn.close()


for i in range (0,k):
    ProcessMesh(arrXAXIS[i],arrYAXIS[i], DT, arrID[i])




#ProcessMesh(69.0,559.0,0.1,140315)
#ProcessMesh(573.0,88.0,0.1)
#ProcessMesh(39,0.1)
#ProcessMesh(191,0.1)
#ProcessMesh(192,0.1)
#ProcessMesh(193,0.1)

#ProcessMesh(368,0.1)
#ProcessMesh(388,0.1)

#ProcessMesh(223,0.1)
#ProcessMesh(183,0.1)




