# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:05:23 2017

@author: a550859
"""
import pymysql

db= pymysql.connect(host="localhost", user="root", 
                    passwd="vignesh",
db="nessu")

cursor = db.cursor()
stmt = "SELECT * from employee"
cursor.execute(stmt)
rows = cursor.fetchall ()

for row in rows:
    print ("Row: ")
    for col in row :
        print ("Column: %s" % (col))
    #print ("End of Row")
#print ("Number of rows returned: %d" % cursor.rowcount)

cursor.close()

db.close()
