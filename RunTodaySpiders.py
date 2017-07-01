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


print 'Today: %s'%(Today),'-'*20
system('scrapy runspider Blitz/BlitzSpider.py -o Blitz/Reports/Blitz-'+str(Today)+'.json -t jsonlines 2> Blitz/Logs/outputBlitz.txt')
system('Python Blitz/CleanBlitz.py > Blitz/Logs/validateBlitz.txt')

system('scrapy runspider 24chasa/24chasaSpider.py -o 24chasa/Reports/24chasa-'+str(Today)+'.json -t jsonlines 2> 24chasa/Logs/output24chasa.txt')
system('Python 24chasa/Clean24chasa.py > 24chasa/Logs/validate24chasa.txt')

system('scrapy runspider Trud/TrudSpider.py -o Trud/Reports/Trud-'+str(Today)+'.json -t jsonlines 2> Trud/Logs/outputTrud.txt')
system('Python Trud/CleanTrud.py > Trud/Logs/validateTrud.txt')

system('scrapy runspider Duma/DumaSpider.py -o Duma/Reports/Duma-'+str(Today)+'.json -t jsonlines 2> Duma/Logs/outputDuma.txt')
system('Python Duma/CleanDuma.py > Duma/Logs/validateDuma.txt')

system('scrapy runspider Mediapool/MediapoolSpider.py -o Mediapool/Reports/Mediapool-'+str(Today)+'.json -t jsonlines 2> Mediapool/Logs/outputMediapool.txt')
system('Python Mediapool/CleanMediapool.py > Mediapool/Logs/validateMediapool.txt')

system('scrapy runspider ClubZ/ClubZSpider.py -o ClubZ/Reports/ClubZ-'+str(Today)+'.json -t jsonlines 2> ClubZ/Logs/outputClubZ.txt')
system('Python ClubZ/CleanClubZ.py > ClubZ/Logs/validateClubZ.txt')
	
system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')