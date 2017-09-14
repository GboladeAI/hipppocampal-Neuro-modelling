
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
    selectstmt ="SELECT Type, AnimalName, NueronID_A,NueronID_B, CorrCoef FROM NueroSCi.PairwiseCorrelation"+str(unit)+"00  " \
                                                             "where type='"+vtype+"'  " \
                                                            "and  CorrCoef >= "+str(CC)+"  order by NueronID_A, NueronID_B  asc "
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

    nx.draw(g, with_labels=True)
    kk=len(nn)
    #nx.draw(g, pos=nx.spectral_layout(g))
    eee= kk*(kk-1)/2
    edgess=g.number_of_edges()




    plt.draw()

    #plt.suptitle("Neurons Associativity: "+vtype+" Pairwise Corr. Coef. of "+str(CC)+", bin:"+str(float(unit*1.00/10.0))+"s  Expected Edges:"+ str(int(eee))  +"  Edges:"+ str(edgess) )
    plt.suptitle(str(kk)+" Neurons  Associativity: +ve Pairwise Corr. Coef. >= " + str(CC) + ", bin:" + str(
        float(unit * 1.00 / 10.0)) + "s  Total Edges:" + str(int(eee)) + " Number of +ve Edges:" + str(edgess))

    red_patch = mpatches.Patch(color='r', label='Nueron  (node)')
    black_patch = mpatches.Patch(color='k', label='Edges')
    plt.legend(handles=[red_patch, black_patch])

    plt.show()

    curr.close()
    conn.close()






cur.close ()
# close the connection
con.close ()
u=4
Type ="Positive"
cc=0

getPaiwireData(u,"Positive",0.001)

getPaiwireData(u,"Positive",0.10)

getPaiwireData(u,"Positive",0.20)

getPaiwireData(u,"Positive",0.30)

getPaiwireData(u,"Positive",0.40)



getPaiwireData(u,"Positive",0.50)

getPaiwireData(u,"Positive",0.60)
getPaiwireData(u,"Positive",0.70)

