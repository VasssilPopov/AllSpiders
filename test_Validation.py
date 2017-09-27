# # -*- coding: utf-8 -*-
				
import jsonlines
import glob
import time
from sys import exit, path
import platform
if platform.system() == 'Linux':
                    
	print 'Linux' 
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	print 'Windows 7' 
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

import HelperTools

count=0

# check data of single report file
def checkReport(jlFile):

    d=dict()
    count = 0
    countAll = 0
    s20='-'*20
    timeStart=0
    print 
    # print s20+jlFile+
    print '>> Validation report of ',jlFile
    with jsonlines.open(jlFile) as reader:
        for obj in reader:
            countAll +=1
            # print countAll
            timeStart=int(time.time())
            if HelperTools.isDataValid(obj):
                count +=1
            timeDuration=int(time.time()) - timeStart
            print 'duration %s' % (timeDuration)
	print '-'*70
    print 'Valid records: %d of %d'%(count, countAll)
    print '-'*70
    print

    
    
checkReport('Duma/Reports/Duma-2017-09-25.json')
