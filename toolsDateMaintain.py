# -*- coding: utf-8 -*-
import scrapy
import logging
import glob
import json
import os
from sys import exit, path
from datetime import date, timedelta
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
from Dates import *
from Duplicates import *

from urllib2 import quote



def makeNewFileName(oldFileName):
    parts=oldFileName.split('\\')
    pos=len(parts)-2
    parts[pos] = 'Data'
    return '\\'.join(parts)

#s=makeNewFileName('Blitz\\Reports\\Blitz-2017-06-23.json')  
#print s


#Blitz
# it converts
def test():
    sdate=u' 20:53 | 06 юни 2017 | '
    print dcMediapool(sdate)

#test()
    
def convertBlitzDatetoStandart(jlFile):
    jlFileOutput=makeNewFileName(jlFile)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                
                strDate=u''+obj['date']
                (year, month, day)=strDate.split('.')
                print strDate , '>>year:',year
                
                if int( year) <32:
                    
                    obj['date']='%s.%s.%s' % (day, month, year)
                    print strDate,'changes ',obj['date']
                else:
                    print strDate,' keeps ',obj['date']

                writer.write(obj)
                
#convertBlitzDatetoStandart('Blitz\\Reports\\Blitz-2017-06-06.json')

def scanAndConvertBlitzDatetoStandart(folderPath):

    s20='-'*20
    files=glob.glob(folderPath)
    print s20+folderPath+s20
    for file in files:
        convertBlitzDatetoStandart(file)

#scanAndConvertBlitzDatetoStandart('Trud\Reports\Trud*.json')
