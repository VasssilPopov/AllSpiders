# -*- coding: utf-8 -*-
import scrapy
import logging
import json
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

from ScrapingHelpers import *
from HelperTools import *

#HelperTools.eho2('Ehooo')

dir('HelperTools')
print HelperTools.__file__
print '*'*10
#from HelperTools import reportDuplicates, checkDate, checkReport
from datetime import date, timedelta

'Get the Today adn Yesterday dates formated'
Today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

# File to check
line ='-'*90
json_datafile = '24chasa/Reports/24chasa-'+Today+'.json'
print line
print 'Data validation on: %s' %(json_datafile)
print (date.today().strftime("Date: %d-%b-%Y time: %H:%M:%S"))
print line
print 'Check for duplicates  '+'-'*30
reportDuplicates (json_datafile)
print '-'*90

print 'Check for date info  '+'-'*30
checkDate(json_datafile)
print '-'*90

#standart checks
print 'Standart data validity checks'+'-'*10
checkReport(json_datafile)
print '-'*30

#check for empty "column" url/title/text/date
# print ' data validity checks'+'-'*10
# check_empty(json_datafile)
# print '-'*30

scanReports('24chasa\Reports\*.json')
