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

# system('scrapy runspider 24chasa/24chasaSpider.py -o 24chasa/Reports/24chasa-'+str(Today)+'.json -t jsonlines 2> 24chasa/Logs/output24chasa.txt')
# system('Python 24chasa/Clean24chasa.py > 24chasa/Logs/validate24chasa.txt')

system('scrapy runspider Trud/TrudSpider.py -o Trud/Reports/Trud-'+str(Today)+'.json -t jsonlines 2> Trud/Logs/outputTrud.txt')
system('Python Trud/CleanTrud.py > Trud/Logs/validateTrud.txt')

# system('scrapy runspider Duma/DumaSpider.py -o Duma/Reports/Duma-'+str(Today)+'.json -t jsonlines 2> Duma/Logs/outputDuma.txt')
# system('Python Duma/CleanDuma.py > Duma/Logs/validateDuma.txt')

system('scrapy runspider Mediapool/MediapoolSpider.py -o Mediapool/Reports/Mediapool-'+str(Today)+'.json -t jsonlines 2> Mediapool/Logs/outputMediapool.txt')
system('Python Mediapool/CleanMediapool.py > Mediapool/Logs/validateMediapool.txt')

system('scrapy runspider ClubZ/ClubZSpider.py -o ClubZ/Reports/ClubZ-'+str(Today)+'.json -t jsonlines 2> ClubZ/Logs/outputClubZ.txt')
system('Python ClubZ/CleanClubZ.py > ClubZ/Logs/validateClubZ.txt')

system('scrapy runspider Classa/ClassaSpider.py -o Classa/Reports/Classa-'+str(Today)+'.json -t jsonlines 2> Classa/Logs/outputClassa.txt')
system('Python Classa/CleanClassa.py > Classa/Logs/validateClassa.txt')

system('scrapy runspider Faktor/FaktorSpider.py -o Faktor/Reports/Faktor-'+str(Today)+'.json -t jsonlines 2> Faktor/Logs/outputFaktor.txt')
system('Python Faktor/CleanFaktor.py > Faktor/Logs/validateFaktor.txt')

system('scrapy runspider Epicenter/EpicenterSpider.py -o Epicenter/Reports/Epicenter-'+str(Today)+'.json -t jsonlines 2> Epicenter/Logs/outputEpicenter.txt')
system('Python Epicenter/CleanEpicenter.py > Epicenter/Logs/validateEpicenter.txt')

system('scrapy runspider Dnes/DnesSpider.py -o Dnes/Reports/Dnes-'+str(Today)+'.json -t jsonlines 2> Dnes/Logs/outputDnes.txt')
system('Python Dnes/CleanDnes.py > Dnes/Logs/validateDnes.txt')

system('scrapy runspider Standartnews/StandartnewsSpider.py -o Standartnews/Reports/Standartnews-'+str(Today)+'.json -t jsonlines 2> Standartnews/Logs/outputStandartnews.txt')
system('Python Standartnews/CleanStandartnews.py > Standartnews/Logs/validateStandartnews.txt')

system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')