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


#scanReports('Dnevnik\Reports\Dnevnik*.json')
#scanReports('24chasa/Reports/24chasa-*.json')
#scanReports('Trud/Reports/Trud-*.json')
#scanReports('Trud/Reports/Trud-2017-07-*.json')
#scanReports('Duma/Reports/Duma-*.json')
#scanReports('Mediapool/Reports/Mediapool-*.json')
#scanReports('ClubZ/Reports/ClubZ-*.json')
#scanReports('Blitz/Reports/Blitz-*.json')
#scanReports('Focus/Reports/Focus-*.json')
#scanReports('News/Reports/News-*.json')
#scanReports('OffNews/Reports/OffNews-*.json')
#scanReports('PIK/Reports/PIK-*.json')


#scanReports('Mediapool/Reports/Mediapool-2017-08-25.json')


#scanReports('Mediapool/Reports/Mediapool-2017-08-09.json')
#scanReports('Mediapool/Reports/Mediapool-2017-08-11.json')

scanReports('PIK/Reports/PIK-2017-08-*.json')
