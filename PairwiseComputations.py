
import pandas as pdb
import numpy as np
import scipy.io as spio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import cm
import sys
import pylab as p
#import matplotlib.axes3d as p3
import mpl_toolkits.mplot3d.axes3d as p3
import mysql.connector

con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

def getDISTINCTNUERONS(AnimalName,unit, vtype, CC):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()
    selectstmt = ""
    selectstmt = selectstmt + "   SELECT distinct NueronID_A    ";
    selectstmt = selectstmt + "  FROM NueroSCi.PairwiseCorrelation"+str(unit)+"00  where type='"+vtype+"'     ";
    selectstmt = selectstmt + "  and  CorrCoef >= " + str(CC) + "    ";

    selectstmt = selectstmt + "  union   ";

    selectstmt = selectstmt + "  SELECT distinct NueronID_B    ";
    selectstmt = selectstmt + "  FROM NueroSCi.PairwiseCorrelation" + str(unit) + "00  where type='" + vtype + "'     ";
    selectstmt = selectstmt + "  and  CorrCoef >= " + str(CC) + "    ";

    selectstmt = selectstmt + "  order by 1 asc   ";
    #print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()
    varNuerons = []

    kk=0
    for row in data :

        varNuerons.append(str(row[0]))
        kk=kk+1

    curr.close()
    conn.close()


    return varNuerons

def getPaiwireData(unit, vtype, CC):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()
    selectstmt ="SELECT Type, AnimalName, NueronID_A,NueronID_B, CorrCoef FROM NueroSCi.PairwiseCorrelation"+str(unit)+"00  where type='"+vtype+"'  and  CorrCoef >= "+str(CC)+"  order by NueronID_A, NueronID_B  asc "
    #print (selectstmt)
    curr.execute(selectstmt)
    data = curr.fetchall()
    varxpoints = []
    varypoints = []
    varCorrCoer = []
    varColor = []  # red for test =0 and  blue for trainging 1 in the CrossValidation Column
    # print the rows
    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    g = nx.DiGraph()
    nn=getDISTINCTNUERONS('I',unit, vtype, CC)
    g.add_nodes_from(nn)
    for row in data :
        g.add_edge(str(row[2]), str(row[3]))

    #nx.draw(g, with_labels=True)
    kk=len(nn)
    #nx.draw(g, pos=nx.spectral_layout(g))
    eee= kk*(kk-1)/2
    edgess=g.number_of_edges()


    curr.close()
    conn.close()
    return kk,eee,edgess,float(edgess*1.00/eee*1.00),CC,unit*0.1



cur.close ()
# close the connection
con.close ()
#u=1
Type ="Positive"
cc=0.001

arrNeurons =[]
arreee =[]
arredgess = []
arrPercentageEdge = []
arrcc = []
arrbinValue =[]
fig=p.figure()
colors = ['red','sienna','green','blue'
,'fuchsia','darkorange','yellow', 'lime', 'lightcoral','black']
mypacthes = []
for u in range (1 , 11):

    Neurons, eee, edgess, PercentageEdge, cc, binValue =getPaiwireData(u,"Positive",0.001)
    arrNeurons.append(Neurons)
    arreee.append(eee)
    arredgess.append(edgess)
    arrPercentageEdge.append(PercentageEdge)
    arrcc.append(cc)
    arrbinValue.append(binValue)
    Neurons, eee, edgess, PercentageEdge, cc, binValue =getPaiwireData(u,"Positive",0.1)
    arrNeurons.append(Neurons)
    arreee.append(eee)
    arredgess.append(edgess)
    arrPercentageEdge.append(PercentageEdge)
    arrcc.append(cc)
    arrbinValue.append(binValue)

    Neurons, eee, edgess, PercentageEdge, cc, binValue =getPaiwireData(u,"Positive",0.2)
    arrNeurons.append(Neurons)
    arreee.append(eee)
    arredgess.append(edgess)
    arrPercentageEdge.append(PercentageEdge)
    arrcc.append(cc)
    arrbinValue.append(binValue)

    Neurons, eee, edgess, PercentageEdge, cc, binValue =getPaiwireData(u,"Positive",0.3)
    arrNeurons.append(Neurons)
    arreee.append(eee)
    arredgess.append(edgess)
    arrPercentageEdge.append(PercentageEdge)
    arrcc.append(cc)
    arrbinValue.append(binValue)

    Neurons, eee, edgess, PercentageEdge, cc, binValue =getPaiwireData(u,"Positive",0.4)
    arrNeurons.append(Neurons)
    arreee.append(eee)
    arredgess.append(edgess)
    arrPercentageEdge.append(PercentageEdge)
    arrcc.append(cc)
    arrbinValue.append(binValue)
    Neurons, eee, edgess, PercentageEdge, cc, binValue =getPaiwireData(u,"Positive",0.5)
    arrNeurons.append(Neurons)
    arreee.append(eee)
    arredgess.append(edgess)
    arrPercentageEdge.append(PercentageEdge)
    arrcc.append(cc)
    arrbinValue.append(binValue)

    Neurons, eee, edgess, PercentageEdge, cc, binValue =getPaiwireData(u,"Positive",0.6)
    arrNeurons.append(Neurons)
    arreee.append(eee)
    arredgess.append(edgess)
    arrPercentageEdge.append(PercentageEdge)
    arrcc.append(cc)
    arrbinValue.append(binValue)
    Neurons, eee, edgess, PercentageEdge, cc, binValue =getPaiwireData(u,"Positive",0.7)
    arrNeurons.append(Neurons)
    arreee.append(eee)
    arredgess.append(edgess)
    arrPercentageEdge.append(PercentageEdge)
    arrcc.append(cc)
    arrbinValue.append(binValue)

    plt.plot(arrcc, arredgess, colors[u-1])
    #print (arrPercentageEdge)
    #print (arrcc)

    patch = mpatches.Patch(color=colors[u-1], label="Time Bin: "+str(float(u*0.1))[:3] + "s")
    mypacthes.append(patch)


    arrNeurons = []
    arreee = []
    arredgess = []
    arrPercentageEdge = []
    arrcc = []
    arrbinValue = []

plt.legend(handles=mypacthes)
plt.title("Variations of Number of Edges versus Corr. Coef. thresholds ")
plt.xlabel("Corr.Coef")
plt.ylabel("Number of Edges")
#fig.add_axes(ax)
p.show()




