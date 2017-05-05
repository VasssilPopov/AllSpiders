# -*- coding: utf-8 -*-
import scrapy
import logging
import json
from sys import exit, path
path.append('C:\STUDY_SPIDERS\Work\Spiders\_LIBRARY')
from ScrapingHelpers import *
from datetime import date, timedelta

'$ scrapy crawl Dnevnik -o Dnevnik.json -t jsonlines'
'scrapy runspider DnevnikSpider.py -o Dnevnik-28-Apr-2017.json -t json'

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%d-%b-%Y")

# Dnevnik za Yesterday
# json_datafile = 'Reports/Dnevnik-'+Yesterday+'.json'
json_datafile = 'Reports/Blitz-2017-05-05.json'

check_empty(json_datafile)
