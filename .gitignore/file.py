# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:15:57 2017

@author: a550859
"""

#array->object->Keypair

import sys
sys.path.append('C:/Users/a55085/Downloads/python')
import json

with open('users.json') as json_data_file:
    response=json.load(json_data_file)
    #print(response)
arraykeys=('id','username','email')
for i in response:
    #print(i)
    for(value) in arraykeys:
        
        print(value,"\t",i[value])
        info=[value]
        searchkey=raw_input('Enter the key')
         print([value].get(int(searchkey)))
        