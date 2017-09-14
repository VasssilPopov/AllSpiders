import glob
import calendar
import os
import sys

def getFullSet(year, month):
    fullSet=set()
    for i in range(1,calendar.monthrange(int(year),int(month))[1]+1):
        fullSet.add(('00'+str(i))[-2:])
    return fullSet
    
    

def scanFolderFiles(folderPath):
    s20='-'*20
    dData=dict()
    
    files=glob.glob(folderPath)
    print s20+folderPath+s20
    fullSet=set()
    for i in range(1,32):
        fullSet.add(('00'+str(i))[-2:])
    #print fullSet
    
    for file in files:
        (year, month, day)=file[-15:][0:10].split('-')
        key = year + month
        if (key not in dData):
            dData[key]=getFullSet(year, month)
        dData[key].remove(day)
    sortedKeys=sorted(dData.keys())
    
    for k in sortedKeys:    #dData.keys():
        print k, sorted(list(dData[k]))
        #print dData[key]        
#    print sorted( list(fullSet))

#scanFolderFiles('PIK/Reports\PIK-2017-*.json')
#scanFolderFiles('OffNews/Reports\OffNews-2017-*.json')
#scanFolderFiles('Dnevnik/Reports\Dnevnik-2017-*.json')
#scanFolderFiles('Mediapool/Reports\Mediapool-20*.json')

#scanFolderFiles('PIK/Reports\\PIK-20*.json')

import jsonlines
import datetime

delimiter='|'
lineD=''
now = datetime.datetime.now()

srcNames=["Date\Src","Dnevnik","Focus","Monitor","News","OffNews","PIK",     "Blitz", "Classa", "24chasa","Trud","Duma","Mediapool","ClubZ"]

def reportColumnHeadings(year, month):
    delimiterColumn=' '
    lineD=delimiterColumn  #+'-'*10+delimiterColumn
    s=delimiter


    for srcName in srcNames:
        lineD=lineD+'-'*10+delimiterColumn
        s=s+'{:>10}'.format(srcName)+delimiter

        title= '-- MONTHLY REPORT --  Year: %s Month: %s ( Reported at: %s )' % (year, month, now.strftime("%Y-%m-%d %H:%M"))
    return title+'\n'+lineD+'\n'+s+'\n'+lineD+'\n'



def getRowCount(fileName):
    count = 0
    try:
        if os.path.isfile(fileName):
            with jsonlines.open(fileName) as reader:
                for obj in reader:
                    count=count+1
    except:
        pass

    return count

#print getRowCount('')
#print getRowCount('Mediapool\\Reports\\Mediapool-2017-07-31.json')

def getCount(fName, date):
    fileName=fName+'\\Reports\\'+fName+'-'+date+'.json'
    return getRowCount(fileName)

#print getCount('Mediapool', '2017-07-31')
def reportLine(date):
    
    line=delimiter+'{:10}'.format(date)+delimiter
    for srcName in srcNames[1:]:
        line=line+'{:>10}'.format(getCount(srcName,date))+delimiter

    
    return line


def monthlyDataReport(repYear, repMonth):

    repCrit='%s-%02d-'%(repYear, repMonth)
    repTitle='-%s-%02d'%(repYear, repMonth)
    fText=open('_MonthlyReports\\MontlyReport'+repTitle+'.txt','w')
    fText.write( reportColumnHeadings(repYear, repMonth))
    days= sorted(list(getFullSet(repYear, repMonth)))
    for day in days:
        fText.write( reportLine(repCrit+day)+'\n')
    fText.write(lineD)
    fText.close()


repYear='2017'
repMonth=9

# single month report
monthlyDataReport(repYear, repMonth)

# range of months report
#for m in range(5,10):
#    monthlyDataReport(repYear, m)
