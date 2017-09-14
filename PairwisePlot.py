
import pandas as pdb
import numpy as np
import scipy.io as spio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
import pylab as p
#import matplotlib.axes3d as p3
import mpl_toolkits.mplot3d.axes3d as p3
import mysql.connector

con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

def getDISTINCTNUERONS(AnimalName):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()
    selectstmt = ""
    selectstmt = selectstmt + "  select distinct (a.NeuronID)  "
    selectstmt = selectstmt + "  from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d   "
    selectstmt = selectstmt + "  where a.id = b.id_tblNEURONSPIKE  "
    selectstmt = selectstmt + "  and b.distance < 1 "
    selectstmt = selectstmt + "  and b.id_tblLOCATIONDATA=d.id  "
    selectstmt = selectstmt + "  and a.AnimalName='"+AnimalName+"'  "
    selectstmt = selectstmt + "  order by 1 asc   "
    #print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()
    varNuerons = []


    for row in data :

        varNuerons.append(str(row[0]))

    curr.close()
    conn.close()


    return varNuerons

def getPaiwireData(unit, vtype, CC):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()
    selectstmt ="SELECT Type, AnimalName, NueronID_A,NueronID_B, CorrCoef FROM NueroSCi.PairwiseCorrelation"+str(unit)+"00  where type='"+vtype+"'  and  CorrCoef >= "+str(CC)+"  order by NueronID_A, NueronID_B  asc "
    print (selectstmt)
    curr.execute(selectstmt)
    data = curr.fetchall()
    varxpoints = []
    varypoints = []
    varCorrCoer = []
    varColor = []  # red for test =0 and  blue for trainging 1 in the CrossValidation Column
    # print the rows
    import networkx as nx
    import matplotlib.pyplot as plt
    g = nx.DiGraph()
    g.add_nodes_from(getDISTINCTNUERONS('I'))
    for row in data :
        g.add_edge(str(row[2]), str(row[3]))

    nx.draw(g, with_labels=True)
    plt.draw()

    plt.suptitle("Neurons Associativity Of Animal (Ibsen) with "+vtype+" Pairwise Correlation Coefficient of "+str(CC)+" at 0.1s  ")
    plt.show()

    curr.close()
    conn.close()






cur.close ()
# close the connection
con.close ()


getPaiwireData(1,"Positive",0.01)

getPaiwireData(1,"Positive",0.10)

getPaiwireData(1,"Positive",0.20)

getPaiwireData(1,"Positive",0.30)

getPaiwireData(1,"Positive",0.40)



getPaiwireData(3,"Positive",0.50)