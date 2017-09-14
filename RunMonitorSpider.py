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


print 'Yesterday: %s'%(Yesterday),'-'*20
print 'Run MonitorSpider'
system('scrapy runspider Monitor/MonitorSpider.py -o Monitor/Reports/Monitor-'+str(Yesterday)+'.json -t jsonlines 2> Monitor/Logs/outputMonitor.txt')

print 'Run CleanMonitor'
system('Python Monitor/CleanMonitor.py > Monitor/Logs/validateMonitor.txt')
	
print 'Run SummaryReport'
system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')