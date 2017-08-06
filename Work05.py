# -*- coding: utf-8 -*-

import jsonlines


def transformDate(monthName):
    monthName=monthName.lower()
    months= {u'january':'01',u'february':'02', u'march':'03',
             u'april':'04',u'may':'05', u'june':'06',
             u'july':'07',u'august':'08', u'september':'09',
             u'october':'10',u'november':'11', u'december':'12'}

    if (monthName in months):
        return months[monthName]
    else:
        return'??'


dateParts='14-july-2017'.split('-')
date='%s.%s.%s'%(dateParts[2],transformDate(dateParts[1]),dateParts[0])

#print date
#-----------------------------------------------------
def makeNewFileName(oldFileName):
    #print oldFileName
    parts=oldFileName.split('\\')
    #print parts
    parts[2] = 'Ready\\'+parts[2]
    return '\\'.join(parts)

def scaneFile(jlFile):
    
    jlFileOutput=makeNewFileName(jlFile)
    print jlFileOutput
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                tmp=obj["date"]
                dateParts=tmp.split('-')
                obj["date"]='%s.%s.%s'%(dateParts[2],transformDate(dateParts[1]),dateParts[0])
                writer.write(obj)

import glob

def formatReportsDate(folderPath):

    files=glob.glob(folderPath)

    s20='-'*20
    print s20+folderPath+s20

    for file in files:
        #print '>>>', makeNewFileName(file)
        #print jsonFileType(file), file
        print scaneFile(file)

#formatReportsDate('Dnevnik\\Reports\\*.json')
        
'''
# -*- coding: utf-8 -*-
import scrapy
import logging
import json
'''
from sys import exit, path
import platform
if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from HelperTools import *
from datetime import date, timedelta

'Get the Today adn Yesterday dates'
Today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

# File to check
json_datafile = 'Dnevnik/Reports/Dnevnik-'+Yesterday+'.json'
print 'Check for %s' %(json_datafile)
#check_empty(json_datafile)


#checkReport('Dnevnik/Reports/Dnevnik-2017-07-18.json')
print jsonFileType('PIK\Reports\PIK-2017-06-05.json')

s="06 Юни 2017, 09:19"
(day, month, year)=s.split(',')[0].split()
print bgMonthstoNumber(unicode(month,'utf-8')


"aaaa"



        
