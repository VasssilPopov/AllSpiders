# -*- coding: utf-8 -*-
from os import system
import platform
from datetime import date, timedelta
from glob import glob
from sys import exit, path

'Get the dates in the YYYY-mm-dd format'
Today = date.today().strftime("%Y-%m-%d")
Yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")


if platform.system() == 'Linux':
	
	# system('ls')
	system('scrapy runspider Dnevnik/DnevnikSpider.py -o Dnevnik/Reports/Dnevnik-'+str(Yesterday)+'.json -t json')
	system('scrapy runspider mediapool/MediapoolSpider.py -o Mediapool/Reports/Dnevnik-'+str(Today)+'.json -t json')
	# scrapy runspider MediapoolSpider.py -o Mediapool-30-Apr-2017.json -t json
