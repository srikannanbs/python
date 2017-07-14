# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:46:10 2017

@author: a550859
"""

import sys
sys.path.append('C:/Users/a55085/Downloads/python')
import requests
response=requests.get("http://jsonplaceholder.typicode.com/users",proxies=
{'http':'proxy-chn.fmr.com:8000'})
if response.status_code==200:
    print("sucess")
    for _ in response.json():
        print(_["id"],"\t",_["username"],"\t",_["address"]["city"])
else:
    print("error")




