#!/usr/bin/python

import jsonlines
import datetime
import time
from datetime import date, datetime

#C:\STUDY_SPIDERS\LAB\JsonPYs
'''
file='SegaBG-2017-07-29.json'
d = dict()
with jsonlines.open(file) as reader:
    for obj in reader:
        date=obj['date']
        if date in d:
            d[date]+=1
        else:
            d[date]=1
print d
for k,v in d.items():
    print 'Key: %s --> %s' %(k, v)

#(12528, '2017.07.28')
'''
from datetime import datetime
'''
start_date = datetime.strptime('19/07/2017', "%d/%m/%Y")
end_date = datetime.strptime('28/07/2017', "%d/%m/%Y")
dif = (end_date-start_date).days
print end_date,dif+12519

def getMagicNumber(enter_date):
    start_date = datetime.strptime('19/07/2017', "%d/%m/%Y")
    theBase=12519
    end_date = datetime.strptime(enter_date, "%d/%m/%Y")
    return (end_date-start_date).days+theBase    





enter_date=raw_input("Please enter an input dd/mm/yyyy: ")
start_date = datetime.strptime('19/07/2017', "%d/%m/%Y")
end_date = datetime.strptime(enter_date, "%d/%m/%Y")

print (end_date-start_date).days+12519

print getMagicNumber('29/07/2017')

import datetime
datetime.datetime.now().strftime ("%Y%m%d")
'''
def getMagicNumber(enter_date):
    start_date = datetime.strptime('28/07/2017', "%d/%m/%Y")
    theBase=12528
    end_date = datetime.strptime(enter_date, "%d/%m/%Y")
    return (end_date-start_date).days+theBase
'''
enter_date=raw_input("Please enter an input dd/mm/yyyy: ")
print getMagicNumber(enter_date)
'''
print datetime.now().strftime ("%d/%m/%Y")
magicNumber= getMagicNumber(datetime.now().strftime ("%d/%m/%Y"))
print magicNumber
