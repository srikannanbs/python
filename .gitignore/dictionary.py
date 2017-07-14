# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:06:35 2017

@author: a550859
"""
'''
http://jsonplaceholder.typicode.com/users
http://jsonplaceholder.typicode.com/posts
http://jsonplaceholder.typicode.com/album
http://jsonplaceholder.typicode.com/comments
'''
from datetime import date
#keypair value
customerDB={
            437956:{'Name':'Anoop','DOB':date(1995,5,5),'Address':'Chn'},
             32845:{'Name':'shyam','DOB':date(1995,5,5),'Address':'Chn'},
             43567:{'Name':'Anbu','DOB':date(1995,5,5),'Address':'Chn'},
}

print(customerDB.keys())
print(customerDB.items())
print(customerDB.values())
print('Key',"\t",'values')
for (k,v) in customerDB.items():
    print(k,"\n")
    for(prop,value) in v.items():
        print(prop,"\t",value)
        
print("Seraching....")
searchkey=raw_input('Enter the key')
print(customerDB.get(int(searchkey)))

#pip install--proxy=proxy-chn.fmr.com:8080 requests