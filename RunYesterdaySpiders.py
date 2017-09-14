# -*- coding: utf-8 -*-

from os import system
import platform
from datetime import date, timedelta
from glob import glob
from sys import exit, path
#----------------------------------------------------
print 'Script Version: ',0.1
#----------------------------------------------------
'Get the dates in the YYYY-mm-dd format'
Today = date.today().strftime("%Y-%m-%d")
Yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")


# print 'Today: %s'%(Today),'-'*20
# system('scrapy runspider Blitz/BlitzSpider.py -o Blitz/Reports/Blitz-'+str(Today)+'.json -t jsonlines 2> Blitz/Logs/outputBlitz.txt')
# system('Python Blitz/CleanBlitz.py > Blitz/Logs/validateBlitz.txt')

# system('scrapy runspider Mediapool/MediapoolSpider.py -o Mediapool/Reports/Mediapool-'+str(Today)+'.json -t jsonlines 2> Mediapool/Logs/outputMediapool.txt')
# system('Python Mediapool/CleanMediapool.py > Mediapool/Logs/validateMediapool.txt')
	
print 'Yesterday: %s'%(Yesterday),'-'*20

system('scrapy runspider Dnevnik/DnevnikSpider.py -o Dnevnik/Reports/Dnevnik-'+str(Yesterday)+'.json -t jsonlines 2> Dnevnik/Logs/outputDnevnik.txt')
system('Python Dnevnik/CleanDnevnik.py > Dnevnik/Logs/validateDnevnik.txt')
	
system('scrapy runspider Focus/FocusSpider.py -o Focus/Reports/Focus-'+str(Yesterday)+'.json -t jsonlines 2> Focus/Logs/outputFocus.txt')
system('Python Focus/CleanFocus.py > Focus/Logs/validateFocus.txt')

system('scrapy runspider Monitor/MonitorSpider.py -o Monitor/Reports/Monitor-'+str(Yesterday)+'.json -t jsonlines 2> Monitor/Logs/outputMonitor.txt')
system('Python Monitor/CleanMonitor.py > Monitor/Logs/validateMonitor.txt')

system('scrapy runspider News/NewsSpider.py -o News/Reports/News-'+str(Yesterday)+'.json -t jsonlines 2> News/Logs/outputNews.txt')
system('Python News/CleanNews.py > News/Logs/validateNews.txt')
	
system('scrapy runspider OffNews/OffNewsSpider.py -o OffNews/Reports/OffNews-'+str(Yesterday)+'.json -t jsonlines 2> OffNews/Logs/outputOffNews.txt')
system('Python OffNews/CleanOffNews.py > OffNews/Logs/validateOffNews.txt')

system('scrapy runspider PIK/PIKSpider.py -o PIK/Reports/PIK-'+str(Yesterday)+'.json -t jsonlines 2> PIK/Logs/outputPIK.txt')
system('Python PIK/CleanPIK.py > PIK/Logs/validatePIK.txt')

system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')
# system('echo Urrra')