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

'$ scrapy crawl Dnevnik -o Dnevnik.json -t jsonlines'
'scrapy runspider DnevnikSpider.py -o Dnevnik-28-Apr-2017.json -t json'

'Get the yesterday date'
Today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

# Dnevnik za Yesterday
json_datafile = 'Report/PIK-'+Today+'.json'

check_empty(json_datafile)
