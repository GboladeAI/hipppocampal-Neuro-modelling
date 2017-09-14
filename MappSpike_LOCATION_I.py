
import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt
import mysql.connector


import threading
con=mysql.connector.connect(user='root', password ='AnuIfe2014$', database='NueroSCi')
cur=con.cursor()
id=1



def worker(valueOfAnimal):
    print 'BtchSQL: %s' % valueOfAnimal
    print "\n"


    #btchSQL = ("CALL getLOCATION('" + valueOfAnimal + "')")
    btchSQL = ("CALL getLOCATION_I()")

    print btchSQL
    print "\n"
    try:
        cur.execute(btchSQL)

        print '*****Ending*****'

    except mysql.connector.ProgrammingError:
        print "The following query failed:"

    return

animal = ["G","H","F","I", "J"]

worker("I")








