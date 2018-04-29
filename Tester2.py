# -*- coding: utf-8 -*
from sys import exit, path
import jsonlines
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

import glob
#- Duplicates in files -----------------------------------------------------------------

def displayDuplicates (path):
        print "displayDuplicates("+str(path)+") "

        # init variables
        s40='-'*40
        #d=dict()
        files=glob.glob(path)
        print files
        for file in files:
                
                d=dict()
                print file+s40

                with jsonlines.open(file) as reader:
                        for obj in reader:
                                if obj['url'] in d:
                                        print obj['url']
                                else:
                                        d[obj['url']]=1
#displayDuplicates ('Focus/Reports/*.json')
#displayDuplicates ('24chasa/Reports/24chasa-2017-07-*.json')


def reportDuplicates (path):
        # init variables
        #print "reportDuplicates("+str(path)+") "
                                                       
        s80='-'  * 89
        #d=dict()
        files=glob.glob(path)
        #print "%-60s %10s %10s" % ('Files', 'All Recs', 'Dupl Recs')
        for file in files:
               
                d=dict()
                #print file #s80
                countAll =0
                countDuplicates=0
 
                with jsonlines.open(file) as reader:
                        for obj in reader:
                                countAll +=1
                                if obj['url'] in d:
                                        #print obj['url']
                                        countDuplicates +=1
                                else:
                                        d[obj['url']]=1
                        if countDuplicates>0:
                            print "%-60s %10d %10d" % (file, countAll, countDuplicates)
                            print s80
#reportDuplicates ("24chasa/Reports/*.json")
#reportDuplicates ('Blitz/Reports\Blitz*.json')




for ff in ('24chasa','Actualno','BGNes','BgOnAir','Blitz','BNews','Classa','ClubZ','Cross','Dnes',
    'Dnevnik','Duma','Epicenter','Faktor','Focus','Mediapool','Monitor','News',
    'Novinite','OffNews','PIK','SegaBG','Standartnews','Trud',):
    print '-- %s --'% (ff)
    reportDuplicates ( '%s/Reports/*.json' % (ff))


#--------------------------------------------
#reportDuplicates ("Monitor/Reports/*.json")


import jsonlines
# def makeNewFileName(oldFileName):
    # #'Trud\Reports\Trud-2017-06-23.json'
    # parts=oldFileName.split('\\')
    # length=len(parts)-1
    # print parts
    # parts[length] = 'out'+parts[length]
    # return '\\'.join(parts)
	
    
    
    
def makeNewFileName(oldFileName):
    print oldFileName
    parts=oldFileName.split('/')
    pos=len(parts)-2
    parts[pos] = 'Data'
    print parts
    return '\\'.join(parts)
# oldFileName='24chasa/Reports/24chasa-2018-04-06.json'

def removeDuplicates(jlFile):
    
    jlFileOutput=makeNewFileName(jlFile)
    print 'FileOutput:' + jlFileOutput
    d=dict()
    s80='-'*88
    print s80
    countAll =0
    countDuplicates=0

    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
			
				countAll +=1
				if obj['url'] in d:
					# print obj['url']
					countDuplicates +=1
					# continue
				else:
					d[obj['url']]=1
					writer.write(obj)

            print "%-60s %10d %10d" % (jlFile, countAll, countDuplicates)

            
# removeDuplicates("Faktor/Reports/Faktor-2017-12-04.json")
            
            
 
# scan files in directory and call removeDuplicates for each one
def scanFolderAndRemoveDuplicates (folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
        print removeDuplicates(file) 
