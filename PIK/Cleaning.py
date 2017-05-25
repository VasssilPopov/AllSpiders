# -*- coding: utf-8 -*-
import scrapy
import logging
import json
from sys import exit, path
import platform
if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from datetime import date, timedelta

'Get the Today adn Yesterday dates'
Today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

# File to check
json_datafile = 'Reports/PIK-'+Yesterday+'.json'
print 'Check for %s' %(json_datafile)
check_empty(json_datafile)


exit()
# print list_urls(json_datafile)
# print type(read_ids(json_datafile)[1])



# url = "http://pik.bg/%D0%BC%D0%BB%D0%B0%D0%B4%D0%B8%D1%8F%D1%82-%D1%81%D0%BE%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%81%D1%82-%D0%BA%D1%80%D1%83%D0%BC-%D0%B7%D0%B0%D1%80%D0%BA%D0%BE%D0%B2-%D0%BA%D0%BE%D1%80%D0%BD%D0%B5%D0%BB%D0%B8%D1%8F-%D0%BD%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0-%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B8-%D0%B7%D0%B0%D0%BC%D0%B5%D1%81%D1%82%D0%BD%D0%B8%D1%86%D0%B8%D1%82%D0%B5-%D1%81%D0%B8-%D0%BD%D0%B8%D0%B5-%D1%81%D0%B0%D0%BC%D0%BE-%D0%B3%D0%B8-%D0%B3%D0%BB%D0%B0%D1%81%D1%83%D0%B2%D0%B0-news657838.html"
url = u"http://pik.bg/рокадите-в-бсп-продължават-нинова-си-избра-&quotстари-муцуни&quot-за-заместници-обновена-news657704.html"
url_encoded = "http://pik.bg/%D0%B1%D0%B0%D1%80%D0%BE%D0%BC%D0%B5%D1%82%D1%8A%D1%80-%D1%81%D0%BE%D1%86%D0%B8%D0%BE%D0%BB%D0%BE%D0%B3-%D1%81-%D1%82%D0%B5%D0%B6%D0%BA%D0%B0-%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%D0%B0-%D0%B7%D0%B0-%D0%B1%D1%81%D0%BF-%D1%8E%D1%80%D0%B8%D0%B9-%D0%B0%D1%81%D0%BB%D0%B0%D0%BD%D0%BE%D0%B2-%D0%B7%D0%B0-%D1%82%D1%80%D1%83%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D0%B5-%D0%BD%D0%B0-%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%B0%D0%BD%D0%BE-news657981.html"

links_seen = [url_encoded, url_encoded]

links_seen = map(lambda url: url.split('news')[1] ,links_seen)
print links_seen


print type(url)
# print url.encode('utf-8')

from urllib2  import  quote
print quote( url.encode('utf-8') ).replace("%3A", ':').replace("%26quot",'')
print url_encoded
# print url.split("http://pik.bg/")[1]
if quote( url.encode('utf-8') ).replace("%3A", ':').replace("%26quot",'')  not in read_ids(json_datafile):
	print 'Not'
else:
	print 'Found'

