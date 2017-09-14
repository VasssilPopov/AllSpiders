from sys import exit, path
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 


import Duplicates

# report all duplicates (their names only) by directory
#Duplicates.reportDuplicates ('24chasa/Reports/24chasa-2017-*.json')
#Duplicates.reportDuplicates ('24chasa/Reports/24chasa-2017-08-17 - Copy.json')
Duplicates.reportDuplicates ('Dnevnik/Reports/Dnevnik-2017-08-25.json')
Duplicates.reportDuplicates ('OffNews/Reports/OffNews-2017-08-25.json')
Duplicates.reportDuplicates ('PIK/Reports/PIK-2017-08-25.json')

#Duplicates.reportDuplicates ('Blitz/Reports/Blitz-*.json')
#Duplicates.reportDuplicates ('24chasa/Reports/24chasa-*.json')
#Duplicates.reportDuplicates ('Trud/Reports/Trud-*.json')
#Duplicates.reportDuplicates ('Duma/Reports/Duma-*.json')
#Duplicates.reportDuplicates ('Mediapool/Reports/Mediapool-2017-*.json')
#Duplicates.reportDuplicates ('ClubZ/Reports/ClubZ-*.json')

#Duplicates.reportDuplicates ('Dnevnik/Reports/Dnevnik-*.json')
#Duplicates.reportDuplicates ('Focus/Reports/Focus-*.json')
#Duplicates.reportDuplicates ('News/Reports/News-*.json')
#Duplicates.reportDuplicates ('OffNews/Reports/OffNews-*.json')
#Duplicates.reportDuplicates ('PIK/Reports/PIK-*.json')

#Duplicates.removeDuplicates('24chasa\\Reports\\24chasa-2017-08-25.json')
#Duplicates.removeDuplicates('24chasa\\Reports\\24chasa-2017-08-22.json')
#Duplicates.removeDuplicates('24chasa\\Reports\\24chasa-2017-08-23.json')

import os.path
from pathlib2 import Path

def checkExistensOfDataFolder():

    s='-' * 10
    print s+u' Съществуване на поддиректория Data '+s
    names=['Blitz', '24chasa', 'Trud', 'Duma', 'Mediapool', 'ClubZ', 'Dnevnik', 'Focus', 'News', 'OffNews', 'PIK', ]
    folders=[x+'\\Data' for x in names]

    for f in folders:
        my_file = Path(f)
        print f,'\t', my_file.is_dir()

    print s*5


# text files
# someTexts=['some text 1', 'some text 2', 'some text 3', 'some text 4', ]
# f=open('TextTest.txt','w')
# for text in someTexts:
    # f.write(text+'\n')
# f.close()

#checkExistensOfDataFolder()
