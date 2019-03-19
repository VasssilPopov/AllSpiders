# -*- coding: utf-8 -*-


import json

from sys import exit, path
from datetime import date, timedelta
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from HelperTools import *
from Dates import *
from Duplicates import *


'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%Y.%m.%d").lower()

#Srcs =['Blitz', '24chasa', 'Trud', 'Duma', 'Mediapool', 'ClubZ', 'Classa', 'Dnevnik', 'Focus', 'News', 'OffNews', 'PIK',]
#Srcs =['PIK', ]

#for src in Srcs:
#    HelperTools.scanReports(src+'/Reports/'+src+'-2017-11-1*.json')

s='News'        
spath='%s\\Reports\\%s-*.json' % (s, s)
#spathD='%s\\Data\\%s-*.json' % (s, s)

# date format
#scanFolderCheckDate(spathD)
# data duplicates

reportDuplicates (spath)


#>#removeDuplicates('24chasa\\Reports\\24chasa-2017-11-19.json')
