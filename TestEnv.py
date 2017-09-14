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
def scanFolderCheckDate1(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
        print('-'*20+file+'-'*20)
        print checkDate(file) 

#Check all *.jon files in folder reports date formats by files
#scanFolderCheckDate('24chasa/Reports/24chasa-2017-*.json')


def scanFolderCheckCounter(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
        print('-'*20+file+'-'*20)
        print checkDate(file) 




        

#spathD='PIK\\Data\\PIK-*.json'

#scanAndConvertBlitzDatetoStandart('PIK\Reports\PIK*.json')

#convertBlitzDatetoStandart('Mediapool\\Reports\\Mediapool-2017-05-21.json')
s='Mediapool'        
spath='%s\\Reports\\%s-*.json' % (s, s)
spathD='%s\\Data\\%s-*.json' % (s, s)

# date format
#scanFolderCheckDate(spathD)
# data duplicates
#reportDuplicates (spathD)
#scanReports(spathD)

#checkReport('C:\STUDY_SPIDERS\LAB\json_Lab\PIK-2017-06-07.json')


#scanAndConvertBlitzDatetoStandart(spath)

#removeDuplicates('Focus\\Reports\\Focus-2017-08-03.json')
#removeDuplicates('24chasa\\Reports\\24chasa-2017-09-01.json')
#removeDuplicates('24chasa\\Reports\\24chasa-2017-09-04.json')
#scanFolderAndRemoveDuplicates(spath)        


#----------------------------------------------------------------------
#Blitz
# it converts

def convertBlitzDatetoStandart(jlFile):
    jlFileOutput=makeNewFileName(jlFile)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:

                    key=obj['date']
                    if ' | ' in key:
                            print key
                            if key.startswith(' | '):
                                    print jlFile
                                    key = key[3:]
                                    print key
                            obj['date']=dcMediapool(key)
                    writer.write(obj)
                   
'''
                date=u''+obj['date']
                (year, month, day)=date.split('.')
                if year <'50':
                        obj['date']='%s.%s.%s' % (day, month, year)
                        print date, obj['date']
'''

                
#convertBlitzDatetoStandart('Blitz\\Reports\\Blitz-2017-06-06.json')

def scanAndConvertBlitzDatetoStandart(folderPath):

    s20='-'*20
    files=glob.glob(folderPath)
    print s20+folderPath+s20
    for file in files:
        convertBlitzDatetoStandart(file)

#scanAndConvertBlitzDatetoStandart('Mediapool\\Reports\\Mediapool*.json')

#----------------------------------------------------------------------

def fileStatus(fileName):
        f = open(fileName)
        allText=f.read()
 
        print allText
        f.close()

#fileStatus("Blitz/Logs/validateBlitz.txt")
#reportDuplicates ('PIK/Reports\PIK-2017-07-*.json')

#checkReport('Dnevnik/Reports/Dnevnik-2017-07-17.json')
json_datafile='Dnevnik/Reports/Dnevnik-2017-07-18.json'
'''
print 'VALIDATIONS for [%s]'%(json_datafile)
print
if os.path.isfile(json_datafile):
	#check for duplicates ---------------------------------------------
	reportDuplicates (json_datafile)

	#checkReport('Dnevnik/Reports/Dnevnik-2017-07-18.json')------------
	checkReport(json_datafile)
'''

def checkSubstring(fName, strText):
        file = open(fName,'r')
        s=file.read()

        return s.count('"text": ""')


def scanPath(folderPath):
        
        s20='-'*20
        count=0
        files=glob.glob(folderPath)
        print s20+folderPath+s20
        for file in files:
                n=checkSubstring(file, '"text": ""')
                print file, n
                count +=n

        print count

scanPath('PIK\\Reports\\PIK*.json')
#'Test\Reports\PIK-2017-08-10.json'


def CreateJson():
        folderPath='PIK\Reports\PIK-*.json'
        with jsonlines.open('Test\Reports\PIK-AllMissing.json', mode='w') as writer:

                files=glob.glob(folderPath)
                for file in files:
                        print file
                        with jsonlines.open(file) as reader:
                                for obj in reader:
                                        if obj['text'] == '':
                                                row={'url':obj['url'],'text': ''}
                                                print 'write row'
                                                writer.write(row)
                                reader.close()
                writer.close()

def getKey(url):
        return url[-10:][0:6]

import jsonlines
'''
d=dict()
count=0

file='Test\Reports\PIK-AllMissing_1.json'
with jsonlines.open(file) as reader:
       for obj in reader:
                key=getKey(ob['url'])
                if key in d:
                        count +=1
                else:
                        d[key]=obj

print count
'''
# scan files in directory and call checkDate for each one
def scanFolderFiles(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)
    print s20+folderPath+s20
    for file in files:
        print(file)


scanFolderFiles('Focus/Reports\Focus-2017-06-*.json')


#-- MonthlyReports --------------------------------------------------

from ScrapingHelpers import *
from Dates import *
import HelperTools

repYear='2017'
repMonth=9

# single month report
monthlyDataReport(repYear, repMonth)
