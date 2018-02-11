# -*- coding: utf-8 -*-

from os import system
import platform
from datetime import date, timedelta
from glob import glob
from sys import exit, path
import items
#----------------------------------------------------
print 'Script Version: ',0.1
#----------------------------------------------------
'Get the dates in the YYYY-mm-dd format'
Today = date.today().strftime("%Y-%m-%d")
Yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")


print 'Today: %s'%(Today),'-'*20
#system('scrapy runspider StandartNewsFeedSpider.py -o Standartnews/Reports/Standartnews-'+str(Today)+'.json -t jsonlines 2> Standartnews/Logs/outputStandartnews.txt')
system('scrapy runspider Standartnews/StandartnewsSpider.py -o Standartnews/Reports/Standartnews-'+str(Today)+'.json -t jsonlines 2> Standartnews/Logs/outputStandartnews.txt')
system('Python Standartnews/CleanStandartnews.py > Standartnews/Logs/validateStandartnews.txt')

system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')