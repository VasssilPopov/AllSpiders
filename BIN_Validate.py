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
from Dates import *
import HelperTools


##>
Srcs=['Actualno', 'BNews', 'BgOnAir', 'Cross', 'Dnevnik', 'Focus', 'Monitor', 'News', 'Novinite', 'OffNews', 'PIK']
##>
Srcs += ['24chasa', 'Blitz', 'Classa', 'ClubZ', 'Dnes', 'Duma', 'Epicenter', 'Faktor', 'Mediapool', 'StandartNews', 'Trud']

for src in Srcs:
#    print src+'\n'
        
#    HelperTools.scanReports(src+'/Reports/'+src+'-2019-01-11.json')
#    HelperTools.scanReports(src+'/Reports/'+src+'-2019-08-23.json')
    
    HelperTools.scanReports(src+'/Reports/'+src+'-2019-12-1*.json')

    #HelperTools.scanReports(src+'/Reports/'+src+'-2019-12-30.json')
