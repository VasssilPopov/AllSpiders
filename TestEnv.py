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


'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%Y.%m.%d").lower()


# modify the file name replacing 'Reports' 'out' at the beggining
    #'Trud\Reports\Trud-2017-06-23.json'

def makeNewFileName(oldFileName):
    parts=oldFileName.split('\\')
    pos=len(parts)-2
    parts[pos] = 'Data'
    return '\\'.join(parts)

#s=makeNewFileName('Blitz\\Reports\\Blitz-2017-06-23.json')  
#print s


#Blitz
# it coverts
'''
def convertBlitzDatetoStandart(jlFile):
    jlFileOutput=makeNewFileName(jlFile)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                
                date=u''+obj['date']
                obj['date'] = dcBlitz(date)
                
                writer.write(obj)
                
#convertBlitzDatetoStandart('Blitz\\Reports\\Blitz-2017-06-06.json')

def scanAndConvertBlitzDatetoStandart(folderPath):

    s20='-'*20
    files=glob.glob(folderPath)
    print s20+folderPath+s20
    for file in files:
        convertBlitzDatetoStandart(file)


'''






'''
It check date values. 
It returns summary date & date count into file
	'Key: 2017.07.15, count:44
'''
def checkDate(jlFile):
    d=dict()
    
    with jsonlines.open(jlFile) as reader:
        for obj in reader:
            newDate = obj['date']
            if (newDate in d.keys()):
                d[newDate] +=1
            else:
                d[newDate] =1

    #print len(d.keys())
    for (k,v) in d.items():
        if (k,v) != None:
            print('Key: %s, count:%d'%(k,v))
    

#checkDate('Blitz\Reports\Blitz-2017-06-06.json')

# scan files in directory and call checkDate for each one
def scanFolderCheckDate(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
        print('-'*20+file+'-'*20)
        print checkDate(file) 

#Check all *.jon files in folder reports date formats by files
#scanFolderCheckDate('24chasa/Reports/24chasa-2017-*.json')

        

        
spath='Focus\\Reports\\Focus-*.json'
spathD='Focus\\Data\\Focus-*.json'

#scanAndConvertBlitzDatetoStandart('PIK\Reports\PIK*.json')

#convertBlitzDatetoStandart('Mediapool\\Reports\\Mediapool-2017-05-21.json')


#scanFolderCheckDate(spathD)
#reportDuplicates (spathD)
scanReports(spathD)

#scanAndConvertBlitzDatetoStandart(spath)

#removeDuplicates('Focus\\Reports\\Focus-2017-08-03.json')
#scanFolderAndRemoveDuplicates(spath)        
