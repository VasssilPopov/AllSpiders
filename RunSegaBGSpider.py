# -*- coding: utf-8 -*-
import scrapy
import logging
import json
from os import system
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
import HelperTools 
from datetime import date, timedelta
from glob import glob


#----------------------------------------------------
print 'Script Version: ',1.0
#----------------------------------------------------
'Get the dates in the YYYY-mm-dd format'
Today = date.today().strftime("%Y-%m-%d")
Yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")


print 'Yesterday: %s'%(Yesterday),'-'*20
system('scrapy runspider SegaBG/SegaBGSpider.py -o SegaBG/Reports/SegaBG-'+str(Yesterday)+'.json -t jsonlines 2> SegaBG/Logs/outputSegaBG.txt')
system('Python SegaBG/CleanSegaBG.py > SegaBG/Logs/validateSegaBG.txt')

system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')