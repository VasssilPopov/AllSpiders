# -*- coding: utf-8 -*-
import glob
import jsonlines

s="06 Юни 2017, 09:19"
(day, month, year)=s.split(',')[0].split()
#print '|'+bgMonthstoNumber(unicode(month,'utf-8')+'|'
#print 'ehoo'


#ClubZ-----------------------------

def getDateClubZ(sDate):
    (day, month, year)=sDate.split('.')
    pubData= '%s.%s.%s'%(year, month, day)
    return pubData

#print getDate('30.06.2017')

#ClubZ-----------------------------
#Blitz---------------------------------------------------------------
#"06 Юни 2017, 07:11"
months= {u'януари':'01',u'февруари':'02', u'март':'03',
    u'април':'04',u'май':'05', u'юни':'06',
    u'юли':'07',u'август':'08', u'септември':'09',
    u'октомври':'10',u'ноември':'11', u'декември':'12'}

def getDateBlitz(sDate):
    global months
    (day, month, year)=sDate.split(',')[0].split()
    month=months[month.lower()]
    pubData= '%s.%s.%s'%(year, month, day)
    return pubData

def getMonthNumber(monthText):
    global months
    
    (day, month, year)=monthText.split('.')
    month=months[month]
    pubDate= '%s.%s.%s'%(year, month, day)
    return pubDate

"23 Юни 2017, 12:52"


def getDateMediapool(sDate):
    global months
    
    (day, month, year)=sDate.split(' | ')[1].split()
    month=months[month.lower()]
    pubData= '%s.%s.%s'%(year, month, day)
    return pubData

#Blitz---------------------------------------------------------------

def scanFile(jlFile):
    
    jlFileOutput=makeNewFileName(jlFile)
    print jlFileOutput
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                tmp=obj["date"]
                dateParts=tmp.split('-')
                obj["date"]='%s.%s.%s'%(dateParts[2],transformDate(dateParts[1]),dateParts[0])
                writer.write(obj)

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
            #newDate = obj['date'].split(',')[0]
            #newDate = obj['date'].split(' | ')[1]

            global months
            print obj['url']
             #ClubZ
            (day, month, year)=obj['date'].split('.')
             #month=months[month.lower()]
            
            #Mediapool
            
            #(day, month, year)=obj['date'].split(' | ')[1].split()
            #month=months[month.lower()]
            
            newDate= '%s.%s.%s'%(year, month, day)


            
            if (newDate in d.keys()):
                d[newDate] +=1
            else:
                d[newDate] =1

    #print len(d.keys())
    for (k,v) in d.items():
        if (k,v) != None:
            print('Key: %s, count:%d'%(k,v))
    


# scan files in directory and call checkDate for each one 
def scanFolder(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
        print file,  checkDate(file)
 
#scanFolder('ClubZ\Reports\ClubZ-*.json')


'''
print getDateClubZ('30.06.2017')
print getDateBlitz(u"23 Юни 2017, 12:52")
print getDateMediapool(u"15:20 | 23 юли 2017 | ")
print getDateMediapool(u"|15:20 | 23 юли 2017 | ")
'''

