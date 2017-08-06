# -*- coding: utf-8 -*-
import scrapy
import logging
import json
import os
from sys import exit, path
import platform
import glob
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

#Get the Today adn Yesterday dates  ------------------------------
Today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
test='OffNews/Reports/OffNews-2017-07-29.json'
# "standart" validation contai a value, Date format etc.----------
json_datafile = 'OffNews/Reports/OffNews-'+Yesterday+'.json'
json_datafile = test

# scan files in directory and call checkDate for each one 
folderPath='News/Reports/News-*.json'
s20='-'*20
files=glob.glob(folderPath)

print s20+folderPath+s20
for json_datafile in files:
    #print file,  checkDate(file)
 
#scanFolder('ClubZ\Reports\ClubZ-*.json')


	print 'VALIDATIONS for %s' %(json_datafile)
	print

	if os.path.isfile(json_datafile):
		#check for duplicates ---------------------------------------------
		HelperTools.reportDuplicates (json_datafile)

		#checkReport('Dnevnik/Reports/Dnevnik-2017-07-18.json')------------
		HelperTools.checkReport(json_datafile)