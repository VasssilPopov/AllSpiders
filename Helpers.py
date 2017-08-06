# -*- coding: utf-8 -*-

#---------------------------------------------------------------------
d=dict()
# obj['date'] --> u'13.07.2017 14:23'
#
'''
with jsonlines.open('cleared.json') as reader:
    for obj in reader:
        newDate = obj['date'].split()[0]
        if (newDate in d.keys()):
            d[newDate] +=1
        else:
            d[newDate] =1

print d
'''

import glob
import jsonlines

def bgMonthstoNumber(monthName):
    monthName=monthName.lower()
    months= {u'януари':'01',u'февруари':'02', u'март':'03',
             u'април':'04',u'май':'05', u'юни':'06',
             u'юли':'07',u'август':'08', u'септември':'09',
             u'октомври':'10',u'ноември':'11', u'декември':'12'}

    if (monthName in months):
        return months[monthName]
    else:
        return'??'


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

    print len(d.keys())
    for (k,v) in d.items():
        if (k,v) != None:
            print('Key: %s, count:%d'%(k,v))
    

#checkDate('Blitz\Reports\Blitz-2017-06-06.json')

def scanFolder(folderPath):
    files=glob.glob(folderPath)
    s20='-'*20
    
    print s20+folderPath+s20
    for file in files:
        print checkDate(file)
        #print file

scanFolder('Dnevnik\Reports\*.json')

#>>> VALIDATION -------------------------------------------------------------




import requests
import datetime

def urlExists(url):
    try:
        request = requests.get(url)
        if request.status_code == 200:
            return True #print('Web site exists')
        else:
            return False #print('Web site does not exist')
    except:
        return False 

def isDataValid(obj):

    resValue={'result':'True','messages': list()}

    
    #url  Not empty  ---------------------------------
    if obj['url']==u'':
        resValue['result'] = False
        resValue['messages'].append("'url' is empty")
    elif urlExists(obj['url'])==False:
    #url  Exists  ---------------------------------
        url=obj['url']
        resValue['result'] = False
        resValue['messages'].append("url:'"+url+"' doesn't exist")

    #title  Not empty   ---------------------------------
    if obj['title']==u'':
        resValue['result'] = False
        resValue['messages'].append("'title' is empty")
        
    #text  Not empty   ---------------------------------
    if obj['title']==u'':
        resValue['result'] = False
        resValue['messages'].append("'text' is empty")
        

    #date  Not empty   ---------------------------------
    if obj['date']==u'':
        resValue['result'] = False
        resValue['messages'].append("'date' is empty")
        
    #date  format YYYY.mm.dd  ---------------------------------
    try:
        datetime.datetime.strptime(obj['date'], '%Y.%m.%d')
        #datetime.datetime.strptime(obj['date'], '%d.%m.%Y')
    except ValueError:
        resValue['result'] = False
        resValue['messages'].append("'"+obj['date']+"' Incorrect date format, should be YYYY.mm.dd")


#    print 'url: %s'%(u''+obj['url']),'-'*20

    if resValue['result']:
        #print 'Data valid'
        pass
    else:
        print 'Data is not valid'
    for msg in resValue['messages']:
        print msg

    return resValue['result']

# test it
t={'url':'alabala','title':'','text':'','date':'12.03.1951'}
#print isDataValid(t)
count=0

def checkReport(jlFile):
    d=dict()
    count = 0
    s20='-'*20
    print s20+jlFile+s20
    with jsonlines.open(jlFile) as reader:
        for obj in reader:
            if isDataValid(obj):
                count +=1
    print 'Valid records: %d'%(count)

#checkReport('Dnevnik/Reports/Dnevnik-2017-07-18.json')


def scanReports(folderPath):
    files=glob.glob(folderPath)
    s20='-'*20
    
    print s20+folderPath+s20
    for file in files:
        print checkReport(file)
        #print file

#scanReports('Dnevnik\Reports\Ready\*.json')

    
#checkReport('Trud\Reports\Trud-2017-06-23.json')

        
def swapDayAndYear(theDate):
    print theDate
    parts=theDate.split('.')
    tmp=parts[0]
    parts[0]=parts[2]
    parts[2]=tmp
    return '.'.join(parts)

#print swapDayAndYear('12.03.1951')
def makeNewFileName(oldFileName):
    #'Trud\Reports\Trud-2017-06-23.json'
    parts=oldFileName.split('\\')
    print parts
    parts[2] = 'out'+parts[2]
    return '\\'.join(parts)

#print makeNewFileName('Trud\Reports\Trud-2017-06-23.json')


def swapDateParts(jlFile):
    jlFileOutput=makeNewFileName(c)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                date=obj['date']
                obj['date'] = swapDayAndYear(date)
                writer.write(obj)

# 2017-06-25 --> 2017.06.25
def chageDelimiter(jlFile):
    jlFileOutput=makeNewFileName(jlFile)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                temp=obj['date']
                temp = temp.replace('-','.')
                obj['date'] = temp
                writer.write(obj)
    
#swapDateParts('Trud\Reports\Trud-2017-06-23.json')
                
def scanAndSwapDateParts(folderPath):
    files=glob.glob(folderPath)
    s20='-'*20
    
    print s20+folderPath+s20
    for file in files:
        #swapDateParts(file)
        chageDelimiter(file)
        #print file


#scanAndSwapDateParts('PIK\Reports\*.json')
'''
def scaneFile(jlFile):

    jlFileOutput=makeNewFileName(jlFile)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                try:
                    writer.write(obj)
                except:
                    continue

scaneFile('PIK\Reports\PIK-2017-06-05.json')

'''
#makeNewFileName('PIK\Reports\PIK-2017-07-06.json')

        
#<<< VALIDATION -------------------------------------------------------------

#>>> TRUD -------------------------------------------------------------------

#checkDate('Trud\Reports\Trud-2017-06-25.json')


#scanFolder('Trud\Reports\*.json')


#<<< TRUD -------------------------------------------------------------------        

# used def read_json(file):

'Recognize the Json file format ("Json_Lines", "Json", "Unknown")'
def jsonFileType(file):

    with open(file) as f:               # Check what is the first char of the file { or [
        first_char = f.read(1)
        f.close()		

    if first_char == '{': # Json Lines
        return "Json_Lines"
    elif first_char == '[': # Json format
        return "Json"
    else:
        return "Unknown"



#print jsonFileType('PIK\Reports\PIK-2017-06-05.json')


def checkReports(folderPath):
    files=glob.glob(folderPath)
    s20='-'*20
    
    print s20+folderPath+s20
    for file in files:
        print jsonFileType(file), file
        #print file

        
#checkReports('PIK/Reports\*.json')

s='28.06.2017'
dateParts=s.split('.')
tmp=dateParts[0]
dateParts[0]=dateParts[2]
dateParts[2]=tmp
date='.'.join(dateParts)
#print date



























