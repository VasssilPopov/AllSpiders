# -*- coding: utf-8 -*-
import scrapy
import urllib
import deathbycaptcha
import os

from datetime import date, timedelta
from sys import exit, path
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from Dates import *
import os.path
import jsonlines


yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
yesterdaysDate = yesterday.strftime("%Y.%m.%d")
BGMonths={u'януари':'01',u'февруари':'02',u'март':'03',u'април':'04',u'май':'05',u'юни':'06',u'юли':'07',u'август':'08',u'септември':'09',u'октомври':'10',u'ноември':'11',u'декември':'12'}

# Събиране на съдебни решения
class CCD(scrapy.Spider):
    name = "CCD"
    start_urls=[
    'https://legalacts.justice.bg/',
    ]
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
        }
    def __init__(self):
        print '-'*10,'CCD v(1.0)','-'*10
        
        # zeroes the file
        fileName="CCD/Reports/CCD-%s.json"%(Yesterday)
        if (os.path.exists(fileName) and os.path.getsize(fileName) > 0):
                f = open(fileName, 'w').close()

        # Put your DBC account username and password here.
        username = 'VassilPopov'
        password = 'vppCaptcha'
        # Use deathbycaptcha.HttpClient for HTTP API.
        client = deathbycaptcha.SocketClient(username, password)
        try:
            balance = client.get_balance()
            print 'Balance: %f' % (balance)
            urlImg=response.xpath('//img[@alt="CAPTCHA"]/@src').extract_first()
            url=response.urljoin(urlImg)
            urllib.urlretrieve(url, "C:/ZZZZ01.jpg")
        except:
            print "Oops!  That was no valid number.  Try again..."
        
