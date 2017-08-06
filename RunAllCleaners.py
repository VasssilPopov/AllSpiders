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
print 'Blitz'
# system('scrapy runspider Blitz/BlitzSpider.py -o Blitz/Reports/Blitz-'+str(Today)+'.json -t jsonlines 2> Blitz/Logs/outputBlitz.txt')
system('Python Blitz/CleanBlitz.py > Blitz/Logs/validateBlitz.txt')

print '24chasa'
# system('scrapy runspider 24chasa/24chasaSpider.py -o 24chasa/Reports/24chasa-'+str(Today)+'.json -t jsonlines 2> 24chasa/Logs/output24chasa.txt')
system('Python 24chasa/Clean24chasa.py > 24chasa/Logs/validate24chasa.txt')

print 'Trud'
# system('scrapy runspider Trud/TrudSpider.py -o Trud/Reports/Trud-'+str(Today)+'.json -t jsonlines 2> Trud/Logs/outputTrud.txt')
system('Python Trud/CleanTrud.py > Trud/Logs/validateTrud.txt')

print 'Duma'
# system('scrapy runspider Duma/DumaSpider.py -o Duma/Reports/Duma-'+str(Today)+'.json -t jsonlines 2> Duma/Logs/outputDuma.txt')
system('Python Duma/CleanDuma.py > Duma/Logs/validateDuma.txt')


print 'Mediapool'
# system('scrapy runspider /MediapoolSpider.py -o Mediapool/Reports/Mediapool-'+str(Today)+'.json -t jsonlines 2> Mediapool/Logs/outputMediapool.txt')
system('Python Mediapool/CleanMediapool.py > Mediapool/Logs/validateMediapool.txt')

print 'ClubZ'
# system('scrapy runspider ClubZ/ClubZSpider.py -o ClubZ/Reports/ClubZ-'+str(Today)+'.json -t jsonlines 2> ClubZ/Logs/outputClubZ.txt')
system('Python ClubZ/CleanClubZ.py > ClubZ/Logs/validateClubZ.txt')


print 'Yesterday: %s'%(Yesterday),'-'*20

print 'Dnevnik'
# system('scrapy runspider Dnevnik/DnevnikSpider.py -o Dnevnik/Reports/Dnevnik-'+str(Yesterday)+'.json -t jsonlines 2> Dnevnik/Logs/outputDnevnik.txt')
system('Python Dnevnik/CleanDnevnik.py > Dnevnik/Logs/validateDnevnik.txt')
	
print 'Focus'
# system('scrapy runspider Focus/FocusSpider.py -o Focus/Reports/Focus-'+str(Yesterday)+'.json -t jsonlines 2> Focus/Logs/outputFocus.txt')
system('Python Focus/CleanFocus.py > Focus/Logs/validateFocus.txt')

print 'News'
# system('scrapy runspider News/NewsSpider.py -o News/Reports/News-'+str(Yesterday)+'.json -t jsonlines 2> News/Logs/outputNews.txt')
system('Python News/CleanNews.py > News/Logs/validateNews.txt')
	
print 'OffNews'
# system('scrapy runspider OffNews/OffNewsSpider.py -o OffNews/Reports/OffNews-'+str(Yesterday)+'.json -t jsonlines 2> OffNews/Logs/outputOffNews.txt')
system('Python OffNews/CleanOffNews.py > OffNews/Logs/validateOffNews.txt')

print 'PIK'
# system('scrapy runspider PIK/PIKSpider.py -o PIK/Reports/PIK-'+str(Yesterday)+'.json -t jsonlines 2> PIK/Logs/outputPIK.txt')
system('Python PIK/CleanPIK.py > PIK/Logs/validatePIK.txt')

system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')
