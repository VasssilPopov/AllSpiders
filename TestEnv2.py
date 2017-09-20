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
from Monthly_Report import *
from urllib2 import quote


# Monthly Reports of collected data (Start)------------------------------------
# during a year and month
# output reports will be text files
# into _MonthlyReports subdirectory of root directory
# file name will be MonthlyReport-YYYY-mm.txt
# example MonthlyReport-2017-05.txt
# report of collected data during 2017 year and
# month of May

# example input parameters
# Report Year 2017 and report month (August)
repYear='2017'
repMonth=9

# single month report
monthlyDataReport(repYear, repMonth)

## range of months report
## create separate text file reports
## from May to September
#!!!! uncomment next lines to have a report
# for m in range(5,10):
#     monthlyDataReport(repYear, m)
# Monthly Reports of collected data (End)------------------------------------
'''
import time
startTime=time.time()

for i in range(0,3):
        time.sleep(1)

endTime=time.time()

print '%s Duration: %f' % (time.localtime(startTime),(endTime - startTime))



'''
