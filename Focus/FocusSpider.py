# -*- coding: utf-8 -*-
import scrapy
import logging
import json
import sys
from sys import exit, path
from datetime import date, timedelta
import os
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from urllib2 import quote

# scrapy runspider FocusSpider.py -o Reports/Focus-2017-05-17.json -t jsonlines
# Windows
#  2017-05-17 yesterday
# RunIt 2017-05-17

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")



'$ scrapy crawl Dnevnik -o Dnevnik.json -t jsonlines'
'scrapy runspider DNSpider.py -o Dnevnik-28-Apr-2017.json -t json'
'scrapy runspider DNSpider3.py -o Dnevnik-28-Apr-2017.json -t json'




# 'Get the yesterday date'

# Today = (date.today()).strftime("%Y-%m-%d")

# yesterday = date.today() - timedelta(1)

# Yesterday = yesterday.strftime("%Y-%m-%d")
# print Yesterday
# translateMonth={u'януари':'january',u'февруари':'february',u'март':'march',u'април':'april',u'май':'may',u'юни':'june',u'юли':'july',u'август':'august',u'септември':'september',u'октомври':'october',u'ноември':'november',u'декември':'december'}



class FocusSpider(scrapy.Spider):
	name = 'Focus'
	allowed_domains = ['focus-news.net']
	custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
	
	def __init__(self):

		cwd = os.getcwd()
		print 'Yesterday information will be collected. Date: %s'%(Yesterday)
		# print 'Current Work Directory: %s '%(cwd)
	
		self.urls = ['http://www.focus-news.net/news/Yesterday/']

		self.json_datafile = 'Reports/Focus-'+Yesterday+'.json'
		self.links_seen = self.get_ids(self.json_datafile)
		self.links_seen = set (map( lambda str: str[31:49], self.links_seen))		

		# print self.links_seen
		
		# Prepare links_seen data structure
		#self.links_seen=read_ids(self.json_datafile)

		print 'Report output: %s' %(self.json_datafile)
		print 'Seen links: %d' %(len(self.links_seen))
		# for link in self.links_seen:
			# print link
		
	def get_ids(self, json_datafile):
		ids = []
		
		try:
			ids = read_ids(json_datafile)
		except (IOError,ValueError):
			return set(ids)

		return set(ids)

	def start_requests(self):

		for url in self.urls:
			yield scrapy.Request(url=url, callback=self.parse)    

	def parse(self, response):

		#links = response.css('div.text h2 a::attr(href)').extract()
		links=response.xpath('//div[@class="cnk-ttl"]/h2/a/@href').extract()
		links = list (map( lambda str: 'http://www.focus-news.net'+str[1:], links))		
		
		
		for link in links:
			if link[31:49] not in self.links_seen:
				try:
					print 'save data: %s'% link 
					yield scrapy.Request(url=link, callback=self.parse_page)
				except:
					e = sys.exc_info()[1]
					print "Error: %s" %(e)

	def parse_page(self, response):

		# 'We need the titles, links and times to index and follow'
		try:
			url   = response.url
			title = response.xpath('//div[@class="inside-top-title"]/h1/text()').extract_first().strip()
			article = ''.join(response.xpath('//div[@class="print-content font-resize-content"]/div[@class="inside-body-content jstf"]/text()').extract()).strip()
			pubDate=yesterday
		except:
			print 'Error url:',url
		yield {
			'url': url,
			'title': title,
			'text': article,
			'date': pubDate
		}	
