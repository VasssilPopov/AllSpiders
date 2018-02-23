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
# Yesterday
#Srcs =['Dnevnik','Focus','Monitor','News','OffNews','PIK','Novinite','Actualno', 'Cross', 'BNews','BgOnAir']

#Today
Srcs =['24chasa','Blitz','Trud','Duma','Mediapool','ClubZ', 'Classa','Epicenter','Faktor','Dnes','StandartNews']

#Srcs =['Blitz', '24chasa', 'Trud', 'Duma', 'Mediapool', 'ClubZ', 'Classa', 'Dnevnik', 'Focus', 'News', 'OffNews', 'PIK','Epicenter','StandartNews']
#Srcs =['Bnews']
#Srcs =['Classa','Dnes']

for src in Srcs:
    HelperTools.scanReports(src+'/Reports/'+src+'-2018-02-1*.json')


#HelperTools.scanReports('PIK/Reports/PIK-2017-10-*.json')
#HelperTools.scanReports('Mediapool/Reports/Mediapool-2017-10-*.json')
#HelperTools.scanReports('Focus/Reports/Focus-2017-06-21.json')
#HelperTools.scanReports('Trud/Reports/Trud-2017-10-02.json')
#HelperTools.scanReports('PIK/Reports/PIK-2017-10-04.json')

# more than one 
#HelperTools.scanReports('Focus/Reports/Focus-2017-09-20.json')


# only one json
##HelperTools.checkReport('PIK/Reports/PIK-2017-09-19.json')
##HelperTools.checkReport('ClubZ/Reports/ClubZ-2017-09-19.json')
#HelperTools.checkReport('Monitor/Reports/Monitor-2017-09-07.json')
#HelperTools.checkReport('Monitor/Reports/Monitor-2017-09-10.json')

#HelperTools.checkReport('Classa/Reports/Classa-2017-09-22.json')

## scan json file
#import jsonlines

#file='Monitor/Reports/Monitor-2017-09-07.json'
#with jsonlines.open(file) as reader:
#        for obj in reader:
#                print obj['url']
'''

# scan json file
import jsonlines

file='Focus/Reports/Focus-2017-09-19.json'
with jsonlines.open(file) as reader:
        for obj in reader:
                print obj['url']

import os
import hashlib

root='PIK'
pathData=root+"/Data/"
pathReports=root+"/Reports/"

items=os.listdir(pathData+'.')


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

count=0
for item in items:
    md5_1=md5(pathData+str(item))
    md5_2=md5(pathReports+str(item))
    if md5_1 != md5_2:
        print '(md5) ',item, md5_1, md5_2,md5_1==md5_2
    else:
        pass


for item in items:
    c1=os.path.getsize(pathData+str(item))
    c2=os.path.getsize(pathReports+str(item))
    if c1 != c2:
        print '(sz) ',item, c1, c2,c1==c2

'''
