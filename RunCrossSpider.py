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
system('scrapy runspider Cross/CrossSpider.py -o Cross/Reports/Cross-'+str(Yesterday)+'.json -t jsonlines 2> Cross/Logs/outputCross.txt')
system('Python Cross/CleanCross.py > Cross/Logs/validateCross.txt')

system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')