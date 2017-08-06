# -*- coding: utf-8 -*-
import jsonlines
def makeNewFileName(oldFileName):
    #'Trud\Reports\Trud-2017-06-23.json'
    parts=oldFileName.split('\\')
    length=len(parts)-1
    print parts
    parts[length] = 'out'+parts[length]
    return '\\'.join(parts)


def scaneFile(jlFile):
    
    jlFileOutput=makeNewFileName(jlFile)
    print jlFileOutput
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
			
                (day, month, year)=obj["date"].split()[0].split('.')
                obj["date"]='%s.%s.%s'%(year, month, day)

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

#formatReportsDate('24chasa\\Reports\\*.json')



def getDate(date):
    return date.replace('-','.')
    #(day, month, year)=date.split()[0].split('.')
    #return('%s.%s.%s')%(year, month, day)


def displayReportsDates( folderPath):
    files=glob.glob(folderPath)
    s20='-'*20
    print s20+folderPath+s20

    for file in files:
        date=file[-15:][0:10].replace('-','.')
        with jsonlines.open(file) as reader:
            for row in reader:
                stdDate=getDate(row['date'])
                if  date != stdDate:
                    print file, date, stdDate, date == stdDate


    





#displayReportsDates('PIK\\Reports\\out*.json')
#----------------------------------------------------------------------------
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
            newDate = obj['date'].split(',')[0]
            if (newDate in d.keys()):
                d[newDate] +=1
            else:
                d[newDate] =1

    print jlFile
    if len(d.items())>1:
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
        print checkDate(file)
 
scanFolder('Trud\Reports\*.json')







