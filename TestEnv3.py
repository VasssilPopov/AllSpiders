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

'''
import sched, time

s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print("From print_time", time.time(), a)


def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    print(time.time())

print_some_times()

'''

'''
import schedule
import time

def job():
    print("I'm working...".time.time())

schedule.every(10).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
'''

'''
import HelperTools
#HelperTools.dir('HelperTools')
print HelperTools.usMonthstoNumber('OCT')
'''

'''
def usMonthstoNumber(monthName):
        monthName=monthName.lower()
        months= {'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'may':'05', 'jun':'06', 'jul':'07', 'aug':'08', 'sep':'09', 'oct':'10', 'nov':'11', 'dec':'12'}
        if (monthName in months):
                return months[monthName]
        else:
                return'??'
pubDate=u'24'
pubDate2=[u'may', u'2017']
print '%s.%s.%s' % (pubDate2[1],usMonthstoNumber(pubDate2[0]), pubDate)
'''

'''''
def getDate( response ):
        pubDate=u''.join(response.xpath('//article[@class="entry single"]/span[@class="entry-date"]/text()').extract()).strip()

        pubDate2 =  response.xpath('//article[@class="entry single"]/span[@class="entry-date"]/span/text()').extract()
        monthName=pubDate2[0][0:3].lower()

        months= {'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'may':'05', 'jun':'06', 'jul':'07', 'aug':'08', 'sep':'09', 'oct':'10', 'nov':'11', 'dec':'12'}
        dateExpr = '????.??.??'
        if (monthName in months):
                montNumber = months[monthName]
                dateExpr =  '%s.%s.%s' % (pubDate2[1],montNumber, pubDate)

        return dateExpr


print getDate(response)



serOutput = [596,552,561,573,560,575,557,560,581,576,586,590,595,603,582,
             578,579,588,594,591,602,600,601,584,553,554,559,566,565,564,572,
             567,570,577,558,583,533,541,546,548]
svyat1=[576,603,595,590,576,581,569,557,575,560,573,561,552,550]
svyat2=[4540,544,537,460,469,538,543,542,552182,539,536,534,535,531,492]
politika=[597, 592,512,398,580,574,568,562]

print len(serOutput)
serOutput.sort()
print serOutput
ws=set(serOutput).intersection(svyat1)
print 'len (set(serOutput).intersection(svyat1))%s'%(len(ws))
print ws
print set(serOutput).intersection(svyat2)
print set(serOutput).intersection(politika)

'''''

# scan json file
import jsonlines

file='Duma/Reports/Duma-2017-10-19.json'
with jsonlines.open(file) as reader:
        for obj in reader:
                print obj['url']

