# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:15:00 2017

@author: a550859
"""
'''
try:
    basicsalary=input('Enter')
    da=input('enter DA')
    Gross=int(basicsalary)+int(da)
    print("Gross","\t",Gross)
except ValueError:
    print('data type incorrect')
    '''
#From modul import PasswordError
import sys

status=None

try:
    
   pwd=input('ENter pwd')
   if (len(pwd)>=4) and (len(pwd)<=8):
        print('Accepted')
   else:
        raise PasswordError('Length not sufficient')
        
except Exception as e:
    print (e)
finally:
    print("all connections closed")
    
        
        