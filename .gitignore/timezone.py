# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:14:35 2017

@author: a550859
"""

from datetime import datetime
from pytz import timezone
from pytz import all_timezones

date_str = datetime.today()
datetime_obj_utc = date_str.replace(tzinfo=timezone('UTC'))
print (datetime_obj_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
datetime_obj_utc = date_str.replace(tzinfo=timezone('US/Pacific'))
print (datetime_obj_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

for zone in all_timezones:
    if 'US' in zone:
        print (zone)
        
from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
timezonelist = ['UTC','US/Pacific','Europe/Berlin']
for zone in timezonelist:
    now_time = datetime.now(timezone(zone))
    print (now_time.strftime(fmt))