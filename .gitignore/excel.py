# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:31:28 2017

@author: a550859
"""

from openpyxl import load_workbook
wb=load_workbook('C:/Users/a550859/Desktop/py training/Sampledata/export.xlsx')
print(type(wb))
print(wb.get_sheet_names())

#sheet=wb.get_sheet_by_name('CDP Data Report')
