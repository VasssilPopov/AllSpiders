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


#HelperTools.scanReports('Blitz\Reports\Blitz*.json')
#HelperTools.scanReports('24chasa/Reports/24chasa*.json')
#HelperTools.scanReports('Trud/Reports/Trud*.json')
#HelperTools.scanReports('Duma/Reports/Duma*.json')
#HelperTools.scanReports('Mediapool/Reports/Mediapool*.json')
##HelperTools.scanReports('ClubZ/Reports/ClubZ*.json')
#HelperTools.scanReports('Dnevnik\Reports\Dnevnik*.json')
#HelperTools.scanReports('Focus\Reports\Focus*.json')
#HelperTools.scanReports('News\Reports\News*.json')
#HelperTools.scanReports('News\Reports\News-2017-07*.json')
#HelperTools.scanReports('News\Reports\News-2017-08*.json')
#HelperTools.scanReports('OffNews\Reports\OffNews-2017-07-2*.json')
#HelperTools.scanReports('PIK\Reports\PIK*.json')


##HelperTools.scanReports('PIK\Reports\PIK-2017-09-15.json')
##HelperTools.scanReports('PIK\Reports\PIK-2017-09-13.json')


#HelperTools.checkReport('PIK/Reports/PIK-2017-09-15.json')
#HelperTools.checkReport('Classa/Reports/Classa-2017-09-17.json')
#HelperTools.scanChangeDateDelimiter('PIK\Reports\*.json')
#HelperTools.scanChangeDateDelimiter('OffNews\Reports\*.json')




#HelperTools.scanReports('Mediapool/Reports/Mediapool-2017-10-05.json')

#Srcs =['Blitz', '24chasa', 'Trud', 'Duma', 'Mediapool', 'Monitor','ClubZ', 'Classa', 'Dnevnik', 'Focus', 'News', 'OffNews', 'PIK','Monitor','Epicenter','Faktor','Dnes']
#All -----------------------------------------------------------------------------------------------

#Srcs=['Actualno', 'BNews', 'BgOnAir', 'Cross', 'Dnevnik', 'Focus', 'Monitor', 'News', 'Novinite', 'OffNews', 'PIK'] + ['24chasa', 'Blitz', 'Classa', 'ClubZ', 'Dnes', 'Duma', 'Epicenter', 'Faktor', 'Mediapool', 'StandartNews', 'Trud']


# Yesterday ------------------------------------------------------------------------------------
#Srcs =['Dnevnik','Focus','Monitor','News','OffNews','PIK','Novinite','Actualno', 'Cross', 'BNews','BgOnAir']

#Srcs=['Actualno', 'BNews', 'BgOnAir', 'Cross', 'Dnevnik', 'Focus', 'Monitor', 'News', 'Novinite', 'OffNews', 'PIK']

#Today ------------------------------------------------------------------------------------
#Srcs =['24chasa','Blitz','Trud','Duma','Mediapool','ClubZ', 'Classa','Epicenter','Faktor','Dnes','StandartNews']

#Srcs = ['24chasa', 'Blitz', 'Classa', 'ClubZ', 'Dnes', 'Duma', 'Epicenter', 'Faktor', 'Mediapool', 'StandartNews', 'Trud']

#Srcs =['Blitz', '24chasa', 'Trud', 'Duma', 'Mediapool', 'ClubZ', 'Classa', 'Dnevnik', 'Focus', 'News', 'OffNews', 'PIK','Epicenter','StandartNews']

#Srcs =[ 'StandartNews']
#Srcs =[ 'Trud']


#Srcs =[ 'Focus','Classa','Dnes','Epicenter','Trud']
Srcs =[ 'Epicenter']


for src in Srcs:
#    HelperTools.scanReports(src+'/Reports/'+src+'-2018-03-*.json')
#    HelperTools.scanReports(src+'/Reports/'+src+'-2017-05-*.json')

#     HelperTools.scanReports(src+'/Reports/'+src+'-2018-01-*.json')
#     HelperTools.scanReports(src+'/Reports/'+src+'-2017-12-*.json')


#    HelperTools.scanReports(src+'/Reports/'+src+'-2018-02-*.json')

    HelperTools.scanReports(src+'/Reports/'+src+'-2018-01-*.json')


#    HelperTools.scanReports(src+'/Reports/'+src+'-2017-*.json')


