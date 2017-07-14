# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:27:50 2017

@author: a550859
"""

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
   file=open(filename,mode='a')
else:
     print("file not exists")
     file=open(filename,mode='w')
     print(glob.glob('*.*'))

#file.write("Information passed to file...")

for dirpath,dirnames,filenames in os.walk("C:/Users/a550859/Desktop/4G"):
    print(dirpath)
    os.chdir(dirpath)
    filearray=(glob.glob('*.*'))
    for fileref in filearray:
        if(os.stat(fileref).st_size>10000):
          file.write(fileref)     
          file.write("\t")
          file.write("==>")
          file.write("\t")
          file.write(str(os.stat(fileref).st_size))
          file.write("\n")
          
file.close()