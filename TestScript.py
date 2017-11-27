#!/usr/bin/python
# -*- coding: utf-8 -*-

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

today = date.today()
Today = today.strftime('%Y-%m-%d')
strToday = today.strftime('%Y.%m.%d')

'''
months ={u'ян.':'01', u'февр.':'02', u'март':'03', u'апр.':'04', u'май':'05', u'юни':'06',
          u'юли':'07', u'авг.':'08', u'септ.':'09', u'окт.':'10', u'ноем.':'11', u'дек.':'12'}

def read_ids(file):

    ids = set()

    try:
        with open(file, 'rb') as f:
            for item in json_lines.reader(f):
                ids.add(item['url'])
    except IOError:
        ids = set()

    # print 'error'

    return ids



def  __start__():
    print '__init__'
    json_datafile = 'Epicenter/Reports/Epicenter-' + Today + '.json'
    links_seen = read_ids(json_datafile)
    #links_seen = set(map(lambda url: url.split('/item/')[1][0:6], links_seen))
    print '-' * 10, 'Epicenter v(1.0)', '-' * 10
    print 'seen: %d' % len(links_seen)
    links_list=list(links_seen)
    print links_list[0]

__start__()
print months[u'ноем.']
'''
date= u'434 | 31 окт. 2017 | 10:18'
date= u'434 | 01 ноем. 2017 | 10:18'

def getStdDate(dateString):

    months ={u'ян.':'01', u'февр.':'02', u'март':'03', u'апр.':'04', u'май':'05', u'юни':'06',
          u'юли':'07', u'авг.':'08', u'септ.':'09', u'окт.':'10', u'ноем.':'11', u'дек.':'12'}

    (day,month, year)=dateString.split('|')[1].strip() .split(' ')
    dateExpr='????.??.??'

    if (month in months):
        month = months[month]
        dateExpr =  '%s.%s.%s' % (year, month, day)

    return dateExpr

print getStdDate(date)
#url='http://www.focus-news.net/news/2017/10/31/2452454/makfaks-makedoniya-ruski-sveshtenik-izprati-podarak-na-radovan-karadzhich.html'




