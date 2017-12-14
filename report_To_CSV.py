# -*- coding: utf-8 -*-

from sys import exit, path
from datetime import date, timedelta
import platform
import os

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
from sys import argv

def convertLine(line):
    ds=line[1:-2].replace('|',',')
    return ds


# read all text file 2017-07
textFileName='_MonthlyReports/MonthlyReport-'+argv[1]+'.txt'
csvFileName='_MonthlyReports/MonthlyReport-'+argv[1]+'.csv'

if not (os.path.exists(textFileName) and os.path.getsize(textFileName) > 0):
    print "File ["+textFileName+"] doesn't exist!!"
    print 'Parameter format is YYYY-mm (example 2017-09)'
    exit()

fInput = open(textFileName, 'r')
lines = fInput.readlines()
fInput.close()

fOutput = open(csvFileName, 'w')
# column headings
fOutput.write( convertLine(lines[2]))
fOutput.write('\n')

i=4
while lines[i][1:5] !='----':
    fOutput.write(convertLine(lines[i]))
    fOutput.write('\n')
    i=i+1
    
