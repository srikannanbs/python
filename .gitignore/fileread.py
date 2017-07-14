# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:15:12 2017

@author: a550859
"""

import os

pathname='C:/Users/a550859/Desktop/py training/Sampledata'
os.chdir(pathname)
file=open('output.csv',mode='r')
for row in file:
    print(row)
    colarray=row.split(',')
    for col in colarray:
        print(col)
    
    