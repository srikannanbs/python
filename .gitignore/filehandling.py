# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:09:56 2017

@author: a550859
"""

import os
import glob
import os.path
print(os.getcwd())
#os.chdir(C:/Users)
pathname='C:/Users/a550859/Downloads'
print(os.path.split(pathname))
filename='text.py'
(filename,extension)=os.path.splitext(filename)
print(extension)

os.chdir('C:/Users/a550859/Downloads')
filelist(glob.glob('*.*')
for _ in filelist:
    print(_,"\n")
    
#print(os.listdir('.')
    
for dirpath,dirnames,filenames in os.walk("C:/Users/a550859/Downloads"):
    print(dirpath)
    os.chdir(dirpath)
    filearray=(glob.glob('*.*'))
    for _ in filearray:
        if(os.stat(_).st_size>10000):
          print(_,"===>",os.stat(_).st_size)
    #print(dirnames)
    #print(filenames)
    
    