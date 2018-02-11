# -*- coding: utf-8 -*-
import scrapy
import logging
import json
import os
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
import Duplicates
from datetime import date, timedelta

#Get the Today adn Yesterday dates  ------------------------------
Today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

# "standart" validation contai a value, Date format etc.----------
json_datafile = 'BgOnAir/Reports/BgOnAir-'+Today+'.json'

print 'VALIDATIONS for %s' %(json_datafile)
print

if os.path.isfile(json_datafile):
	#check for duplicates ---------------------------------------------
	Duplicates.reportDuplicates (json_datafile)

	#checkReport('Dnevnik/Reports/Dnevnik-2017-07-18.json')------------
	HelperTools.checkReport(json_datafile)