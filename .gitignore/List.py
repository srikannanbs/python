# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:10:15 2017

@author: a550859
"""
'''
data=[4389,67.78,'training',True]
for ele in data:
    print (ele,"\n")
 '''   
list1=[]
list2=[]
import random
for i in range(10):
    list1.append(random.randint(1,100))
    list2.append(random.randint(1,100))
list1=list1.sort(key=None,reverse=True)
print(list1)
list2=list2.sort(key=None,reverse=False)   
print(list2)
list3=[list1,list2]
print(list3)

names=['H','T','I','F']
names.sort(key=None)
print(names)
print(names[1:4:2])
print(list(range(6,-2)))

list1=[4,5,6,7,10,12]
list2=[7,8,89,76,61]
list3=[]
for(x,y) in zip(list1,list2):
    list3.append(x+y)
    
print(list3)
len1=len(list1)
len2=len(list2)
print(len1)
if(len1 > len2):
    print(list1[len2:])
    
    
#tuples
    
tupledata=(3579,'35679',True) #cannot append  cannot inset,modify in tuple
print(tupledata)
    
nestedtuple=(list1,list2)
print(nestedtuple)

for lt in nestedtuple:
  for data in lt:
      print(data)


data=tuple(range(1,20))
print(data)
result=tuple(map(lambda y:hex(y),data))
print(result)

