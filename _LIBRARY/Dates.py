#  -*- coding: utf-8 -*-
#------------------------Date Formating "YYYY.mm.dd"

from datetime import date, timedelta
import glob

def bgShortMonthstoNumber(monthName):
    monthName=monthName.lower()[0:3]
    months= {u'яну':'01',u'фев':'02', u'мар':'03',
             u'апр':'04',u'май':'05', u'юни':'06',
             u'юли':'07',u'авг':'08', u'сеп':'09',
             u'окт':'10',u'ное':'11', u'дек':'12'}

    if (monthName in months):
        return months[monthName]
    else:
        return'??'


#--------------- 24chasa---------------------------------
# input '01.08.2017 17:33'

def dc24chasa(date):
    (day, month, year)=date.split()[0].split('.')
    return '%s.%s.%s' % (year, month, day)

#print '24chasa: \t','01.08.2017 17:33-->', dc24chasa('01.08.2017 17:33')

#< Blitz >---------------------------
# input '01 Авг. 2017, 13:09'


def dcBlitz(date):
    (day, month, year)=date.split(',')[0].replace('.',' ').split()
    month = bgShortMonthstoNumber(month)
    return '%s.%s.%s' % (year, month, day)

#print 'Blitz: \t',u'01 Авг. 2017, 13:09 -->' ,dcBlitz(u'01 Авг. 2017, 13:09')

#< ClubZ >---------------------------

def dcClubZ(date):
    (day, month, year)=date.split(',')[0].split('.')
    return '%s.%s.%s' % (year, month, day)

#print 'ClubZ: \t',u'30.06.2017, 9:27 ч.-->', dcClubZ('30.06.2017, 9:27 ч.')

#< Dnevnik >---------------------------
# 22:49, 27 юни 17
def dcDnevnik(date):
    (day, month, year)=date.split(',')[1].split()
    month = bgShortMonthstoNumber(month)
    year='20'+year
    return '%s.%s.%s' % (year, month, day)

#print 'Dnevnik: \t',u'22:49, 27 юни 17.-->', dcDnevnik(u'22:49, 27 юни 17')

#< Duma >---------------------------
#'28. Юни 2017'
def dcDuma(date):
    (day, month, year)=date.replace('.',' ').split()
    month = bgShortMonthstoNumber(month)
    return '%s.%s.%s' % (year, month, day)

#print 'Duma: \t',u'28. Юни 2017-->', dcDuma(u'28. Юни 2017')

#< Focus >---------------------------
#'Yesterday'
def dcFocus():
    yesterday = date.today() - timedelta(1)
    Yesterday = yesterday.strftime("%Y.%m.%d")
    return Yesterday


#print 'Focus: \t','Yesterday -->', dcFocus()

#<Mediapool >---------------------------
#'17:36 | 28 юни 2017 | '
def dcMediapool(date):
    (day, month, year)=date.split(' | ')[1].split()
    month = bgShortMonthstoNumber(month)
    return '%s.%s.%s' % (year, month, day)

#print 'Mediapool: ',u'17:36 | 28 юни 2017 | -->', dcMediapool(u'17:36 | 28 юни 2017 | ')


#<News >---------------------------
#'2017-06-28T23:44:43+03:00'
def dcNews(date):
    return date.split('T')[0].replace('-','.')

#print 'News: ',u'2017-06-28T23:44:43+03:00 | -->', dcNews(u'2017-06-28T23:44:43+03:00 ')


#<OffNews >---------------------------
#'Последна промяна на 20 юли 2017 в 22:12'
def dcOffNews(date):
    (day, month, year )= date.split()[3:6]
    month = bgShortMonthstoNumber(month)
    s= '%s.%s.%s' % (year, month, day)
    return s

#print 'OffNews: ',u'Последна промяна на 20 юли 2017 в 22:12 -->', dcOffNews(u'Последна промяна на 20 юли 2017 в 22:12 ')


#<PIK >---------------------------
#'Последна промяна на 20 юли 2017 в 22:12'
def dcPIK(date):
    (day,month,year) = date.split('|')[1].strip().split('.')
    date='%s.%s.%s'%(year,month,day)
    return date

#print 'PIK: ',u'19:09 | 22.07.2017 -->', dcPIK(u'19:09 | 22.07.2017')

#<Trud >---------------------------
#'28.06.2017'
def dcTrud(date):
    (day,month,year) = date.split('.')
    date='%s.%s.%s'%(year,month,day)
    return date

#print 'Trud: ',u'28.06.2017 -->', dcTrud(u'28.06.2017')

'''
It check date values. 
It returns summary date & date count into file
	'Key: 2017.07.15, count:44
'''

