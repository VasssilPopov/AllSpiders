# -*- coding: utf-8 -*-
import scrapy
import logging
import json
from sys import exit, path
import platform
import os
if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from datetime import date, timedelta
import HelperTools 
import Duplicates
# 'Get the Today adn Yesterday dates'
# Today = date.today().strftime("%Y-%m-%d")
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")

# # File to check
# json_datafile = 'Reports/Cross-'+Yesterday+'.json'
# print 'Check for %s' %(json_datafile)
# check_empty(json_datafile)


#Get the Today adn Yesterday dates  ------------------------------
Today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

# "standart" validation contai a value, Date format etc.----------
json_datafile = 'Cross/Reports/Cross-'+Yesterday+'.json'
print 'VALIDATIONS for %s' %(json_datafile)
print

if os.path.isfile(json_datafile):
	#check for duplicates ---------------------------------------------
	Duplicates.reportDuplicates (json_datafile)

	#checkReport('Cross/Reports/Cross-2017-07-18.json')------------
	HelperTools.checkReport(json_datafile)