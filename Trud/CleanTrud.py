# -*- coding: utf-8 -*-
import scrapy
import logging
import json
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
from datetime import date, timedelta

'Get the Today adn Yesterday dates formated'
Today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

# File to check
json_datafile = 'Trud/Reports/Trud-'+Today+'.json'
print 'Input file %s' %(json_datafile)
check_empty(json_datafile)

