# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:50:11 2017

@author: a550859
"""

import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
#Next log in to server
server.login("srikannan.bs@gmail.com","pwd")
#send mail
msg='Hello'
server.sendmail("srikannan.bs@gmail.com","srikannan.bs@gmail.com",msg)





#https://wwww.google.com/settings/security/lesssecureapps