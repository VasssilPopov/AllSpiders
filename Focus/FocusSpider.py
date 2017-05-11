# -*- coding: utf-8 -*-
import scrapy
import logging
import json
import sys
from sys import exit, path
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\Spiders\Library')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from datetime import date, timedelta
import os





'$ scrapy crawl Dnevnik -o Dnevnik.json -t jsonlines'
'scrapy runspider DNSpider.py -o Dnevnik-28-Apr-2017.json -t json'
'scrapy runspider DNSpider3.py -o Dnevnik-28-Apr-2017.json -t json'




'Get the yesterday date'

Today = (date.today()).strftime("%Y-%m-%d")

yesterday = date.today() - timedelta(1)

Yesterday = yesterday.strftime("%Y-%m-%d")
print Yesterday
translateMonth={u'януари':'january',u'февруари':'february',u'март':'march',u'април':'april',u'май':'may',u'юни':'june',u'юли':'july',u'август':'august',u'септември':'september',u'октомври':'october',u'ноември':'november',u'декември':'december'}



class FocusSpider(scrapy.Spider):
	name = 'Focus'
	allowed_domains = ['focus-news.net']
	custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
	
	def __init__(self):

		cwd = os.getcwd()
		print 'Yesterday information will be collected. Date: %s'%(Yesterday)
		print 'Current Work Directory: %s '%(cwd)
	
		self.urls = ['http://www.focus-news.net/news/Yesterday/']

		# Their date format is: http://www.dnevnik.bg/allnews/2017/03/19/
		# 'http://www.dnevnik.bg/rss/'

		self.json_datafile = 'Reports/Focus-'+Yesterday+'.json'
		self.links_seen = self.get_ids(self.json_datafile)
		
		# Prepare links_seen data structure
		#self.links_seen=read_ids(self.json_datafile)

		print 'Report output: %s' %(self.json_datafile)
		print 'Seen links: %d' %(len(self.links_seen))
		
		
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
		# 'We need the titles, links and times to index and follow'


		# If we start from the rss
		# titles = response.xpath('//item/title/text()').extract()
		# links  = response.xpath('//item/link/text()' ).extract()
		# 
		#links = response.css('div.text h2 a::attr(href)').extract()
		links=response.xpath('//div[@class="cnk-ttl"]/h2/a/@href').extract()
		links = list (map( lambda str: 'www.focus-news.net'+str[1:], links))		
		
		print type(links[0])
		
		
		for link in links:
			if link not in self.links_seen:
				try:
					yield scrapy.Request(url=link, callback=self.parse_page)
					print 'Mark2'
				except:
					e = sys.exc_info()[0]
					# print "Error: %s" %(e)

	def parse_page(self, response):

		print 'Mark3'

		
		url   = response.url
		try:
			title = response.xpath('//div[@class="inside-top-title"]/h1/text()').extract_first().strip()
		except:
			title = ""
		# art_alternatives = {}
		# art_alternatives[0] = response.css('div.article::text').extract()
		# art_alternatives[1] = response.css('div.article span::text').extract()
		# art_alternatives[2] = response.css('div.article div.story::text').extract()
		# art_alternatives[3] = response.css('div.gallery p::text').extract()

		# for key in art_alternatives:
		# 	art_alternatives[key] = list( map   ( lambda str: str.strip(), art_alternatives[key] ) )
		# 	art_alternatives[key] = list( filter( lambda str: str != u'' , art_alternatives[key] ) )
		# 	art_alternatives[key] = ' '.join(art_alternatives[key])

		# art_alternatives = list( filter( lambda str: str != u'' , art_alternatives.values() ) )	

		# # assert len(art_alternatives) == 1, 'Issue with %s'%url		
		
		article = ''.join(response.xpath('//div[@class="print-content font-resize-content"]/div[@class="inside-body-content jstf"]/text()').extract()).strip()
		#pubDate=response.xpath('//div[@class="info wbig"]/text()').extract_first()
		pubDate=esponse.xpath('//div[@class="inside-top-title"]/span[@class="date"]/text()').extract_first()
		
		#extract and prepare Article date
		dateParts=pubDate.split()
		pubDate= ('%s-%s-%s' %(dateParts[2],dateParts[1],dateParts[0])).lower()
		articleDate=pubDate.replace(dateParts[1],translateMonth[dateParts[1]])
		todaysDate=yesterday.strftime("%Y-%b-%d").lower()

		print 'articleDate:%s == todaysDate:%s'%(articleDate, todaysDate)
		# Filter on todays date
		if (articleDate == todaysDate):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate

			}	
