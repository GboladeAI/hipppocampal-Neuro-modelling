
import pandas as pdb
import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
import pylab as p
#import matplotlib.axes3d as p3
import mpl_toolkits.mplot3d.axes3d as p3
import mysql.connector

con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()

cur.execute("SELECT d.id,d.AnimalName,d.time_at_location,d.x_axis,d.y_axis, d.mesh , a.CrossValidation from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d where a.id = b.id_tblNEURONSPIKE and b.distance < 1 and b.id_tblLOCATIONDATA=d.id  and  d.x_axis!=0.00 and d.y_axis !=0.00    and a.TimeSpike >= 5285 and a.TimeSpike<=7353       ")
# fetch all of the rows from the query
data = cur.fetchall ()
xpoints = []
ypoints = []
varColor = []
MyData = []
MyTime = []
# print the rows
for row in data :
    xpoints.append( float(row[3]))
    ypoints.append( float(row[4]))
    MyTime.append(float(row[2]))

    if row[6] == 0:
        varColor.append('blue')
        MyData.append(int('1'))
    if row[6] == 1:
        varColor.append('blue')
        MyData.append(int('0'))
nX=20.00
nY=20.00
gapX=1.00
gapY=1.00
# the gap is added to maxpoint
X=float(max(xpoints))
Y=float(max(ypoints))
maxValue_Xaxis=float(X)  + gapX
maxValue_Yaxis=float(Y ) + gapY

plt.axis('off')
plt.scatter(xpoints,ypoints,color=varColor, s=.8)
plt.suptitle("Location of Rat (Ibsen) full maze of ("+str(X)+" X " +str(Y)+ ")")
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.axis('off')
ax.scatter(xpoints,ypoints,MyData, s=.8)
#ax.title("Location of Rat (Ibsen) full maze of ("+str(X)+" X " +str(Y)+ ")")
p.show()


cur.execute("SELECT distinct d.id,d.AnimalName,d.time_at_location,d.x_axis,d.y_axis, d.mesh , a.CrossValidation from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d where a.id = b.id_tblNEURONSPIKE  and b.distance < 1 and b.id_tblLOCATIONDATA=d.id  and  d.x_axis!=0.00 and d.y_axis !=0.00    and a.TimeSpike >= 5285 and a.TimeSpike<=7353       ")
# fetch all of the rows from the query
data = cur.fetchall ()
xpoints = []
ypoints = []
varColor = []
MyData = []
MyTime = []
# print the rows
for row in data :
    xpoints.append(float(row[3]))
    ypoints.append(float(row[4]))
    MyTime.append(float(row[2]))
    varColor.append('b')

fig=p.figure()
ax = p3.Axes3D(fig)
# plot3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array
ax.scatter3D(xpoints,ypoints,MyTime,color='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time @ location (s)')
ax.set_title("")
fig.add_axes(ax)
p.suptitle("Location of the animal in 3D")
p.show()


cur.execute("SELECT distinct d.id,d.AnimalName,d.time_at_location,d.x_axis,d.y_axis, d.mesh , a.CrossValidation from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d where a.id = b.id_tblNEURONSPIKE and  a.CrossValidation=0 and b.distance < 1 and b.id_tblLOCATIONDATA=d.id  and  d.x_axis!=0.00 and d.y_axis !=0.00    and a.TimeSpike >= 5285 and a.TimeSpike<=7353   AND a.CrossValidation=0       ")
# fetch all of the rows from the query
data = cur.fetchall ()
xpoints = []
ypoints = []
varColor = []
MyData = []
MyTime = []
# print the rows
for row in data :
    xpoints.append( float(row[3]))
    ypoints.append( float(row[4]))
    MyTime.append(float(row[2]))
    varColor.append('r')

fig=p.figure()
ax = p3.Axes3D(fig)
# plot3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array
ax.scatter3D(xpoints,ypoints,MyTime,color ='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time @ location (s)')
ax.set_title("TEST DATA SET")
fig.add_axes(ax)
p.show()




meshlengthX = float(maxValue_Xaxis) / nX
meshlengthY = float(maxValue_Yaxis) / nY

minValue_Xaxis=-1.00
minValue_Yaxis=-1.00
meshCounter=1

xy = int(nY)+int(nX)

for i in range(0, int(nY)):
    for j in range(0, int(nX)):
        # update NueroSCi.tblLOCATIONDATAI sets mesh= '%s'  wher x_axis >=minValue_Xaxis  and x_axis < minValue_Xaxis + meshlengthX
        xx=minValue_Xaxis + meshlengthX
        yy=maxValue_Yaxis - meshlengthY

        if yy < 0.0001 : yy=0.00
        if xx < 0.0001: xx = 0.00
        updatestmt = (
        "update NueroSCi.tblLOCATIONDATAI set mesh = %s  where (x_axis >= %s  and x_axis < %s ) and (y_axis < %s  and y_axis >= %s )"
        % (
            meshCounter,minValue_Xaxis,xx,maxValue_Yaxis,yy )
        )

        minValue_Xaxis=minValue_Xaxis + meshlengthX

        meshCounter=meshCounter+1

        #update to divide the maze into meshes

        try:
            print updatestmt
            cur.execute(updatestmt)
            cur.execute("commit")

        except mysql.connector.ProgrammingError:
            print "The following query failed:"
            print updatestmt

    #reset Minimum value of x axiss to begin at the level of y axis
    minValue_Xaxis = 0.00
    maxValue_Yaxis = float(maxValue_Yaxis) - float(meshlengthY)
#sys.exit(-1)

def getMesh(meshID):
    conn=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
    curr=conn.cursor()
    selectstmt =(("SELECT d.id,d.AnimalName,d.time_at_location,d.x_axis,d.y_axis, d.mesh , a.CrossValidation from NueroSCi.tblNeuronspikeI a, NueroSci.tblMAP b,NueroSCi.tblLOCATIONDATAI d where a.id = b.id_tblNEURONSPIKE and b.distance < 1 and b.id_tblLOCATIONDATA=d.id  and a.TimeSpike >= 5285 and a.TimeSpike<=7353    and d.mesh = '%s'  ") % (meshID))
    print selectstmt
    curr.execute(selectstmt)
    data = curr.fetchall()
    varxpoints = []
    varypoints = []
    varmesh_in_grid = []
    varColor = []  # red for test =0 and  blue for trainging 1 in the CrossValidation Column
    # print the rows
    for row in data :
        varxpoints.append( row[3])
        varypoints.append( row[4])
        varmesh_in_grid.append(row[5])
        if row[6]==0 :
            varColor.append('red')
        if row[6]==1 :
            varColor.append('green')


    curr.close()
    conn.close()


    return varxpoints, varypoints,meshID,varColor


# Compute Rows required
Tot = nX * nY
Rows = Tot // nY
Rows += Tot % nY

# Create a Position index

Position = range(1,int(Tot + 1))

# Create main figure

fig = plt.figure(1)
for k in range(int(Tot)):
  # add every single subplot to the figure with a for loop
  varxpoints, varypoints, meshID, varColor = getMesh(k)
  ax = fig.add_subplot(Rows,nY,Position[k])
  countx=len(varxpoints)
  # add every single subplot to the figure with a for loop
  varxpoints, varypoints, meshID, varColor = getMesh(k)
  ax = fig.add_subplot(Rows, nY, Position[k])
  ax.set_axis_bgcolor('white')

  #ax.axis('Off')
  if countx == 0:
      #plt.rcParams['axes.facecolor'] = 'gray'
      ax.set_axis_bgcolor('white')
      #ax.scatter(varxpoints, varypoints, color=varColor, s=.5)  # Or whatever you want in the subplot
      ax.set_title(str(int(k + 1)), fontsize=5)
      #ax.set_yticklabels([])
      #ax.set_xticklabels([])

      #ax.axis('on')
  else:
      #plt.rcParams['axes.facecolor'] = 'white'
      ax.set_axis_bgcolor('white')
      #ax.scatter(varxpoints, varypoints, color=varColor, s=.5)  # Or whatever you want in the subplot
      ax.set_title(str(int(k + 1)), fontsize=5)
      #ax.set_yticklabels([])
      #ax.set_xticklabels([])
      #ax.axis('off')


plt.suptitle("Location of Rat (Ibsen) divided into smaller meshes  of ("+str(float(X/nX))+" X " +str(float(Y/nY))+ "       )")
plt.grid(True)
plt.show()





cur.close ()
# close the connection
con.close ()
# exit the program
#sys.exit()