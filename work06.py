# -*- coding: cp1251 -*

from sys import exit, path

import platform
if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from  HelperTools import *

#print jsonFileType('PIK\Reports\PIK-2017-06-05.json')
#checkReports('PIK\Reports\*.json')
#checkReport('Dnevnik/Reports/Dnevnik-2017-07-18.json')


#scanAndSwapDateParts('OffNews\Reports\*.json')
#scanReports('OffNews\Reports\out*.json')
"13:56 | 09 юни 2017 | "

import os
    
os.system('cls')
'''
#d=dict()

s20='-'*20
files=glob.glob('Focus/Reports/*.json')
#print s20+folderPath+s20
for file in files:
        d=dict()
        jlFile=file
        print file+s20

        with jsonlines.open(jlFile) as reader:
                for obj in reader:
                        if obj['url'] in d:
                                print obj['url']
                        else:
                                d[obj['url']]=1
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
        print "reportDuplicates("+str(path)+") "
                                                       
        s80='-'  * 82
        #d=dict()
        files=glob.glob(path)
        print "%-60s %10s %10s" % ('Files', 'All Recs', 'Dupl Recs')
        for file in files:
               
                d=dict()
                print s80
                countAll =0
                countDuplicates=0
 
                with jsonlines.open(file) as reader:
                        for obj in reader:
                                countAll +=1
                                if obj['url'] in d:
                                        print obj['url']
                                        countDuplicates +=1
                                else:
                                        d[obj['url']]=1

                        print "%-60s %10d %10d" % (file, countAll, countDuplicates)

reportDuplicates ('24chasa\\Reports\\24chasa*.json')
#reportDuplicates ('Blitz/Reports\Blitz*.json')

#--------------------------------------------
#reportDuplicates ('Monitor/Reports/*.json')


#----------------------------------------------------------------
s=' | 17:34 | 20 юли 2017 |'
s=s.split('|')
print s
def getMediapoolDate(pDate):
    parts=pDate.split('|')
    sDate=parts[1].strip()
    parts=sDate.split()
    print parts[1]
    print bgMonthstoNumber(parts[1])
    #print parts[2].split()[1]

#t=getMediapoolDate('08:20 | 08 юли 2017 | ')



#-------------------------------------------------------------          
#scanReports('Blitz/Reports\Blitz*.json')
sDate='22 Юни 2017, 15:20'
months= {u'януари':'01',u'февруари':'02', u'март':'03',
             u'април':'04',u'май':'05', u'юни':'06',
             u'юли':'07',u'август':'08', u'септември':'09',
             u'октомври':'10',u'ноември':'11', u'декември':'12'}

#(day, month, year)=sDate.split(',')[0].split()
#print month.lower()
#month=months[month.lower().encode('utf-8')]
s=u' 21 \u044e\u043b\u0438 2017 '.split()
print months[s[1]]
