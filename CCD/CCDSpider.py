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
    client=object
    
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
        }
    # def __init__(self):
        # print '-'*10,'CCD v(1.0)','-'*10
        
    def getCaptchaText(self):
        print "getCaptchaText"
        # Put your DBC account username and password here.
        username = 'VassilPopov'
        password = 'vppCaptcha'
        # Use deathbycaptcha.HttpClient for HTTP API.
        client = deathbycaptcha.SocketClient(username, password)
        try:
            balance = client.get_balance()
            print 'Balance: %f' % (balance)
            urlImg=response.xpath('//img[@alt="CAPTCHA"]/@src').extract_first()
            print 'Marker'
            print u'Get UrlImg:'+urlImg
            url=response.urljoin(urlImg)
            print u'url join:'+url
            captcha_file_name= "C:/ZZZZ01.jpg"
            timeout=10
            urllib.urlretrieve(url, captcha_file_name)
            print u'Марк 03'
            
            # Put your CAPTCHA file name or file-like object, and optional
            # solving timeout (in seconds) here:
            captcha = client.decode(captcha_file_name, timeout)
            captchaText=""
            if captcha:
                # The CAPTCHA was solved; captcha["captcha"] item holds its
                # numeric ID, and captcha["text"] item its text.
                print "CAPTCHA %s solved: %s" % (captcha["captcha"], captcha["text"])
                captchaText=captcha["text"]
           
        except :
            print "Oops!  That was no valid number.  Try again..."
        return captchaText
        
    def parse(self, response):
        print "Parse"
        captchaText=self.getCaptchaText()
        if (captchaText != ""):
            print 'captchaText:'+captchaText
        else:
            print "Error"


            
        # # Put your DBC account username and password here.
        # username = 'VassilPopov'
        # password = 'vppCaptcha'
        # # Use deathbycaptcha.HttpClient for HTTP API.
        # client = deathbycaptcha.SocketClient(username, password)
        # try:
            # balance = client.get_balance()
            # print 'Balance: %f' % (balance)
            # #return
            # urlImg=response.xpath('//img[@alt="CAPTCHA"]/@src').extract_first()
            # print u'Get UrlImg:'+urlImg
            # url=response.urljoin(urlImg)
            # print u'url join:'+url
            # captcha_file_name= "C:/ZZZZ01.jpg"
            # timeout=10
            # urllib.urlretrieve(url, captcha_file_name)
            # print u'Марк 03'
            
            # # Put your CAPTCHA file name or file-like object, and optional
            # # solving timeout (in seconds) here:
            # captcha = client.decode(captcha_file_name, timeout)
            # if captcha:
                # # The CAPTCHA was solved; captcha["captcha"] item holds its
                # # numeric ID, and captcha["text"] item its text.
                # print "CAPTCHA %s solved: %s" % (captcha["captcha"], captcha["text"])

            
        # except :
            # print "Oops!  That was no valid number.  Try again..."






            
        # try:
            # from scrapy.shell import inspect_response
            # print 'calling the shell'
            # inspect_response(response, self)
        # except:
            # print 'Calling shell error'
