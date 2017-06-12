# -*- coding: utf-8 -*-

from os import system
import platform
from datetime import date, timedelta
from glob import glob
from sys import exit, path
#----------------------------------------------------
print 'Version: ',0.1
#----------------------------------------------------
'Get the dates in the YYYY-mm-dd format'
Today = date.today().strftime("%Y-%m-%d")
Yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")


print 'Today: %s'%(Today)
print '---------- Blitz ------------'
system('scrapy runspider Blitz/BlitzSpider.py -o Blitz/Reports/Blitz-'+str(Today)+'.json -t jsonlines 2> Blitz/Logs/outputBlitz.txt')
print '---------- Mediapool ------------'
system('scrapy runspider Mediapool/MediapoolSpider.py -o Mediapool/Reports/Mediapool-'+str(Today)+'.json -t jsonlines 2> Mediapool/Logs/outputMediapool.txt')
	
# print 'Yesterday: %s'%(Yesterday)
system('scrapy runspider Dnevnik/DnevnikSpider.py -o Dnevnik/Reports/Dnevnik-'+str(Yesterday)+'.json -t jsonlines 2> Dnevnik/Logs/outputDnevnik.txt')
	
system('scrapy runspider Focus/FocusSpider.py -o Focus/Reports/Focus-'+str(Yesterday)+'.json -t jsonlines 2> Focus/Logs/outputFocus.txt')

system('scrapy runspider News/NewsSpider.py -o News/Reports/News-'+str(Yesterday)+'.json -t jsonlines 2> News/Logs/outputNews.txt')
	
system('scrapy runspider OffNews/OffNewsSpider.py -o OffNews/Reports/OffNews-'+str(Yesterday)+'.json -t jsonlines 2> OffNews/Logs/outputOffNews.txt')

system('scrapy runspider PIK/PIKSpider.py -o PIK/Reports/PIK-'+str(Yesterday)+'.json -t jsonlines 2> PIK/Logs/outputPIK.txt')

