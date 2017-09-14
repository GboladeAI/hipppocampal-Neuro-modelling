
import numpy as np
import scipy.io as spio
import matplotlib.pyplot
import matplotlib.pyplot as plt
import mysql.connector
con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()
i=1
matfile = '/Users/akingboladeshada/Desktop/Project_MSc/ProjectDATA_New/Tmaze_location_data (1).mat'
matdata = spio.loadmat(matfile)
#create connection to the database

x =[]
y=[]
kolor = ['red','blue','green','yellow','black']
ii=0
for ratLocationData in matdata.keys():
    if ratLocationData.find('positiondata') != -1:

        locationdata = matdata[ratLocationData]
        ratLocationData = ratLocationData.replace("positiondata", "")
        n = len(locationdata)
        print n
        for j in range(n):
            #print ratLocationData,locationdata[j][0],locationdata[j][1],locationdata[j][2]
            animalname = ratLocationData
            timeatspike=locationdata[j][0] * 10**-6   # this convert
            xaxis = locationdata[j][1]
            yaxis = locationdata[j][2]

            insertstmt = (
                "INSERT INTO NueroSCi.tblLOCATIONDATA(id,AnimalName, time_at_location, x_axis, y_axis) VALUES('%s','%s', '%s', '%s', '%s')" % (
                    i,animalname, timeatspike, xaxis, yaxis))

            try:
                cur.execute(insertstmt)
                print i
                i=i+1

            except mysql.connector.ProgrammingError:
                print "The following query failed:"
                print insertstmt
        con.commit()
con.close()
