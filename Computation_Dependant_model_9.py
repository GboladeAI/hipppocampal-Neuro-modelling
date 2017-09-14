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


def getSpikeCountInMesh_Test(TimeAtLocation, Dt,meshID):
    vDt = Dt * 10  # convert it to whole numebr soa as to pick the correct table storing the information.
    vDt = int(vDt)
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()

    t1 = float(TimeAtLocation) - Dt
    t2 = float(TimeAtLocation) + Dt

    selectstmt = "   "
    selectstmt = selectstmt + "  select X.NeuronID,   (SELECT   count(*)  from NueroSCi.tblNeuronspikeI a,   "
    selectstmt = selectstmt + "  NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d      "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE      "
    selectstmt = selectstmt + "  and b.distance < 1    and b.id_tblLOCATIONDATA=d.id      "

    selectstmt = selectstmt + "  and d.time_at_location >= "+str(t1)+"   "
    selectstmt = selectstmt + "  and d.time_at_location <= " + str(t2) + "  "
    selectstmt = selectstmt + "  and d.y_axis !=0.00      "
    selectstmt = selectstmt + "  and a.CrossValidation=0      "


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

    if np.sum(varNeuronSpikeCount) !=0:


        length= len(varNueronID)
        # the NueronID with maximu spike
        print (varNeuronSpikeCount)
        NueronidMaxSPikecount = str(np.where(varNeuronSpikeCount == np.max(varNeuronSpikeCount)))
        print (NueronidMaxSPikecount)
        NueronidMaxSPikecount = NueronidMaxSPikecount.replace("(array([", "", 1)
        NueronidMaxSPikecount = NueronidMaxSPikecount.replace("]),)", "", 1)
        NueronidMaxSPikecount = NueronidMaxSPikecount.split(",")[0]
        NueronidMaxSPikecount =int(NueronidMaxSPikecount)

        nueronIDWithMaxVal = varNueronID[NueronidMaxSPikecount]
        nueronIDSpikeCounVal=varNeuronSpikeCount[NueronidMaxSPikecount]
        print ("************************")
        print (nueronIDWithMaxVal)
        print(nueronIDSpikeCounVal)

        #check the Dt and improvise the  spikecount using correlation coefficient
        for nueronIDindex in range (0,length-1):
            if varNeuronSpikeCount[nueronIDindex]==0:
                # use the correlation coeficient to improvise
                ssql = "     "
                ssql = ssql+"   SELECT CorrCoef FROM NueroSCi.PairwiseCorrelation"+str(vDt)+"00   where AnimalName='I' "
                ssql = ssql + "    and NueronID_A = " + str(nueronIDWithMaxVal) + " "
                ssql = ssql + "    and NueronID_B = " + str(varNueronID[nueronIDindex]) + " "
                ssql = ssql + "    and Type='Positive' "
                print(ssql)
                curr.execute(ssql)
                data = curr.fetchall()
                vCorrCoef=0.00
                for row in data: vCorrCoef=row[0]
                #set the spike count to  the pairewice approximated value
                x= nueronIDSpikeCounVal * float(vCorrCoef)
                varNeuronSpikeCount[nueronIDindex]=round(x)




        print (varNeuronSpikeCount)

        curr.close()
        conn.close()

        #print varNeuronSpikeCount

    return meshID, varNueronID,varNeuronSpikeCount



def getSpikeCountInMesh_Train( meshID,Dt):
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

    #print data
    for row in data:
        TimeiNMesh = row[2]
        for nFields in range(3,39) :
            varNeuronSpikeCount.append(row[nFields])


    curr.close()
    conn.close()
    return meshID, varNueronID,varNeuronSpikeCount,TimeiNMesh


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
        varTimeAccrossGrid.append(vTimeinMesh)

    npsum= np.sum(varTimeAccrossGrid)

    curr.close()
    conn.close()


    return npsum,varTimeAccrossGrid



import datetime
print (datetime.datetime.now())




def ProcessMesh(x_axis,y_axis,myDt, testDataID):

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






    meshID, varNueronIDTEST, varNeuronSpikeCountTEST = getSpikeCountInMesh_Test(time_AT_Location, myDt,meshID)
    outValmeshID=meshID
    varProbInMeshTest =[]
    MyMesh = []

    if np.sum(varNeuronSpikeCountTEST) != 0:
        for k in range(0,NumberOfMeshes-1):

            vaMeshID=k+1
            MyMesh.append(k+1)
            meshID, varNueronID, varNeuronSpikeCount ,TotalTimeINMesh = getSpikeCountInMesh_Train(vaMeshID,myDt)
            sumxx = 0.00



            sizeofarr = len(varNueronIDTEST)
            # add the spikecouts for train and test
            NueronSPikeAfterAddition = []
            for ll in range(0, sizeofarr ):
                SpikeCountforMesh = int(varNeuronSpikeCountTEST[ll] ) +  varNeuronSpikeCount[ll]
                NueronSPikeAfterAddition.append(SpikeCountforMesh)


            #print "NueronSPikeAfterAdditionNueronSPikeAfterAdditionNueronSPikeAfterAdditionNueronSPikeAfterAddition"
            #print NueronSPikeAfterAddition
            #compute the probability
            summm=np.sum(NueronSPikeAfterAddition)
            #print "summmsummmsummmsummmsummmsummmsummmsummmsummmsummm"
            #print summm
            NueronSPikeProbability =[]
            for l in range(0, sizeofarr ):
                prob=NueronSPikeAfterAddition[l]*1.00000/summm*1.0000
                NueronSPikeProbability.append(float(prob))


            p=1.00
            p= getDependentProb(NueronSPikeProbability[0],NueronSPikeProbability[1])
            for l in range(2, sizeofarr ):
                #print"******************************************"
                p = getDependentProb(p,NueronSPikeProbability[l])
                #print p

            #Multiply the total Probability with the Prior..
            priorProb = (float(TimeArrInMehses[k]) )/ float (TotalTimeInGrid )
            #Pmesh=priorProb * p
            if priorProb ==0.00:
                Pmesh=0.00
            else:
                Pmesh =  priorProb * p
            varProbInMeshTest.append(Pmesh)
            #print  "Mesh ::" + str(k)   +"       Prior Probability::" + str(priorProb)  +"   Posterior Probability::"+ str(p)
            print  str(k) + "  ::" + str(priorProb) + "  ::" + str(p)  + "  ::"+str(Pmesh)

        s = pd.Series(varProbInMeshTest, index=MyMesh)
        s.sort_values(axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')
        df = pd.DataFrame(s)
        prmesh= s[s == df[0].iloc[0]].index[0]
        maxprmesh = df[0].iloc[0]
        import matplotlib.pyplot as plt
        plt.bar(MyMesh, varProbInMeshTest)
        plt.suptitle("Dependant(PairewiseCorrelation): Test Mesh:" + str(outValmeshID) + " , Dt: " + str(float(myDt)) + "s  Predicted Prob.: " + str(
            maxprmesh) + " Mesh: " + str(prmesh))
        plt.xlabel("Mesh")
        plt.ylabel("Probabilty")

        plt.savefig(
            "/Users/akingboladeshada/Desktop/Project_MSc/ProjectDATA_New/REPORT_DEPENDANT_9/Mesh" + str(outValmeshID) + "_" + str(
                testDataID) + "_prediction")
        plt.close()



        updatestmt = "  UPDATE NueroSCi.tblBPRM_Dt900    "
        updatestmt = updatestmt + "    SET              "

        updatestmt = updatestmt + "    PredictedMesh_D =  " + str(prmesh) + " "
        updatestmt = updatestmt + "    WHERE id = " + str(testDataID) + " "
        print (updatestmt)

        conn = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
        curr = conn.cursor()
        # print updatestmt
        try:
            curr.execute(updatestmt)
            curr.execute("commit")

            conn.close()
            curr.close()
        except mysql.connector.ProgrammingError:
            print("The following query failed:")
            print (updatestmt)

    return




conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
curr=conn.cursor()
arrID = []
arrXAXIS = []
arrYAXIS = []
selectstmt = "  "
#selectstmt = selectstmt + " SELECT id,x_axis, y_axis FROM NueroSCi.tblBPRM_Dt100 where  PriorProb_mesh is  null and mesh in (28)  limit 5  "
selectstmt = selectstmt + " SELECT id,x_axis, y_axis FROM NueroSCi.tblBPRM_Dt900  where   PriorProb_mesh is not null and PredictedMesh_D is  null  "

curr.execute(selectstmt)
data = curr.fetchall()

k=0

# Get the total Time inMeshes and TimeArra accros the meshes.
TotalTimeInGrid, TimeArrInMehses = getTotalTimeByRatInMesh()

for row in data :
    arrID.append(row[0])
    arrXAXIS.append(row[1])
    arrYAXIS.append(row[2])
    k=k+1


curr.close()
conn.close()


for i in range (0,k-1):
    ProcessMesh(arrXAXIS[i],arrYAXIS[i], 0.9, arrID[i])


#ProcessMesh(256.0,525.0,0.1,163238)








print (datetime.datetime.now())
