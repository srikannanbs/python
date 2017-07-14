# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:01:30 2017

@author: a550859
"""

import os
import glob
os.chdir('C:/Users/a550859/Desktop/py training')
print(os.getcwd())
if (os.path.exists('C:/Users/a550859/Desktop/py training/Sampledata')):
    print("path exists")
else:
     os.mkdir("Sampledata")
os.chdir('C:/Users/a550859/Desktop/py training/Sampledata')
print(os.getcwd())
filename=input('enter file')
pathname=os.getcwd()
filepath=pathname+'\\'+filename
if (os.path.exists(filepath)):
#file=open(pathname+"systemlogger.log",mode='w')
   print("file exists")
else:
     #print("file not exists")
     open('filename',mode='w')
     
   #print(glob.glob('*.*'))
