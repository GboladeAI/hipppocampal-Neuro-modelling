
import math

import numpy as numpy
from pandas import *
import pylab as pltlab
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import bisect
import pandas as pdb
import numpy as np
import pandas as pd
import scipy.io as spio
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
from math import exp, factorial, pow, log
from decimal import Decimal
import mysql.connector
import os

import sys

#orig_stdout = sys.stdout
#f = open('outputPairwiseCorrelation.txt', 'w')
#sys.stdout = f

cwd = os.getcwd()
import datetime
print (datetime.datetime.now())

def getSpikeDatPoint(NueronID):
    conn = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
    curr = conn.cursor()
    selectstmt = " SELECT "
    selectstmt = selectstmt + " d.id, d.AnimalName, d.time_at_location, a.TimeSpike, d.x_axis, d.y_axis, d.mesh, a.CrossValidation  "
    selectstmt = selectstmt + " from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP "
    selectstmt = selectstmt + " b, NueroSCi.tblLOCATIONDATAI d "
    selectstmt = selectstmt + " where "
    selectstmt = selectstmt + " a.id = b.id_tblNEURONSPIKE and b.distance < 1    "
    selectstmt = selectstmt + " and b.id_tblLOCATIONDATA = d.id    and    a.TimeSpike >= 5285 and a.TimeSpike<=7353 "
    selectstmt = selectstmt + " and a.NeuronID  = " + str(NueronID) + " "
    selectstmt = selectstmt + " order by  "
    selectstmt = selectstmt + "   3 asc "
    #print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()
    varTimeSpike = []
    varTimeSpikeDiff = []
    Neuron =[]
    k = 0
    summ = 0.00

    for row in data:
        varTimeSpike.append(float(row[2]))
        Neuron.append(float(row[2]) * 1000)
        if k == 0:
            varTimeSpikeDiff.append(float("0.00"))
        else:
            if abs((float(varTimeSpike[k]) - float(varTimeSpike[k - 1]))) < 6.00:
                varTimeSpike.append(float(row[2]))
                Neuron.append(float(row[2])* 1000)
        k = k + 1


    curr.close()
    conn.close()

    return Neuron


def getDistinctNueron():
    conn = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
    curr = conn.cursor()

    curr = conn.cursor()
    selectstmt = " SELECT "
    selectstmt = selectstmt + " distinct a.NeuronID as NeuronID "
    selectstmt = selectstmt + " from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP "
    selectstmt = selectstmt + " b, NueroSCi.tblLOCATIONDATAI d "
    selectstmt = selectstmt + " where "
    selectstmt = selectstmt + " a.id = b.id_tblNEURONSPIKE and b.distance < 1    "
    selectstmt = selectstmt + " and b.id_tblLOCATIONDATA = d.id    and    a.TimeSpike >= 5285 and a.TimeSpike<=7353 "
    selectstmt = selectstmt + " order by 1 asc       "
    #print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()

    NeuronIDs = []

    for row in data:
        NeuronIDs.append(row[0])


    curr.close()
    conn.close()

    return NeuronIDs
N=getDistinctNueron()
sizeN = len(N)
positivecorrcoef = []
positivepairnueron = []

negativecorrcoef = []
negativepairnueron = []
zeropairnueron =[]
zerocorrcoef = []
lp=0
ln=0
lz=0
ticksp=[]
ticksn=[]
ticksz=[]
np=0
nn=0
nz=0
DtTAB=5
Dt=(DtTAB/10.0) *  1000 # 0.1 seconds
for k in range(0, sizeN ):
    nuerona=N[k]
    Nueron_A =getSpikeDatPoint(nuerona)
    # get the spike count   for Nueron A based on Dt time bin
    spikecountNoise_A, binsA, patchesA = plt.hist(Nueron_A, bins=int(Dt), histtype='bar', color='blue')
    #plt.savefig(str(cwd) + '/test.png')
    print  " nuerona : " + str(nuerona)

    for j in range(k+1, sizeN ):
        nueronb = N[j]
        Nueron_B = getSpikeDatPoint(nueronb)
        # get the spike count   for Nueron B based on Dt time bin
        spikecountNoise_B, binsB, patchesB = plt.hist(Nueron_B, bins=int(Dt), histtype='bar', color='blue')
        #plt.savefig(str(cwd)+'/test.png')

        ### COmpute the Spearman correlation
        a, b = numpy.corrcoef(spikecountNoise_A, spikecountNoise_B)[0]
        cc = str(nuerona) +'_'+ str(nueronb)
        if b>0.00:
            positivecorrcoef.append(float(b))
            positivepairnueron.append(str(cc))
            ticksp.append(np)
            np=np+1

        if b < 0.00:
            negativecorrcoef.append(float(b))
            negativepairnueron.append(str(cc))
            ticksn.append(nn)
            nn=nn+1

        if b==0.00:
            zerocorrcoef.append(float(b))
            zeropairnueron.append(str(cc))
            ticksn.append(nz)
            nz = nz + 1



dfpositive = DataFrame({'PairNueron':positivepairnueron, 'CorrCoef': positivecorrcoef})
#df=df.sort([ 'CorrCoef'], ascending=[ False])
dfpositive.sort_values('CorrCoef', axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')

dfnegative = DataFrame({'PairNueron':negativepairnueron, 'CorrCoef': negativecorrcoef})
#df=df.sort([ 'CorrCoef'], ascending=[ False])
dfnegative.sort_values('CorrCoef', axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')


dfzero = DataFrame({'PairNueron':zeropairnueron, 'CorrCoef': zerocorrcoef})







print("Positive Pairwise Correlation")
print("**************************************************")
conn = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
curr = conn.cursor()
for row in dfpositive.iterrows():
    index, data = row
    print (data['PairNueron']), (data['CorrCoef'])
    INSERTstmt = "  Insert into PairwiseCorrelation"+str(DtTAB)+"00   VALUES( 'Positive','I', "+str(data['PairNueron']).split("_")[0] +",   "
    INSERTstmt=INSERTstmt +str(data['PairNueron']).split("_")[1]+",  "+ str(data['CorrCoef']) +" ) "
    try:
        curr.execute(INSERTstmt)
        curr.execute("commit")
    except mysql.connector.ProgrammingError:
        print( "The following query failed:")
        print (INSERTstmt)
conn.close()
curr.close()


print("Negative Pairwise Correlation")
print("**************************************************")
conn = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
curr = conn.cursor()
for row in dfnegative.iterrows():
    index, data = row
    #print (data['PairNueron']), (data['CorrCoef'])
    INSERTstmt = "  Insert into PairwiseCorrelation"+str(DtTAB)+"00   VALUES( 'Negative','I', "+str(data['PairNueron']).split("_")[0] +",   "
    INSERTstmt=INSERTstmt +str(data['PairNueron']).split("_")[1]+",  "+ str(data['CorrCoef']) +" ) "
    try:
        curr.execute(INSERTstmt)
        curr.execute("commit")
    except mysql.connector.ProgrammingError:
        print( "The following query failed:")
        print (INSERTstmt)
conn.close()
curr.close()

print("")
print("")
print("")

print("Zero Pairwise Correlation")
print("**************************************************")

conn = mysql.connector.connect(user='root', password='AnuIfe2014$', database='NueroSCi')
curr = conn.cursor()
for row in dfzero.iterrows():
    index, data = row
    #print (data['PairNueron']), (data['CorrCoef'])
    INSERTstmt = "  Insert into PairwiseCorrelation"+str(DtTAB)+"00   VALUES( 'Zero','I', "+str(data['PairNueron']).split("_")[0] +",   "
    INSERTstmt=INSERTstmt +str(data['PairNueron']).split("_")[1]+",  "+ str(data['CorrCoef']) +" ) "
    try:
        curr.execute(INSERTstmt)
        curr.execute("commit")
    except mysql.connector.ProgrammingError:
        print( "The following query failed:")
        print (INSERTstmt)
conn.close()
curr.close()


print("")
print("")
print("")

#sys.stdout = orig_stdout
#f.close()


print (datetime.datetime.now())













