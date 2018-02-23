# -*- coding: utf-8 -*-
import jsonlines
import glob
from Dates import *

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
		print ">> Duplicates Report"
		#print ">> for ["+str(path)+"]"

		s80='-'*70
		#d=dict()
		files=glob.glob(path)
		# print s80
		# print "%-60s %10s %10s" % ('Files', 'All Recs', 'Dupl Recs')
		for file in files:
                
			d=dict()
			print s80
			countAll =0
			countDuplicates=0

			with jsonlines.open(file) as reader:
					for obj in reader:
							countAll +=1
							if obj['url'] in d:
									print obj['url']
									countDuplicates +=1
							else:
									d[obj['url']]=1

					# print "%-60s %10d %10d" % (file, countAll, countDuplicates)
					print "Records: (All: %s, Duplicates: %s ), File: %s" % (countAll, countDuplicates, file)
		# print s80

	
#reportDuplicates ('PIK/Reports/PIK-2017-07-10.json')
#reportDuplicates ('Monitor/Reports/*.json')

# def removeDuplicates (path):
		# # init variables
		# print "Report Duplicates for ("+str(path)+") "

		# s80='-'*88
		# #d=dict()
		# files=glob.glob(path)
		# print s80
		# print "%-60s %10s %10s" % ('Files', 'All Recs', 'Dupl Recs')
		# for file in files:
                
			# d=dict()
			# print s80
			# countAll =0
			# countDuplicates=0

			# with jsonlines.open(file) as reader:
					# for obj in reader:
							# countAll +=1
							# if obj['url'] in d:
									# print obj['url']
									# countDuplicates +=1
									# # continue
							# else:
									# d[obj['url']]=1

					# print "%-60s %10d %10d" % (file, countAll, countDuplicates)

	
#removeDuplicates ('PIK/Reports\PIK-2017-07-10.json')
#removeDuplicates ('Monitor/Reports/*.json')

import jsonlines
# def makeNewFileName(oldFileName):
    # #'Trud\Reports\Trud-2017-06-23.json'
    # parts=oldFileName.split('\\')
    # length=len(parts)-1
    # print parts
    # parts[length] = 'out'+parts[length]
    # return '\\'.join(parts)
	
def makeNewFileName(oldFileName):
    parts=oldFileName.split('\\')
    pos=len(parts)-2
    parts[pos] = 'Data'
    print parts
    return '\\'.join(parts)

def removeDuplicates(jlFile):
    
    jlFileOutput=makeNewFileName(jlFile)
    print jlFileOutput
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

 
# scan files in directory and call removeDuplicates for each one
def scanFolderAndRemoveDuplicates (folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
        print removeDuplicates(file) 

		
		
		
		
def checkDate(jlFile):
    d=dict()
    
    with jsonlines.open(jlFile) as reader:
        for obj in reader:
            #newDate = obj['date'].split()[0]
            #newDate = obj['date'].split(',')[0]
            #newDate = obj['date'].split(' | ')[1]

            global months
            print obj['url']
             #ClubZ
            (day, month, year)=obj['date'].split('.')
             #month=months[month.lower()]
            
            #Mediapool
            
            #(day, month, year)=obj['date'].split(' | ')[1].split()
            #month=months[month.lower()]
            
            newDate= '%s.%s.%s'%(year, month, day)


            
            if (newDate in d.keys()):
                d[newDate] +=1
            else:
                d[newDate] =1

		print jlFile
    #print len(d.keys())
    for (k,v) in d.items():
        if (k,v) != None:
            print('>> %s Key: %s, count:%d'%(jlFile,k,v))
    


# scan files in directory and call checkDate for each one 
def scanFolder(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print s20+folderPath+s20
    for file in files:
        print file,  checkDate(file)
 
#scanFolder('ClubZ\Reports\ClubZ-*.json')

'''
It check date values. 
It returns summary date & date count into file
	'Key: 2017.07.15, count:44
'''
def checkDate(jlFile):
    d=dict()
    
    with jsonlines.open(jlFile) as reader:
        for obj in reader:
            newDate = obj['date']
            if (newDate in d.keys()):
                d[newDate] +=1
            else:
                d[newDate] =1

    #print len(d.keys())
    for (k,v) in d.items():
        if (k,v) != None:
			fd=jlFile[-15:][0:10].replace('-','.')
			res=(k == fd)
			if res == False:
				print 'Key: %s, count: %d %s'%(k,v,res)
    

#checkDate('Blitz\Reports\Blitz-2017-06-06.json')

# scan files in directory and call checkDate for each one
def scanFolderCheckDate(folderPath):
    s20='-'*20
    files=glob.glob(folderPath)

    print folderPath+s20
    for file in files:
        print(file+'-'*20)
        print checkDate(file) 


#scanFolderCheckDate('Blitz/Reports/Blitz-2017-*.json')

#Blitz
# it coverts 
# def makeNewFileName(oldFileName):
    # parts=oldFileName.split('\\')
    # pos=len(parts)-2
    # parts[pos] = 'Data'
    # return '\\'.join(parts)
	
def convertBlitzDatetoStandart(jlFile):
    jlFileOutput=makeNewFileName(jlFile)
    with jsonlines.open(jlFile) as reader:
        with jsonlines.open(jlFileOutput, mode='w') as writer:
            for obj in reader:
                
                date=u''+obj['date'].replace('-','.')
                obj['date'] = date

                # (day, month, year)=date.split('-')
                # month = bgShortMonthstoNumber(month)
                # obj['date'] = '%s.%s.%s' % (year, month, day)

                # print jlFile
                # if (date[0:4] != '2017'):
					# obj['date'] = dcMediapool(date)
                writer.write(obj)
                
#convertBlitzDatetoStandart('Mediapool\\Reports\\Mediapool-2017-05-21.json')

def scanAndConvertBlitzDatetoStandart(folderPath):

    s20='-'*20
    files=glob.glob(folderPath)
    print s20+folderPath+s20
    for file in files:
		convertBlitzDatetoStandart(file)
