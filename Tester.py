# -*- coding: utf-8 -*
from sys import exit, path
import jsonlines
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

import glob

'''
s = '27.07.2017 07:36'
(day, month, year)=s.split(' ')[0].split('.')
pubDate='%s.%s.%s'%(year, month, day)

print pubDate

'''
#- Duplicates in files -----------------------------------------------------------------

def displayDuplicates (path):
        print "displayDuplicates("+str(path)+") "

        # init variables
        s40='-'*40
        #d=dict()
        files=glob.glob(path)
        print files
        for file in files:
                
                d=dict()
                print file+s40

                with jsonlines.open(file) as reader:
                        for obj in reader:
                                if obj['url'] in d:
                                        print obj['url']
                                else:
                                        d[obj['url']]=1
#displayDuplicates ('Focus/Reports/*.json')
#displayDuplicates ('24chasa/Reports/24chasa-2017-07-*.json')


def reportDuplicates (path):
        # init variables
        #print "reportDuplicates("+str(path)+") "
                                                       
        s80='-'  * 89
        #d=dict()
        files=glob.glob(path)
        #print "%-60s %10s %10s" % ('Files', 'All Recs', 'Dupl Recs')
        for file in files:
               
                d=dict()
                #print file #s80
                countAll =0
                countDuplicates=0
 
                with jsonlines.open(file) as reader:
                        for obj in reader:
                                countAll +=1
                                if obj['url'] in d:
                                        #print obj['url']
                                        countDuplicates +=1
                                else:
                                        d[obj['url']]=1
                        if countDuplicates>0:
                            print "%-60s %10d %10d" % (file, countAll, countDuplicates)
                            print s80
#reportDuplicates ("24chasa/Reports/*.json")
#reportDuplicates ('Blitz/Reports\Blitz*.json')




for ff in ('24chasa','Actualno','BGNes','BgOnAir','Blitz','BNews','Classa','ClubZ','Cross','Dnes',
    'Dnevnik','Duma','Epicenter','Faktor','Focus','Mediapool','Monitor','News',
    'Novinite','OffNews','PIK','SegaBG','Standartnews','Trud',):
    print '-- %s --'% (ff)
    reportDuplicates ( '%s/Reports/*.json' % (ff))
#--------------------------------------------
#reportDuplicates ("Monitor/Reports/*.json")

def scanAllFileReportDate(folderPath):

    files=glob.glob(folderPath)
    print len(files)
    s20='-'*20
    print s20+folderPath+s20

    
    for file in files:
        #print file
        #print scaneFile(file)
        reportDuplicates(file)

    print 'Scaned %s files'%(len(files))



#scanAllFileReportDate('OffNews/Reports/*.json') 
#scanAllFileReportDate(24chasa/Reports/*.json') 
#formatReportsDate('24chasa/Reports/*.json')


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
        
#----------------------------------------------------------------
# modify the file name adding 'out' at the beggining
# makeNewFileName('Trud\Reports\Trud-2017-06-23.json') --> 'Trud\Reports\outTrud-2017-06-23.json'
def makeNewFileName(oldFileName):
    #'Trud\Reports\Trud-2017-06-23.json'
    parts=oldFileName.split('\\')
    length=len(parts)-1
    print parts
    parts[length] = 'out'+parts[length]
    return '\\'.join(parts)

	
#print makeNewFileName('Trud\Reports\Trud-2017-06-23.json')

#  copy jlFile and swap the day and year in the result file
def swapDateParts(jlFile):
    jlFileOutput=makeNewFileName(c)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                date=obj['date']
                obj['date'] = swapDayAndYear(date)
                writer.write(obj)

				
#swapDateParts('Trud\Reports\Trud-2017-06-23.json')

'''
It check date values. 
It returns summary date & date count into file
	'Key: 2017.07.15, count:44
'''
def checkDate(jlFile):
    d=dict()
    
    with jsonlines.open(jlFile) as reader:
        for obj in reader:
            #newDate = obj['date'].split()[0]
            newDate = obj['date'].split(' ')[0]
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
def scanFolder(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
        print(file)
        print checkDate(file) 


#scanFolder('Blitz/Reports/Blitz-2017-*.json')

#scanFolder('24chasa/Reports/24chasa-2017-*.json')


#scanAllFileReportDate('24chasa/Reports/*.json')

#eho2( 'kjhkdaskj')
#scanAndSwapDateParts('24chasa\Reports\*.json')

