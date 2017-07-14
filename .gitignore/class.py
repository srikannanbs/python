# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:14:58 2017

@author: a550859
"""

class PasswordError(Exception):
    def __init__(self,status):
        self.passwordstatus=status
                
    def exceptionMessage(self):    
        return self.passwordstatus