# -*- coding: utf-8 -*-

from os import system
import platform
from datetime import date, timedelta
from glob import glob
from sys import exit, path
#----------------------------------------------------
print 'Script Version: ',0.1
#----------------------------------------------------
'Get the dates in the YYYY-mm-dd format'
Today = date.today().strftime("%Y-%m-%d")
Yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")


print 'Today: %s'%(Today),'-'*20
system('scrapy runspider CCD/CCDSpider.py -o CCD/Reports/CCD-'+str(Yesterday)+'.json -t jsonlines 2> CCD/Logs/outputCCD.txt')
system('Python CCD/CleanCCD.py > CCD/Logs/validateCCD.txt')

#system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')