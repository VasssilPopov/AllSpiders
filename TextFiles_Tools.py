from datetime import date
from datetime import timedelta

srcNames=[['Blitz',0],
          ['24chasa',0],
          ['Trud',0],
          ['Duma',0],
          ['Mediapool',0],
          ['ClubZ',0],
          ['Classa',0],
          ['Dnevnik',-1],
          ['Focus',-1],
          ['Monitor',-1],
          ['News',-1],
          ['OffNews',-1],
          ['PIK',-1]]


# listSrcNames

#for srcName in srcNames:
#    print srcName

#for rep in [x+'/Reports' for x in srcNames]:
#    print rep

    
#for log in [x[0]+'/Logs/validate'+x[0]+'.txt' for x in srcNames]:
#    print log
    
#for log in [x+'/Logs/output'+x+'.txt' for x in srcNames]:
#    print log


#f = open("VALIDATIONS.txt")
#text = f.read()
#print(text)

def displayRowPattern(srcName, srcTotalRecs, srcDuplRecs, srcValidRecs):
    print '|%-45s|%10s|%10s|%10s|'%(srcName.strip(), str(srcTotalRecs), str(srcDuplRecs), str(srcValidRecs))

def displayRow(srcName, srcTotalRecs, srcDuplRecs, srcValidRecs):
    displayRowPattern(srcName.strip(), str(srcTotalRecs), str(srcDuplRecs), str(srcValidRecs))
    
#displayRow('OffNews/Reports/OffNews-2017-08-29.json', 155,10, 145)
#displayRow('PIKs/Reports/PIK-2017-08-29.json', 155,10, 145)    

def getSrcData(fileName):
    srcTotal,srcDuplicates,srcValid='','',''
    # Prepare dates
    Today = date.today()
    delta = timedelta(days=-1)
    Yesterday = Today + delta

#    print 'Yesterday:%s' % (Yesterday)
#    print 'Today:%s' % (Today)
    
    textFile = open(fileName)
    lines=textFile.readlines()
    srcName = lines[0][16:]

    for line in lines:
        if line.startswith('Records: (All:'):
            tmp=line.find(',')
            srcTotal = line[14:tmp].strip()
            srcDuplicates = line[30:33].strip()
#            print srcTotal, srcDuplicates
        if line.startswith('Valid records:'):
            srcValid= line[14:18].strip()
#            print srcValid

    displayRow(srcName,srcTotal,srcDuplicates,srcValid)
    
def getSrcData1(srcName):
    f = open(srcName)
    lines = f.readlines()


def getLatestTopDataStatus():
    line=' '+'-'*45+ ' '+'-'*10+' '+'-'*10+' '+'-'*10
    print line
    #displayRowPattern('-'*45, '-'*10,'-'*10,'-'*10)
    displayRowPattern('Source Name', 'Total Recs', 'Dupl Recs', 'ValidRecs')
    #displayRowPattern('-'*45, '-'*10,'-'*10,'-'*10)
    print line
   
    for log in [x[0]+'/Logs/validate'+x[0]+'.txt' for x in srcNames]:
        getSrcData(log)

    print line
    #displayRowPattern('-'*45, '-'*10,'-'*10,'-'*10)

getLatestTopDataStatus()


