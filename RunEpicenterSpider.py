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
system('scrapy runspider Epicenter/EpicenterSpider.py -o Epicenter/Reports/Epicenter-'+str(Today)+'.json -t jsonlines 2> Epicenter/Logs/outputEpicenter.txt')
system('Python Epicenter/CleanEpicenter.py > Epicenter/Logs/validateEpicenter.txt')

system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')