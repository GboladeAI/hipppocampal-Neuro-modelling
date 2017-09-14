
import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt
import mysql.connector
con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()
id=1



matfile = '/Users/akingboladeshada/Desktop/Project_MSc/ProjectDATA_New/Tmaze_spiking_data (1).mat'
matdata = spio.loadmat(matfile)
print matdata.keys()
for ratCells in matdata.keys():
    if ratCells.find('cells') != -1:
        tspk = matdata[ratCells]
        n = len(tspk)
        ratCells = ratCells.replace("cells", "")
        print "animal:::::::::::" + ratCells

        for j in range(n):
        #if tspk[0][0][34][0]!='hc':
            tempData= tspk[ j ][0][0]
            o = len(tspk[j][0][0])
            for i in range(o):
                #print ratCells, j+1, tempData[ i ][0], tspk[0][0][34][0]
                animalname = ratCells
                timeatspike = tempData[ i ][0]
                brainregion = tspk[0][0][34][0]


                insertstmt = (
                    "INSERT INTO NueroSCi.tblNEURONSPIKE(id,AnimalName, NeuronID, TimeSpike,BrainRegion) VALUES('%s','%s', '%s', '%s','%s')" % (
                        id, animalname, j+1,timeatspike, brainregion))

                try:
                    cur.execute(insertstmt)
                    #print id
                    id = id + 1

                except mysql.connector.ProgrammingError:
                    print "The following query failed:"
                    print insertstmt

    con.commit()

con.close()




