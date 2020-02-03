# # -*- coding: utf-8 -*-
				
import jsonlines
import glob

				
#-------------------------------------------------------------------------
'''
It maps month name to month sequential number.
It returns '??' when the name is not found 
'''
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

'''
It checks date values. 
It returns summary date & date count into file
	'Key: 2017.07.15, count:44
    
'''
def usMonthstoNumber(monthName):
    monthName=monthName.lower()
    months= {'jan':'01',  
        'feb':'02',  
        'mar':'03',  
        'apr':'04',  
        'may':'05',  
        'jun':'06',  
        'jul':'07',  
        'aug':'08',  
        'sep':'09',  
        'oct':'10',  
        'nov':'11',  
        'dec':'12'}
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

    #print len(d.items())
    for (k,v) in d.items():
        #if (k,v) != None:
        if (k != None) and (v != None):
			res=jlFile[-15:][0:10].replace('-','.')   
			if (res!=k):
				print '%s Key: %s, count: %s' % (jlFile, k,v)
    

#checkDate('Blitz\Reports\Blitz-2017-06-06.json')

# scan files in directory and call checkDate for each one
def scanFolder(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
 		print checkDate(file)
 
#scanFolder('Dnevnik\Reports\*.json')

#>>> VALIDATION -------------------------------------------------------------


import requests
import datetime

# check existens of url
def urlExists(url):
    try:
        request = requests.get(url)
        if request.status_code == 200:
            return True #print('Web site exists')
        else:
            return False #print('Web site does not exist')
    except:
        return False 
		
# standard validation procedure
#Item Level Validation
# it returns one result = True/False depending of are all validation checks true / or some of them failed		
def isDataValid(obj, rowNo):

    resValue={'result':'True','messages': list()}

    
    #url  Not empty  ---------------------------------
    if obj['url']==u'':
        resValue['result'] = False
        resValue['messages'].append(u"'url' is empty")
#    elif urlExists(obj['url'])==False:
#    #url  Exists  ---------------------------------
#        url=obj['url']
#        resValue['result'] = False
#        resValue['messages'].append(u"url:'"+url+"' doesn't exist")

    #title  Not empty   ---------------------------------
    if (obj['title'] is None) or (obj['title'].strip() ==u''):
        resValue['result'] = False
        resValue['messages'].append(u"'title' is empty")
        
    #text  Not empty   ---------------------------------
#    if obj['text'] == u'':

    #if (obj is None) or (obj.get['text'] is None):
    if obj['text'].strip() == u'':

#    if (obj is None) or (obj.get['text'] is None):
        resValue['result'] = False
        resValue['messages'].append(u"'text' is empty")
    elif obj['text'].strip() == u'':
        resValue['result'] = False
        resValue['messages'].append(u"'text' is empty")
    elif len(obj['text'].strip()) < 8:
        resValue['result'] = False
        resValue['messages'].append(u"'text' is shorter than 8")
     

    #date  Not empty   ---------------------------------

    if obj['date'].strip() == u'':
        resValue['result'] = False
        resValue['messages'].append(u"'date' is empty")
        
    #date  format YYYY.mm.dd  ---------------------------------
    try:
        datetime.datetime.strptime(obj['date'], '%Y.%m.%d')
        #datetime.datetime.strptime(obj['date'], '%d.%m.%Y')
    except ValueError:
        resValue['result'] = False
        resValue['messages'].append(u"date value:'"+obj['date']+"' Incorrect date format, should be YYYY.mm.dd")


#    print 'url: %s'%(u''+obj['url']),'-'*20

    if resValue['result']:
        #print 'Data valid'
        pass
    else:
        #print 'Data is not valid'
        #print 'url:'+obj['url']
        print '<%d>  %s' % (rowNo,obj['url'])
    
    for msg in resValue['messages']:
        print u''+msg
        #print u'' 
    return resValue['result']

# test it
t={'url':'alabala','title':'','text':'','date':'12.03.1951'}
#print isDataValid(t)
count=0

# check data of single report file
def checkReport(jlFile):


    d=dict()
    count = 0
    countAll = 0
    s20='-'*20
    #print 
    # print s20+jlFile+
    #print '>> Validation of %s '% (jlFile)
    with jsonlines.open(jlFile) as reader:
        for obj in reader:
            countAll +=1
            # print countAll
            if isDataValid(obj, countAll):
                count +=1
	#print '-'*70
    if (count != countAll):
        print '<<Valid records: %d of %d'%(count, countAll)
    #print '-'*70
    #print

#checkReport('Dnevnik/Reports/Dnevnik-2017-07-18.json')
#checkReport('Trud\Reports\Trud-2017-06-23.json')
#checkReport('ClubZ/Reports\ClubZ-2017-07-03.json')
# check data of multiple report files
def scanReports(folderPath):
#    print '>> '+folderPath

    files=glob.glob(folderPath)

#    print len(files)
    s20='-'*10 +'Start'+ '-'*10 + '\n'
   
    print s20+folderPath
    for file in files:
#        print '>2>'
        checkReport(file)


    s20='-'*10 +'End'+ '-'*10 + '\n'
    print s20
#    print '>1>'

#scanReports('Dnevnik\Reports\Ready\*.json')

# it swaps the day and the year positions into date
# 31.12.1999 --> 1999.12.31
# 1999.12.31 --> 31.12.1999
def swapDayAndYear(theDate):
    print theDate
    parts=theDate.split('.')
    tmp=parts[0]
    parts[0]=parts[2]
    parts[2]=tmp
    return '.'.join(parts)

#print swapDayAndYear('12.03.1951')



# modify the file name adding 'out' at the beggining
# makeNewFileName('Trud\Reports\Trud-2017-06-23.json') --> 'Trud\Reports\outTrud-2017-06-23.json'
def makeNewFileName(oldFileName):
    #'Trud\Reports\Trud-2017-06-23.json'
    parts=oldFileName.split('\\')
    length=len(parts)-1
    #print parts
    parts[length] = 'out'+parts[length]
    return '\\'.join(parts)

	
#print makeNewFileName('Trud\Reports\Trud-2017-06-23.json')

#  copy jlFile and swap the day and year in the result file
def swapDateParts(jlFile):
    jlFileOutput=makeNewFileName(jlFile)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                date=obj['date']
                obj['date'] = swapDayAndYear(date)
                writer.write(obj)

				
#swapDateParts('Trud\Reports\Trud-2017-06-23.json')

def getNewFileName(oldFileName):
    parts=oldFileName.split('\\')
    pos=len(parts)-2
    parts[pos] = 'Data'
    print parts
    return '\\'.join(parts)
#copy the file and change delimiters
# 2017-06-25 --> 2017.06.25
def chageDelimiter(jlFile):
	print jlFile
	jlFileOutput=getNewFileName(jlFile)
	with jsonlines.open(jlFile) as reader:
		with jsonlines.open(jlFileOutput, mode='w') as writer:
			for obj in reader:
				temp=obj['date']
				temp = temp.replace('-','.')
				obj['date'] = temp
				writer.write(obj)
    
	
# change delimiters in multiple files
def scanAndSwapDateParts(folderPath):

    s20='-'*20
    files=glob.glob(folderPath)
    print s20+folderPath+s20
    for file in files:
        swapDateParts(file)
        #chageDelimiter(file)

#scanAndSwapDateParts('PIK\Reports\*.json')
# change delimiters in multiple files
def scanChangeDateDelimiter(folderPath):

    s20='-'*20
    files=glob.glob(folderPath)
    print s20+folderPath+s20
    for file in files:
        chageDelimiter(file)

#scanAndSwapDateParts('PIK\Reports\*.json')
#scanChangeDateDelimiter('PIK\Reports\*.json')





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
        

# used def read_json(file):

'Recognize the Json file format ("Json_Lines", "Json", "Unknown")'
#It's a single file
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

# check multiple files
def checkReports(folderPath):
    files=glob.glob(folderPath)
    s20='-'*20
    
    print s20+folderPath+s20
    for file in files:
        print jsonFileType(file), file

        
##checkReports('PIK\Reports\*.json')


#-------------------------------------------------------------------------
# def bgMonthstoNumber(monthName):
    # monthName=monthName.lower()
    # months= {u'януари':'01',u'февруари':'02', u'март':'03',
             # u'април':'04',u'май':'05', u'юни':'06',
             # u'юли':'07',u'август':'08', u'септември':'09',
             # u'октомври':'10',u'ноември':'11', u'декември':'12'}

    # if (monthName in months):
        # return months[monthName]
    # else:
        # return'??'
		

def eho2(msg):
	print msg


#----------------------------------------------------------------
