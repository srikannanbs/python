# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:50:47 2017

@author: a550859
"""

from xml.dom import minidom
doc=minidom.parse("Country.xml")
table=doc.getElementsByTagName("Table")
for nodedata in table:
    data= nodedata.getElementsByTagName("Country")
    for c1 in data:
        print(c1.firstChild.data)
    
    data=nodedata.getElementsByTagName("City")
    for c2 in data:
        print(c2.firstChild.data)
        
import xml.etree.ElementTree as ET
tree=ET.parse('Country.xml')
root=tree.getroot()
for child in root:
    print(child.tag,child.attrib)
    
    